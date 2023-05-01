from django.db.models import Sum
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Sale
from .serializers import SaleSerializer


class SaleListCreateView(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        sale = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SaleRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer


class SalesByDateView(generics.ListAPIView):
    serializer_class = SaleSerializer

    def get_queryset(self):
        fecha_desde = self.request.query_params.get('fecha_desde', None)
        fecha_hasta = self.request.query_params.get('fecha_hasta', None)
        queryset = Sale.objects.all()
        if fecha_desde:
            queryset = queryset.filter(fecha_venta__gte=fecha_desde)
        if fecha_hasta:
            queryset = queryset.filter(fecha_venta__lte=fecha_hasta)
        return queryset


class SalesByEmployeeView(generics.ListAPIView):
    serializer_class = SaleSerializer

    def get_queryset(self):
        empleado_id = self.request.query_params.get('empleado_id', None)
        queryset = Sale.objects.all()
        if empleado_id:
            queryset = queryset.filter(empleado_id=empleado_id)
        return queryset.annotate(total_venta=Sum('productos__precio_unitario') * Sum('productos__cantidad'))

