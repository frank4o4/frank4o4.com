from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.BlogListView.as_view(), name="BlogListView"),
    path('admin/', admin.site.urls),
]
