from src.utils.constants import *
from src.utils.message import *
from src.utils.response import Response
from src.services.TestService import TestService


class TestController:
    @classmethod
    async def get_test(cls) -> Response:
        try:
            response = await TestService().get_test()
            return Response(status=OK, message=OK_MESSAGE, response=response)
        except Exception as e:
            return Response(status=INTERNAL_SERVER_ERROR, message=INTERNAL_SERVER_ERROR_MESSAGE, response={})
            
