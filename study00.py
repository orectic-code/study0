# ## １ 変数の使い方
# 変数を使って、「ねずこ」と「ぜんいつ」 は仲間ですとprint文を使って表示させてみよう<BR>
# なお、ねずこをname1、ぜんいつをname2として定義してください。
name1 = "ねずこ"
name2 = "ぜんいつ"
print(name1 + "と" + name2 + "は、仲間です")

# ## ２ if文の使い方
# １のソースを改造して、name2が敵キャラの「むざん」だった場合に<BR>
# 仲間ではありませんと表示させてみよう。
name2 = "むざん"
if name2 == "むざん":
    print(name2 + "は、仲間ではありません")


# ## ３ 配列の使い方
# 以下の配列に対して、キャラクター「ぜんいつ」を追加してみよう。
# appendを使うことで追加できます。
names = ["たんじろう","ぎゆう","ねずこ","むざん"]
names.append("ぜんいつ")
print(names)


# ## ４ for文の使い方
# ３のソースコードで使用したnameのキャラクターをfor文を使って<BR>
# １行に１キャラクター表示してみよう

for name in names:
    print(name)

## ５　関数の使い方
# 関数を１つ作ってみましょう。<BR>
# 関数化したら、関数を呼び出して結果が表示されることを確認してみよう。

def print_hand():
    print('ピース')

print_hand()
# ## ６ 引数を使う関数の使い方
# 以下のようにhikisuuの部分が引数です。引数は関数の外から変数を関数内に渡すことができます。\n
# このような引数を使う関数を作成してみよう。<BR>

# def test(hikisuu):<BR>

# 【仕様】<BR>
# 関数名：なんでも良い<BR>
# 引数：キャラクターの名前を格納する変数<BR>
# 関数で行う処理：キャラクターのリスト（３、４で使ったもの）の中に、<BR>
# 引数で入力されたキャラクター名が存在するか確認して結果をprint文で表示させる<BR>
# 例）引数が「ぎゆう」→nameにぎゆうが存在する→ぎゆうは含まれますと表示

name = "ぎゆう"

if name in names:
    print('{}は含まれます.{}'.format(name, names))
else:
    print('{}は含まれません.{}'.format(name, names))
# 0 is a member of [0, 1, 2].