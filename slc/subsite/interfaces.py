from zope import schema
from zope.interface import Interface, alsoProvides

class IAnySubsiteCapable(Interface):
    """Any aspect of subsite capable.
    """

class IPossibleSubsite(IAnySubsiteCapable):
    """ All objects that could be subsites should implement this interface.
    """
    
class ISubsiteEnhanced(Interface):
    """ Marker interface for subsites
    """    
    
class IMediaActivator(Interface):
    """ For seeing the activation status or toggling activation.
    """
    media_activated = schema.Bool(title=u'Subsite Activated',required=True, readonly=False)    