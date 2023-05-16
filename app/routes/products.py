from fastapi import APIRouter
from app.schemas.product import Product
from redis_client.crud import Crud

routes_product = APIRouter()

fake_db = []
__crud = Crud()


@routes_product.get("/")
async def get_products()->list:
    return fake_db


@routes_product.post("/create", response_model=Product)
async def create(product: Product):
    try:
        fake_db.append(product.dict())
        print(fake_db)
        __crud.save_hash(key=product.dict()['id'], data = product.dict())
        return product
    except Exception as e:
        return e


@routes_product.get("/get/{id_product}")
async def get_by_id(id_product: str):
    try:
        data = __crud.get_hash(key=id)
        if len(data) == 0:
            product =  list(filter(lambda field: field["id"] == id_product, fake_db))[0]
            __crud.save_hash(key = id, data = product)
            return product 
        return data
    except Exception as e:
        return e


@routes_product.delete("/delete/{id_product}")
async def delete_by_id(id_product: str):
    try:
        keys = Product.__fields__.keys()
        
        __crud.delete_hash(key = id, keys= keys)
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
