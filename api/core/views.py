from django.shortcuts import render
from django.views import View

from core.models import PersonalInfo, Job, Education


class IndexView(View):
    def get(self, request):
        return render(request, "index.html")


class IndexTestView(View):  # TODO: This is just temp test
    def get(self, request):
        person = PersonalInfo.objects.all().first()
        jobs = Job.objects.all()
        educations = Education.objects.all()
        context = {"person": person, "jobs": jobs, "educations": educations}
        return render(request, "indextest.html", context)
