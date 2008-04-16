from zope import interface
from p4a.subtyper import interfaces as stifaces
from slc.subsite import interfaces

class AbstractSubsiteDescriptor(object):
    interface.implements(stifaces.IPortalTypedFolderishDescriptor)

    title = u'Subsite'
    description = u'Container to store Subsites with their own skin'
    type_interface = interfaces.ISubsiteEnhanced

class FolderSubsiteDescriptor(AbstractSubsiteDescriptor):
    for_portal_type = 'Folder'

class LargeFolderSubsiteDescriptor(AbstractSubsiteDescriptor):
    for_portal_type = 'Large Plone Folder'


