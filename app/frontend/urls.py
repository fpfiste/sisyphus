from django.urls import path
from . import views


urlpatterns = [
    path('', views.render_home, name='index'),
    path('_config', views.send_config, name='config'),
    path('schedule', views.render_schedule, name='schedule'),
    path('projects', views.render_projects, name='projects'),
    path('tasks', views.render_tasks, name='tasks'),
    path('sales', views.render_sales, name='sales'),
    path('companies', views.render_companies, name='companies'),
    path('employees', views.render_employees, name='employees'),
    path('assets', views.render_assets, name='assets'),
    path('templates', views.render_templates, name='task-templates'),
    path('terms', views.render_terms, name='terms'),
    path('receivables', views.render_invoices, name='receivables'),
    path('payables', views.render_payables, name='payables'),
    path('billing', views.render_billing, name='billing'),
    path('settings', views.render_settings, name='settings'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/login/', views.login_view, name='login'),
    path('errors/403', views.render_403, name='error_403'),
]