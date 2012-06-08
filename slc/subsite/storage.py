from zope.interface import implements

from persistent import Persistent
from BTrees.OOBTree import OOBTree

from slc.subsite.interfaces import ISubsiteSkinStorage


class SubsiteSkinStorage(Persistent):
    """Stores subsite paths and skinnames.
    """
    implements(ISubsiteSkinStorage)

    def __init__(self):
        self._paths = OOBTree()

    def add(self, path, skin):
        path = self._canonical(path)

        if not skin or not path:
            return

        self._paths[path] = skin

    def remove(self, path):
        path = self._canonical(path)
        del self._paths[path]

    def has_path(self, path):
        path = self._canonical(path)
        return bool(path in self._paths)

    def get(self, path, default=None):
        path = self._canonical(path)
        longest = ''
        for p in self._paths.keys():
            if path.startswith(p) and len(p) > len(longest):
                longest = p
        return self._paths.get(longest, default)

    def _canonical(self, path):
        if path.endswith('/'):
            path = path[:-1]
        return path

    def __iter__(self):
        return iter(self._paths)
