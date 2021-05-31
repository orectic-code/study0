# 1
name1 = "ねずこ"
name2 = "ぜんいつ"
print(f'{name1}と{name2}は仲間です')

# 2
name2 = "今井"
if name2 == "むざん":
    print(f'{name2}仲間ではありません')
else:
    print(f'{name2}は仲間です')

# 3
names=["たんじろう","ぎゆう","ねずこ","むざん"]
names.append("ぜんいつ")
print(names)

# 4
for i in names:
    print(i)

# 5
def microwave():
    print("時間を指定します")
    print("温めます")
    print("温めるのをやめます")

microwave()

# 6
def search(name):
    if name in names:
        print(f'{name}は含まれます.')
    else:
        print(f'{name}は含まれません.')
        #0 is a member of [0, 1, 2]

search('ねずこ')