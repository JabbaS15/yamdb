from django.contrib.admin import ModelAdmin, site

from users.models import CustomUser


class UserAdmin(ModelAdmin):
    list_display = (
        'username',
        'email',
    )


site.register(CustomUser, UserAdmin)
