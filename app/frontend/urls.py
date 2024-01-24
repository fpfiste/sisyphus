from django.urls import path
from . import views


urlpatterns = [
    path('', views.render_page, name='index'),
    path('_config', views.send_config, name='config'),
    path('_list_media', views.list_media, name='media'),
    path('schedule', views.render_page, name='schedule'),
    path('projects', views.render_page, name='projects'),
    path('tasks', views.render_page, name='tasks'),
    path('sales', views.render_page, name='sales'),
    path('companies', views.render_page, name='companies'),
    path('employees', views.render_page, name='employees'),
    path('assets', views.render_page, name='assets'),
    path('templates', views.render_page, name='task-templates'),
    path('receivables', views.render_page, name='receivables'),
    path('payables', views.render_page, name='payables'),
    path('billing', views.render_page, name='billing'),
    path('settings', views.render_page, name='settings'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/login/', views.login_view, name='login'),
    path('errors/403', views.render_403, name='error_403'),
    path('export', views.render_page, name='export'),
]