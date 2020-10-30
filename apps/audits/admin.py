from django.contrib import admin

from .models import *


class ChoiceAnswerAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'category')
    search_fields = ('name',)
    list_filter = ('enabled', 'category')


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'enabled', 'category')
    list_filter = ('type', 'enabled', 'category')
    search_fields = ('name',)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'enabled', 'category')
    list_filter = ('enabled', 'category')
    search_fields = ('name',)


class AuditAdmin(admin.ModelAdmin):
    list_display = ('representative', 'template', 'call_date', 'phone', 'department')
    list_filter = ('template',)
    search_fields = ('template__name', 'phone')


class ResponseAdmin(admin.ModelAdmin):
    list_display = ('audit', 'question')
    search_fields = ('audit__name', 'question__name')


class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'file_extension', 'audit')
    list_filter = ('file_extension',)
    search_fields = ('name', 'audit__name')


admin.site.register(ChoiceAnswer, ChoiceAnswerAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Audit, AuditAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Attachment, AttachmentAdmin)
