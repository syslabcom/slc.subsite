from AccessControl import ModuleSecurityInfo
from slc.subsite.interfaces import ISubsiteEnhanced

def isSubsite(ob):
    """ convenience method for skin scripts """
    return ISubsiteEnhanced.providedBy(ob)

import patches

ModuleSecurityInfo('slc.subsite').declarePublic('isSubsite')


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


