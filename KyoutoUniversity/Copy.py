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