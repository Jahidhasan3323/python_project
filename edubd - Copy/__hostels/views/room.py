from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from ..models import Room, RoomType
from ..form import RoomForm


class RoomCreateView(CreateView):
    model = Room
    template_name = 'room/create.html'
    fields = (
        'number', 'number_of_bed', 'bed_cost', 'type', 'description',
    )
    success_url = reverse_lazy('room_list')


class RoomListView(ListView):
    model = Room
    context_object_name = 'types'
    form_class = RoomForm
    initial = {'key': 'value'}
    template_name = 'room/index.html'

    def get(self, request):
        rooms = Room.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'rooms': rooms, 'form': form}
        return render(request, self.template_name, context)


class RoomUpdateView(UpdateView):
    model = Room
    template_name = 'room/create.html'
    context_object_name = 'room'
    fields = ('number', 'number_of_bed', 'bed_cost', 'type', 'description',)
    success_url = reverse_lazy('room_list')


class RoomDeleteView(DeleteView):
    def get(self, request, pk):
        hostel_type=Room.objects.get(id=pk)
        hostel_type.delete()
        return redirect('room_list')


