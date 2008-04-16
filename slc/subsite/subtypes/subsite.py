from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from Products.CMFPlone import PloneMessageFactory as _
from Products.Archetypes import atapi 
from Products.validation import V_REQUIRED
from archetypes.schemaextender.interfaces import ISchemaExtender, IOrderableSchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.vocabulary import SimpleVocabulary

class SkinField(ExtensionField, atapi.StringField):
    """ The Skin to show """


class SchemaExtender(object):
    implements(IOrderableSchemaExtender)

    _fields = [
            SkinField('skin',
                schemata='default',
                languageIndependent=True,
                vocabulary_factory='slc.subsite.SkinNamesVocabulary',
                widget=atapi.SelectionWidget(
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
        other = original.get('default', [])

        original['default'] = other

        return original
        
class SkinNamesVocabulary(object):
    """ Vocabulary to list the available skins """
    implements(IVocabularyFactory)
    
    def __call__(self, context):
        context = getattr(context, 'context', context)
        skintool = getToolByName(context, 'portal_skins')
        items = [ (v, v, v) for v in skintool.getSkinSelections()]
        return SimpleVocabulary.fromTitleItems(items)
    
    
