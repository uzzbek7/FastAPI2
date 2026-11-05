from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.order import Orders, order_products
from app.models.products import Products

def get_by_id(db: Session, order_id: int) -> Orders | None:
    return db.get(Orders, order_id)


def get_all(db: Session) -> list[Orders]:
    return list(db.scalars(select(Orders).order_by(Orders.id)))



def getByUserId(db: Session, user_id: int) -> list[Orders]:
    stmt = (
        select(Orders)
        .where(Orders.user_id == user_id)
        .order_by(Orders.id)
    )
    return list(db.scalars(stmt))

def add_order(db: Session, order: Orders) -> Orders:
    order = Order(**data.model_dump())
    db.add(order)
    db.flush()
    return order


def getBestProductsRange(
    db: Session,
    limit: int = 10,
    offset: int = 0,
) -> list[Products]:
    sales = (
        select(
            order_products.c.product_id,
            func.count().label("sales_count"),
        ).group_by(order_products.c.product_id).subquery()
    )

    stmt = (select(Products)
        .join(sales, Products.id == sales.c.product_id)
        .order_by(sales.c.sales_count.desc(), Products.id)
        .limit(limit)
        .offset(offset))

    return list(db.scalars(stmt))