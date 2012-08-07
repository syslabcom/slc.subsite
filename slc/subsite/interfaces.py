from zope import schema
from zope.interface import Interface
from plone.app.layout.navigation.interfaces import INavigationRoot


class IIsolatedObject(Interface):
    """
    Marker interface for object to isolate from their siblings
    """


class IPotentialBadRequest(Interface):
    """
    Marker interface for a request to isolate traversed object from the
    IIsolatedObject siblings
    """


class IObjectToIsolate(Interface):
    """
    Marker interface for object(s) in root that you cannot acquire
    while traversing
    """

class IAnySubsiteCapable(Interface):
    """Any aspect of subsite capable.
    """


class IPossibleSubsite(IAnySubsiteCapable):
    """ All objects that could be subsites should implement this interface.
    """


class ISubsiteEnhanced(INavigationRoot, IIsolatedObject):
    """ Marker interface for subsites
    """


class IMediaActivator(Interface):
    """ For seeing the activation status or toggling activation.
    """
    media_activated = schema.Bool(
        title=u'Subsite Activated',
        required=True,
        readonly=False)


class ISubsiteSkinStorage(Interface):
    """A storage for subsites which maps the skin to the subsite physical path.
    Will be registered as a local utility.
    """

    def add(path, skin):
        """registers a skinname for the path of a subsite
           updating if path exists
        """

    def remove(path):
        """Forget the skinname for this subsite
        """

    def has_path(path):
        """Check if we have a registration
        """

    def get(path, default=None):
        """Get the longest matching subsite path for the given request path.
        Will return None if nothing found.
        """

    def __iter__():
        """Iterate over all existing subsite paths."""

