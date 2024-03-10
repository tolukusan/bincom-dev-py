from django.contrib import admin
from .models import PollingUnit, AnnouncedPuResults

class PollingUnitAdmin(admin.ModelAdmin):
    fields = ('uniqueid',
    'polling_unit_id',
    'ward_id',
    'lga_id',
    'uniquewardid',
    'polling_unit_number',
    'polling_unit_name',
    'polling_unit_description',
    'lat',
    'long',
    'entered_by_user',
    'date_entered',
    'user_ip_address',)

class AnnouncedPuResultsAdmin(admin.ModelAdmin):
    fields = (
        'result_id',
    'polling_unit_uniqueid',
    'party_abbreviation',
    'party_score',
    'entered_by_user',
    'date_entered',
    'user_ip_address',
    )

admin.site.register(PollingUnit, PollingUnitAdmin)
admin.site.register(AnnouncedPuResults, AnnouncedPuResultsAdmin)