from django.contrib import admin

# Register your models here.


from myapp.models import register
admin.site.register(register)
