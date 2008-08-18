from Acquisition import aq_base

from slc.subsite.interfaces import ISubsiteEnhanced

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils

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
    while not ISubsiteEnhanced.providedBy(obj) and aq_base(obj) is not aq_base(portal):
        obj = utils.parent(obj)
    if ISubsiteEnhanced.providedBy(obj) and aq_base(obj) is not aq_base(portal):
        return '/'.join(obj.getPhysicalPath())

    rootPath = relativeRoot
    portalPath = portal_url.getPortalPath()
    contextPath = '/'.join(context.getPhysicalPath())

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
