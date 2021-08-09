from rest_framework import permissions, status, views, viewsets, pagination
from rest_framework.parsers import MultiPartParser
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import mixins
from .serializers import CSVObjectSerializer
from .models import CSVObject
from django.utils.datastructures import MultiValueDictKeyError
from .func_for_create_objects import bulk_create_objects


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'content': data,
            'total_pages': self.page.paginator.num_pages,
            'page_number': self.page.number,
        })


class UploadCSVFileView(views.APIView):
    parser_classes = (MultiPartParser,)
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response(template_name='upload_template.html', status=status.HTTP_200_OK)

    def post(self, request):
        try:
            file = request.FILES['file']
        except MultiValueDictKeyError:
            return Response({'data': 'Выберите файл!'}, template_name='upload_template.html',
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            file_data = file.read().decode('cp1251')
        except UnicodeDecodeError:
            return Response({'data': 'Это не CSV файл!'}, template_name='upload_template.html',
                            status=status.HTTP_400_BAD_REQUEST)
        bulk_create_objects(file_data)
        return Response({'link_for_list': reverse('objects-list')}, template_name='upload_template.html',
                        status=status.HTTP_200_OK)


class ListCSVFileView(mixins.CreateModelMixin, viewsets.ReadOnlyModelViewSet):
    queryset = CSVObject.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CSVObjectSerializer
    pagination_class = CustomPagination
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'roundedtable.html'

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return Response({'content': CSVObjectSerializer(self.queryset, many=True).data},
                        template_name=self.template_name, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        CSVObject.objects.all().delete()
        return Response({'content': 'Clear'}, status=status.HTTP_200_OK)
