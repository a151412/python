from rest_framework import serializers
from .models import Squad, atividades, FreezingPeriod

class SquadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Squad
        fields = '__all__'

class AtividadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = atividades
        fields = '__all__'

class FreezingPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreezingPeriod
        fields = '__all__'
