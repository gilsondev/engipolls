# -*- coding: utf8 -*-

from django.contrib import admin

from .models import Talk


class TalkAdmin(admin.ModelAdmin):
    list_display = ('name', 'at', 'type_talk')
    list_filter = ['at', 'type_talk']
    search_fields = ('name',)

admin.site.register(Talk, TalkAdmin)
