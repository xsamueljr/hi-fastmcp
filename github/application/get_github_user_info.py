from github.domain.service import GitHubServicePort
from github.domain.user import GitHubUser


class GetGiHubUserInfoUseCase:

    def __init__(self, service: GitHubServicePort) -> None:
        self.__service = service
    
    def run(self, username: str) -> GitHubUser:
        return self.__service.get_user_info(username)
