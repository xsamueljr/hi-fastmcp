import asyncio

from fastmcp import Client

from main import mcp


client = Client(mcp)

async def main():
    async with client:
        result = await client.call_tool("quadratic_equation", {"a": 1, "b": -5, "c": 6})

        print(result)
        print(result.data)

        gusy_profile = await mcp._mcp_call_tool("get_user_info", {"username": "ggusyyy"})

        print(gusy_profile)
        # print(gusy_profile)


if __name__ == '__main__':
    asyncio.run(main())