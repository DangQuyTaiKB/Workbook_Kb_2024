from fastapi import FastAPI
import json
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


def read_josn(file_name):
    with open(file_name , 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def main():
    data = read_josn('systemdata.json')
    users_dat= data['users']
    
    import pandas as pd
    df = pd.DataFrame(users_dat)
    # print(df)

    df.to_excel('users_data.xlsx', index=False)

    # create pivot table
    pivot_table = df.pivot_table(values='id', index='name', columns='surname', aggfunc='count')
    pivot_table.to_excel('pivot_table.xlsx')

if __name__ == '__main__':
    main()





