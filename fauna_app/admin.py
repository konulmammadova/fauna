from django.contrib import admin

from .models import Menu, GlobalModel, Slider, Service, Testimony, Appointment, Category, Product, Post, \
    ProductImage, PostImage
from django.contrib.admin import SimpleListFilter


class MenuParentFilter(SimpleListFilter):
    title = "filter"
    parameter_name = 'decade'

    def lookups(self, request, model_admin):
        return ((item.pk, item.name) for item in Menu.objects.filter(parent__isnull=True) if
                item.get_children().count() != 0)

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(parent_id=self.value())
        else:
            return queryset


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'parent', 'order')
    list_filter = (MenuParentFilter,)


@admin.register(GlobalModel)
class GlobalModel(admin.ModelAdmin):
    list_display = (
        'get_logo', 'email', 'phone', 'facebook_account', 'twitter_account', 'google_plus_account', 'youtube_account',
        'address', 'copyright_info', 'created_at', 'updated_at')


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'text')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','get_bg_image', 'get_image', 'sub_title', 'slug')
    list_display_links = ('title',)


@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'name', 'title', 'statement')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'origin', 'gender', 'age', 'price', 'slug', 'created_at')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'product')

@admin.register(PostImage)
class PosttImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'post')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
