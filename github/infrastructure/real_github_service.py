import httpx

from github.domain.exceptions.user_not_found import GitHubUserNotFoundException
from github.domain.service import GitHubServicePort
from github.domain.user import GitHubUser


BASE_URL = "https://api.github.com"

class RealGitHubService(GitHubServicePort):

    def get_user_info(self, username: str) -> GitHubUser:
        response = httpx.get(f"{BASE_URL}/users/{username}")
        
        if response.status_code == 404:
            raise GitHubUserNotFoundException()
        
        data = response.json()
        
        return GitHubUser(
            username=data["login"],
            name=data["name"],
            repos_count=data["public_repos"]
        )