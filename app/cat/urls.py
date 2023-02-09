from django.urls import path

from cat.views import base, articles

urlpatterns = [
    path('', base.main_page),
    path('cat_stats', articles.cat_stats)
]
