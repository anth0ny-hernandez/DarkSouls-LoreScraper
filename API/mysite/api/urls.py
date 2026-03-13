from django.urls import path
from . import views

urlpatterns = [
    path("soulsborne/", views.SoulsborneListCreate.as_view(), name="soulsborne-view-create")
]