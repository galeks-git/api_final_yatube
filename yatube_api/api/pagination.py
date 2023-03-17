from rest_framework.pagination import LimitOffsetPagination
# from rest_framework.pagination import PageNumberPagination


# class PostsPagination(PageNumberPagination):
#     page_size = 5
class PostsPagination(LimitOffsetPagination):
    # page_size = 5
    default_limit = 10
    # limit_query_param = 10
    # offset_query_param = 20
    # max_limit = 30
