from django.contrib import admin

# import model Contact manually
from home.models import Contact

from home.models import FilesAdmin

# Register your models here.

# added manually or register model Contact here 
admin.site.register(Contact)


admin.site.register(FilesAdmin)
