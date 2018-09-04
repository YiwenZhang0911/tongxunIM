from rest_framework import status
from rest_framework.exceptions import APIException


class BaseExcept(APIException):
    def __init__(self, detail, code=None):
        if detail:
            self.detail = {'detail': detail}
            if code:
                self.detail['code'] = code


class BadRequest(BaseExcept):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'Bad Request'


class NotFound(BaseExcept):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = 'Not Found'


class Forbidden(BaseExcept):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'forbidden'


class ServerError(BaseExcept):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'internal server error'
