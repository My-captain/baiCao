from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    """
    分页器
    """
    page_size = 5
    page_size_query_param = "page_size"
    page_query_param = "page_number"
    max_page_size = 10
