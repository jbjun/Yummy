from django.apps import AppConfig
from django.conf import settings as django_settings
from django_summernote.utils import (
    LANG_TO_LOCALE, uploaded_filepath, get_theme_files,
    example_test_func)

class BoardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'board'

# class DjangoSummernoteConfig(AppConfig):
#     name = 'django_summernote'
#     verbose_name = 'Django Summernote'
#
#     theme = 'bs3'
#     config = {}
#
#     def __int__(self, app_name, app_module):
#         super(DjangoSummernoteConfig, self).__init__(app_name, app_module)
#         self.update_config()
#
#     def get_defalut_config(self):
#         return {
#             'iframe': True,
#         }