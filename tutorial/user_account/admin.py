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
        print("---------hewrr--------",request.user)
        obj.save()
        super(MessageAdmin, self).save_model(request, obj, form, change)

    def post_edit(self,request, post_id):
        print("-------post---edit")
        item = Message.objects.get(pk=post_id)
        if request.user == item.user:
            print("-------------IF------->>>>>>>>>>>")

    def has_change_permission(self, request, obj=None):
        print("-------------objiiiiiiiiiii",obj)
        if obj is not None:
            if request.user.is_superuser:
                return True
            else: 
                if obj.user_id != request.user:
                    print("--------if----------222")
                    return False
                else:
                    print("----------else---------")
                    return True

admin.site.register(UserProfile)
admin.site.register(Message)