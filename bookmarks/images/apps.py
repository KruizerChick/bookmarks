from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'bookmarks.images'
    label = 'images'
    verbose_name = 'Image bookmarks'

    def ready(self):
        # import signal handlers
        import bookmarks.images.signals
