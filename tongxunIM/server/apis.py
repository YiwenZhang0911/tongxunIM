from django.contrib import auth
from rest_framework.response import Response
from rest_framework.views import APIView

from server.serializers import UserRegisterSerializer
from server.services import UserServices, request_im
from server.exceptions import BadRequest, Forbidden


class UserRegister(APIView):
    """网易云通信ID注册"""

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        valid_data = serializer.validated_data
        UserServices.create_user(valid_data)

        return Response({'detail': 'ok', })


class UserLogin(APIView):
    """用户登录"""

    def post(self, request):
        accid = request.data.get("username")
        password = request.data.get("password")

        if not all([accid, password]):
            raise BadRequest('账号密码不能为空', 1)

        user = auth.authenticate(username=accid, password=password)
        if not user:
            raise Forbidden('登陆失败', 0)
        return Response({'detail': 'ok', 'token': user.token, 'accid': user.accid})
