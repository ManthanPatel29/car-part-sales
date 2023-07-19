from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .models import part_info


# Create your views here.
class home(View):
    def get(self, request):
        return render(request, 'insert_part.html')

class insert_part(View):
    def post(self, request):
        part = part_info()
        part.name = request.POST.get('part_name')
        part.car_name = request.POST.get('car_name')
        part.brand_name = request.POST.get('brand_name')
        part.category = request.POST.get('category')
        part.description = request.POST.get('desc')
        part.is_new = request.POST.get('is_new')
        part.owner_info = self.request.user
        part.save(self)
        return HttpResponseRedirect('../list-part/')

class list_part(View):
    def get(self, request):
        all_data = part_info.objects.filter(owner_info=self.request.user)
        if all_data is not None:
            data = []
            for i in all_data:
                one_data = {}
                one_data["id"] = i.id
                one_data["name"] = i.name
                one_data["car_name"] = i.car_name
                one_data["brand_name"] = i.brand_name
                one_data["category"] = i.category
                one_data["desc"] = i.description
                one_data["is_new"] = i.is_new
                one_data["owner_name"] = i.owner_info
                data.append(one_data)
        return render(request, 'list_part.html', {"data":data})
    
class update_list(View):
    def get(self, request, *args, **kwargs):
        all_data = part_info.objects.filter(id= kwargs["pk"])
        if all_data is not None:
            one_data = {}
            for i in all_data:
                one_data["id"] = i.id
                one_data["name"] = i.name
                one_data["car_name"] = i.car_name
                one_data["brand_name"] = i.brand_name
                one_data["category"] = i.category
                one_data["desc"] = i.description
                one_data["is_new"] = i.is_new
        return render(request, 'update_list.html', one_data)
    def post(self, request):
        part = part_info()
        all_data = part_info.objects.get(id= kwargs["pk"])
        if all_data is not None:
            all_data.name = request.POST.get('part_name')
            all_data.car_name = request.POST.get('car_name')
            all_data.brand_name = request.POST.get('brand_name')
            all_data.category = request.POST.get('category')
            all_data.description = request.POST.get('desc')
            all_data.is_new = request.POST.get('is_new')
            all_data.save(update_fields=['name','car_name','brand_name','category','description','is_new'])
        return HttpResponseRedirect('../list-part/')

class delete_list(View):
    def get(self, request, *args, **kwargs):
        all_data = part_info.objects.filter(id= kwargs["pk"]).delete()
        return HttpResponseRedirect('../list-part/')