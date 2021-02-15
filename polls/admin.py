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


class ChoiceInline(admin.TabularInline):
    model = Choice
    fields = ['id', 'choice_text', 'votes']
    readonly_fields = ['id']
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['id', 'question_text', 'pub_date']


class ChoiceAdmin(admin.ModelAdmin):
    raw_id_fields = ['question']
    list_display = ['id', 'question_id', 'choice_text', 'votes']
    list_select_related = True


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
