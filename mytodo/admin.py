from django.contrib import admin

from .models import Todo

class Display_task(admin.ModelAdmin):
    list_display = ('task','is_completed','create_at','update_at')
# Register your models here.
admin.site.register(Todo,Display_task)
