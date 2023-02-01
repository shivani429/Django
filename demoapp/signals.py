from django.db.models import signals
from django.dispatch import receiver
from .models import Demoapp

@receiver(signals.post_save,sender=Demoapp)
def create_product(sender,instance,created,**kwargs):
    print('save method is called -signals.py')

@receiver(signals.pre_save,sender=Demoapp)
def check_product_description(sender,instance,**kwargs):
    if not instance.description:
        instance.description='this is default description -signals.py'