import aiohttp

async def tarkov_api_request(query: str) -> dict:
    url = 'https://api.tarkov.dev/graphql'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json={'query': query}, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Failed to fetch data: {response.status}")  # Debugging statement
                return {}
