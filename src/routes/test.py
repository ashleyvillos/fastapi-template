from src.utils.response import Response
from fastapi import APIRouter
from src.controllers.TestController import TestController

router = APIRouter(prefix='/test')

@router.get('/')
async def get_test() -> Response:
    return await TestController.get_test()