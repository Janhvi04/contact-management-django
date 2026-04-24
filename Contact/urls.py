from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add/',views.add, name='add_contact'),
    path('list/', views.contact_list, name='contact_list'),
    path('update/<int:id>/', views.update_contact , name='update_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
]