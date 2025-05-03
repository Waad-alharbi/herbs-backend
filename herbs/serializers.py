from rest_framework import serializers
from .models import Category, Herb, HealthTracker
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  

class HerbSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        allow_empty=True,
        required=False
    )

    class Meta:
        model = Herb
        fields = ['id', 'name', 'uses', 'preparation', 'warnings', 'image_url', 'category']
#https://stackoverflow.com/questions/31820389/can-to-representation-in-django-rest-framework-access-the-normal-fields
#https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    def to_representation(self, instance):
        represent = super().to_representation(instance)
        represent['category'] = CategorySerializer(instance.category.all(), many=True).data
        return represent
    
class HealthTrackerSerializer(serializers.ModelSerializer):
    herb_name = serializers.CharField(source='herb.name', read_only=True)
    class Meta:
        model = HealthTracker
        fields = ['id', 'herb', 'herb_name','perceived_effectiveness', 'side_effects', 'comment', 'date']