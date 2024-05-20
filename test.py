import json

def read_json(file_name):
    with open(file_name , 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data



def main():
    data = read_json('users_data.json')
    users_dat = data["data"]["userPage"]
    

    import pandas as pd
    df = pd.DataFrame(users_dat)
    print(df)

    df.to_excel('users_data.xlsx', index=False)

    # create pivot table
    pivot_table = df.pivot_table(values='id', index='name', columns='surname', aggfunc='count')
    pivot_table.to_excel('pivot_table.xlsx')

if __name__ == '__main__':
    main()



