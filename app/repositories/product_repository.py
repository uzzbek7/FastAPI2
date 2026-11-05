from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.products import Products

def get_by_id(db: Session, product_id: int) -> Products | None:
    return db.get(Products, product_id)


def get_all(db: Session) -> list[Products]:
    return list(db.scalars(select(Products).order_by(Products.id)))

def getProductByCategory(db: Session, category: int) -> Products | None:
    return db.get(Products, category)