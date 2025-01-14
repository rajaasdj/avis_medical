from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_emojis, name='avis_form'),
    path('merci/', views.page_merci, name='merci'),
    path('fail/', views.page_scanned, name='scan_fail'),
]