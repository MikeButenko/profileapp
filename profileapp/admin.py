from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import Profile


class ProfileHist(SimpleHistoryAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'biography', 'contacts')

admin.site.register(Profile, ProfileHist)