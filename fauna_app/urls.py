from django.conf.urls import url
from .views import BaseIndexView, ServiceDetailView, AboutView, ShopView, BlogView

urlpatterns = [
    url(r'^$', BaseIndexView.as_view(), name="index"),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^service/(?P<slug>[-\w]+)/$', ServiceDetailView.as_view(), name="service-detail"),
    url(r'^shop/$', ShopView.as_view(), name="shop"),
    url(r'^blog/$', BlogView.as_view(), name="blog"),
    url(r'^contact/$', BlogView.as_view(), name="contact"),
]
