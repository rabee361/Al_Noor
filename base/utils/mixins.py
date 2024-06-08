from django.views.decorators.cache import cache_page
from functools import wraps

class CachePageMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        return cache_page(60 * 15)(view)  # Cache for 15 minutes

    def dispatch(self, request, *args, **kwargs):
        self.cache_timeout = getattr(self, 'cache_timeout', 60 * 15)
        return super().dispatch(request, *args, **kwargs)