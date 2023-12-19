import os

print(os.getcwd())
f = open("japanese_file.txt", "w")
f.write("日本語\n日本語\n日本語\n")
f.close()

f = open("japanese_file.txt", "r")
s = f.read()
f.close()
print(s)