from dataclasses import dataclass


@dataclass
class GitHubUser:
    username: str
    name: str | None
    repos_count: int
