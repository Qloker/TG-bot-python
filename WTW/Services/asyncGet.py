import requests
import asyncio
import aiohttp

#response = requests.get('https://example.com/')
#print(response)

'''
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
    
async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://example.com/')
        print(html)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

'''

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()
    
async def main():
    async with aiohttp.ClientSession() as session:
        task = []
        for i in range(110):
            html = await fetch(session, 'https://bohemahotel.com/')
            print(i)
            #await asyncio.sleep(1)
            #task.append(fetch(session, 'https://example.com/'))
            #await asyncio.sleep(2)
        #result = await asyncio.gather(*task)
        #print(result)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())