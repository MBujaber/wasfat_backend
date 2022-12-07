
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView


from recipes.serializer import RecipeListSerializer, CategoryListSerializer, IngredientListSerializer


from recipes.models import Category, Recipe, Ingredient

from recipes.permissions import IsUploader


# ------------- RECIPE VIEWS -------------

class RecipeListView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    # permission_classes=[IsAdminUser]

class RecipeUpdateView(UpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'recipe_id'
    permission_classes = [IsUploader]

class RecipeDeleteView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'recipe_id'


# ------------- CATEGORY VIEWS -------------

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryCreateView(CreateAPIView):
    serializer_class = CategoryListSerializer

    def perform_create(self, serializer):
        serializer.save()


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'



# ------------- INGREDIENT VIEWS -------------

class IngredientListView(ListAPIView):

    serializer_class = IngredientListSerializer

    def get_queryset(self):
        recipes = Recipe.objects.all()

        category = self.request.query_params.get('category')

        if category is not None:
            recipes = Recipe.objects.filter(category__id = category)
        queryset = Ingredient.objects.filter(recipes__in=list(recipes)).distinct()
        
        return queryset


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer

class CategoryCreateView(CreateAPIView):
    serializer_class = CategoryListSerializer

    def perform_create(self, serializer):
        serializer.save()

class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'

class DeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'category_id'

