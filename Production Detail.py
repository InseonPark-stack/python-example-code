import pandas as pd
import re
import time

# 엑셀 파일에서 데이터프레임 불러오기
df = pd.read_excel('/Users/park-inseon/Desktop/Kore/DaewonCTS/Code/미등록 정상 유무 확인.xlsx', sheet_name='숫자NO만 추출')

# 추출할 키
keys_to_extract = ['CPU 넘버','GPU 종류','메모리 용량','SSD 용량','무게','화면 크기','운영체제(OS)','용도']
# keys_to_extract = ['용도']

findedRowNum = []

# PRDT_SPC_INFO 열의 각 링크를 확인
for index, row in df.iterrows():
    details = row['PRDT_SPC_INFO']
    try:
        data_list = details.split(",")

        # key-value 형태의 변수를 저장할 딕셔너리 초기화
        data_dict = {}

        # 분할된 항목을 순회하며 key-value 쌍으로 추출하여 딕셔너리에 저장
        for item in data_list:
            # key, value = item.split(":", 1)  # ":"를 기준으로 key와 value 분할, 1번만 분할
            # data_dict[key.strip()] = value.strip()  # 공백 제거 후 딕셔너리에 저장
            for key in keys_to_extract:
                if key in item:
                    # 키가 발견되면 값을 추출해서 딕셔너리에 저장
                    key_value = item.split(':')
                    if len(key_value) == 2 and len(key_value[1]) > 0 and '범위' not in key_value[0]:
                        data_dict[key_value[0]] = key_value[1]
                        print(f'{index} 열에서 추출한 값입니다')
                        print(f'{key_value[0]} : {key_value[1]}')
                        findedRowNum.append(index);
                        df.at[index, key_value[0]] = key_value[1]
            # df.at[index, '추출한 값'] = pd.Series(data_dict)
        time.sleep(1);
    
    except Exception as e:
        print(f'{index} 줄에 문제가 있습니다. 오류 메시지: {str(e)}')

df.to_excel('extract_value.xlsx',index=False)
print(findedRowNum);