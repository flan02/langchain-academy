
# $ Using LangGraph SDK

import asyncio
from langgraph_sdk import get_client

async def main():
  url_for_cli_deployment = 'http://localhost:8123'
  client = get_client(url=url_for_cli_deployment)

  # Calls the co-rutine using async
  assistants = await client.assistants.search()
  print(assistants)

# Run the async function
if __name__ == '__main__':
  asyncio.run(main())