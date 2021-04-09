from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializer import UserModelSerializer, UserModelSerializerAll


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '0.2':
            return UserModelSerializerAll
        return UserModelSerializer


# def dispatch(request, *args, **kwargs):
#     """
#     Проверка на ошибки, которые не отлавливаются во views
#     :param request:
#     :param args:
#     :param kwargs:
#     :return:
#     """
#     try:
#         response = super().dispatch(request, *args, **kwargs)
#     except Exception as e:
#         sentry_sdk.capture_exception(error=e)
#         BaseView.error_log(error_log, e, request)
#         return JsonResponse({'status': 'Failed', 'message': 'Server Error'}, status=500)
#
#     if isinstance(response, (dict, list)):
#         status = response.pop('code')
#         return JsonResponse(response, safe=False, status=status)
#     else:
#         return response

