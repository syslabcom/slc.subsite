from zope.interface import implements
from Products.CMFPlone import PloneMessageFactory as _
from Products.Archetypes import atapi 
from Products.validation import V_REQUIRED
from archetypes.schemaextender.interfaces import ISchemaExtender, IOrderableSchemaExtender
from archetypes.schemaextender.field import ExtensionField



class SkinField(ExtensionField, atapi.StringField):
    """ The Skin to show """


class SchemaExtender(object):
    implements(IOrderableSchemaExtender)

    _fields = [
            SkinField('skin',
                schemata='other',
                languageIndependent=True,
                widget=atapi.StringWidget(
                    label = _(u'label_skin', default=u'Skin'),
                    description=_(u'description_skin', default=u'Choose an existing skin name'),
                ),
            ),

            ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self._fields

    def getOrder(self, original):
        other = original.get('other', [])

        original['other'] = other

        return original

