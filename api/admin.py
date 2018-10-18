from django.contrib import admin

from .models import TrashCan, TrashState

admin.site.register(TrashCan)
admin.site.register(TrashState)
