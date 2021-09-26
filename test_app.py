from fastapi.testclient import TestClient
from main import app

# test to check the correct functioning of the /ping route
def test_ping():
    with TestClient(app) as client:
        response = client.get("/ping")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"ping": "pong"}


# test to check if Iris Virginica is classified correctly
def test_pred_virginica():
    # defining a sample payload for the testcase
    payload = {
        "sepal_length": 3,
        "sepal_width": 5,
        "petal_length": 3.2,
        "petal_width": 4.4,
    }
    with TestClient(app) as client:
        response = client.post("/predict_flower", json=payload)
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"flower_class": "Iris Virginica"}
def test_calcs():
    with TestClient(app) as client:
        response = client.get("/calcs")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"calcs": "operations performed successufully"}
def test_vetran():
    with TestClient(app) as client:
        response = client.get("/vetran")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"vetran": "operations performed successufully"}
def test_kuts():
    with TestClient(app) as client:
        response = client.get("/kuts")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"kuts": "This is Shiuli"}

def test_group():
    with TestClient(app) as client:
        response = client.get("/group")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"Group": "My Cool Group"}

def test_glgroup():
    with TestClient(app) as client:
        response = client.get("/glgroup")
        # asserting the correct response is received
        assert response.status_code == 200
        assert response.json() == {"Group": "My Gl group"}
