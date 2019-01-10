from django.db.models.signals import pre_save
from django.dispatch import receiver

from fauna_app.models import Service, Product, Post
from fauna_app.options.tools import slugify


@receiver(pre_save, sender=Service, dispatch_uid='signal_create_service_slug')
def signal_create_service_slug(*args, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug or instance.title_cache != instance.title:
        instance.title_cache = instance.title
        instance.slug = slugify(instance.title)
        instance.save()


@receiver(pre_save, sender=Product, dispatch_uid='signal_create_product_slug')
def signal_create_product_slug(*args, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug or instance.name_cache != instance.name:
        instance.name_cache = instance.name
        instance.slug = slugify(instance.name)
        instance.save()


@receiver(pre_save, sender=Post, dispatch_uid='signal_create_post_slug')
def signal_create_post_slug(*args, **kwargs):
    instance = kwargs.get('instance')
    if not instance.slug or instance.title_cache != instance.title:
        instance.title_cache = instance.title
        instance.slug = slugify(instance.title)
        instance.save()
