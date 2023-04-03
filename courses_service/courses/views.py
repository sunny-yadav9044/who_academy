from rest_framework import generics
from rest_framework.response import Response
from .token_authentication import TokenAuthentication
from .services import CourseService


class CourseListView(generics.ListAPIView):
    permission_classes = [TokenAuthentication]

    def list(self, request):
        page = self.request.query_params.get('page', 1)
        page_size = self.request.query_params.get('page_size', 5)
        fields = self.request.query_params.get('fields', 'default_field_list')
        service = CourseService()
        courses = service.get_courses(page=page, page_size=page_size, fields=fields)
        courses['pagination']['next'] = self.get_next_url(request, courses['pagination']['next'])
        return Response(courses)
    
    @staticmethod
    def get_next_url(request, url):
        url_list = url.split('?')
        url_list[0] = request.build_absolute_uri().split('?')[0]
        return '?'.join(url_list)
