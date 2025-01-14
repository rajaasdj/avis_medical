from django.contrib import admin
from .models import *

@admin.register(Avis)
class AvisAdmin(admin.ModelAdmin):
    list_display = ('emoji', 'date', 'visite')

admin.site.register(Visite)
class VisiteAdmin(admin.ModelAdmin):
    list_display = ('code', 'ref_pat', 'specialite', 'service')
    list_filter = ('specialite', 'service')

admin.site.register(Setting)
