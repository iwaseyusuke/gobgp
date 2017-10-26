# Copyright (C) 2017 Nippon Telegraph and Telephone Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import print_function

import sys
import time
import unittest

from fabric.api import local
import nose

from lib.noseplugin import OptionParser, parser_option
from lib import base
from lib.base import (
    Bridge,
    BGP_FSM_ESTABLISHED,
)
from lib.gobgp import GoBGPContainer
from lib.quagga import QuaggaOSPFContainer


def check_metric(cnt, prefix, metric):
    for nw in cnt.get_global_rib(prefix=prefix):
        for path in nw['paths']:
            if path['metric'] == metric:
                return True
    return False


def check_aigp_metric(cnt, prefix, metric):
    for nw in cnt.get_global_rib(prefix=prefix):
        for path in nw['paths']:
            if path['aigp-metric'] == metric:
                return True
    return False


def wait_for(f, timeout=120):
    interval = 1
    count = 0
    while True:
        if f():
            return

        time.sleep(interval)
        count += interval
        if count >= timeout:
            raise Exception('timeout')


def get_ifname_with_prefix(prefix, f=local):
    command = (
        "ip addr show to %s"
        " | head -n1 | cut -d'@' -f1 | cut -d' ' -f2") % prefix

    return f(command, capture=True)


