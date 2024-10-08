from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.loginview,name='login'),
    path('logout',views.logoutview,name='logout'),
    path('post',views.post,name='post'),
    path('profile',views.profile,name='profile'),
    path('single/<int:n>',views.single,name='single'),
    path('delete/<int:n>',views.deleteview,name='delete'),
    path('update/<int:n>',views.updateview,name='update'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)