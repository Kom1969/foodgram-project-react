from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientToRecipe, Recipe,
                     ShopCart, Tag)


class IngredientInline(admin.TabularInline):
    """
    Позволяет выводить кол-во ингредиентов в карточке рецепта.
    """
    model = IngredientToRecipe
    extra = 2
    min_num = 1


class RecipeAdmin(admin.ModelAdmin):
    """ Админка управление рецептами """
    list_display = ('name', 'author', 'cooking_time',
                    'in_favorite',)
    list_filter = ('name', 'author', 'tags')
    search_fields = ('name', 'author', 'tags')
    inlines = (IngredientInline,)
    empty_value_display = '-пусто-'

    def in_favorite(self, obj: Recipe):
        return obj.favorites.count()


class IngredientAdmin(admin.ModelAdmin):
    """ Админка управление ингридиентами """
    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    """ Админка управление тегами """
    list_display = ('name', 'color', 'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    """ Админка управление подписками """
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user', 'recipe')
    empty_value_display = '-пусто-'


class ShopCartAdmin(admin.ModelAdmin):
    """ Админка списка покупок """
    list_display = ('recipe', 'user')
    list_filter = ('recipe', 'user')
    search_fields = ('user', )
    empty_value_display = '-пусто-'


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShopCart, ShopCartAdmin)
