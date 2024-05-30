from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RecipeListView,CreateRecipeView,RecipeUpdateView,RecipeDeleteView


router = DefaultRouter()

router.register('list',RecipeListView)
router.register('create',CreateRecipeView,basename='create')
router.register('update',RecipeUpdateView,basename='update')
router.register('delete',RecipeDeleteView,basename='Delete')
urlpatterns = [
    path('',include(router.urls)),
]