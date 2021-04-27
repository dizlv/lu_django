from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users import models

admin.site.register(models.User, UserAdmin)
