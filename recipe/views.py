from django.shortcuts import render
from .models import RecipeModel
from .serializers import RecipeSerializer
# Rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets

# Create your views here.


class RecipeListView(viewsets.ModelViewSet):
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeSerializer
    def retrieve(self,request,pk):
        try:
            book = RecipeModel.objects.get(pk=pk)
        except:
            return Response({"error":"Revcipe Not Found"},status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeSerializer(book)
        return Response(serializer.data)

class CreateRecipeView(viewsets.ViewSet):
    def create(self,request):
        serializer=RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data  created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class RecipeUpdateView(viewsets.ModelViewSet):
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeSerializer
    def update(self,request,*args, **kwargs):
        try:
            recipe = self.get_object()

            serializer = RecipeSerializer(instance=recipe,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Recipe Updated','data':serializer.data}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({"error":"There is no recipe with is primary key"},status=status.HTTP_404_NOT_FOUND)
    
        return Response({"error":"Something wrong"},status=status.HTTP_400_BAD_REQUEST)
    
    # patch method
    def partial_update(self, request, *args, **kwargs):
        try:
            recipe = self.get_object()
            serializer = RecipeSerializer(recipe, data=request.data, partial=True)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        except:
            return Response({'error':'There is no Recipe with this primary key'},status=status.HTTP_404_NOT_FOUND)
    
class BookDeleteView(viewsets.ModelViewSet):
    queryset = RecipeModel.objects.all()
    serializer_class = RecipeSerializer
    def destroy(self, request, *args, **kwargs):
        try:
            recipe = self.get_object()
            self.perform_destroy(recipe)
            return Response({'msg':'recipe Deleted','data':recipe}, status=status.HTTP_202_ACCEPTED)
        except:
            return Response({"error":"There is no recipe with is primary key"},status=status.HTTP_404_NOT_FOUND)
        
