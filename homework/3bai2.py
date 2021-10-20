chieu_cao = int(input("nhập chiều cao cm: "))
if chieu_cao >=1 :
    can_nang = int(input("nhập cân nặng kg: "))
    chieucao = chieu_cao * 0.01
    bmi = can_nang / 2 * chieucao
    print("BMI của bạn: ", bmi)
    if bmi <16 :
        print("Thiếu cân nghiêm trọng")
    if 16 <= bmi <= 18.5 :
        print("Thiếu cân")
    if 18.5 < bmi <= 25 :
        print("Bình thường")
    if 25<bmi<30 :
        print("thừa cân")
    if bmi > 30 :
        print("béo phì")


