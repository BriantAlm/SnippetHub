from django.views import View
from django.urls import reverse
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import redirect, render, redirect

from .models import Snippet
from .forms import SnippetForm


class SnippetAdd(LoginRequiredMixin, CreateView):
    model = Snippet
    form_class = SnippetForm
    template_name = "snippets/snippet_add.html"
    extra_context = {"action": "Cargar"}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.get_absolute_url()

class SnippetEdit(LoginRequiredMixin, UpdateView):
    model = Snippet
    form_class = SnippetForm
    template_name = "snippets/snippet_add.html"
    extra_context = {"action": "Editar"}
    pk_url_kwarg = "id"

    def get_success_url(self):
        return self.object.get_absolute_url()


class SnippetDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Snippet
    template_name = "snippets/snippet_delete.html"
    pk_url_kwarg = "id"
    
    def test_func(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        snippet = self.get_object()
        return reverse("user_snippets", args=[snippet.user.username])
    
    def delete(self, request, *args, **kwargs):
        snippet = self.get_object()
        breakpoint()
        username = snippet.user.username
        response = super().delete(request, *args, **kwargs)
        return redirect("user_snippets", username=username)


class SnippetDetails(DetailView):
    model = Snippet
    template_name = "snippets/snippet.html"
    context_object_name = "snippet"
    pk_url_kwarg = 'id'


class UserSnippets(View):
    model = Snippet
    queryset = Snippet.objects.all()

    def get(self, request, *args, **kwargs):
        user = request.user
        username = self.kwargs["username"]
        snippets = self.queryset.filter(user__username=username, public=True)
        if user.is_authenticated and user.username == username:
            snippets = self.queryset.filter(user__username=username)
        return render(
            request,
            "snippets/user_snippets.html",
            {"snippetUsername": username, "snippets": snippets},
        )


class SnippetsByLanguage(View):
    model = Snippet

    def get(self, request, *args, **kwargs):
        user = request.user
        language = self.kwargs["language"]
        snippets = self.model.objects.filter(language__slug=language, public=True)
        return render(request, "index.html", {"snippets": snippets})


class Login(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
        return render(request, 'login.html', {'form': form})


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class Index(View):
    def get(self, request, *args, **kwargs):
        snippets = Snippet.objects.filter(public=True)
        return render(request, "index.html", {"snippets": snippets})
