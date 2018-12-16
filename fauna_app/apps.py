from django.apps import AppConfig


class FaunaAppConfig(AppConfig):
    name = 'fauna_app'

    def ready(self):
        import fauna_app.signals
