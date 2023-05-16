from fastapi import APIRouter

import app.redis_client.crud as crud
from app.schemas.product import Product

routes_product = APIRouter()


@routes_product.post("/create", response_model=Product)
async def create(product: Product):
    try:
        crud.save_hash(key=product.dict()['id'], data=product.dict())
        return product
    except Exception as e:
        return e


@routes_product.get("/get/{id_product}")
async def get_by_id(id_product: str):
    try:
        data = crud.get_hash(key=id_product)
        return data
    except Exception as e:
        return e


@routes_product.delete("/delete/{id_product}")
async def delete_by_id(id_product: str):
    try:
        keys = Product.__fields__.keys()
        crud.delete_hash(key=id_product, keys=keys)
        return {
            "message": "success"
        }
    except Exception as e:
        return e
