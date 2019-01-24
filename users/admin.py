# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from users.models import *
admin.site.register(Note)
admin.site.register(University)
admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(Favourite)
admin.site.register(Rating)
admin.site.register(Tag)
admin.site.register(Discussion)
admin.site.register(NoteTag)
admin.site.register(Course)
admin.site.register(User)

