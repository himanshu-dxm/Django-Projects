
from django.urls import path
from . import views

urlpatterns = [
    path('',views.myfunctioncall,name="index"),
    path('about',views.myfunctionabout,name="about"),
    path('add/<int:a>/<int:b>',views.add,name='add'),
    path('intro/<str:name>/<int:age>',views.intro,name="intro"),
    path('firstpage',views.firstPage,name='firstapage'),
    path('secondpage',views.secondPage,name="secondpage"),
    path('thirdpage',views.thirdPage,name="thirdpage"),
    path('imagepage',views.imagePage,name="imagepage"),
    path('form',views.form,name="form"),
    path('submitform',views.submitForm,name="submitform"),
    path('form2',views.form2,name="form2"),
]
