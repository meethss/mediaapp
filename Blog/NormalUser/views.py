from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import BlogCreateForm
from BlogApp.models import Category
from .models import Blog

from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.
class RegUser(LoginRequiredMixin,View):
    def get(self,request,**kwargs):
        context ={'id':kwargs['id']}
        return render(request, 'NormalUser/home.html', context)

class NewBlog(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        new_blog = BlogCreateForm()
        context = {'new_blog':new_blog, 'id':kwargs['id'], 'catogerys':Category.objects.all()}
        return render(request, 'NormalUser/new.html', context)
    
    def post(self, request, **kwargs):
        new_blog = BlogCreateForm(request.POST)
        if new_blog.is_valid():
            new_blog = new_blog.save(commit = False)
            new_blog.owner = User.objects.get(id=kwargs['id'])
            new_blog.save()
            return redirect('userhome', id=kwargs['id'])
        else:
            new_blog = BlogCreateForm(request.POST)
            context={'new_blog':new_blog, 'id':kwargs['id']}
            return render(request, 'NormalUser/new.html', context)

class MyBlog(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        my_blog = Blog.objects.filter(owner = kwargs['id'])
        context = {'my_blog': my_blog, 'id':kwargs['id']}
        return render(request, 'NormalUser/my_blog.html', context)


class AllBlog(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        all_blog = Blog.objects.filter(~Q(owner =kwargs['id']))
        context = {'all_blog': all_blog, 'id':kwargs['id']}
        return render(request, 'NormalUser/all_blog.html', context)

class EditBlog(LoginRequiredMixin, View):
    def get(self, request, **kwargs):
        blog = Blog.objects.get(id=kwargs['bid'])
        edit_blog = BlogCreateForm(instance = blog)
        context = {'new_blog':edit_blog, 'id':kwargs['id'], 'catogerys':Category.objects.all()}
        return render(request, 'NormalUser/new.html', context)
    def post(self, request, **kwargs):
        blog = Blog.objects.get(id=kwargs['bid'])
        edit_blog = BlogCreateForm(request.POST, instance=blog)
        if edit_blog.is_valid():
            new_blog = edit_blog.save(commit = False)
            new_blog.owner = User.objects.get(id=kwargs['id'])
            new_blog.save()
            return redirect('userhome', id=kwargs['id'])
        else:
            new_blog = BlogCreateForm(request.POST, instance=blog)
            context={'new_blog':new_blog, 'id':kwargs['id'], 'catogerys':Category.objects.all()}
            return render(request, 'NormalUser/new.html', context)

class DeleteBlog(LoginRequiredMixin, View):
    def get(self, request,**kwargs):
        blog = Blog.objects.get(id=kwargs['bid']).delete()
        my_blog = Blog.objects.filter(owner = kwargs['id'])
        context = {'my_blog': my_blog, 'id':kwargs['id']}
        return redirect('my_blog',context['id'])
