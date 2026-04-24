from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login

User = get_user_model()

def register(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        password = request.POST.get("password")

        if not cpf or not password:
            return render(request, "register.html", {"error": "Preencha tudo"})

        User.objects.create_user(
            username=cpf,
            password=password,
            cpf=cpf
        )

        return render(request, "register.html", {"success": "Usuário criado!"})

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=cpf,
            password=password
        )

        if user:
            login(request, user)
            return render(request, "home.html", {"success": "Login feito com sucesso!"})
        else:
            return render(request, "login.html", {"error": "Credenciais inválidas"})

    return render(request, "login.html")

from django.shortcuts import render

def home(request):
    return render(request, "home.html")