from django.urls import path
from .views import visitorbook
app_name = 'frontOffice'
urlpatterns = [
    #visitor_book
    path('visitorbooks/',visitorbook.VisitorbookView.as_view(), name="visitorbooks"),
    path('visitorbook/<int:pk>',visitorbook.DetailVisitorbookView.as_view(), name="visitorbook"),
    path('add_visitorbook/',visitorbook.AddVisitorbookView.as_view(), name="add_visitorbook"),
    path('edit_visitorbook/<int:pk>',visitorbook.EditVisitorbookView.as_view(), name="edit_visitorbook"),
    path('delete_visitorbook/<int:pk>',visitorbook.DeleteVisitorbookView.as_view(), name="delete_visitorbook"),
  
]