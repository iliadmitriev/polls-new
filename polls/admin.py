import json
from django.utils.safestring import mark_safe
from django.contrib import admin
from django.contrib.sessions.models import Session
from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Question, Choice


class PermissionAdmin(admin.ModelAdmin):
    pass


class ContentTypeAdmin(admin.ModelAdmin):
    pass


class MigrationAdmin(admin.ModelAdmin):
    pass


class QuestionAdmin(admin.ModelAdmin):
    pass


class ChoiceAdmin(admin.ModelAdmin):
    pass


class LogEntryAdmin(admin.ModelAdmin):
    pass


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        s = obj.get_decoded()
        return mark_safe(u'<pre>%s' % (json.dumps(s, indent=4)))

    list_display = ['session_key', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']


admin.site.register(Permission, PermissionAdmin)
admin.site.register(ContentType, ContentTypeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(Session, SessionAdmin)
