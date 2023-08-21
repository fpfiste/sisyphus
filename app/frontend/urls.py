from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('companies', views.organizations, name='companies'),
    path("companies/<int:id_company>/", views.organization_detail, name='organization_detail'),
    path('projects', views.projects, name='projects'),
    path("projects/<int:id_project>/", views.project_detail, name='project_detail'),
    path('tasks', views.tasks, name='tasks'),
    path('sales', views.sales, name='sales'),
    path('employees', views.employees, name='employees'),
    path('assets', views.assets, name='assets'),
    path('invoices', views.invoices, name='invoices'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
]