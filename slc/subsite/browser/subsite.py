import Acquisition
import AccessControl
import datetime
import urllib

from zope import event
from zope import component
from zope import interface
from zope import schema
from zope.formlib import form

from Products.CMFCore import utils as cmfutils

from Products.statusmessages import interfaces as statusmessages_ifaces

from slc.subsite import interfaces 

from p4a.common import at
from p4a.common import formatting





class SubsiteView(object):
    """View for subsite containers.
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        

    def contentsMethod(self):
        return self.context.getFolderContents

    def has_syndication(self):
        try:
            view = self.context.restrictedTraverse('@@rss.xml')
            return True
        except:
            # it's ok if this doesn't exist, just means no syndication
            return False
            

