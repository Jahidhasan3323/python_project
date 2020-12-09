from django.urls import path
from .views import hostel_type, hostel, room_type, room, designation
from hostels.views import hostel_type
from hostels.views import hostel

urlpatterns = [
    #hostel type

    path('hostel_type_list', hostel_type.TypesListView.as_view(), name='hostel-type-list'),
    path('edit/hostel/<int:pk>', hostel_type.EditHostelTypeView.as_view(), name="edit_hostel"),
    path('delete/hostel/<int:pk>', hostel_type.DeleteHostelTypeView.as_view(), name="delete_hostel"),
    
    #hostel
    path('hostels', hostel.HostelListView.as_view(), name='list-hostel'),
    path('add_hostel', hostel.AddHostelView.as_view(), name="add-hostel"),
    path('hostel/<int:pk>/detail', hostel.HostelDetailView.as_view(), name='hostel-detail'),
    path('update/<int:pk>/hostel', hostel.HostelUpdateView.as_view(), name='hostel-update'),
    path('delete/<int:pk>/hostel', hostel.HostelDeleteView.as_view(), name='hostel-delete'),


    #Room Type Urls
    path('room_list_types', room_type.RoomTypeListView.as_view(), name="room_types_list"),
    path('add_room_type', room_type.TypeCreateView.as_view(), name="room_type_create"),
    path('edit_room_type/<int:pk>', room_type.RoomTypeUpdateView.as_view(), name="edit_room_type"),
    path('delete_room_type/<int:pk>', room_type.RoomTypeDeleteView.as_view(), name="delete_room_type"),


    # room
    path('room_list/', room.RoomListView.as_view(), name="room_list"),
    path('add_room', room.RoomCreateView.as_view(), name="add_room"),
    path('edit_room/<int:pk>', room.RoomUpdateView.as_view(), name="edit_room"),
    path('delete_room/<int:pk>', room.RoomDeleteView.as_view(), name="delete_room"),


    path('room/<int:pk>', hostel.HostelRoomView.as_view(), name="hostel_room"),
    path('hostel_add_room', hostel.AddHostelRoomView.as_view(), name="hostel_add_room"),
    path('add-hostel-room', hostel.HostelCreateRoomView.as_view(), name="add_hostel_room"),
    path('delete_room/<int:pk>/', hostel.DeleteHostelRoomView.as_view(), name="hostel_delete_room"),
    path('assign/student/<int:pk>/<int:room>', hostel.AddStudentView.as_view(), name="add_student"),
    path('add_student_room', hostel.AssignStudentView.as_view(), name="add-student-room"),
    path('hostel/add_student/<int:pk>', hostel.DerectAddStudent.as_view(), name="direct-add-student"),
    path('hostel/staff/<int:pk>', hostel.AddStaffView.as_view(), name="direct-add-student"),
    path('assign_staff', hostel.AssignStaff.as_view(), name="assign-staff")





]