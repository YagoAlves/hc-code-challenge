from rest_framework import serializers
from .models import Report
from .models import User
from .models import ReportResponse

class UserSerializers(serializers.ModelSerializer):
        
    class Meta:
        model = User
        fields = ['id','first_name','last_name','email']


class ReportResponseSerializers(serializers.ModelSerializer):
        
    class Meta:
        author = UserSerializers(source='author')
        model = ReportResponse
        fields = ['message','author']
        depth = 1


class ReportSerializers(serializers.ModelSerializer):
    
    authors = UserSerializers(source='author')
    reports_set = ReportResponseSerializers(many=True)
    class Meta:
        model = Report
        fields = ['id','message','authors','supervisors','reports_set']
        depth = 1
        