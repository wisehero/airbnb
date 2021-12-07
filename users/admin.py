from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)  # 관리자 등록
class CustomUserAdmin(admin.ModelAdmin):

    pass
