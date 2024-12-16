from django.contrib import admin
from .models import Banner, Houses, MiniCards, Reviews, OurAgents, Footer, Advantages, Numbers


admin.site.register(Banner)


@admin.register(Houses)
class HousesAdmin(admin.ModelAdmin):
    list_display = ('image', 'price', 'addres', 'state', 'first_description', 'second_description')
    search_fields = ('addres', 'price', 'state')  # Можно добавить поля для поиска


@admin.register(MiniCards)
class MiniCardsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'star', 'profession', 'description', 'image')  # Здесь есть поля для отображения
    search_fields = ('name', 'profession')


@admin.register(OurAgents)
class OurAgentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'profession', 'image')
    search_fields = ('name', 'profession')


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('addres', 'number1', 'number2', 'mail')  # Поля для отображения
    search_fields = ('addres', 'number1', 'mail')


@admin.register(Advantages)
class AdvantagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')
    search_fields = ('title', 'description')


@admin.register(Numbers)
class NumbersAdmin(admin.ModelAdmin):
    list_display = ('number', 'description')
    search_fields = ('number', 'description')
