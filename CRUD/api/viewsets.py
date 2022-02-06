from rest_framework import generics
from rest_framework.response import Response
from ..models import Empresa
from .serializers import EmpresaSerializer
from rest_framework import status

class List (generics.ListAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class Create (generics.CreateAPIView):
    serializer_class = EmpresaSerializer
    def create(self, request):
        empresaCreate = Empresa(
        name=request.data['name'], 
        address=request.data['address'], 
        nit=request.data['nit'], 
        phone=request.data['phone'])
        empresaCreate.save()
        return Response({'titulo': 'Empresa Ingresada Correctamente'}, status=status.HTTP_201_CREATED)

class Detail (generics.ListAPIView):
    def list(self, request, pk):
        try:
            queryset = Empresa.objects.get(pk=pk)
        except(KeyError, Empresa.DoesNotExist):
            return Response({"titulo": "No existe ese ID"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(EmpresaSerializer(queryset).data)
        

class Delete(generics.DestroyAPIView):
    def delete(self, request, pk):
        try:
            queryset = Empresa.objects.get(pk=pk)
        except(KeyError, Empresa.DoesNotExist):
            return Response({"titulo": "No existe ese ID"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            queryset.delete()
            query = Empresa.objects.all()
        return Response(EmpresaSerializer(query, many=True).data)

class Update (generics.UpdateAPIView):
    serializer_class = EmpresaSerializer
    queryset = Empresa.objects.all()