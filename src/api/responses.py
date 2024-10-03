from fastapi import status, HTTPException

def status_error_401():
    
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

def status_success_200(detail = None):
    
    return {"status": "success", "detail": detail}

def status_error_403():
    
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

