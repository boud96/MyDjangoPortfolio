from django.urls import path

from api.core.views import IndexTestView, IndexView, DownloadCVView

urlpatterns = [
    path("test/", IndexTestView.as_view()),
    path('download-cv/', DownloadCVView.as_view(), name='download-cv/'),
    path("", IndexView.as_view()),
]
