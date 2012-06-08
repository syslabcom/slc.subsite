from Acquisition import aq_parent
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.interfaces import ISiteRoot
from Products.PloneLanguageTool.LanguageTool import LanguageTool
from slc.subsite import isSubsite
from zope.component import getUtility


def setDefaultLanguage(self, langCode):
    """Sets the default language."""
    if isSubsite(aq_parent(self)):
        return aq_parent(self).getField(
            'default_language').getMutator(aq_parent(self))(langCode)
    portal_properties = getToolByName(self, "portal_properties")
    site_properties = portal_properties.site_properties
    if site_properties.hasProperty('default_language'):
        return site_properties._updateProperty('default_language', langCode)
    portal = getUtility(ISiteRoot)
    if portal.hasProperty('default_language'):
        return portal._updateProperty('default_language', langCode)
    self.default_lang = langCode

LanguageTool.setDefaultLanguage = setDefaultLanguage


def getDefaultLanguage(self):
    """Returns the default language."""
    if isSubsite(aq_parent(self)):
        field = aq_parent(self).getField('default_language')
        if field is not None:
            return field.getAccessor(aq_parent(self))()
    portal_properties = getToolByName(self, "portal_properties", None)
    if portal_properties is None:
        return 'en'
    site_properties = portal_properties.site_properties
    if site_properties.hasProperty('default_language'):
        return site_properties.getProperty('default_language')
    portal = getUtility(ISiteRoot)
    if portal.hasProperty('default_language'):
        return portal.getProperty('default_language')
    return getattr(self, 'default_lang', 'en')

LanguageTool.getDefaultLanguage = getDefaultLanguage
