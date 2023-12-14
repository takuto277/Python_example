a = 1
b = 2
c, d = a*2, b*a
print(c,d)

h = 1
i = 2
h, i = i, h
print(h, i)

hoge = [5, 1, 4, 5]
print(hoge)
huga = [4]*10
print(huga)
text = "I have a friend that has five children"
split = text.split()
print(split)
# countに似てるかも
print(len(huga)) #10
print(len(split)) #8

# スライス
print(hoge[1:5])
yam = [5,1,3,4]
yam.append(2)
print(yam)
hoge.append(4)
hoge.extend(huga)
print(hoge)            

