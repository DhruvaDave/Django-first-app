from django.contrib.auth import get_user_model
from .models import Message

class MyAuthenticationBackend:

    def authenticate(self, *args, **kwargs):
        pass


    def get_user(self, user_id):
        print("-----user_id--->>>>>>>>>>>>>>>---",user_id)
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

    def has_perm(self, user_obj, perm, obj=None):
        print("-----user_obj---has_perm---",user_obj,"----perms----",perm,"----",obj)
        # print("-------obj----------",Message,"---user_obj.pk",user_obj)

        if perm == "view_category":
            return True # everybody can view
        # otherwise only the owner or the superuser can delete
        return user_obj.is_active 
        # and obj.user.pk==user_obj.pk

    def has_perms(self, user_obj, perm_list, obj=None):
        print("--------perm_list----------",perm_list)
        print("--------user_obj-------111---",user_obj)
        return all(self.has_perm(user_obj, perm, obj) for perm in perm_list)