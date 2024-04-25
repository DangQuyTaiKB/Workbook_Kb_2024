from fastapi import FastAPI
import json
import pandas as pd
import aiohttp
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

# read json file
@app.get("/data")
async def read_json():
    with open('systemdata.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


@app.get("/users")
async def users():
    data = await read_json()
    users = data['users']
    df = pd.DataFrame(users)
    return df.to_dict()


async def send_query_async(query, url, headers):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=query, headers=headers) as response:
            return await response.json()

@app.get("/query")
async def query():
    gateway_url = "http://localhost:33000/api/gql"
    headers = {"Content-Type": "application/json"}
    # query = {"query": "{taskPage{id name lastchange briefDes dateOfEntry dateOfFulfillment dateOfSubmission detailedDes reference}}"}
    query = {"query": "{userPage{id name surname email}}"}
    result = await send_query_async(query, gateway_url, headers)
    return result






