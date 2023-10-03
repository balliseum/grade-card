from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
# from sqlalchemy.orm import Session
# from app import schemas, crud
# from api.deps import get_db

router = APIRouter()


@router.get("",)
def read_products() -> Any:
    return {"data": "hello world"}

