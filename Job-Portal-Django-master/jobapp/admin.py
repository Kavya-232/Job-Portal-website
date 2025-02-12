from django.contrib import admin
from .models import *


admin.site.register(Category)

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('job','user','timestamp')
    
admin.site.register(Applicant,ApplicantAdmin)


class JobAdmin(admin.ModelAdmin):
    list_display = ('title','is_published','is_closed','timestamp')

admin.site.register(Job,JobAdmin)

class BookmarkJobAdmin(admin.ModelAdmin):
    list_display = ('job','user','timestamp')
admin.site.register(BookmarkJob,BookmarkJobAdmin)




from .models import Interm, Apply

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job', 'email', 'phone', 'date_applied')
    search_fields = ['full_name', 'email', 'job__title']
    list_filter = ['date_applied']

admin.site.register(Interm)
admin.site.register(Apply, ApplicationAdmin)
