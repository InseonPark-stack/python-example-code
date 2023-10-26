import pandas as pd
import requests
import time
from bs4 import BeautifulSoup

# 엑셀 파일에서 데이터프레임 불러오기
df = pd.read_excel('/Users/park-inseon/Desktop/Kore/DaewonCTS/상품정보_20230621 suhyeok.xlsx', sheet_name='Sheet2')

# 새로운 열 '상태'를 추가하고 초기값을 '미등록'으로 설정
df['상태'] = '미등록'

# PRODUCT_URL 열의 각 링크를 확인
for index, row in df.iterrows():
    url = row['PRODUCT_URL']
    try:
        print(f'{index} 줄 확인 중입니다.')
        response = requests.get(url)
        if response.status_code == 200:
            # 응답을 BeautifulSoup을 사용하여 파싱
            soup = BeautifulSoup(response.text, 'html.parser')
            scripts = soup.find_all('script')

            # 스크립트에서 alert 메시지를 찾아 '상태' 열을 '정상'으로 업데이트
            for script in scripts:
                if '미등록 상품입니다.' in script.text:
                    df.at[index, '상태'] = '미등록'
                    print(f'{url} 링크: 미등록 상품입니다.')

            # "미등록 상품입니다."가 없는 경우 '상태' 열을 '정상'으로 업데이트
            if '미등록 상품입니다.' not in response.text:
                df.at[index, '상태'] = '정상'
            time.sleep(5);        
        else:
            print(f'{url} 링크에 문제가 있습니다. 응답 코드: {response.status_code}')
    except Exception as e:
        print(f'{url} 링크에 문제가 있습니다. 오류 메시지: {str(e)}')

# 새로운 엑셀 파일로 저장
df.to_excel('updated_excel_file.xlsx', index=False)