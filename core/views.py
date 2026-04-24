from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout
from validate_docbr import CPF

User = get_user_model()

def cpf_valido(cpf):
    cpf_clean = ''.join(filter(str.isdigit, cpf))
    return CPF().validate(cpf_clean)

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        cpf = request.POST.get("cpf")

        if not username or not cpf:
            return render(request, "register.html", {"error": "Preencha tudo"})

        cpf_clean = ''.join(filter(str.isdigit, cpf))

        if not CPF().validate(cpf_clean):
            return render(request, "register.html", {"error": "CPF inválido"})

        if User.objects.filter(cpf=cpf_clean).exists():
            return render(request, "register.html", {"error": "CPF já cadastrado"})

        User.objects.create_user(
            username=username,
            password=cpf_clean,
            cpf=cpf_clean
        )

        return render(request, "register.html", {"success": "Usuário criado!"})

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        cpf = request.POST.get("cpf")

        if not username or not cpf:
            return render(request, "login.html", {"error": "Preencha tudo"})

        try:
            user = User.objects.get(username=username, cpf=cpf)
            login(request, user)
            return redirect("/")
        except User.DoesNotExist:
            return render(request, "login.html", {"error": "Dados inválidos"})

    return render(request, "login.html")

def home(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect("/login/")