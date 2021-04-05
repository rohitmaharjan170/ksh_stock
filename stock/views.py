from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# from .models import Stock
# from .serializers import StockSerializer

# from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

# class StockViewSet(viewsets.ModelViewSet):
# 	authentication_classes = (BasicAuthentication,)
# 	permission_classes = (IsAuthenticated,)
# 	queryset = Stock.objects.all()
# 	serializer_classes = StockSerializer

def home(request):
	return render(request, "home.html", {})
