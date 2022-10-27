"""Solution30 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *


urlpatterns = [

    path('', index, name='index'),

    path('login', auth_views.LoginView.as_view(template_name='Dashboard/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register', register, name='register'),
    path('interventions/list',list_interventions ,name='list_interventions'),
    path('Planification/',Planning ,name='plan'),
    path('Techniciens/list',list_techniciens ,name='list_techniciens'),
    path('clients/list',clients ,name='clients'),
    path('interventions/list/effectuees',list_interventions_effectuees ,name='list_interventions_effectuees'),
    path('interventions/list/en_attente',list_interventions_enattente ,name='list_interventions_enattente'),
    path('interventions/list/historique',list_interventions_historique ,name='list_interventions_historique'),
    path('interventions/Ajouter', ajouter_intervention, name='ajouter_intervention'),
    path('interventions/Détail/<int:pk>', intervention_detail, name='intervention_detail'),
    path('interventions/Editer/<int:inter_id>', Edit_intervention, name='Edit_intervention'),
    path('client/Ajouter', ajouter_client, name='ajouter_client'),
    path('profile/', users_profile, name='users_profile'),
    url(r'^calendar/$', CalendarView.as_view(), name='calendar'),  # here
    path('population-chart/', population_chart, name='population-chart'),

]
