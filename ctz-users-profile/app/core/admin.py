from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ["id"]
    list_display = ["email", "first_name", "last_name", "is_activate", "had_company"]
    list_filter = []
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal Info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "type_user",
                    "birthdate",
                    "years"
                )
            },
        ),
        (_("Permissions"), {"fields": ("is_activate", "is_staff", "is_superuser")}),
        (_("Important dates"), {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2")}),
    )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.ContactAddress)
admin.site.register(models.ProfileCompany)
admin.site.register(models.ProfessionalProfile)
admin.site.register(models.SocialNetwork)
