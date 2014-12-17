from django.contrib import admin
from sitecontent.models import Content

# Register your models here.
class ContentAdmin(admin.ModelAdmin):
	fields = ['title', 'content',]

admin.site.register(Content, ContentAdmin)