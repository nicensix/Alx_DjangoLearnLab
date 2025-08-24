from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Book
from django.contrib.auth.models import Group, Permission
from django.apps import apps

Book = apps.get_model('bookshelf', 'Book')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # columns to show
    search_fields = ('title', 'author')  # enables search bar
    list_filter = ('publication_year',)  # adds filter by year

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

def create_groups():
    # Get model permissions
    can_view = Permission.objects.get(codename='can_view', content_type__app_label='bookshelf')
    can_create = Permission.objects.get(codename='can_create', content_type__app_label='bookshelf')
    can_edit = Permission.objects.get(codename='can_edit', content_type__app_label='bookshelf')
    can_delete = Permission.objects.get(codename='can_delete', content_type__app_label='bookshelf')

    # Create groups
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    editors, _ = Group.objects.get_or_create(name="Editors")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Assign permissions
    viewers.permissions.set([can_view])
    editors.permissions.set([can_view, can_create, can_edit])
    admins.permissions.set([can_view, can_create, can_edit, can_delete])

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book)