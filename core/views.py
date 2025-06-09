import os

import markdown
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from django.views import View

from core.models import (
    PersonalInfo,
    Job,
    Education,
    Skill,
    Project,
    Photo,
    SocialMediaAccount,
    CVFile,
)


class IndexView(View):
    def get(self, request):
        person = PersonalInfo.objects.get(active=True)
        person.age = (timezone.now().date() - person.date_of_birth).days // 365
        person.about_me = markdown.markdown(person.about_me)

        socials = SocialMediaAccount.objects.filter(owner=person)
        person.linkedin = socials.filter(type=0).first()  # TODO: Hardcoded like this is not the best idea.
        person.facebook = socials.filter(type=1).first()
        person.instagram = socials.filter(type=2).first()
        person.github = socials.filter(type=3).first()

        jobs = Job.objects.all()
        for job in jobs:
            job.description = markdown.markdown(job.description)

        educations = Education.objects.all()

        skills = Skill.objects.exclude(type_skill__title="Other").order_by("type_skill__order", "order")
        for skill in skills:
            skill.type_skill.bg_color = self.add_alpha(skill.type_skill.color)
        skills_other = Skill.objects.filter(type_skill__title="Other").order_by("order")  # TODO: Does not work with translations.

        projects = Project.objects.all()

        photos = Photo.objects.all()

        context = {
            "person": person,
            "jobs": jobs,
            "educations": educations,
            "skills": skills,
            "skills_other": skills_other,
            "projects": projects,
            "photos": photos
        }
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
        return render(request, "templates/indextest.html", context)


class DownloadCVView(View):
    def get(self, request, *args, **kwargs):
        try:
            cv_file = CVFile.objects.get(active=True)  # Fetch active CVFile
        except ObjectDoesNotExist:
            raise Http404("No active CV file found")

        response = FileResponse(cv_file.file, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename={os.path.basename(cv_file.file.name)}'
        return response
