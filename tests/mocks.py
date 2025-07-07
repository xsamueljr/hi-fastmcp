from github.domain.service import GitHubServicePort
from github.domain.user import GitHubUser


class MockGitHubService(GitHubServicePort):

    def __init__(
        self,
        name: str = "irrelevant-name",
        repos_count: int = 0
    ) -> None:
        self.name = name
        self.repos_count = repos_count

    def get_user_info(self, username: str) -> GitHubUser:
        return GitHubUser(
            username,
            self.name,
            self.repos_count
        )