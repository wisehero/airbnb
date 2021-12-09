from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as room_models

# Register your models here.


class RoomInline(admin.TabularInline):
    model = room_models.Room


@admin.register(models.User)  # 관리자 등록
class CustomUserAdmin(UserAdmin):

    inlines = (RoomInline,)

    """ CUSTOM USER ADMIN """
    fieldsets = UserAdmin.fieldsets + (
        ("Custom Profile", {
            "fields": (
                "avatar",
                "gender",
                "bio",
                "birthdate",
                "language",
                "currency",
                "superhost"
            ),
        }),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )
