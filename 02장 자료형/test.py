# 사용자로부터 이름과 성적을 입력받아 총점과 평균을 구해 출력하는
# 프로그램을 작성하세요
name = input("이름을 입력하세요: ")
kor = input("국어 점수를 입력하세요: ")
eng = input("영어 점수를 입력하세요: ")
math = input("수학 점수를 입력하세요: ")

total = int(kor) + int(eng) + int(math) # str -> int
avg = total / 3

print(name, "님의 총점=", total, "평균=", avg, "입니다.")

# print("입력하신 이름은 ", name, "입니다.")
# print(type(data))

