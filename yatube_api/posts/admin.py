from django.contrib import admin

from .models import Comment, Group, Post, Follow


# class PostAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'text', 'pub_date', 'author')
#     search_fields = ('text',)
#     list_filter = ('pub_date',)
#     empty_value_display = '-пусто-'


# admin.site.register(Post, PostAdmin)
# admin.site.register(Group)
# admin.site.register(Comment)


class PostAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    # Содержимое поля group можно редактировать в админке
    list_editable = ('group',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('pub_date', 'group', 'author',)
    empty_value_display = '-пусто-'


class GroupAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', 'slug', 'description',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title', 'slug', 'description',)
    empty_value_display = '-пусто-'


class CommentAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'text', 'created', 'author', 'post',)
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('text',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('created', 'author',)
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'user', 'following',)
    # Добавляем возможность фильтрации по дате
    list_filter = ('user', 'following',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Follow, FollowAdmin)
