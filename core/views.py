from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView        
from django.views.generic.list import ListView       
from django.views.generic.edit import UpdateView 
from django.views.generic.detail import DetailView 
from django.views.generic.edit import DeleteView
from .models import Post,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User, auth


class PostCreateView(CreateView):
       model = Post

       fields = '__all__'
       template_name = 'create.html'
       success_url = 'index'
       

class PostListView(ListView):
       model = Post
       template_name = 'index.html'
       
       
class PostUpdateView(UpdateView):
       model = Post
       fields = [
              'title',
              'description'
       ]
       template_name = 'update.html'
       success_url = '/'
       
       
class PostDetailView(DetailView):
       model = Post
       template_name = 'detail.html'


class PostDeleteView(DeleteView):
       model = Post
       template_name = 'delete.html'
       success_url = '/'
       
       
def register(request):
       if request.method == "POST":
              first_name = request.POST['first_name']
              last_name = request.POST['last_name']
              username = request.POST['username']
              email = request.POST['email']
              password = request.POST['password']
              password2 = request.POST['password2']
              
              if User.objects.filter(username=username).exists():
                     messages.info(request, 'username taken')
                     return redirect('register')
              elif User.objects.filter(email=email).exists():
                     messages.info(request, 'email already in use. If this is your account, please login')
                     return redirect('register')
              elif password != password2: 
                     messages.error(request, 'Passwords do not match')
                     return redirect('register')
              
              elif not len(password) >=8  : 
                     messages.error(request, 'Password is too short')
                     return redirect('register')
              
              else: 
                     user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email,password=password)
                     user.save()
                     return redirect('login')
       else:
              return render(request, 'register.html')
  
       
def login(request):
       if request.method == "POST":
              username = request.POST['username']
              # email = request.POST['email']
              password = request.POST['password']
              user = auth.authenticate(username=username, password=password)
              if user is not None:
                     auth.login(request, user)
                     # user = Post.objects.get(user=user)
                     return redirect('/')
              
              
              else:
                     messages.info(request,' invalid login credentials')
                     return redirect( 'login')
       # else:
       #        return redirect('/index')
              
       else:
              return render(request, 'login.html')
       
       
def logout(request):
       auth.logout(request)
       return redirect('/')