from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('submit',views.submit,name="submit"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('list',views.list,name="list"),
    path('add',views.add,name="add"),
    path('sortdata',views.sortdata,name="sortdata"),
    path('search',views.search,name="search"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
]
