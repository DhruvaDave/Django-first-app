from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    description = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    website = models.URLField(default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    print("----kwargs---create_profile---",kwargs)
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Message(models.Model):
    
   
    user_messsage = models.CharField(max_length=300)
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    
    # def save(self, *args, **kwargs):
    #     # if not self.slug:
    #     #     self.slug = slugify(self.title)
    #     super(Message, self).save(*args, **kwargs)




# @receiver(post_save, sender=User)
# def user_post_save(sender, **kwargs):
#     """
#     Create a Profile instance for all newly created User instances. We only
#     run on user creation to avoid having to check for existence on each call
#     to User.save.
#     """
#     user, created = kwargs["instance"], kwargs["created"]
#     if created and user.username != settings.ANONYMOUS_USER_NAME:
        
#         profile = Message.objects.create(pk=user.pk, user=user, creator=user)
#         assign_perm("change_user", user, user)
#         assign_perm("change_profile", user, profile)