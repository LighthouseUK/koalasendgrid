"""
This file is just a helper for running unittests in PyCharm.
As the module test files are not in the root of the project the 'vendor' setups fom *.yaml break.
Subsequently the unittest will fail to load as the dependencies are missing.
"""

import unittest
from koalasendgrid.test_koalasendgrid import TestKoalaSendgrid


__author__ = 'Matt'


class TestApex(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
