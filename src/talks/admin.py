# -*- coding: utf8 -*-

from django.contrib import admin

from .models import Talk


class TalkAdmin(admin.ModelAdmin):
    list_filter = ['at', 'type_talk']

admin.site.register(Talk, TalkAdmin)
