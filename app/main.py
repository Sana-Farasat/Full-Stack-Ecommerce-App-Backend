from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from app.db.database import engine

# IMPORTANT
from app.models.user import User
from app.models.category import Category
from app.models.product import Product
from app.models.cart import Cart
from app.models.order import Order
from app.models.order_item import OrderItem

from app.api.auth import router as auth_router
from app.api.products import router as product_router
from app.api.categories import router as category_router
from app.api.cart import router as cart_router
from app.api.orders import router as order_router

app = FastAPI(title="AI Ecommerce")

@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://full-stack-ecommerce-app-six.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(category_router)
app.include_router(cart_router)
app.include_router(order_router)
@app.get("/")
async def root():
    
    return {"message": "Hello!"}





