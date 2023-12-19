from rest_framework import serializers

from .models import Customer, Vacancy, Task

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Customer


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Vacancy



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Task