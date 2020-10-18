"""stepik_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vacancies.views import MainPage, VacanciesElement, VacanciesList, VacanciesListBySpecialty, CompaniesElement, \
    CompaniesList, AboutProject


urlpatterns = [
    # main
    path('', MainPage.as_view(), name='main_page'),
    path('about/', AboutProject.as_view(), name='about_project'),
    # vacancies
    path('vacancies/', VacanciesList.as_view(), name='vacancies_list'),
    path('vacancies/<int:vacancy_id>/', VacanciesElement.as_view(), name='vacancies_element'),
    path('vacancies/cat/<str:specialty_code>/', VacanciesListBySpecialty.as_view(), name='vacancies_list_by_specialty'),
    # companies
    path('companies/', CompaniesList.as_view(), name='companies_list'),
    path('companies/<int:company_id>/', CompaniesElement.as_view(), name='companies_element'),
    # admin
    path('admin/', admin.site.urls),
]
