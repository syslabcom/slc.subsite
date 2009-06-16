from Products.PloneTestCase import PloneTestCase

from Products.PloneTestCase.layer import onsetup
from Products.PloneTestCase import layer

SiteLayer = layer.PloneSite

class SubsiteLayer(SiteLayer):
    @classmethod
    def setUp(cls):
        """Set up additional products and ZCML required to test this product.
        """
        PloneTestCase.setupPloneSite()
        SiteLayer.setUp()

class SubsiteTestCase(PloneTestCase.PloneTestCase):
    layer = SubsiteLayer

class SubsiteFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    layer = SubsiteLayer
