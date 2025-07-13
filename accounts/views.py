from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')  # Redireciona para a lista de carros após o registro
    else:
        user_form = UserCreationForm()  # Apenas cria novo formulário se for GET

    return render(request, 'register.html', {'user_form': user_form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') # Obtendo o nome de usuário do formulário
        password = request.POST.get('password') # Obtendo a senha do formulário
        user = authenticate(request, username=username, password=password) # Verifica se o usuário existe e a senha está correta
        if user is not None:
            login(request, user)  # Faz o login do usuário
            return redirect('cars_list')
    
    else:

        login_form = AuthenticationForm()
        return render (request, 'login.html', {'login_form': login_form})
    
def logout_view(request):
    logout(request)
    return redirect('cars_list')  # Redireciona para a lista de carros após o logout

