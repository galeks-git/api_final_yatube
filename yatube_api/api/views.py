from django.shortcuts import get_object_or_404
from rest_framework import viewsets
# from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
# from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, Group, Follow
from api.serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
from api.permissions import IsAuthorOrReadOnly
from api.pagination import PostsPagination


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    search_fields = ('following',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated, ]
    permission_classes = [IsAuthorOrReadOnly, ]
    # permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    # Даже если на уровне проекта установлен PageNumberPagination
    # Для котиков будет работать LimitOffsetPagination
    # pagination_class = LimitOffsetPagination
    pagination_class = PostsPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]
    permission_classes = [IsAuthorOrReadOnly, ]

    def get_post(self):
        return get_object_or_404(
            Post, pk=self.kwargs.get('post_id')
        )

    def get_queryset(self):
        return self.get_post().comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())
