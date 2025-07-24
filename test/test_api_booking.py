import requests

def test_create_booking():
    url = "https://restful-booker.herokuapp.com/booking"
    payload = {
        "firstname": "Asad",
        "lastname": "Rahoo",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-08-01",
            "checkout": "2025-08-05"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    assert response.status_code == 200
    data = response.json()
    assert "bookingid" in data
    assert data["booking"]["firstname"] == "Asad"
    assert data["booking"]["lastname"] == "Rahoo"
