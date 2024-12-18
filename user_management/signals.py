from django.db.models.signals import post_save  
from django.dispatch import receiver  
from django.core.mail import send_mail  
from .models import User  


@receiver(post_save,sender=User)
def notify_user_creation(sender,instance,created,**kwargs):
    if created:
        send_mail(
            subject='Welcome!',  
            message='Thank you for registering as a user.',  
            from_email='##',  
            recipient_list=[instance.email],  
            fail_silently=False,  
        )