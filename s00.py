# 1
name1 = "ねずこ"
name2 = "ぜんいつ"
print(name1,name2)

# 2
name2 = "むざん"
if name2 == "むざん":
    print("仲間ではありません")

# 3
names=["たんじろう","ぎゆう","ねずこ","むざん"]
names.append("ぜんいつ")
print(names)

# 4
for i in names:
    print(i)

# 5
def print_hand():
    print('ピース')

print_hand()

# 6
def search(name):
    if name in names:
        print(f'{name}は含まれます.')
    else:
        print(f'{name}は含まれません.')
        #0 is a member of [0, 1, 2]

search('今井')