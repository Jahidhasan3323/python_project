from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('details/<int:course_id>',views.details, name="details"),
    path('delete/<int:course_id>',views.delete, name="delete")
]
