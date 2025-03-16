from app.main import outdated_products
import datetime
from unittest.mock import patch, Mock


@patch("app.main.datetime.date")
def test_outdated_products(mocked_date: Mock) -> None:
    mocked_date.today.return_value = datetime.datetime(2000, 1, 1)
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
    mocked_date.today.return_value = datetime.datetime(2025, 1, 1)

    result = outdated_products(all_products)
    assert result == []
