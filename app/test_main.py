from app.main import outdated_products
import datetime
import pytest


fake_time = datetime.datetime(2000, 1, 1)


@pytest.fixture
def patch_datetime_now(monkeypatch: None) -> datetime:
    class MyDatetime(datetime.datetime):
        @classmethod
        def now(cls) -> datetime:
            return fake_time
    monkeypatch.setattr(datetime, "datetime", MyDatetime)


def test_outdated_products(patch_datetime_now: None) -> None:
    fake_time = datetime.datetime(2000, 1, 1)
    all_products = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    result = outdated_products(all_products)
    assert result == [x["name"] for x in all_products]

    fake_time = datetime.datetime(2025, 1, 1)
    fake_time.weekday()
    result = outdated_products(all_products)
    assert result == []
