name1 = "ねずこ"
name2 = "ぜんいつ"
print(name1 + "と" + name2 + "は、仲間です")


name2 = "むざん"
if name2:
    print(name2 +"は仲間ではありません")


names=["たんじろう","ぎゆう","ねずこ","れんごく"]
names.append("ぜんいつ")
print(names)


name = "むざん"
if name in names:
    print('{}'"が含まれます" .format(name,names))
else:
    print('{}'"は含まれません".format(name,names))
# 0 is a member of [0, 1, 2].
