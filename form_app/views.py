from typing import Any
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from form_app.models import *
from django.views import View
from form_app.form import *
from django.views.generic.edit import CreateView 
from django.views.generic.base import TemplateView
from django.views.generic import ListView
# Create your views here.

def index(request):
    return render(request,"base.html",{})

class Login_page(CreateView):
    def get(self,request):
        form = Login_form()
        return render(request,'login.html',{'form':form})
    
    def post(self,request):
        form = Login_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thank_you')
        return render(request,'login.html',{'form':form})

# class Thank_youView(View):
#     def get(self,request):
#         return render(request,'thank_you.html')

# def thank_you(request):
#     return render(request,'thank_you.html')
    
class Thank_youView(TemplateView):
    template_name = 'thank_you.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['message'] = "This works fine!"
        return context
    
# class Login_lists(TemplateView):
#     template_name = 'login_list.html'

#     def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         login_list = Login.objects.all()
#         context['login_list'] = login_list
#         return context
    
class Login_lists(ListView):
    template_name = 'login_list.html'
    model = Login