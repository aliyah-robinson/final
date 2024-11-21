from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "first_name",
        "last_name",
        "email",
        "username",
        "age",
        "is_active",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age","first_name", "last_name", "email",)}),)

class SearchUsers(CustomUser):
    search_fields = ["username", "email"]

admin.site.register(CustomUser, CustomUserAdmin)