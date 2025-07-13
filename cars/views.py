from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required  # Importa o decorador para exigir login
from django.utils.decorators import method_decorator  # Importa o decorador para métodos de classe
from django.urls import reverse_lazy # Importa reverse_lazy para redirecionar após ações



class CarsListView(ListView): # Usando ListView para listar os carros
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars' # Nome do contexto que será usado no template

    def get_queryset(self): # Método para procurar carros com base no termo de busca
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars
    


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'



@method_decorator(login_required(login_url='login'), name='dispatch')  # Exige que o usuário esteja logado para acessar as views abaixo    
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'  # Redireciona para a lista de carros após criar um novo carro

    def form_valid(self, form):
        return super().form_valid(form)  # Chama o método form_valid da classe base para salvar o formulário e redirecionar
    
    

@method_decorator(login_required(login_url='login'), name='dispatch')  # Exige que o usuário esteja logado para acessar as views abaixo
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})  # Redireciona para a página de detalhes do carro atualizado

    def form_valid(self, form):
        return super().form_valid(form)  # Chama o método form_valid da classe base para salvar o formulário e redirecionar



@method_decorator(login_required(login_url='login'), name='dispatch')  # Exige que o usuário esteja logado para acessar as views abaixo    
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'  # Redireciona para a lista de carros após excluir um carro

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)  # Redireciona para o método post para confirmar a exclusão