from rest_framework.serializers import ModelSerializer
from .models import UploadFile

class FileSerializer(ModelSerializer):

    class Meta:
        model = UploadFile
        fields = "__all__"