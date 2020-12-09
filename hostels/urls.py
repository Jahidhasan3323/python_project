from django.urls import path
from . import hostel_type

urlpatterns = [
    path('hostel_type_list',hostel_type.hostel_type, name="hostel_type.list"),
    path('hostel_type/create',hostel_type.hostel_type_create, name="hostel_type.create"),
    path('hostel_type/edit/<int:pk>',hostel_type.hostel_type_edit, name="hostel_type.edit"),
    path('hostel_type/delete/<int:pk>',hostel_type.hostel_type_delete, name="hostel_type.delete"),
    
]