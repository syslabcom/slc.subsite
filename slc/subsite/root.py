from Acquisition import aq_base, aq_parent

from slc.subsite.interfaces import ISubsiteEnhanced

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from Products.CMFPlone.interfaces import IFactoryTool


def getSubsiteRoot(context, relativeRoot=None):
    """Get the path to the root of the navigation tree. If context or one of
    its parents until (but not including) the portal root implements
    ISubsiteEnhanced, return this.

    Otherwise, if an explicit root is set in navtree_properties or given as
    relativeRoot, use this. If the property is not set or is set to '/', use
    the portal root.
    """

    portal_url = getToolByName(context, 'portal_url')

    if not relativeRoot:
        portal_properties = getToolByName(context, 'portal_properties')
        navtree_properties = getattr(portal_properties, 'navtree_properties')
        relativeRoot = navtree_properties.getProperty('root', None)

    portal = portal_url.getPortalObject()
    obj = context
    while (not ISubsiteEnhanced.providedBy(obj)
           and aq_base(obj) is not aq_base(portal)):
        # XXX a bit ugly: if this method is called with a context from inside
        # the portal_factory, we cannot use the parent() method, as it calls
        # aq_parent on aq_inner of the object. This directly returns the main
        # portal
        if IFactoryTool.providedBy(obj):
            obj = aq_parent(obj)
        else:
            obj = utils.parent(obj)
    if (ISubsiteEnhanced.providedBy(obj)
        and aq_base(obj) is not aq_base(portal)):
        return '/'.join(obj.getPhysicalPath())

    rootPath = relativeRoot
    portalPath = portal_url.getPortalPath()
    # contextPath = '/'.join(context.getPhysicalPath())

    if rootPath:
        if rootPath == '/':
            return portalPath
        else:
            if len(rootPath) > 1 and rootPath[0] == '/':
                return portalPath + rootPath
            else:
                return portalPath

    # Fall back on the portal root
    if not rootPath:
        return portalPath
