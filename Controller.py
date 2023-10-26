import pandas as pd
import requests
import json
import re
import time

# 전체 테이블 데이터 가져오기
def all_query():
    url = "https://bots.kore.ai/api/public/tables/Laptop/query?sys_limit=1000&sys_offset=0"

    payload = json.dumps({
    "query": {
        "expressions": [
        {
            "field": "sys_Id",
            "operand": ">",
            "value": 0
        }
        ],
        "operator": "and"
    }
    })


    response = requests.request("POST", url, headers=headers, data=payload)
    
    data = response.json()

    return data

# 컬럼 이름만 출력
def print_column():
    
    data = all_query()
    # 특정 문자열들을 리스트로 정의
    exclude_fields = ['sys_Id', 'Created_On', 'Updated_On', 'Created_By', 'Updated_By']

    column = data['metaInfo']
    output = []
    for value in column:
        name = value['name']
        if name not in exclude_fields:
            output.append(name)
    
    print(' '.join(output))


def output_data():
    data = all_query()
    
    
    return 0

def input_data():
    # 엑셀 파일에서 데이터프레임 불러오기
    df = pd.read_excel('/Users/park-inseon/Desktop/Kore/DaewonCTS/StoredData.xlsx', sheet_name='Sheet1')

    # Data Table
    # ProductDetails Price ScreenSize Weight OS Usage SSD Memory GPUType CPUCode ImageURL ProductName ProductNo Manufacture
    # Excel
    # CATEGORYNM3	NO	NAME	IMAGE_URL	PRDT_SPC_INFO	PRICE	CPU 넘버	용도	GPU 종류	화면 크기	무게	메모리 용량	SSD 용량	운영체제(OS)

    for index, row in df.iterrows():
        manufacture = row['CATEGORYNM3']
        productNo = str(row['NO'])
        productName = row['NAME']
        imageURL = row['IMAGE_URL']
        cpuCode = row['CPU 넘버']
        gpuType = row['GPU 종류']
        memory = row['메모리 용량']
        SSD = row['SSD 용량']
        Usage = row['용도']
        OS = row['운영체제(OS)']
        weight = row['무게']
        screenSize = row['화면 크기']
        price = str(row['PRICE'])
        productDetails = row['PRDT_SPC_INFO']

        # 화면 인치 수와 무게는 숫자만 추출
        screenInch = str(re.findall(r'\d+\.\d+|\d+', screenSize)[1])
        weights = str(re.findall(r'\d+\.\d+|\d+', weight)[0])

        # 입력 API 호출
        url = "https://bots.kore.ai/api/public/tables/Laptop"

        payload = json.dumps({
        "data": {
            'Manufacture' : manufacture,
            'ProductNo' : productNo,
            'ProductName' : productName,
            'ImageURL' : imageURL,
            'CPUCode' : cpuCode,
            'GPUType' : gpuType,
            'Memory' : memory,
            'SSD' : SSD,
            'Usage' : Usage,
            'OS' : OS,
            'Weight' : weights,
            'ScreenSize' : screenInch,
            'Price' : price,
            'ProductDetails' : productDetails
        }
        })


        response = requests.request("POST", url, headers=headers, data=payload)
        
        print(f'{index} 열의 데이터 결과값 : {response.status_code}')

        time.sleep(3)


def delete_data():
    print("조건을 입력해주세요")
    print("1. 필드명")
    field_name = input("필드 이름: ")

    print("2. 조건")
    oper = input("(> , < , = ): ")

    print("3. 값")
    value = input("값 : ")

    url = "https://bots.kore.ai/api/public/tables/Laptop"

    payload = json.dumps({
    "query": {
        "expressions": [
        {
            "field": field_name,
            "operand": oper,
            "value": value
        }
        ],
        "operator": "and"
    }
    })

    response = requests.request("DELETE", url, headers=headers, data=payload)

    # 응답의 Content-Type 헤더를 확인하여 JSON 응답인지 확인합니다.
    if response.status_code == 200 and response.headers.get('content-type') == 'application/json':
        data = response.json()
        print(f'{data.get("nDeleted", 0)} 의 row가 삭제되었습니다')
    else:
        print("삭제 중 문제가 발생했습니다.")