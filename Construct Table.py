import Controller as Ct
import Token as tk

def output_data():
    print("This is a function")

def input_data():    
    Ct.input_data()

if __name__ == "__main__":
    while True:
        print("메뉴를 선택하세요:")
        print("0. 컬럼 출력")
        print("1. 데이터 출력")
        print("2. 데이터 입력")
        print("3. JWT토큰 생성")
        print("4. 데이터 삭제")
        print("99. 프로그램 종료")
        
        choice = input("선택: ")
        
        if choice == "0":
            Ct.print_column()
        elif choice == "1":
            output_data()
        elif choice == "2":
            Ct.input_data()
        elif choice == "3":
            tk.getToken()
        elif choice == "4":
            Ct.delete_data()
        elif choice == "99":
            print("프로그램을 종료합니다.")
            break
        else:
            print("유효하지 않은 선택입니다. 1, 2 또는 3 중에서 선택하세요.")
