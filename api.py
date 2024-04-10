import aiohttp

async def get_details(id):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://tbox-vids.vercel.app/api?data={id}") as response:
                data = await response.json()
                return data
    except Exception as e:
        print(e)
