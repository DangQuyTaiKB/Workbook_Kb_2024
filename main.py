from fastapi import FastAPI
import json
import pandas as pd
import aiohttp
app = FastAPI()


############ Test FastAPI ################

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

def outfile(data, filename):
    with open(filename + '.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# async def send_query_async(query, url, headers):
#     async with aiohttp.ClientSession() as session:
#         async with session.post(url, json=query, headers=headers) as response:
#             return await response.json()

# @app.get("/query")
# async def query():
#     gateway_url = "http://localhost:33000/api/gql"
#     headers = {"Content-Type": "application/json"}
#     # query = {"query": "{taskPage{id name lastchange briefDes dateOfEntry dateOfFulfillment dateOfSubmission detailedDes reference}}"}
#     query = {"query": "{userPage{id name surname email}}"}
#     result = await send_query_async(query, gateway_url, headers)
#     return result

############ Test FastAPI ################


from send_payload import getToken, query, flatten, toTable
from auth import username, password
from query.userPage import queryStr, mappers
# from query.groupById import queryStr, mappers
# from query.acClassificationPage import queryStr, mappers
@app.get("/query")
async def fullPipe():
    # username = "john.newbie@world.com" , password = "john.newbie@world.com", queryStr, mappers = 

    global pandasData
    token = await getToken(username, password)
    qfunc = query(queryStr, token)
    response = await qfunc({})

    outfile(response, 'response')

    data = response.get("data", None)
    result = data.get("result", None)
    if result is None:
        return {"error": "No 'result' key in response data"}

    flatData = flatten(result, {}, mappers)
    pandasData = toTable(flatData)
    return pandasData


import aiofiles
import pandas as pd
from fastapi.responses import FileResponse

@app.get("/download")
# The user can click on the button then go to the download/{file_format} endpoint
async def info():
    return {"message": "In fontend we will create csv and xlsx buttons to download the file. The user can click on the button then go to the download/{file_format} endpoint"}


from datetime import datetime
from fastapi import HTTPException, BackgroundTasks
import os

def remove_file(file_name: str):
    os.remove(file_name)

@app.get("/download/{file_format}")
async def download(file_format: str, background_tasks: BackgroundTasks):
    # Validate file format
    valid_formats = ['csv', 'xlsx', 'xls']
    if file_format not in valid_formats:
        raise HTTPException(status_code=400, detail=f"Invalid file format. Valid formats are {', '.join(valid_formats)}")

    df = await fullPipe()

    # Use the current time to create a unique file name
    file_name = f'table_{datetime.now().strftime("%Y%m%d%H%M%S")}.{file_format}'

    try:
        if file_format == 'csv':
            df.to_csv(file_name, index=False, encoding='utf-8')
            response = FileResponse(file_name, media_type='text/csv', filename=file_name)
        elif file_format in ['xlsx', 'xls']:
            df.to_excel(file_name, index=False)
            response = FileResponse(file_name, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=file_name)
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while creating the file.")

    # Schedule the file to be deleted after the response is sent
    background_tasks.add_task(remove_file, file_name)

    return response

# create sunburst chart
@app.get("/sunburst")
async def sunburst():
    df = await fullPipe()
    df = df.fillna('NA')
    df = df.to_dict(orient='records')
    return df

