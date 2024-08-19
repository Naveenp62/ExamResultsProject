from django.urls import path
from app1 import views
urlpatterns=[
    path('result/',views.fun1,name="sr")
]