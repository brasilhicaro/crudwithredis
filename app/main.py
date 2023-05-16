import uvicorn
from fastapi import FastAPI
from app.routes.products import routes_product

description = """
RedisDemo é um projeto para a disciplina BD2, ministrada em 2023.2.
"""

app = FastAPI(
    title="RedisDemo",
    description=description,
    version="0.0.1",
)


@app.get("/")
async def root():
    return {"message": "Servidor de teste"}

app.include_router(routes_product, prefix="/products")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
