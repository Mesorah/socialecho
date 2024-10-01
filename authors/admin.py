from django.contrib import admin
from .models import AuthorUser


@admin.register(AuthorUser)
class AuthorUserAdmin(admin.ModelAdmin):
    pass
