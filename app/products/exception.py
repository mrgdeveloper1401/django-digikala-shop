from rest_framework.exceptions import APIException

class Deplicated(APIException):
    status_code = 400