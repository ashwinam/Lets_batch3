from django.shortcuts import render,redirect, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post, Comment as CommentModel
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='Login')
def Allpost(request,page=1):
	posts = Post.objects.all()
	p1 = Paginator(posts,3)  #3 posts per page 
	posts = p1.page(page)

	context = {'posts': posts}
	return render(request,'blog/all_posts.html', context)

@login_required(login_url='Login')
def CreatePost(request):
	form = PostForm 
	context = {'form': form, 'legend': 'Post Now'}

	if request.method =='POST':
		form = PostForm(request.POST)
		if form.is_valid():
			mark1 = form.save(commit=False)
			mark1.author = request.user
			form.save()
			return redirect('AllPost')

	return render(request, 'blog/createpost.html', context)

@login_required(login_url='Login')
def SpecificPost(request,id1):
	post = Post.objects.filter(id=id1)[0] #select * from blog_post where id=1;
	context = {'post': post}
	return render(request,'blog/onepost.html', context)

# Class Based View ########
##############################
###########################
from django.views.generic import CreateView, DetailView, ListView, UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	fields = ['title','content']
	template_name = 'blog/createpost.html'
	login_url = '/login/'

	def form_valid(self, form ):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostDetailView(LoginRequiredMixin,DetailView):
	model = Post
	template_name = 'blog/onepost_cls.html'
	context_object_name = 'post1'
	login_url = '/login/'


class PostListView(LoginRequiredMixin,ListView):
	model = Post
	context_object_name = 'posts'    # Post.objects.all()
	template_name = 'blog/all_posts_cls.html'   
	paginate_by =3
	ordering = ['-date1']
	login_url = '/login/'

class UserPostListView(LoginRequiredMixin,ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/all_posts_cls.html'
	paginate_by =2 
	ordering = ['-date1']
	login_url = '/login/'

	def get_queryset(self):
		return Post.objects.filter(author=self.request.user)


class OtherUserPostListView(LoginRequiredMixin,ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'blog/all_posts_cls.html'
	paginate_by =2 
	ordering = ['-date1']
	login_url = '/login/'

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('u1'))
		return Post.objects.filter(author=user)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
	model = Post
	fields = ['title','content']
	template_name = 'blog/createpost.html'
	login_url = '/login/'

	def form_valid(self, form ):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		print (post,type(post))
		if self.request.user== post.author:
			return True 
		return False 

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Post 
	success_url = "/blog/post/view/"

	def test_func(self):
		post = self.get_object()
		print (post,type(post))
		if self.request.user== post.author:
			return True 
		return False 

def CommentPost(request, id1):    # Post id not comment id 
	form = CommentForm()
	post = Post.objects.filter(id=id1)[0]
	comments = post.comment.all()

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			mark1 = form.save(commit=False)
			mark1.post = post 
			mark1.author = request.user 
			form.save()
	context = {'form':form, 'post1': post, "comments" : comments}

	return render(request,'blog/onepost_function_comment.html', context)


def comment_approve(request,id1):  # id1 is comment id not post id 
	comment = get_object_or_404(CommentModel, id=id1)
	comment.approve()
	return redirect('post-comment', id1= comment.post.id )   # post id 
