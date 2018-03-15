#!/usr/bin/env python3.6

# Author: Eric Turgeon
# License: BSD
# Location for tests into REST API of FreeNAS

import unittest
import sys
import os
import xmlrunner
apifolder = os.getcwd()
sys.path.append(apifolder)
from functions import DELETE, PUT, BSD_TEST
from auto_config import results_xml

try:
    from config import BRIDGEHOST
except ImportError:
    RunTest = False
else:
    MOUNTPOINT = "/tmp/iscsi" + BRIDGEHOST
    RunTest = True
TestName = "delete iscsi"
DEVICE_NAME_PATH = "/tmp/iscsi_dev_name"
TARGET_NAME = "iqn.freenas:target0"


class delete_iscsi_test(unittest.TestCase):

    # Clean up any leftover items from any previous failed runs
    @classmethod
    def setUpClass(inst):
        PUT("/services/services/iscsitarget/", {"srv_enable": False})
        BSD_TEST("iscsictl -R -t %s" % TARGET_NAME)
        cmd = 'umount -f "%s" &>/dev/null ; ' % MOUNTPOINT
        cmd += 'rmdir "%s" &>/dev/null' % MOUNTPOINT
        BSD_TEST(cmd)

    # Remove iSCSI target
    def test_01_Delete_iSCSI_target(self):
        assert DELETE("/services/iscsi/target/1/") == 204

    # Remove iSCSI extent
    def test_02_Delete_iSCSI_extent(self):
        assert DELETE("/services/iscsi/extent/1/") == 204


def run_test():
    suite = unittest.TestLoader().loadTestsFromTestCase(delete_iscsi_test)
    xmlrunner.XMLTestRunner(output=results_xml, verbosity=2).run(suite)

if RunTest is True:
    print('\n\nStarting %s tests...' % TestName)
    run_test()
