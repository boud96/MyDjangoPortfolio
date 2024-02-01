from django.urls import path

from core.views import IndexTestView, IndexView

urlpatterns = [
    path("test/", IndexTestView.as_view()),
    path("", IndexView.as_view()),
]
