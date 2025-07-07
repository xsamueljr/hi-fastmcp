from dataclasses import dataclass


@dataclass
class GitHubUser:
    username: str
    name: str
    repos_count: int
