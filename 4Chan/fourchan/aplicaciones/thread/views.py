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

	def get_context_data(self, **kwargs):
		return dict(super(CategoryView, self).get_context_data(**kwargs), context=Post.objects.all()[0:100])