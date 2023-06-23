from django.shortcuts import render, redirect,get_object_or_404
# from .models import parcels,carrier
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import logout, get_user
from .models import Post
from django.views.generic import ListView


# def index(request):
#     return render(request, 'home.html')

class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'