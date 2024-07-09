from rest_framework.pagination import PageNumberPagination,CursorPagination

class ReviewListPagination(PageNumberPagination):
    page_size = 1
    page_size_query_param = 'record' #************Take input from user***********************
    max_page_size = 20
    last_page_strings = "last"

#**********In cursor pagination, we can't go to a specific page by giving page number
#**********We have to go through all pages one by one
#**********Use case = Aggrement, terms & policy

class ReviewListCursorPagination(CursorPagination):
    page_size = 1
    # cursor_query_param = "c"
    ordering = "created"
    # ordering = "-created"