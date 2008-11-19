from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from Products.CMFPlone import PloneMessageFactory as _
from Products.Archetypes import atapi 
from Products.validation import V_REQUIRED
from archetypes.schemaextender.interfaces import ISchemaExtender, IOrderableSchemaExtender
from archetypes.schemaextender.field import ExtensionField
from Products.CMFCore.utils import getToolByName
from Products.CMFDefault.formlib.vocabulary import SimpleVocabulary

class ExtendedStringField(ExtensionField, atapi.StringField):
    """ A String Field """


class SchemaExtender(object):
    implements(IOrderableSchemaExtender)

    _fields = [
            ExtendedStringField('skin',
                schemata='default',
                languageIndependent=True,
                vocabulary_factory='slc.subsite.SkinNamesVocabulary',
                widget=atapi.SelectionWidget(
                    label = _(u'label_skin', default=u'Skin'),
                    description=_(u'description_skin', default=u'Choose an existing skin name'),
                ),
            ),
            ExtendedStringField('default_language',
                schemata="default",
                languageIndependent=True,
                vocabulary_factory='slc.subsite.SupportedLangsVocabulary',
                widget=atapi.SelectionWidget(
                    label = _(u'label_default_language', default=u'Default language'),
                    description=_(u'description_default_language', default=u'Select the default language for the subsite.'),
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
        items = [(None, '', 'None')] + items
        return SimpleVocabulary.fromTitleItems(items)


class SupportedLangsVocabulary(object):
    """ Vocabulary to list the availabkle languages.
    Uses either the global language tool, or a locally installed version"""
    implements(IVocabularyFactory)

    def __call__(self, context):
        context = getattr(context, 'context', context)
        langtool = getToolByName(context, 'portal_languages')
        items = [ (k,k,v) for k, v in langtool.listSupportedLanguages()]
        return SimpleVocabulary.fromTitleItems(items)


