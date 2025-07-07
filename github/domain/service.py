from abc import ABC, abstractmethod

from github.domain.user import GitHubUser


class GitHubServicePort(ABC):

    @abstractmethod
    def get_user_info(self, username: str) -> GitHubUser:
        ...

    