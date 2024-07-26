from fastapi import FastAPI
import httpx

app = FastAPI()
@app.get('/')
async def fetch_data():
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get("http://35.232.53.183")
        return response.json()