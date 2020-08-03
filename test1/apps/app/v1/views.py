from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from test1.apps.app.models import Request
from .serializers import RequestSerializer, OfferSerializer


class RequestAPIView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, *args, **kwargs):
        try:
            instance = Request.objects.prefetch_related('offers').get(uuid=kwargs['uuid'])
        except Request.DoesNotExist:
            return Response({'message': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = RequestSerializer(instance)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({'message': 'No access'}, status=status.HTTP_403_FORBIDDEN)
        instance = get_object_or_404(Request.objects.prefetch_related('offers').all(), uuid=kwargs['uuid'])
        data = {'status': request.data.get('status')}
        serializer = RequestSerializer(instance=instance, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)


class OfferAPIView(APIView):
    permission_classes = (permissions.IsAdminUser, )

    def post(self, request, *args, **kwargs):
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
