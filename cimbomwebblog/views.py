from typing import List
from django.views.generic import DetailView, FormView, ListView
from .models import Category, Players, Post
from .forms import AddPostForm
from django.shortcuts import get_object_or_404, render 
from django.db.models import Q


class HomePageView(ListView):
    http_method_names = ["get"]
    template_name = "index.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('-id')[0:12]
    paginate_by = 6



class PostDetailView(DetailView):
    template_name = "post.html"
    model = Post


class AddPostView(FormView):
    template_name = "add_post.html"
    form_class = AddPostForm
    success_url = "/"

    def form_valid(self, form):
        context = {}

        form = AddPostForm(self.request.POST or None, self.request.FILES or None)

        if form.is_valid():
            
            item = form.save(commit=False)
            item.author = self.request.user
            item.save()

        context['form'] = form
        return render(self.request, "index.html", context)

    
  

    


class CategoryView(ListView):
    template_name = "category.html"
    model = Post
    context_object_name = "catlist"

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context


class SearchView(ListView):
    model = Post
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )
        return object_list
    
class PlayersView(ListView):
    http_method_names = ["get"]
    template_name = "players.html"
    model = Players
    context_object_name = "players"
    queryset = Players.objects.all().order_by('id')
 

   






