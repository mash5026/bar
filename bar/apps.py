from django.apps import AppConfig


class BarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bar'
    verbose_name = 'رستوران'

    def ready(self):
        import bar.signals
