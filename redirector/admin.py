from django.contrib import admin
from redirector.models import Redirection, MissDirection

class RedirectionAdmin(admin.ModelAdmin):
    pass
class MissDirectionAdmin(admin.ModelAdmin):
    pass

admin.site.register(Redirection, RedirectionAdmin)
admin.site.register(MissDirection, MissDirectionAdmin)
