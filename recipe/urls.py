from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RecipeListView,CreateRecipeView,BookUpdateView,BookDeleteView


router = DefaultRouter()

router.register('list',RecipeListView)
router.register('create',CreateRecipeView,basename='create')
router.register('update',BookUpdateView,basename='update')
router.register('delete',BookDeleteView,basename='Delete')
urlpatterns = [
    path('',include(router.urls)),
]