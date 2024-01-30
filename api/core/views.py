from django.shortcuts import render
from django.views import View

from core.models import PersonalInfo, Job, Education


class IndexView(View):
    def get(self, request):  # TODO: This is just temp test
        person = PersonalInfo.objects.all().first()
        jobs = Job.objects.all()
        educations = Education.objects.all()
        context = {"person": person, "jobs": jobs, "educations": educations}
        return render(request, "index.html", context)
