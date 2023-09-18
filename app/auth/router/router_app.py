from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.utils import AppModel

from ..service import Service, get_service
from ..utils.security import check_password
from . import router
class EmailRequest(AppModel):
    email: str


@router.post("/email")
def testemail(
    email: EmailRequest,
    svc: Service = Depends(get_service),
    ):
    if email.email:
        return {"msg":"ok"}
    return {"msg":"error"}