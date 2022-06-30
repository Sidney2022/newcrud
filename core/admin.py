from django.contrib import admin
from .models import Post,Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
       list_display = ('username', 'email', 'password')

admin.site.register(Post)
admin.site.register(Profile, ProfileAdmin)