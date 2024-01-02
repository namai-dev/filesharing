from django.http import FileResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import UploadFile
from .serializers import FileSerializer
# Create your views here.

class Hello(APIView):
    def get(self, request):
        return Response("Hello")
    

class FileManager(APIView):
    def post(self, request):
        uploaded_file = request.FILES['file']
        file_instance = UploadFile(
            filename = uploaded_file.name,
            size = uploaded_file.size,
            file_type = uploaded_file.content_type,
            file = uploaded_file
        )

        file_instance.save()

        return Response("Saved successifully")
    
    # def get(self, request, pk):
    #     file = UploadFile.objects.get(pk=pk)
    #     file1 = FileSerializer(file)
    #     return Response(file1.data)

    def get(self, request, pk):
        file = UploadFile.objects.get(pk=pk)
        filename = file.filename
        response = FileResponse(open(filename, 'rb'), as_attachment=True)
        return response
    

    def get(self, request):
        files = []
        file_list = UploadFile.objects.all()
        serializer = FileSerializer(file_list, many=True)
        for file in file_list:
            files.append(serializer.data)

        return Response(files)
    
    def delete(self, request, pk):
        file = UploadFile.objects.get(pk=pk)
        file.delete()
        return Response("deleted")





 

