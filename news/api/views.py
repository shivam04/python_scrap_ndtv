from .serializers import (
    NewsListSerializer,
    )
from news.models import (
    NewsNdtv,
    )
from rest_framework.generics import (
    ListAPIView, 
    )
from .pagination import PostLimitOffsetPagination,PostPageNumberPagination
class NewsList(ListAPIView):
    queryset = NewsNdtv.objects.all()
    #pagination_class = PostPageNumberPagination
    serializer_class = NewsListSerializer