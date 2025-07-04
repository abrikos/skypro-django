from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from . import forms
load_dotenv()

# Create your views here.
class BlogListView(ListView):
    """Posts list"""
    model = Post
    template_name = 'posts.pug'
    def get_queryset(self):
        return Post.objects.filter(published=True)

class BlogDetailView(DetailView):
    """Posts view"""
    model = Post
    template_name = 'view.pug'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views += 1
        obj.save()
        return obj

    def get_context_dataBAK(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'].views += 1
        context['post'].save()
        views = 100
        if context['post'].views > views:
            msg = MIMEMultipart()
            msg['Subject'] = f'Posts views more than {views}'
            msg['From'] = os.getenv('MAIL_USER')
            msg['To'] = os.getenv('EMAIL')
            msg.attach(MIMEText('Congratulations!!','plain'))
            server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
            server.login(os.getenv('MAIL_USER'), os.getenv('MAIL_PASSWORD'))
            text = msg.as_string()
            server.sendmail(os.getenv('MAIL_USER'), os.getenv('EMAIL'), text)
            server.quit()
        return context

class BlogDeleteView(DeleteView):
    """Posts delete"""
    model = Post
    template_name = 'view.pug'
    success_url = reverse_lazy('blog_posts')

class BlogCreateView(CreateView):
    """Add Post"""
    model = Post
    form_class = forms.BlogPostForm
    template_name = 'add.pug'
    success_url = reverse_lazy('blog_posts')

class BlogUpdateView(UpdateView):
    """Post update"""
    model = Post
    form_class = forms.BlogPostForm
    template_name = 'add.pug'
    def get_success_url(self):
        return reverse_lazy('blog_view', kwargs={'pk': self.object.pk})



