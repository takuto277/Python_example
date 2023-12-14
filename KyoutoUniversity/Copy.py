import math

# リストの中身は参照型
hoge = [[1,2],[3,4]]
fuga = hoge.copy()

fuga.append([5,6])
print(hoge)
print(fuga)

fuga[0][0] = 0
print(hoge)
print(fuga)

# Python Tutor というウェブサイト（http://www.pythontutor.com）では
# 短い Python プログラムを入力して，その動作（変数の利用）を可視化してくれる

age = {"one":1, "two":2, "three":3}
print(age)
print(age["one"])
age["four"] = 4
print("four" in age)

for i in range(10):
    if i == 1:
        continue
    if i == 8:
        print("finish")
        break
    print(i)

for i, d in enumerate(age):
    print(i,d)

a = [3,4,5,6]
sum = 0
for i in range(len(a)):
    sum += a[i]
average = sum/len(a)
print(average)

(a == 1) and (b != 0)

c = 2.99792458E8
na = 6.02214076E23
form = "light speed is {0:12.8g} m/s, abogadoto figure is {1:12.8g} mol**(-1)."
print(form.format(c, na))

while True:
    x = input("input plus figure")
    try:
        x = float(x)
    except ValueError:
        print(x, "this isnot figure")
        continue
    except:
        print("it is unexpected")
        exit()
    if x <= 0:
        print(x, "it is not plus")
        continue
    print(x)