class ZebraNHTTest(unittest.TestCase):
    """
    Test case for Next-Hop Tracking with Zebra integration.
    """
    # R1: GoBGP
    # R2: GoBGP + Zebra + OSPFd
    # R3: GoBGP + Zebra + OSPFd
    # R4: Zebra + OSPFd
    #
    #       +----+
    #       | R3 | ... lo 3.3.3.3/32
    #       +----+
    #        /  |
    #       /   |
    #      /   +----+
    #     /    | R4 | ... lo 4.4.4.4/32
    #    /     +----+
    # +----+      |
    # | R2 |------+ ... lo 2.2.2.2/32
    # +----+
    #   |
    #   |
    # +----+
    # | R1 |
    # +----+

    @classmethod
    def setUpClass(cls):
        gobgp_ctn_image_name = parser_option.gobgp_image
        base.TEST_PREFIX = parser_option.test_prefix

        cls.r1 = GoBGPContainer(
            name='r1', asn=65001, router_id='1.1.1.1',
            ctn_image_name=gobgp_ctn_image_name,
            log_level=parser_option.gobgp_log_level,
            zebra=False)

        cls.r2 = GoBGPContainer(
            name='r2', asn=65000, router_id='2.2.2.2',
            ctn_image_name=gobgp_ctn_image_name,
            log_level=parser_option.gobgp_log_level,
            zebra=True,
            zapi_version=3,
            bgp_config={
                'global': {
                    'route-selection-options': {
                        'config': {
                            'enable-aigp': True,
                        },
                    },
                },
            },
            zebra_config={
                'interfaces': {
                    'lo': [
                        'ip address 2.2.2.2/32',
                    ],
                },
            },
            ospfd_config={
                'networks': {
                    '2.2.2.2/32': '0.0.0.0',
                    '192.168.23.0/24': '0.0.0.0',
                    '192.168.24.0/24': '0.0.0.0',
                },
            })

        cls.r3 = GoBGPContainer(
            name='r3', asn=65000, router_id='3.3.3.3',
            ctn_image_name=gobgp_ctn_image_name,
            log_level=parser_option.gobgp_log_level,
            zebra=True,
            zapi_version=3,
            bgp_config={
                'global': {
                    'route-selection-options': {
                        'config': {
                            'enable-aigp': True,
                        },
                    },
                },
            },
            zebra_config={
                'interfaces': {
                    'lo': [
                        'ip address 3.3.3.3/32',
                    ],
                },
            },
            ospfd_config={
                'networks': {
                    '3.3.3.3/32': '0.0.0.0',
                    '192.168.23.0/24': '0.0.0.0',
                    '192.168.34.0/24': '0.0.0.0',
                },
            })

        cls.r4 = QuaggaOSPFContainer(
            name='r4',
            zebra_config={
                'interfaces': {
                    'lo': [
                        'ip address 4.4.4.4/32',
                    ],
                },
            },
            ospfd_config={
                'networks': {
                    '4.4.4.4/32': '0.0.0.0',
                    '192.168.34.0/24': '0.0.0.0',
                    '192.168.24.0/24': '0.0.0.0',
                },
            })

        wait_time = max(ctn.run() for ctn in [cls.r1, cls.r2, cls.r3, cls.r4])
        time.sleep(wait_time)

        cls.br_r1_r2 = Bridge(name='br_r1_r2', subnet='192.168.12.0/24')
        [cls.br_r1_r2.addif(ctn) for ctn in (cls.r1, cls.r2)]

        cls.br_r2_r3 = Bridge(name='br_r2_r3', subnet='192.168.23.0/24')
        [cls.br_r2_r3.addif(ctn) for ctn in (cls.r2, cls.r3)]

        cls.br_r2_r4 = Bridge(name='br_r2_r4', subnet='192.168.24.0/24')
        [cls.br_r2_r4.addif(ctn) for ctn in (cls.r2, cls.r4)]

        cls.br_r3_r4 = Bridge(name='br_r3_r4', subnet='192.168.34.0/24')
        [cls.br_r3_r4.addif(ctn) for ctn in (cls.r3, cls.r4)]

    def test_00_BGP_neighbor_established(self):
        # Test if the BGP connections establish between r1-r2 and r2-r3.

        self.r1.add_peer(self.r2, bridge=self.br_r1_r2.name)
        self.r2.add_peer(self.r1, bridge=self.br_r1_r2.name)
        self.r2.add_peer(self.r3, bridge=self.br_r2_r3.name,
                         neighbor_addr='3.3.3.3', local_addr='2.2.2.2')
        self.r3.add_peer(self.r2, bridge=self.br_r2_r3.name,
                         neighbor_addr='2.2.2.2', local_addr='3.3.3.3')

        self.r1.wait_for(expected_state=BGP_FSM_ESTABLISHED, peer=self.r2)
        self.r2.wait_for(expected_state=BGP_FSM_ESTABLISHED, peer=self.r3)

    def test_01_OSPF_established(self):
        # Test to start OSPF connection up between r2-r3.
        r3_router_id = '3.3.3.3'

        def _f():
            return self.r2.local(
                "vtysh -c 'show ip ospf neighbor %s'" % r3_router_id,
                capture=True)

        wait_for(f=_f)

    def test_02_initial_metric(self):
        # Test if r2 calculates the initial Metric to r3 (using redistributed
        # connected route from r3).
        metric = 10
        r3_router_id = '3.3.3.3'

        def _f():
            return check_metric(self.r2, r3_router_id, metric)

        wait_for(f=_f)

    def test_03_add_ipv4_route(self):
        # Test r3 adds an IPv4 route whose nexthop is r3.
        # Also, test if r1 receives the AIGP Metric of the r3 advertised AIGP
        # Metric + r2 incremented Metric.
        prefix = '10.3.1.0/24'
        aigp_metric = 50
        metric = 10

        def _f():
            return check_aigp_metric(self.r1, prefix, aigp_metric + metric)

        self.r3.local(
            'gobgp global rib add -a ipv4 %s aigp metric %d'
            % (prefix, aigp_metric))

        wait_for(f=_f)

    def test_04_link_r2_r3_down(self):
        # Test if the Metric is updated when the nexthop state is changed by
        # the link down.
        # If the link r2-r3 goes down, the Metric should be increased.
        prefix = '10.3.1.0/24'
        metric = 20
        r3_if_addr_to_r2 = '192.168.23.3/24'

        def _f():
            return check_metric(self.r2, prefix, metric)

        # Make r4's interface connecting to r2 down.
        ifname = get_ifname_with_prefix(r3_if_addr_to_r2, f=self.r3.local)
        self.r3.local('ip link set %s down' % ifname)

        wait_for(f=_f)

    def test_05_link_r2_r3_restore(self):
        # Test if the Metric is updated when the nexthop state is changed by
        # the link up again.
        # If the link r2-r3 goes up again, the Metric should go back again to
        # the initial value.
        prefix = '10.3.1.0/24'
        metric = 10
        r3_if_addr_to_r2 = '192.168.23.3/24'

        def _f():
            return check_metric(self.r2, prefix, metric)

        ifname = get_ifname_with_prefix(r3_if_addr_to_r2, f=self.r3.local)
        self.r3.local('ip link set %s up' % ifname)

        wait_for(f=_f)


if __name__ == '__main__':
    output = local("which docker 2>&1 > /dev/null ; echo $?", capture=True)
    if int(output) is not 0:
        print("docker not found")
        sys.exit(1)

    nose.main(argv=sys.argv, addplugins=[OptionParser()],
              defaultTest=sys.argv[0])
