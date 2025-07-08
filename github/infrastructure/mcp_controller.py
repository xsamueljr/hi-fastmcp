from github.application.get_github_user_info import GetGitHubUserInfoUseCase
from github.domain.service import GitHubServicePort
from github.domain.user import GitHubUser


class GitHubMCPController:

    def __init__(self, service: GitHubServicePort) -> None:
        self.usecase = GetGitHubUserInfoUseCase(service)

    def get_user_info(self, username: str) -> GitHubUser:
        return self.usecase.run(username)
