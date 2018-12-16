from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView
from fauna_app.models import Menu, GlobalModel, Slider, Service, Testimony


class BaseDataView(View):

    def get_context_data(self, **kwargs):
        context = dict()
        context['site'] = GlobalModel.objects.first()
        context["menu_items"] = Menu.objects.filter(parent__isnull=True)
        context["menu_items_all"] = Menu.objects.all()
        return context


class BaseIndexView(BaseDataView, TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super(BaseIndexView, self).get_context_data(**kwargs)
        context['sliders'] = Slider.objects.all()
        context['services'] = Service.objects.all()
        context['testimonies'] = Testimony.objects.all()
        return context


class AboutView(BaseDataView, TemplateView):
    template_name = 'about/about.html'


class ServiceDetailView(BaseDataView, DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'


class ShopView(BaseDataView, TemplateView):
    template_name = 'shop/shop.html'


class BlogView(BaseDataView, TemplateView):
    template_name = 'blog/blog.html'


class ContactView(BaseDataView, TemplateView):
    template_name = 'contact/contact.html'
