from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = 'Пользователю не хватает прав для выполнения операции.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsUserOrReadOnly(permissions.BasePermission):
    message = 'Пользователю не хватает прав для выполнения операции.'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
