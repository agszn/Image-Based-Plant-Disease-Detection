from django.contrib import admin
from django.contrib.auth.models import User, Group

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    list_filter = ()  # Removed 'is_active'

# Unregister the original User admin and register the custom one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Unregister the Group model
admin.site.unregister(Group)
