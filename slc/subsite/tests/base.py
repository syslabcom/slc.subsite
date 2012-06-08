from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile


class SlcSubsite(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        import slc.subsite
        self.loadZCML('configure.zcml', package=slc.subsite)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'slc.subsite:default')


SLC_SUBSITE_FIXTURE = SlcSubsite()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(SLC_SUBSITE_FIXTURE,),
    name="SlcSubsite:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(SLC_SUBSITE_FIXTURE,),
    name="SlcSubsite:Functional")
