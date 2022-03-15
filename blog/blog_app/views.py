from django.shortcuts import render, get_object_or_404, reverse, redirect, HttpResponse
from django.urls import reverse_lazy
from .models import Blog, Profile
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView, ListView
from django.utils.decorators import method_decorator
from .forms import BlogCreateForm
from django.contrib.auth.mixins import LoginRequiredMixin



class ListBlog(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog_app/home.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class MyBlog(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog_app/my_blogs.html'
    context_object_name = 'blogs'
    
    def get_object(self):
        return Blog.objects.filter(user=self.request.user)


class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogCreateForm
    template_name = 'blog_app/create_blog.html'
    success_url = reverse_lazy('home')
    
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CreateBlog, self).form_valid(form)



class BlogDetail(DetailView):
    model = Blog
    template = 'blog_app/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user
        context['blog_owner_profil'] = self.object.user.profile
        return context

        


class EditBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'blog_app/edit_blog.html'
    fields = ['title', 'content']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class DeleteBlog(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'blog_app/delete_blog.html'
    success_url = reverse_lazy('home')



class ViewProfile(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'blog_app/profile.html'
    context_object_name = 'profile'
    
    


class EditProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ('name', 'address', 'phone_no', 'bio', 'image')
    template_name = 'blog_app/edit_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
    def get_success_url(self):
        pk = self.request.user.profile.id
        return reverse_lazy('profile', kwargs={'pk': pk})  


