"""
이름, 전화번호, 이메일, 주소를 받아서연락처 입력, 출력, 삭제하는 프로그램을 완성하시오.
"""
class Contacts(object):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    def to_string(self):
        return f'이름: {self.name} 전화번호: {self.phone} 이메일: {self.email} 주소: {self.address}'

    @staticmethod
    def del_element(ls,name):
        for i, j in enumerate(ls):
            if j.name == name:
                del ls[i]
    @staticmethod
    def main():
        ls = []
        while True:
            menu = int(input("1. 주소록 추가\n"
              "0. 프로그램 종료\n""2. 출력\n""3. 수정\n""4. 삭제\n"))
            if menu == 1:
                ls.append(Contacts(input('이름:'),input('전화번호:'),input('이메일:'),input('주소:')))
            elif menu == 2:
                for i in ls:
                    print(f'출력결과: {i.to_string()}')
            elif menu == 3:

                name = input('수정할 이름:')
                contacts = Contacts(name, input('수정 전화번호'), input('수정 이메일'), input('수정 주소'))
                contacts.del_element(ls,name)
                ls.append(contacts)

            elif menu == 4:

                contacts = input('삭제할 이름:')
                contacts.del_element(ls)

            elif menu == 0:
                print("프로그램 종료")
                break
            else:
                print("잘못된 주문입니다.")
                continue

Contacts.main()