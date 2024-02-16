from fastapi import Depends, HTTPException, Header
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

def verify_basic_auth(credentials: HTTPBasicCredentials = Depends(security)):
    if not credentials.username or not credentials.password:
        raise HTTPException(
            status_code=401,
            detail="Authentication error has occurred. Please confirm authentication parameters are not empty.")
    return credentials

def verify_x_boc_owner_id(x_boc_owner_id: int = Header(..., ge=1, le=2, description="1 - BIE, 2 - BIC")):
    return x_boc_owner_id

def verify_service_program(service_program: str = Header(...)):
    valid_programs = [ "brother_plus_us", "brother_plus_ca", ... ]  # 完整的列表
    if service_program not in valid_programs:
        raise HTTPException(
            status_code=400,
            detail="Service-Program is invalid. Please confirm Service-Program.")
    return service_program
