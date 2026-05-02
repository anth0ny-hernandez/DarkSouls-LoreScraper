from django.urls import path
from . import views

urlpatterns = [
    path("soulsborne/", views.SoulsEntityList.as_view(), name="soulsborne-view-create"),
    path("soulsborne/tags/", views.TaggingList.as_view(), name="tagging-view-create"),
    path("soulsborne/tagsofentities/", views.TagsOfEntsList.as_view(), name="tag-ents-view-create"),
    path("soulsborne/interpretations/", views.InterpretList.as_view(), name="theory-view-create"),
    path("soulsborne/interpretationofentities/", views.InterpretEntsList.as_view(), name="interpret-ents-view-create"),
]