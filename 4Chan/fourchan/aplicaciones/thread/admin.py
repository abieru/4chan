from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    


class PostAdmin(admin.ModelAdmin):
    #para mostrar en lectura la creación y edición 
    readonly_fields = ('created', 'updated')  
    #para mostrar en pantalla por fila    
    list_display = ('published',)
    #para ordenar
    ordering = ('published',)
    #metodos para busqueda en el panel de admin
    search_fields = ('content',)
    #para jerarquizar la busqueda por fechas
    date_hierarchy = 'published'
    #par filtrar las busquedas


    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name") ])
    post_categories.short_description = "Categorias"




admin.site.register(Category, CategoryAdmin)

admin.site.register(Post, PostAdmin) 