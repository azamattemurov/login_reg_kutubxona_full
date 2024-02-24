from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register(Book)

@admin.register(Book)
class Bookadmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'price', 'image_tag')
    list_filter = ['title', 'price']
    readonly_fields = ['image_tag']
