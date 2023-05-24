# 条件分岐・ループ

## 前回練習問題４（RSA暗号）補足

RSA復号鍵を作るときに、変数 $e$ と $f$ が整数で互いに素のとき、

$$
d \times e \equiv 1 \ \ \mod{f}
$$

を満たす整数 $d$ を見つけるという処理がありました。

当初はループで計算する方法しか思いつかなかったのですが、実は`pow`という演算を使うと簡単に計算できるらしいです。

```python
pow(base, exp, mod)
```

> base の exp 乗を返します; mod があれば、base の exp 乗に対する mod の剰余を返します。

>  mod が存在して exp が負の整数の場合、 base は mod と互いに素 (最大公約数が1) でなければなりません。この場合、 inv_base を base に対する mod を法とするモジュラ逆数 (base と inv_base の積を mod で割った余りが1になるような数) として、 pow(inv_base, -exp, mod) が返されます。

```python
d = pow(e, -1, f)
```

## プログラムの流れ

プログラムは、

- 逐次処理
- 条件分岐
- 繰り返し

の３種類の処理の組み合わせです。

例えば、テトリスのプログラムを考えると、

1. ブロックを落とす（逐次処理）
1. もし一列埋まったら消す（条件分岐）
1. フィールド上部に達するまで繰り返す（繰り返し）

となっています。

Pythonでは、条件分岐を`if`文と`match`文で行い、繰り返しを`for`文と`while`文で行います。

## if文

`if`文では条件により２つの処理を切り替えます。

### if ... else ...

条件が満たされたときは`if`の処理を行い、満たされないときは`else`の処理を行います。`if`の処理内容や`else`の処理内容の部分は、行頭にインデント（字下げ）を入れます。

```python
x = 1

if x == 1:
    print("x is 1")
else:
    print("x is not 1")
```

### if ...

`else`は省略することができます。

```python
x = 1

if x == 1:
    print("x is 1")
```

### if ... elif ... else ...

条件が満たされなかったときに、さらに別の条件をチェックすることもできます。

```python
x = 1

if x == 1:
    print("x is 1")
elif x == 2:
    print("x is 2")
elif x >= 3:
    print("x is 3")
else:
    print("x is not positive")
```

### 例題１

|くだもの|値段|
|-|-|
|リンゴ|150|
|ミカン|80|

ある青果店ではリンゴとミカンを販売しています。変数`x`が商品名を表すとき、`x`に応じて商品の値段を表示するプログラムは次のように書けます。

```python
x = "Apple"

if x == "Apple":
    print(150)
elif x == "Orange":
    print(80)
else:
    print("We do not have " + x)
```

### 練習問題１

整数`x`が偶数か奇数かを表示するプログラムを作ってください。

```python
x = 1

???
```

## match文

`match`文では、複数の条件分岐を一度に表すことができます。`if`文とは違い、条件として、`case`の後に変数の値を指定します。どの条件にも当てはまらない場合の処理は、`case _`に書きます。

```python
x = "Apple"

match x:
    case "Apple":
        print(150)
    case "Orange":
        print(80)
    case _:
        print("We do not have " + x)
```

`match`文で条件式を条件に使いたい場合は、次のように書きます。

```python
x = 1

match x:
    case x if x % 2 == 0:
        print("x is even")
    case x if x % 2 == 1:
        print("x is odd")
```

### 練習問題２

整数`x`が負、零、正のいずれかを表示するプログラムを作成してください。

```python
x = 1

???
```

## for文

リストの要素を一つずつ取得して変数に代入し、処理を行います。

```python
ls = [1, 2, 3]

for e in ls:
    print(e)
```

```
> 1
  2
  3
```

### range演算

`[0, 1, 2, 3, ..., n-1]`というリストはよく使われるため、`range(number)`という特別な形で表すことができるようになっています。

```python
ls = ["a", "b", "c"]

for i in range(3):
    print(f"{i}th element is {ls[i]}")
```

```
> 0th element is a
  1th element is b
  2th element is c
```

### 例題３（fold演算）

整数のリスト`ls`の中身の合計を求めて表示するプログラムは次のように書けます。

```python
ls = [1, 2, 3, 4, 5]

r = 0
for e in ls:
    r += e

print(r)
```

もしくは、リストの添字をループ変数とすると次のようになります。

