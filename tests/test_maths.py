from fastmcp import Client
import pytest

from main import mcp


@pytest.fixture
def client() -> Client:
    return Client(mcp)


@pytest.mark.asyncio
async def test_quadratic_equation_works(client: Client):
    async with client:
        result = await client.call_tool("quadratic_equation", {"a": 1, "b": -5, "c": 6})

        print(type(result.data))

        assert result.data.x1 == 3
        assert result.data.x2 == 2
