from django.contrib import admin
from .models import Dish, Table


class AdminDish(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price',)
    search_fields = ('name', 'description')


class AdminTable(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Dish, AdminDish)
admin.site.register(Table, AdminTable)