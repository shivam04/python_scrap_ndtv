from rest_framework_mongoengine.serializers import (
    DocumentSerializer,
    )
from news.models import (
	NewsNdtv,
	)

class NewsListSerializer(DocumentSerializer):
	class Meta:
		model = NewsNdtv
		fields = '__all__'

