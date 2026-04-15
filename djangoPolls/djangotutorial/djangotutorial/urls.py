
from django.contrib import admin
from django.urls import path
from djangoPolls.djangotutorial.polls import views
from polls import polls,urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name ="index")
]
