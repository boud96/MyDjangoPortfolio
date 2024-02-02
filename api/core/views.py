from django.shortcuts import render
from django.utils import timezone
from django.views import View

from core.models import PersonalInfo, Job, Education, Skill


class IndexView(View):
    def get(self, request):
        person = PersonalInfo.objects.get(active=True)
        person.age = (timezone.now().date() - person.date_of_birth).days // 365

        jobs = Job.objects.all()

        educations = Education.objects.all()

        skills = Skill.objects.all().order_by("type_skill__order", "order")
        for skill in skills:
            skill.type_skill.bg_color = self.add_alpha(skill.type_skill.color)

        context = {"person": person, "jobs": jobs, "educations": educations, "skills": skills}
        return render(request, "index.html", context)

    def add_alpha(self, color):
        return color + "55"


class IndexTestView(View):  # TODO: This is just temp test
    def get(self, request):
        person = PersonalInfo.objects.all().first()
        jobs = Job.objects.all()
        educations = Education.objects.all()
        skills = Skill.objects.all()
        context = {"person": person, "jobs": jobs, "educations": educations, "skills": skills}
        return render(request, "indextest.html", context)
