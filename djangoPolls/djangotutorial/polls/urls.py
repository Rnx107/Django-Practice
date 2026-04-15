from django.urls import path

from polls import views


urlpatterns=[
    path('home/', views.index, name ="index")
]