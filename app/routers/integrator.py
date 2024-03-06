from fastapi import APIRouter
from starlette import status


router = APIRouter(
    prefix='/integrator',
    tags=['Integrator'],
    responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
)


@router.get("/greetings", status_code=status.HTTP_200_OK)
def public():
    result = {
        "status": "success",
        "msg": ("Hello from a public endpoint! You don't need to be "
                "authenticated to see this.")
    }
    return result
