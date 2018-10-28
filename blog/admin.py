from django.contrib import admin
from .models import Category, Post

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')
    date_hierarchy = 'published'
    # para el list filter crear os filtros por campos relacionados, dos rayas abajo y la coumna que quiero filtrar
    list_filter = ('author__username', 'categories__name', )

    # campos personalizados
    def post_categories(self, obj):
        """
        :param obj: variable de objeto para iterarla
        :return: cadena de caracteres creada a partir de una funcion
        """
        return ', '.join([c.name for c in obj.categories.all().order_by('name')])
    post_categories.short_description = 'Categorias'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)



