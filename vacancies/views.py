from django.shortcuts import render, HttpResponse, Http404
from django.views import View
from django.db.models import Count

from stepik_vacancies.settings import PROJECT_NAME
from vacancies.models import Vacancy, Company, Specialty


class MainPage(View):

    def get(self, request):

        context = {
            'project_name': PROJECT_NAME,
            'specialties': Specialty.objects.annotate(count=Count('vacancies')),
            'companies':  Company.objects.annotate(count=Count('vacancies')),
        }

        return render(request, 'vacancies/index.html', context=context)


class AboutProject(View):

    def get(self, request):

        return HttpResponse('Здесь будет страница о проекте.')


class VacanciesElement(View):

    def get(self, request, vacancy_id):

        vacancy_qs = Vacancy.objects.filter(id=vacancy_id)
        if len(vacancy_qs) != 1:
            raise Http404
        vacancy_obj = vacancy_qs[0]

        context = {
            'title_prefix': vacancy_obj.title,
            'project_name': PROJECT_NAME,
            'vacancy': vacancy_obj,
        }

        return render(request, 'vacancies/vacancy.html', context=context)


class VacanciesList(View):

    def get(self, request):

        context = {
            'title_prefix': "Вакансии",
            'project_name': PROJECT_NAME,
            'specialty_title': 'ВСЕ ВАКАНСИИ',
            'vacancies': Vacancy.objects.all(),
        }

        return render(request, 'vacancies/vacancies.html', context=context)


class VacanciesListBySpecialty(View):

    def get(self, request, specialty_code):

        specialty_qs = Specialty.objects.filter(code=specialty_code)
        if len(specialty_qs) != 1:
            raise Http404
        specialty_obj = specialty_qs[0]

        context = {
            'title_prefix': specialty_obj.title,
            'project_name': PROJECT_NAME,
            'specialty_title': specialty_obj.title,
            'vacancies': specialty_obj.vacancies.all(),
        }

        return render(request, 'vacancies/vacancies.html', context=context)


class CompaniesElement(View):

    def get(self, request, company_id):

        company_qs = Company.objects.filter(id=company_id)
        if len(company_qs) != 1:
            raise Http404
        company_obj = company_qs[0]
        vacancies = Vacancy.objects.filter(company=company_obj)

        context = {
            'title_prefix': company_obj.name,
            'project_name': PROJECT_NAME,
            'vacancies': vacancies,

        }
        return render(request, 'vacancies/company.html', context=context)



class CompaniesList(View):

    def get(self, request):

        return HttpResponse('Здесь будет список компаний.')