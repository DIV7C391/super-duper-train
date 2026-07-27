import httpx
import asyncio

#async httpx get request
async def create_post():
    async with httpx.AsyncClient() as client:
        a=await client.post("https://www.google.com/")
    print(a.json())
asyncio.run(create_post())


#async httpx post request
async def create_post():
    async with httpx.AsyncClient() as client:
        a=await client.post("https://www.google.com/",json={"name":"Divyanshu"})
    print(a.json())
asyncio.run(create_post())

#calling multiple api endpoints concurrently

async def fetch(client,url):
    a=await client.get(url)
    print(a.json())

async def main():
    async with httpx.AsyncClient() as client:
        url_1="https://www.google.com/"
        url_2="https://www.youtube.com/"
        b=await asyncio.gather(fetch(client,url_1),fetch(client,url_2))
    print(b)

asyncio.run(main())