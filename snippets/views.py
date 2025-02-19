from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.views import View


class SnippetAdd(View):None
#    TODO: Implement this class to handle snippet creation, only for authenticated users.

class SnippetEdit(View): None
#    TODO: Implement this class to handle snippet editing. Allow editing only for the owner.

class SnippetDelete(View): None
#    TODO: Implement this class to handle snippet deletion. Allow deletion only for the owner.


class SnippetDetails(View):
    def get(self, request, *args, **kwargs):
        snippet_id = self.kwargs["id"]
        # TODO: Implement logic to get snippet by ID
        # snippet = Snippet.objects.get(id=snippet_id)
        # Add conditions for private snippets
        return render(
            request, "snippets/snippet.html", {"snippet": snippet}
        )  # Placeholder


class UserSnippets(View):
    def get(self, request, *args, **kwargs):
        username = self.kwargs["username"]
        # TODO: Fetch user snippets based on username and public/private logic
        # snippets = Snippet.objects.filter(...)
        return render(
            request,
            "snippets/user_snippets.html",
            {"snippetUsername": username, "snippets": snippets},
        )  # Placeholder


class SnippetsByLanguage(View):
    def get(self, request, *args, **kwargs):
        language = self.kwargs["language"]
        # TODO: Fetch snippets based on language
        return render(request, "index.html", {"snippets": []})  # Placeholder


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
        # TODO: Fetch and display all public snippets
        return render(request, "index.html", {"snippets": []})  # Placeholder
