from Products.PloneTestCase import PloneTestCase
PloneTestCase.setupPloneSite()

class SubsiteTestCase(PloneTestCase.PloneTestCase):
    pass
    
class SubsiteFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    pass