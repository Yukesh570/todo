from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Persondetail),
admin.site.register(PhoneNO),
admin.site.register(Email),
admin.site.register(Task)