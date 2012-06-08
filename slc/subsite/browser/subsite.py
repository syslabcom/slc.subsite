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
            self.context.restrictedTraverse('@@rss.xml')
            return True
        except:
            # it's ok if this doesn't exist, just means no syndication
            return False
