from fastapi import status


def test_root_should_return_message(client):
    response = client.get('/')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'Hello World'}
