from django.contrib import admin
from users.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.

"""
Class to registrate the model to the Admin cms
"""
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','phone_number','website','picture')
    list_display_links = ('pk','user')
    list_display_editable = ('phone_number','website','picture')
    search_fields = ('user__email','user__first_name','user__lastname')
    list_filter = ('created','modified','user__is_active','user__is_staff')

    fieldsets = (
        ('Profile',{
            'fields':(('user','profile'),),
        }),
        ('Extra info',{
            'fields':(
                ('website','phone_nomber'),
                ('biography')
            ),
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        }),
    )
    readonly_fields = ('created','modified')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)