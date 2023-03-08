from django.contrib import admin

from products.admin import BasketAdmin
# Register your models here.
from users.models import EmailVerification, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    in_lines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    last_display = ('code', 'user', 'expiration_date')
    fields = ('code', 'user', 'expiration_date', 'created')
    readonly_fields = ('created',)
