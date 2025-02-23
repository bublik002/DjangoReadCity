from modeltranslation.translator import translator, TranslationOptions
from main.models import BooksModel


class BooksTranslationOptions(TranslationOptions):
    fields = ('title', 'author', 'info_txt', 'interpreter', 'publishing_house', 'publishing_brand', 'series', 'cover_type')


translator.register(BooksModel, BooksTranslationOptions)