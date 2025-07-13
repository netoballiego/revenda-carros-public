from django.db import models

# Criando a classe Marca que herda de models.Model
# Essa classe representa a tabela marcas no banco de dados
class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Criando a classe Carro que herda de models.Model
# Essa classe representa a tabela carros no banco de dados
class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # PROTECT significa que não podemos excluir uma marca se houver carros associados a ela
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)  # O upload_to define o diretório onde as fotos serão armazenadas
    bio = models.TextField(blank=True, null=True)  # Campo de texto para descrição do carro, maior que o CharField
    
    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    cars_count = models.IntegerField(default=0)  # Contador de carros no inventário
    cars_value = models.FloatField(default=0.0)  # Valor total dos carros no inventário
    created_at = models.DateTimeField(auto_now=True)  # Data e hora da última atualização do inventário, auto_now=True atualiza o campo sempre que o objeto é salvo

    class Meta:
        ordering = ['-created_at']  # Ordena os registros do inventário pela data de criação, do mais recente para o mais antigo

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value} - {self.created_at.strftime("%Y-%m-%d %H:%M:%S")}'
