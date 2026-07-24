from app import app


def test_home():

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_tasks():

    client = app.test_client()

    response = client.get("/tasks")

    assert response.status_code == 200


def test_about():

    client = app.test_client()

    response = client.get("/about")

    assert response.status_code == 200