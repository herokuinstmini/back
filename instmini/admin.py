from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'created_at')
    filter_horizontal = ['tags']


admin.site.register(Tag)
