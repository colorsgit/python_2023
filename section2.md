# 値と演算

Pythonでは数値や文字といった基本的な値(リテラル)を組み合わせてデータを表現します。

## リテラル

Pythonの代表的なリテラルは、次の５つです。

- 整数
- 小数
- 真偽値
- 文字列
- リスト
- タプル
- 辞書

### 整数 (int)

```python
0, 1, 2, ...
```

```python
-1, -2, ...
```

### 小数 (float)

```python
0.1, -0.1, 3.14, 1e10...
```

### 真偽値 (bool)

```python
True, False
```

### 文字(列) (str)

```python
'A', "A", "abc", 'abc', ...
```

### リスト (list)

```python
[0, 1, 2], [0, 0.1, "abc"], [0], [], ...
```

### タプル (tuple)

```python
(0, 1), (0, 0.1, "abc"), (0,), (), ...
```

### 辞書 (dict)

```python
{"apple": 150, "orange": 100}, ...
```

## 例題

|くだもの|値段|
|-|-|
|Apple|150|
|Orange|100|
|Peach|300|

この値段表を辞書を使って表すと以下のようになります。

```python
{
    "Apple": 150,
    "Orange": 100,
    "Peach": 300
}
```

## 練習問題

|名前|算数|国語|
|-|-|-|
|北野|80|85|
|山本|75|83|
|岡本|88|72|

この３人の成績を表すデータを作ってください。

<!--
```python
[
    ("北野", 80, 85),
    ("山本", 75, 83),
    ("岡本", 88, 72),
]
```
-->

## 演算

リテラルは演算により別のリテラルを作ることができます。

### 整数・小数

```python
1 + 1 # 2 足し算
1 - 1 # 0 引き算
2 * 3 # 6 掛け算
6 / 3 # 2 割り算
3 / 2 # 1.5 割り算
5 // 3 # 1 割り算ver.2
5 % 3 # 2 剰余
2 ** 3 # 8 指数
```

### 真偽値

```python
True and False # False 論理積
True or False # True 論理和
not True # False 否定
```

### 文字列・リスト・タプル

```python
"abc" + "def" # "abcdef"　結合
len("abc") # 3 長さ取得
"abc"[1] # 'b' 要素取得
```

```python
[0, 1] + [2, 3] # [0, 1, 2, 3]　結合
len([0, 1, 2]) # 3 長さ取得
[0, 1, 2, 3][1] # 1 要素取得
```

```python
(0, 1) + (2, 3) # (0, 1, 2, 3)　結合
len((0, 1, 2)) # 3 長さ取得
(0, 1, 2, 3)(1) # 1 要素取得
```

要素取得のインデックスは0から始まります。

### 辞書

```python
{"apple": 150, "orange": 100}["apple"] # 150
```

## 演算子の優先順位

以下のプログラムの実行結果はどうなるでしょうか。

```python
1 + 2 * 3
```

答えは7です。こうなるのは、足し算の演算子`+`より掛け算の演算子`*`が優先的に計算されるからです。

```python
1 + (2 * 3)
```

全ての演算子には、このように優先順が設定されており、優先度の高い演算子から順番に計算されていきます。

演算子の優先順が分からないときや、ややこしいときは、丸括弧`()`を使って優先順を指示できます。

```python
(1 + 2) * 3 # 9
```

## 文字列、リスト、タプルの使い分け

文字列、リスト、タプルはほとんど同じように使えますが、慣習的に使い分けます。

|文字列|リスト|タプル|
|-|-|-|
|要素の変更や追加をしない<br/>要素が文字のみ|要素の更新や追加をする<br/>全ての要素が同じ種類|要素の更新や追加をしない<br/>要素が異なる種類でも良い|

例えば、人名は文字列、クラス名簿はリスト、空間座標はタプルを用いるのが普通です。

## 変数

リテラルは変数という「入れ物」に代入することで、使い回すことができます。

変数への代入は次のように行います。

```python
x = 1
```

この例では、変数`x`に値`1`を代入しています。

変数の利用は次のように行います。

```python
a = 1
b = 2
a + b # 3
```

複数の変数にまとめて代入することもできます。

```python
a, b, c = 1, 2, 3
a, b, c = [1, 2, 3]
a, b, c = (1, 2, 3)
```

同じ変数に再度代入をすると、変数の値が上書きされます。

```python
a = 1
a = 2
# a = 2
```

## 値の表示

Pythonで演算の結果や変数の中身を表示するには、`print`を使います。

```python
a = 1
print(a) # 2
print(a + 1) # 2
```

## 例題

|くだもの|値段|
|-|-|
|Apple|150|
|Orange|100|
|Peach|300|

この値段表を表す辞書`store`を作成し、これを用いて、りんごを10個とももを2個買ったときの価格を求めて表示してください。

```python
store = {
    "Apple": 150,
    "Orange": 100,
    "Peach": 300
}

print(store["Apple"]*10 + store["Peach"]*2)
```

## 練習問題

|名前|算数|国語|
|-|-|-|
|北野|80|85|
|山本|75|83|
|岡本|88|72|

この３人の情報をまとめたリスト`grades`を作成してください。次に、これを用いて、算数の点数と国語の点数の平均点の差を求めて表示してください。

```python
grades = [
    ("北野", 80, 85),
    ("山本", 75, 83),
    ("岡本", 88, 72)
]
```

```python
sum_math = grades[0][1] + grades[1][1] + grades[2][1]
sum_jpn = grades[0][2] + grades[1][2] + grades[2][2]
print(sum_math/3 - sum_jpn/3)
```