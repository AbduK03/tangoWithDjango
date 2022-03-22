from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rango.models import Category, Page , courseTitle ,startDate , desc

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(courseTitle)
admin.site.register(startDate)
admin.site.register(desc)


