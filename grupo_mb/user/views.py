from django.shortcuts import render

from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListViewByAge(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = self.mergesort_age(queryset)
        return queryset

    def mergesort_age(self, queryset):
        if len(queryset) <= 1:
            return queryset
        mid = len(queryset) // 2
        left_half = queryset[:mid]
        right_half = queryset[mid:]
        left_half = self.mergesort_age(left_half)
        right_half = self.mergesort_age(right_half)
        return self.merge_age(left_half, right_half)

    def merge_age(self, left_half, right_half):
        result = []
        i, j = 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].edad < right_half[j].edad:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[j])
                j += 1
        result += left_half[i:]
        result += right_half[j:]
        return result


class UserListViewByLastName(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        queryset = self.mergesort_last_name(queryset)
        return queryset

    def mergesort_last_name(self, queryset):
        if len(queryset) <= 1:
            return queryset
        mid = len(queryset) // 2
        left_half = queryset[:mid]
        right_half = queryset[mid:]
        left_half = self.mergesort_last_name(left_half)
        right_half = self.mergesort_last_name(right_half)
        return self.merge_last_name(left_half, right_half)

    def merge_last_name(self, left_half, right_half):
        result = []
        i, j = 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i].apellido_paterno < right_half[j].apellido_paterno:
                result.append(left_half[i])
                i += 1
            else:
                result.append(right_half[j])
                j += 1
        result += left_half[i:]
        result += right_half[j:]
        return result

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
