from django.contrib import admin

# Register your models here.
from users.models import User, EmailVerification
from products.admin import BasketAdmin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    in_lines =  (BasketAdmin, )
@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    last_display = ('code', 'user', 'expiration_date')
    fields = ('code', 'user', 'expiration_date', 'created')
    readonly_fields = ('created', )
