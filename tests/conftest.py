from fastmcp import Client
import pytest

from main import create_app
from shared.infrastructure.env import ENV, AppEnvType
from tests.mocks import MockGitHubService
from tests.setups import McpSetup


@pytest.fixture(scope="session", autouse=True)
def check_environment_is_valid_for_testing():
    if ENV.APP_ENV != AppEnvType.TEST:
        raise RuntimeError(
            f"Current app environment is {ENV.APP_ENV} instead of testing."
            "Please fix and run again"
        )


@pytest.fixture
def mcp_setup() -> McpSetup:
    github_service = MockGitHubService()
    mcp = create_app(github_service)
    client = Client(mcp)
    
    return McpSetup(mcp, client, github_service)
