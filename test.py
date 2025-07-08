import asyncio

from fastmcp import Client

from github.infrastructure.real_github_service import RealGitHubService
from main import create_app


mcp = create_app(RealGitHubService())
client = Client(mcp)

async def main():
    async with client:
        result = await client.call_tool("quadratic_equation", {"a": 1, "b": -5, "c": 6})

        print(result)
        print(result.data)

        gusy_profile = await mcp._mcp_call_tool("get_user_info", {"username": "ggusyyy"})

        print(gusy_profile)
        print(gusy_profile[0])
        print(gusy_profile[1])

        # print(gusy_profile)


if __name__ == '__main__':
    asyncio.run(main())