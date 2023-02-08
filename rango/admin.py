from django.contrib import admin
from rango.models import Category, Page



class PageAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'category', 'url')
    
    
    
# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)










"""Finally, register the PageAdmin class with Django’s admin interface.
You should modify the line admin.site.register(Page). Change it to
admin.site.register(Page, PageAdmin) in Rango’s admin.py file"""