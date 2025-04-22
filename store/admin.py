from django.contrib import admin
from .models import Genre, Developer, Game, Order, OrderItem

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'founded']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['game']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'created', 'updated', 'paid']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['title', 'developer', 'price', 'release_date', 'available']
    list_filter = ['available', 'created', 'updated', 'developer']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'description']
    filter_horizontal = ['genres']

