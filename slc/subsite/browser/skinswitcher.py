from Acquisition import aq_base, aq_inner

from zope import interface
from zope import component

from slc.subsite.interfaces import ISubsiteSkinStorage
from p4a.subtyper.interfaces import ISubtyper


def setskin(site, event): 
     """ Depending on the skin property set on the subsite we override the default skin. 
     """ 
     storage = component.queryUtility(ISubsiteSkinStorage)
     if storage is None:
        return
     skinname = storage.get(event.request.PATH_INFO, None)
     if skinname is None:
        return

     site.changeSkin(skinname, event.request) 



def registerSubsiteSkin(ob, event):
    """ registers a new skinname for the subsite if set
    """
    
    field = ob.getField('skin')
    if field is None:
        return
    
    skinname = field.getAccessor(ob)()
        
    storage = component.queryUtility(ISubsiteSkinStorage)
    if storage is None:
        return
    
    subsitepath = "/".join(ob.getPhysicalPath())
    if not skinname and storage.has_path(subsitepath):    
        storage.remove(subsitepath)
    else:
        storage.add(subsitepath, skinname)
    
    
    
# Event handler to catch our own patched event while translation named IObjectTranslationReferenceSetEvent
# We need this to be able to subtype an object while it is translated.
def subtype_on_translate(obj, evt):
    """ EVENT: 
        Update the chapter links based on the new set values in chapters
    """    
    canonical = aq_base(aq_inner(evt.object))
    target = aq_base(aq_inner(evt.target))
    subtyper = component.getUtility(ISubtyper)    
    subtype = subtyper.existing_type(canonical)
    if subtype is not None:
        subtyper.change_type(target, subtype.name)    