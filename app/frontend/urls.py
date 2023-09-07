from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('companies', views.render_template, name='companies'),
    path('projects', views.render_template, name='projects'),
    path('tasks', views.render_template, name='tasks'),
    path('projects/sales', views.render_template, name='sales'),
    path('employees', views.render_template, name='employees'),
    path('employees/absences', views.render_template, name='employee_absences'),
    path('assets', views.render_template, name='assets'),
    path('assets/absences', views.render_template, name='asset_absences'),
    path('invoices', views.render_template, name='invoices'),
    path('logout', views.logout_view, name='logout'),
    path('login', views.login_view, name='login'),
]