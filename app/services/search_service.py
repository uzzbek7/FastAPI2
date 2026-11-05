from datetime import date

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.ad import AdStatus
from app.repositories import ad_repo


def search_ads(
    db: Session,
    *,
    ad_status: AdStatus | None = None,
    category: str | None = None,
    title: str | None = None,
    price: int | None = None,
    pricemin: int | None = None,
    pricemax: int | None = None,
    create_at: date | None = None,
    is_adult: bool | None = None,
    page: int = 1,
    limit: int = 20,
):
    if pricemin is not None and pricemax is not None and pricemin > pricemax:
        raise HTTPException(
            status_code=422,
            detail="pricemin must be less than or equal to pricemax",
        )

    return ad_repo.get_all(
        db,
        ad_status=ad_status.value if ad_status else None,
        category=category,
        title=title,
        price=price,
        pricemin=pricemin,
        pricemax=pricemax,
        create_at=create_at,
        is_adult=is_adult,
        page=page,
        limit=limit,
    )
