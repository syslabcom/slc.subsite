from slc.subsite.interfaces import ISubsiteSkinStorage
from zope.component import queryUtility

def setskin(site, event): 
     """ Depending on the skin property set on the subsite we override the default skin. 
     """ 
     storage = queryUtility(ISubsiteSkinStorage)
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
        
    storage = queryUtility(ISubsiteSkinStorage)
    if storage is None:
        return
    
    subsitepath = "/".join(ob.getPhysicalPath())
    if not skinname and storage.has_path(subsitepath):    
        storage.remove(subsitepath)
    else:
        storage.add(subsitepath, skinname)
    