from django.urls import path
from . import views


urlpatterns = [
    path('workflow', views.workflow, name='workflow'),
    path('workflow/workrep', views.workrep, name='workrep'),
    path('workflow/final', views.workfinal, name='final'),
]