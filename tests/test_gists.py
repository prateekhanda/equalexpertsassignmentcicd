def test_get_gists_valid_user(client):
    response = client.get("/api/v1/users/octocat")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)

    if data:  # only check structure if gists exist
        gist = data[0]
        assert "id" in gist
        assert "url" in gist
        assert "files" in gist


def test_get_gists_invalid_user(client):
    response = client.get("/api/v1/users/thisuserdoesnotexist123456789")
    assert response.status_code == 404