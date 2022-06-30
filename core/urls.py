from msilib.schema import ListView
from django.urls import path
from . views import PostCreateView, PostListView, PostUpdateView, PostDeleteView, PostDetailView,register,login

from . import views

urlpatterns = [
       # path('', views.index, name= 'index'),
       path('', PostListView.as_view(), name= 'list'),
       path('create', PostCreateView.as_view(), name= 'create'),
       path('<pk>/detail/', PostDetailView.as_view(), name = 'detail'),
       path('<pk>/update/', PostUpdateView.as_view(), name= 'update'),
       path('<pk>/delete/', PostDeleteView.as_view(), name= 'update'),
       path('register', views.register , name= 'register'),
       path('login', views.login , name= 'login'),
       path('logout', views.logout , name= 'logout'),

]
