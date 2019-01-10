from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, CreateView, FormView, RedirectView, ListView

from base_user.models import MyUser
from fauna_app.forms import AppointmentForm, RegisterForm, LoginForm
from fauna_app.models import Menu, GlobalModel, Slider, Service, Testimony, Appointment, Product, Post


class BaseDataView(View):

    def get_context_data(self, **kwargs):
        context = dict()
        context['site'] = GlobalModel.objects.first()
        context["menu_items"] = Menu.objects.filter(parent__isnull=True)
        context["menu_items_all"] = Menu.objects.all()
        return context


class BaseIndexView(BaseDataView, TemplateView):
    template_name = 'home/index.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        context['form'] = AppointmentForm(request.POST)

        if context['form'].is_valid():
            context['form'].save()
            messages.success(request, 'Muracietiniz gonderildi.  Tesekkur edirik!')
            # return super(TemplateView, self).render_to_response(context)
            return redirect(reverse('index'))

        return render(request, self.template_name, self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(BaseIndexView, self).get_context_data(**kwargs)
        if self.request.method == 'GET':
            form = AppointmentForm()
            context['form'] = form

        context['sliders'] = Slider.objects.all()
        context['services'] = Service.objects.all()
        context['testimonies'] = Testimony.objects.all()
        context['products'] = Product.objects.all()[:4]
        context['blogs'] = Post.objects.all()[:3]
        return context


class AboutView(BaseDataView, TemplateView):
    template_name = 'about/about.html'


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(ServiceDetailView, self).get_context_data(**kwargs)
        context.update({**BaseDataView.get_context_data(BaseDataView)})
        return context
    context_object_name = 'service'


class ShopView(BaseDataView, TemplateView):
    template_name = 'shop/shop.html'


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'shop/product-detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context.update({**BaseDataView.get_context_data(BaseDataView)})
        return context


class BlogListView(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog/blog.html'
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context.update({**BaseDataView.get_context_data(BaseDataView)})
        return context


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/blog-detail.html'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context.update({**BaseDataView.get_context_data(BaseDataView)})
        return context
    context_object_name = 'blog'


class ContactView(BaseDataView, TemplateView):
    template_name = 'contact/contact.html'


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'account/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        new_user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        new_user.set_password(password)
        new_user.save()
        messages.success(self.request, 'Uğurla qeydiyyatdan keçdiniz! Zəhmət olmasa daxil olun.')
        return super(RegisterView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(RegisterView, self).get_context_data(**kwargs)
        context.update({**BaseDataView.get_context_data(BaseDataView)})
        return context


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'account/login.html'
    success_url = reverse_lazy('blog')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(self.request, user)
        return super(LoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        context.update({**BaseDataView.get_context_data(BaseDataView)})
        return context


class LogoutView(RedirectView):
    permanent = False
    pattern_name = 'index'
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            logout(self.request)
        return super(LogoutView, self).get_redirect_url(*args, **kwargs)

