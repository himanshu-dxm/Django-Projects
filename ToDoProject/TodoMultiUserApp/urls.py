from . import views
from django.urls import path

urlpatterns = [
    path( '' , views.indexM , name="indexM" ),
    path( 'login' , views.login , name="login" ),
    path( 'signup' , views.signup , name="signup" ),
    path( 'addtodo' , views.addtodo , name="addtodo" ),
]
