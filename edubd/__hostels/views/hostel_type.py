from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import View, ListView

from ..models import HostelType
from ..form import HostelTypeForm
#from .form import *
from django.contrib import messages
# Create your views here.


# class TypeView(View):
#     def get(self, request):
#         return HttpResponse('ok')

class TypesListView(ListView):
    model = HostelType
    context_object_name = 'types'
    form_class = HostelTypeForm
    initial = {'key': 'value'}
    template_name = 'hosteltype/index.html'

    def get(self, request):
        hostel_types = HostelType.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        context = {'hostel_types': hostel_types, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        hostel_types = HostelType.objects.all().order_by('-id')
        form = self.form_class(initial=self.initial)
        hostel_type = request.POST
        form = HostelTypeForm(request.POST)
        if form.is_valid():
            hostel_type = form.save()
            messages.success(request, 'Data store successfull', extra_tags='success')
            return redirect('hostel-type-list')
        context = {'hostel_types': hostel_types, 'form': form}
        return render(request, self.template_name, context)


class EditHostelTypeView(View):
    def get(self, request, pk):
        hostel_types=HostelType.objects.all().order_by('-id')
        hostel_type=HostelType.objects.get(id=pk)
        form = HostelTypeForm(instance=hostel_type)
        if request.method=='POST':
            form = HostelTypeForm(request.POST, instance=hostel_type)
            if form.is_valid():
               form.save()
               messages.success(request,'Data update successfull',extra_tags='success')
               return redirect('hostel-type-list')
        context={'form':form, 'hostel_types':hostel_types}
        return render(request, 'hosteltype/index.html',context)


class DeleteHostelTypeView(View):
    def get(self, request, pk):
        hostel_type=HostelType.objects.get(id=pk)
        hostel_type.delete()
        messages.success(request,'Data delete successfull',extra_tags='success')
        return redirect('hostel-type-list')


