import doctest
import unittest2 as unittest

from slc.subsite.tests.base import FUNCTIONAL_TESTING
from plone.testing import layered

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)

TESTFILES = [
    '../README.txt',
    'skinstorage.txt'
]


def test_suite():
    suite  = unittest.TestSuite()
    suite.addTests([
        layered(
                doctest.DocFileSuite(
                    docfile,
                    optionflags=OPTIONFLAGS),
                layer=FUNCTIONAL_TESTING)
         for docfile in TESTFILES
    ])
    return suite
