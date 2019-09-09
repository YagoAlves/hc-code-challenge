from rest_framework import viewsets
from .serializers import ReportSerializers,UserSerializers,ReportSerializers
from core.models import Report, ReportResponse, User
from rest_framework.response import Response

class ReportViewSet(viewsets.ModelViewSet):

    serializer_class = ReportSerializers

    def get_queryset(self):

        user_id = self.request.query_params.get('user_id',None)
        pagination_offset = self.request.query_params.get('pagination_offset',None)
        pagination_limit = self.request.query_params.get('pagination_limit',None)

        queryset = Report.objects.all()

        if ((user_id) and (pagination_limit)):
            queryset = Report.objects.filter(author_id=user_id)[:pagination_limit]
            return queryset

        if ((user_id) and (pagination_limit) and (pagination_offset)):
            queryset = Report.objects.filter(author_id=user_id)[pagination_offset:pagination_limit]
            return queryset

        if ((pagination_limit) and (pagination_offset)):
            queryset = Report.objects.all().order_by('-id')[pagination_offset:pagination_limit]
            return queryset

        if (user_id):
            queryset = Report.objects.filter(author_id=user_id)
            return queryset

        if (pagination_limit):
            queryset = Report.objects.all().order_by('id')[:pagination_limit]
            return queryset

        if (pagination_offset):
            queryset = Report.objects.all().order_by('id')[pagination_offset:]
            return queryset

        return queryset

        

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializers


