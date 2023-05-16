from fastapi import APIRouter
from app.schemas.product import Product

routes_product = APIRouter()

fake_db = []


@routes_product.get("/")
async def get_products():
    return fake_db


@routes_product.post("/create", response_model=Product)
async def create(product: Product):
    try:
        fake_db.append(product.dict())
        print(fake_db)
        return product
    except Exception as e:
        return e


@routes_product.get("/get/{id_product}")
async def get_by_id(id_product: str):
    try:
        return list(filter(lambda field: field["id"] == id_product, fake_db))[0]
    except Exception as e:
        return e


@routes_product.delete("/delete/{id_product}")
async def delete_by_id(id_product: str):
    try:
        product = list(filter(lambda field: field["id"] == id_product, fake_db))[0]
        print(product)
        if product in fake_db:
            fake_db.remove(product)
            print(fake_db)

        return {
            "message": "success"
        }
    except Exception as e:
        return e



