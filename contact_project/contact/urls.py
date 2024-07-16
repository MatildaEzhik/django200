from django.urls import path

from contact import views

urlpatterns = [
    path('', views.contact_view, name='contact'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
]