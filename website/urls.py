from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    # path('login/', views.login_user, name="login" ),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_user,name='logout'),
    path("navbar/",views.navbar ,name="navbar"),
    path("record/<int:pk>",views.customer_record,name='record'),
     path("delete_record/<int:pk>",views.delete_record,name='delete_record'),
]