import jwt

def getToken():


    # JWT 토큰 생성
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')

    # 생성된 토큰 출력
    print(token)
    return token
