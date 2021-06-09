from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import UserCreate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *

class Home(View):
    def get(self,request):
        return render(request, 'BlogApp/home.html')
    # def post(self)

class Contact(View):
    def get(self,request):
        return render(request,'BlogApp/contact.html')

class Login(View):
    def get(self,request):
        return render(request, 'BlogApp/login.html')
    def post(self, request):
        user = authenticate(request, username=request.POST['inputEmail'], password=request.POST['inputPassword'])
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('userhome',id=user.id)
            elif user.is_active:
                return redirect('userhome',id=user.id)
            else:
                return redirect('login')    
        else:
            return redirect('login')


class Register(View):
    def get(self, request):
        user_create = UserCreate()
        context = {'user_create':user_create}
        return render(request, 'BlogApp/register.html', context)

    def post(self, request):
        user_create = UserCreate(request.POST)
        if user_create.is_valid():
            user_create = user_create.save(commit=False)
            user_create.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
        else:
            # messages.errors(request, user_create_form.errors)
            context = {'user_create':user_create}
            return render(request, 'BlogApp/register.html',context)

def Logout(request):
    logout(request)
    return redirect('home')  

class NewCategory(View, LoginRequiredMixin):
    def get(self, request, **kwargs):
        new_category = CreateCategory()
        context={'new_category':new_category, 'id':kwargs['id']}
        return render(request, 'BlogApp/category.html',context)
    
    def post(self, request, **kwargs):
        new_category = CreateCategory(request.POST)
        if new_category.is_valid():
            new_category = new_category.save(commit=False)
            new_category.save()
            return redirect('all_category', kwargs['id'])
        else:
            context={'new_category':new_category, 'id': kwargs['id']}
            return render(request, 'BlogApp/category.html', context)


class AllCategory(View, LoginRequiredMixin):
    def get(self, request, **kwargs):
        all_category = Category.objects.all()
        context={'all_category':all_category, 'id':kwargs['id']}
        return render(request, 'BlogApp/all_category.html',context)

class EditCategory(View, LoginRequiredMixin):
    def get(self, request, **kwargs):
        category = Category.objects.get(id=kwargs['cid'])
        edit_category = CreateCategory(instance = category)
        context = {'new_category':edit_category, 'id':kwargs['id']}
        return render(request, 'BlogApp/category.html', context)
    def post(self, request, **kwargs):
        category = Category.objects.get(id=kwargs['cid'])
        edit_category = CreateCategory(request.POST, instance = category)
        if edit_category.is_valid():
            edit_category = edit_category.save(commit = False)
            edit_category.save()
            return redirect('all_category', id=kwargs['id'])
        else:
            edit_category = CreateCategory(request.POST, instance=category)
            context={'new_category':edit_category, 'id':kwargs['id']}
            return render(request, 'BlogApp/category.html', context)

class DeleteCategory(LoginRequiredMixin, View):
    def get(self, request,**kwargs):
        Category.objects.get(id=kwargs['cid']).delete()
        all_category = Category.objects.all()
        context = {'all_category':all_category, 'id':kwargs['id']}
        return redirect('all_category', context['id'])