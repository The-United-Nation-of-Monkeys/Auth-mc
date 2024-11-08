from fastapi import status, HTTPException
from fastapi.responses import JSONResponse

def status_error_401():
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

def status_success_200(detail: str | dict | list | None = None):
    if detail:
        return {"status": "success", "detail": detail}
    else:
        return {"status": "success"}

def status_error_403():
    
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

def status_error_400(detail: str | dict | None = None):
    
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

def status_error_409(detail: str | dict | None = None):
    if detail:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"detail": detail})
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail={"detail": detail})

def status_success_201(detail: str | dict | list | None = None):
    if detail:
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={"status": "success", "detail": detail})
    else:
        return JSONResponse(status_code=status.HTTP_201_CREATEDб, content={"status": "success"})