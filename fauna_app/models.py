from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe

from fauna_app.options.tools import get_slider_image, get_service_bg_image, get_service_image, get_testimony_image


class GlobalModel(models.Model):
    logo = models.ImageField(upload_to='logo/', null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    facebook_account = models.URLField(null=True, blank=True)
    twitter_account = models.URLField(null=True, blank=True)
    google_plus_account = models.URLField(null=True, blank=True)
    youtube_account = models.URLField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    copyright_info = models.CharField(max_length=100, null=True, blank=True)

    # log
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_logo(self):
        if self.logo:
            return mark_safe("<img style='width:100px' src='{}' alt=''>".format(self.logo.url))

    def __str__(self):
        return 'Global'

    class Meta:
        verbose_name = 'Global'
        verbose_name_plural = 'Global'


class Menu(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    url = models.CharField(max_length=50, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(default=0)

    # log
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_children(self):
        return Menu.objects.filter(parent=self)

    class Meta:
        verbose_name = 'Menyu'
        verbose_name_plural = 'Menyular'
        ordering = ('order',)


class Slider(models.Model):
    image = models.ImageField(upload_to=get_slider_image)
    title = models.CharField(max_length=150, null=True, blank=True)
    text = models.CharField(max_length=300, null=True, blank=True)
    btn_green = models.CharField(max_length=50, null=True, blank=True)
    btn_gray = models.CharField(max_length=50, null=True, blank=True)

    # log
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_image(self):
        if self.image:
            return mark_safe("<img style='width:350px' src={} />".format(self.image.url))

    def __str__(self):
        return self.title


class Service(models.Model):
    icon_class = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    sub_title = models.CharField(max_length=300, null=True, blank=True)
    bg_image = models.ImageField(upload_to=get_service_bg_image, null=True, blank=True)
    image = models.ImageField(upload_to=get_service_image, null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    # log
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_bg_image(self):
        if self.bg_image:
            return mark_safe("<img style='width: 200px'/>".format(self.bg_image.url))

    def get_image(self):
        if self.image:
            return mark_safe("<img style='width: 200px'/>".format(self.image.url))

    def __init__(self, *args, **kwargs):
        super(Service, self).__init__(*args, **kwargs)
        self.title_cache = self.title

    def get_absolute_url(self):
        return reverse('service-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title


class Testimony(models.Model):
    image = models.ImageField(upload_to=get_testimony_image, null=True, blank=True)
    statement = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)

    # log
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_image(self):
        if self.image:
            return mark_safe("<img style='width: 100px' src = {} />".format(self.image.url))

    def __str__(self):
        return self.name
