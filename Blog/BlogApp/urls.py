from . import views
from django.urls import path

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('contact/',views.Contact.as_view(),name='contact'),
    path('login/',views.Login.as_view(),name='login'),
    path('register/',views.Register.as_view(),name='register'),
    path('logout/',views.Logout,name='logout'),

    # Admin urls
    path('usr/<int:id>/new_category',views.NewCategory.as_view(), name='new_category'),
    path('usr/<int:id>/all_category',views.AllCategory.as_view(), name='all_category'),
    path('usr/<int:id>/edit_category/<int:cid>',views.EditCategory.as_view(), name='edit_category'),
    path('usr/<int:id>/delete_category/<int:cid>',views.DeleteCategory.as_view(), name='delete_category'),
    
]