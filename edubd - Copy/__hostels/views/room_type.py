from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from ..models import Room, RoomType
from ..form import RoomForm


class TypeCreateView(CreateView):
    model = RoomType
    template_name = 'roomtype/create.html'
    fields = (
        'type', 'description',
    )
    success_url = reverse_lazy('room_types_list')


class RoomTypeListView(ListView):
    model = RoomType
    context_object_name = 'types'
    form_class = RoomForm
    initial = {'key': 'value'}
    template_name = 'roomtype/index.html'

    def get(self, request):
        room_types = RoomType.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'room_types': room_types, 'form': form}
        return render(request, self.template_name, context)


class RoomTypeUpdateView(UpdateView):
    model = RoomType
    template_name = 'roomtype/create.html'
    context_object_name = 'room'
    fields = ( 'type', 'description',)
    success_url = reverse_lazy('room_types_list')


class RoomTypeDeleteView(DeleteView):
    def get(self, request, pk):
        room_type=RoomType.objects.get(id=pk)
        room_type.delete()
        return redirect('room_types_list')


