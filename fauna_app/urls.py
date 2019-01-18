from django.conf.urls import url
# from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from .views import BaseIndexView, ServiceDetailView, AboutView, ShopView, BlogListView, ProductDetailView, RegisterView, \
    LoginView, LogoutView, BlogDetailView, ContactView

urlpatterns = [
    url(r'^$', BaseIndexView.as_view(), name="index"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    # url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^about/$', AboutView.as_view(), name="about"),
    url(r'^service/(?P<slug>[-\w]+)/$', ServiceDetailView.as_view(), name="service-detail"),
    url(r'^shop/$', ShopView.as_view(), name="shop"),
    url(r'^product/(?P<slug>[-\w]+)/$', ProductDetailView.as_view(), name="product-detail"),
    url(r'^blog/$', BlogListView.as_view(), name="blog-list"),
    url(r'^blog/(?P<slug>[-\w]+)/$', BlogDetailView.as_view(), name="blog-detail"),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
]