```python
ls = [1, 2, 3, 4, 5]

r = 0
for i in range(len(ls)):
    r += ls[i]

print(r)
```

## 練習問題３（map演算）

整数のリスト`ls`の中身に、各々3を足したリストを作り、表示するプログラムを作ってください。

例えば、

```python
ls = [1, 2, 3, 4, 5]
```

のときは、

```python
[4, 5, 6, 7, 8]
```

と表示してください。

## while文

条件式が満たされている間、処理を繰り返し続けます。

```python
x = 3

while x > 0:
    print(x)
    x -= 1
```

```
> 3
  2
  1
```

### 例題４（for文の書き換え）

```python
ls = [1, 2, 3]

for e in ls:
    print(e)
```

このプログラムを`while`文を使って書き換えると次のようになります。

```python
ls = [1, 2, 3]
i = 0

while i < len(ls):
    print(ls[i])
    i += 1
```

## break文・else文

`break`文を使うと、繰り返し処理を途中で強制的に終了することができます。

```python
ls = [1, 2, 3, 4, 5]
x = 3

for e in ls:
    if e == x:
        print("ls includes x")
        break
```

`else`文は、繰り返し処理が`break`文で強制終了されなかったときにのみ実行されます。

```python
ls = [1, 2, 3, 4, 5]
x = 6

for e in ls:
    if e == x:
        print("ls includes x")
        break
else:
    print("ls does not include x")
```

### 例題４（数当てゲーム）

ユーザーに数字`x`の値を当ててもらうゲームは次のように書けます。ユーザーに文字を入力してもらうときは、`input()`を使います。また、文字を整数に変換するときには、`int(string)`を使います。

```python
x = 3

while True:
    print("Please input a number.")

    s = input()
    n = int(s)

    if n == x:
        print("Exactly!!")
        break
```

## 練習問題５（ユークリッドの互除法）

変数 $e$ と $f$ が整数で互いに素で $f > e$ のとき、

$$
d \times e \equiv 1 \ \ \mod{f}
$$

を満たす整数 $d$ を見つけて表示してください。

この問題は、二元一次不定方程式の解を求める問題に帰着できます。

$$
\begin{align*}
d \times e &\equiv 1 \ \ \mod{f} \\
\therefore \ \ d \times e &= f \times a + 1 \ \ \text{(there exists such a)} \\
\therefore \ \ f \times (-a) + e \times d &= 1
\end{align*}
$$

これは、拡張ユークリッドの互助法で解くことができます。

### （普通の）ユークリッドの互除法

$$
a = b \times q + r
$$

のとき、 $a$ と $b$ の最大公約数は $q$ と $r$ の最大公約数と等しい。

### 拡張ユークリッドの互除法

$a$ と $b$ が互いに素で $a > b$ のとき、

$$
ax + by = 1
$$

を満たす $x$ と $y$ を求めることを考えます。

この式は、

$$
\begin{align*}
ax + by &= 1 \\
\therefore \ \ (qb + r)x + by &= 1 \\
\therefore \ \ b(qx + y) + rx &= 1 \\
\end{align*}
$$

と式変形できます。ここで、

$$
\begin{align*}
x' &= qx + y \\
y' &= x
\end{align*}
$$

とすると、

$$
bx' + ry` = 1
$$

となり、 $b$ と $r$ に関する方程式になります。ユークリッドの互除法より、 $b$ と $r$ は互いに素であり、 $b > r$です。これを繰り返すと、

$$
\begin{align*}
1x'' + 0y'' &= 1 \\
\therefore x'' &= 1
\end{align*}
$$

となり、解が求まります。解の不定性は、 $y''$ の選び方の任意性に現れています。

後は、このプロセスを逆に辿ると $x$ と $y$が求まります。

### 問題

以下のプログラムは拡張ユークリッドの互除法で $d$ を求めるプログラムです。２箇所の`???`を埋めてプログラムを完成させてください。なお、`#`で始まる行はコメント行といい、プログラムの実行時には無視されます。

```python
e = 43
f = 60

# Solve below equation
#   ax + by = 1
# where
#   a is f
#   b is e
#   x is (-a)
#   y is d
a = f
b = e
qs = []
while b != 0:
    q = a // b
    r = a % b

    # store q in qs
    qs = ???

    a = b
    b = r

# x'' = 1
# y'' = 0
x = 1
y = 0
for q in qs:
    ???

# y is d
d = y

print(d)
```
