from django.views.generic.edit import CreateView
from .models import Post, Category
from django.shortcuts import render 
from .forms import PostForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, HttpResponse

def is_valid_queryparam(param):
	return param != '' and param is not None


class ThreadView(CreateView):
	template_name = "thread/thread.html"
	form_class = PostForm
	success_url = reverse_lazy('thread')
	post1 = Post.objects.all()
	http_method_names = ['post']
	if http_method_names('c1'):
		categoria1 = http_method_names.get('c1')
		post1 = post.filter(categories__gte="1")
	def get_context_data(self, **kwargs):
		return dict(super(ThreadView, self).get_context_data(**kwargs), context=Post.objects.all()[0:100])


def FilterView(resquest):
	post = Post.objects.all()
	categoria = resquest.GET.get('categories')
	form = PostForm

	if is_valid_queryparam(categoria):
		post = post.filter(categories=categoria)


	context = {
		'queryset': post
	}
	return render(resquest, "thread/categoria.html", context)


class CategoryView(CreateView):
	template_name = "thread/categoria.html"
	form_class = PostForm
	success_url = reverse_lazy('categoria')

 #creo que si cambio el fiel de name por un foregkey creo q puedo buscar por el id
	def get_context_data(self, **kwargs):

		#quiero hacer un if de un post request pero para eso tengo q crear unos botones con ese metodo
		return dict(super(CategoryView, self).get_context_data(**kwargs), context=Post.objects.filter(name__gte="1")[0:100])