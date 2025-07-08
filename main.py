from fastmcp import FastMCP

from github.infrastructure.mcp_controller import GitHubMCPController
from github.infrastructure.real_github_service import RealGitHubService
from maths.application.dtos.quadratic_equation_result import QuadraticEquationResult
from maths.application.quadratic_equation import SolveQuadraticEquationUseCase
from maths.application.square_root import CalculateSquareRootUseCase
from shared.infrastructure.env import ENV, AppEnvType
from tests.mocks import MockGitHubService

mcp = FastMCP("MCP example")

@mcp.tool
def add_two_numbers(a: int, b: int) -> int:
    return a + b

@mcp.tool
def square_root(x: int) -> float:
    return CalculateSquareRootUseCase().run(x)

@mcp.tool
def quadratic_equation(a: int, b: int, c: int) -> QuadraticEquationResult:
    return SolveQuadraticEquationUseCase().run(a, b, c)

if ENV.APP_ENV == AppEnvType.PRODUCTION:
    print("using real")
    github_service = RealGitHubService()
else:
    print("using mock")
    github_service = MockGitHubService()


github_controller = GitHubMCPController(github_service)
mcp.tool(github_controller.get_user_info)

if __name__ == "__main__":
    mcp.run()
