from rest_framework.exceptions import APIException


class WrongInputException(APIException):
    status_code = 400

    def __init__(self, detail):
        self.detail = {"message": detail}


class ServiceException(APIException):
    status_code = 400

    def __init__(self, detail):
        self.detail = {"message": detail}


class BackendException(APIException):
    status_code = 500

    def __init__(self, detail):
        self.detail = {"message": detail}
