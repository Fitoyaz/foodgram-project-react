from django.contrib import admin

from .models import Ingredient, Recipe, IngredientRecipe, Subscription, Tag, \
    Favorite, ShoppingList


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color_name')


class RecipeIngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = (RecipeIngredientInline,)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author')

    def get_author(self, obj):
        return obj.author.username


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_author')
    search_fields = ('get_user',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'author')

    def get_user(self, obj):
        return obj.user.username

    def get_author(self, obj):
        return obj.author.username


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_recipe')
    search_fields = ('get_user',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'recipe')

    def get_user(self, obj):
        return obj.user.username

    def get_recipe(self, obj):
        return obj.recipe.name


class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_recipe')
    search_fields = ('get_user',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user', 'recipe')

    def get_user(self, obj):
        return obj.user.username

    def get_recipe(self, obj):
        return obj.recipe.name


# Register your models here.

admin.site.register(Tag, TagAdmin)
admin.site.register(Ingredient)
admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(IngredientRecipe)
admin.site.register(Subscription, SubscriptionAdmin)
