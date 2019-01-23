from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.safestring import mark_safe
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from base_user.models import MyUser
from fauna_app.options.tools import get_slider_image, get_service_bg_image, get_service_image, get_testimony_image, \
    GENDER_CHOICES, basker_token_generator, BASKET_STATUS, ORDER_STATUS

myuser = settings.AUTH_USER_MODEL


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
    appointment_title = models.CharField(max_length=50, null=True, blank=True)
    appointment_image = models.ImageField(upload_to='appointment/', null=True, blank=True)

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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return mark_safe("<img style='width:350px' src={} />".format(self.image.url))


class Service(models.Model):
    icon_class = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    sub_title = models.CharField(max_length=300, null=True, blank=True)
    bg_image = models.ImageField(upload_to=get_service_bg_image, null=True, blank=True)
    image = models.ImageField(upload_to=get_service_image, null=True, blank=True)
    content = RichTextUploadingField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Servis"
        verbose_name_plural = "Servislər"
        ordering = ('id',)

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


class Testimony(models.Model):
    image = models.ImageField(upload_to=get_testimony_image, null=True, blank=True)
    statement = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return mark_safe("<img style='width: 100px' src = {} />".format(self.image.url))


class Category(MPTTModel):
    name = models.CharField(max_length=250, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(myuser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=40)
    origin = models.CharField(max_length=350, null=True, blank=True)
    gender = models.BooleanField(choices=GENDER_CHOICES)
    age = models.PositiveIntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"
        ordering = ("-created_at",)

    def __init__(self, *args, **kwargs):
        super(Product, self).__init__(*args, **kwargs)
        self.name_cache = self.name

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={'slug': self.slug})

    def get_main_image(self):
        return self.productimage_set.first()


class ProductImage(models.Model):
    title = models.ImageField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Appointment(models.Model):
    full_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Ad, Soyad')
    email = models.EmailField(null=True, blank=True, verbose_name='Elektron poçt')
    phone = models.CharField(max_length=25, null=True, blank=True, verbose_name='Telefon')
    service_type = models.ForeignKey(Service, null=True, blank=True)
    pet_category = models.ForeignKey(Category,
                                     limit_choices_to={'parent': None},
                                     null=True, blank=True)
    visiting_date = models.DateField(null=True, blank=True)
    message = models.TextField(null=True, blank=True, verbose_name='Əlavə Mesajınız')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Post(models.Model):
    title = models.CharField(max_length=80)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(myuser, on_delete=models.CASCADE, null=True, blank=True)
    origin = models.CharField(max_length=350, null=True, blank=True)
    gender = models.BooleanField(choices=GENDER_CHOICES, default=False)
    age = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.title_cache = self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})

    def get_main_image(self):
        return self.postimage_set.first()

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"
        ordering = ('-created_at',)


class PostImage(models.Model):
    title = models.ImageField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class BasketManager(models.Manager):
    def new(self, user=None):
        user_obj = None
        if user is not None:
            if user.is_authenticated():
                user_obj = user
        return self.model.objects.create(user=user_obj)


class Basket(models.Model):
    token = models.CharField(max_length=40, default=basker_token_generator)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(myuser, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=BASKET_STATUS, default='open')

    objects = BasketManager()

    def __str__(self):
        return f'{self.id}'

    class Meta:
        verbose_name = 'Səbət'
        verbose_name_plural = 'Səbətlər'


class Line(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)


class ShippingDetails(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=255)
    note = models.TextField(null=True, blank=True)


class Order(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    user = models.ForeignKey(myuser, on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=25, null=True, blank=True)
    ship_detail = models.ForeignKey(ShippingDetails, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='pending')

