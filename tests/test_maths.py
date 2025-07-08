import pytest

from tests.setups import McpSetup


@pytest.mark.asyncio
async def test_quadratic_equation_works(mcp_setup: McpSetup):
    async with mcp_setup.client:
        result = await mcp_setup.client.call_tool("quadratic_equation", {"a": 1, "b": -5, "c": 6})

        print(type(result.data))

        assert result.data.x1 == 3
        assert result.data.x2 == 2
