from time import time
from unidecode import unidecode

# from fauna_app.models import Service

# PET_CATEGORIES = ((service.title, service.title) for service in Service.objects.all())
SERVICE_TYPES = (
    ('a', 'A'),
    ('b', 'B'),
    ('a', 'A'),
    ('b', 'B'),
)

PET_CATEGORIES = (
    ('category1', 'Category1'),
    ('category2', 'Category2'),
    ('category3', 'Category3'),
    ('category4', 'Category4'),
    ('category5', 'Category5'),
)

GENDER_CHOICES = {
    (True, 'Male'),
    (False, 'Female'),
}


# Custom slugify function
def slugify(title):
    title_url = unidecode(title).lower().replace(' ', '-')
    return title_url


def get_slider_image(instance, filename):
    return "slider/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))


def get_service_bg_image(instance, filename):
    return "services/bg/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))


def get_service_image(instance, filename):
    return "services/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))


def get_testimony_image(instance, filename):
    return "testimonies/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))

# def get_doctor_image(instance, filename):
#     return "doctor/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))
#
#
# def get_home_icons(instance, filename):
#     return "icons/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))
#
#
# # cover images>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def get_news_cover(instance, filename):
#     return "news/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))
#
#
# def get_flatpage_cover(instance, filename):
#     return "flatpage/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))
#
#
# def get_faq_cover(instance, filename):
#     return "news/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))
#
#
# def get_doctor_image(instance, filename):
#     return "doctor/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))
#
#
# def get_departments_cover(instance, filename):
#     return "news/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))
#
#
# def get_contact_cover(instance, filename):
#     return "contact/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))
#
#
# def get_cover_path(instance, filename):
#     return "contact/%s_%s" % (str(time()).replace('.', '_'), filename.replace(' ', '_'))
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
