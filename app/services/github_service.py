# app/services/github_service.py
from app.core.config import settings
from app.utils.http_client import get_request

def fetch_user_gists(username: str):
    url = f"{settings.GITHUB_BASE_URL}/users/{username}/gists"
    response = get_request(url)

    if response.status_code == 200:
        gists = response.json()
        return [
            {
                "id": gist.get("id"),
                "description": gist.get("description"),
                "url": gist.get("html_url"),
                "files": list(gist.get("files", {}).keys())
            }
            for gist in gists
        ]

    elif response.status_code == 404:
        return None

    else:
        raise Exception("GitHub API error")