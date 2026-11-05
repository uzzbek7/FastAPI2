from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, Table, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.basemodel import Base
from app.models.products import Products


order_products = Table(
    "order_products",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True),
)


class Orders(Base):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    sum: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    order_Items: Mapped[list[Products]] = relationship(secondary=order_products)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))