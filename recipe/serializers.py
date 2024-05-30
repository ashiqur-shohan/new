from rest_framework import serializers
from .models import RecipeModel

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecipeModel
        fields = "__all__"
