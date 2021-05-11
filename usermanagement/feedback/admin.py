from django.contrib import admin

from .models import Feedback, Reply

admin.site.register(Feedback)
admin.site.register(Reply)