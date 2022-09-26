from rest_framework import serializers
from .models import PpAgent, PricingModel, DiscountsModel
# 1 Serializer
class PpAgentSerializer(serializers.Serializer):
    surname = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return PpAgent.objects.create(validated_data)

    def update(self, instance, validated_data):
        instance.surname = validated_data.get('surname', instance.surname)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save
        return instance
    
# 2 model serializer

class PpAgentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PpAgent
        fields = ['id', 'surname', 'last_name']

class PricingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingModel
        fields = ['name', 'base_fare', 'cancellation_fee', 'is_active']

class DiscountsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountsModel
        fields = '__all__'