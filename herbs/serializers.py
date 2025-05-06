from rest_framework import serializers
from .models import Category, Herb, HealthTracker
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
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
#https://stackoverflow.com/questions/51940976/django-rest-framework-currentuserdefault-with-serializer
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = HealthTracker
        fields = ['id', 'user', 'herb', 'herb_name', 'perceived_effectiveness', 'side_effects', 'comment', 'date']
        read_only_fields = ['user']




class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['is_staff'] = user.is_staff

        return token
    
