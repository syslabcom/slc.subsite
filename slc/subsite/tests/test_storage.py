import unittest
import doctest
from Testing.ZopeTestCase import FunctionalDocFileSuite as Suite
from base import SubsiteFunctionalTestCase
from slc.subsite import storage

OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)
               
def test_suite():
    return unittest.TestSuite((

            Suite('tests/skinstorage.txt',
                   optionflags=OPTIONFLAGS,
                   package='slc.subsite',
                   test_class=SubsiteFunctionalTestCase) ,

    ))