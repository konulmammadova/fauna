from django.db.models.signals import pre_save
from django.dispatch import receiver

from fauna_app.models import Service
from fauna_app.options.tools import slugify


@receiver(pre_save, sender=Service, dispatch_uid='signal_create_service_slug')
def signal_create_service_slug(*args, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug or instance.title_cache != instance.title:
        instance.title_cache = instance.title
        instance.slug = slugify(instance.title)
        instance.save()
