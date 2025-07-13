from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from cars.models import Car, CarInventory
from django.db.models import Sum
from openai_api.client import get_car_ai_bio # Importa a função para gerar biografia de carro por meio da API OpenAI

def car_inventory_update(): # Função para atualizar o inventário de carros
    cars_count = Car.objects.all().count()
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value']

    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )


@receiver(post_save, sender=Car)  # Conecta o sinal post_save ao modelo Car
def car_post_save(sender, instance, **kwargs):
    car_inventory_update() # Chama a função criada para atualizar o inventário de carros após salvar um Car
    


@receiver(post_delete, sender=Car)  # Conecta o sinal post_delete ao modelo Car
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()



@receiver(pre_save, sender=Car) 
def car_pre_save(sender, instance, **kwargs): # Gera a biografia do carro antes de salvar por meio da API OpenAI
    if not instance.bio:
        ai_bio = get_car_ai_bio(instance.model, instance.brand, instance.model_year)
        instance.bio = ai_bio