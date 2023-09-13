from django.contrib.auth.management import create_permissions
from django.apps import apps
create_permissions(apps.get_app_config('api'))
