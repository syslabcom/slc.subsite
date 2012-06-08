from zope import interface
from zope import component
from slc.subsite import interfaces

import p4a.z2utils  # Patch CMFDynamicViewFTI
from Products.CMFDynamicViewFTI import interfaces as cmfdynifaces


class SubsiteDynamicViews(object):
    interface.implements(cmfdynifaces.IDynamicallyViewable)
    component.adapts(interfaces.ISubsiteEnhanced)

    def __init__(self, context):
        self.context = context  # Actually ignored...

    def getAvailableViewMethods(self):
        """Get a list of registered view method names
        """
        return [view for view, name in self.getAvailableLayouts()]

    def getDefaultViewMethod(self):
        """Get the default view method name
        """
        return "subsite-container.html"

    def getAvailableLayouts(self):
        """Get the layouts registered for this object.
        """
        return (("subsite-container.html", "Subsite view"),)
