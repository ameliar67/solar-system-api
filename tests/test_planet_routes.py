def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet(client, one_data):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Earth",
        "description": "cool",
        "has_rings": False
    }

def test_get_one_planet(client):
    # Act
    response = client.get("/planets/1")

    # Assert
    assert response.status_code == 404

def test_create_one_planet(client):
    # Act
    response = client.post("/planets", json={
        "name": "Mars",
        "description": "Chocolate",
        "has_rings": False
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "Mars",
        "description": "Chocolate",
        "has_rings": False
    }