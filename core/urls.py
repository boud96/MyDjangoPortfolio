from django.urls import path

from core.views import IndexView, DownloadCVView

urlpatterns = [
    path('download-cv/', DownloadCVView.as_view(), name='download-cv'),
    path("", IndexView.as_view()),
]
