from . import views
from django.urls import path
from . import views
urlpatterns = [
   path('usr/<int:id>/', views.RegUser.as_view() , name='userhome'), 
   path('usr/<int:id>/new_blog/',views.NewBlog.as_view(), name='new'),
   path('usr/<int:id>/my_blog/',views.MyBlog.as_view(), name='my_blog'),
   path('usr/<int:id>/all_blog/',views.AllBlog.as_view(), name='all_blog'),
   path('usr/<int:id>/edit_blog/<int:bid>',views.EditBlog.as_view(), name='edit_blog'),
   path('usr/<int:id>/delete_blog/<int:bid>',views.DeleteBlog.as_view(), name='delete_blog'),
]