from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserProfile, Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    model = Message
    fields = ('user_messsage')
    exclude = ('user_id')

    def save_model(self, request, obj, form, change):
        obj.user_id = request.user
        obj.save()
        super(MessageAdmin, self).save_model(request, obj, form, change)


admin.site.register(UserProfile)
admin.site.register(Message)