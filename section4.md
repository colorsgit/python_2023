# 関数

## 関数とは

Pythonでは、関数という仕組みによって、よく使うプログラムの使いまわしが出来るようになっています。

例えば、ある数`x`が偶数かどうか調べるプログラムを考えます。

```python
x = 143
r = False

if x % 2 == 0:
    r = True
else:
    r = False
```

このプログラムを何度も使いたいときは関数を作ります。

```python
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False
```

関数はプログラムの集まりです。値を関数に渡すと、関数が実行されて結果が返されます。関数に渡す値を引数といい、関数から返される値を返り値といいます。

今まで出てきた、`print`、`len`、`range`などは全て関数でした。

### 関数の定義

Pythonでの関数定義は次のように行います。

```python
def [関数名]([引数１], [引数２], ...):
    [関数の中身]
    return [返り値]
```

関数の中には複数の`return`を書くこともできます。その場合は、最も早く実行された`return`で関数の実行が終了し、返り値が返されます。また、引数のない関数や、返り値のない関数も定義できます。

### 関数の利用

関数を利用するには次のように書きます。

```python
[関数名]([引数１], [引数２], ...)
```

例えば、以下は先程定義した`isEven`関数の結果を表示するプログラムです。

```python
x = 3

if isEven(x):
    print("x is even")
else:
    print("x is not even")
```

### ローカル変数

関数内部で定義した変数をローカル変数といいます。

以下の例では、`x`と`y`が引数、`r`がローカル変数です。

```python
def add(x, y):
    r = x + y
    return r
```

## 例題１

ある数が素数かどうか判定する関数は次のように書くことができます。

```python
def isPrime(x):
    for n in range(1, x):
        if x % n == 0:
            return True
    return False
```

## 練習問題１

ある値がリストに含まれているか判定する`has`関数を書いてください。

```python
def has(x, ls):
    ???

has(1, [0, 1, 2]) # True
has(3, [2, 4, 6]) # False
```

## 高階関数

関数は引数に関数を渡すこともできます。

例えば、以下は渡された関数を実行し、実行開始と終了を表示する関数です。

```python
def log(f):
    print("start")
    f()
    print("end")
```

## 例題２（fold関数）

先週紹介した`fold`演算を関数にしました。

```python
def fold(f, b, ls):
    r = b
    for e in ls:
        r = f(r, e)
    return r
```

例えば、数値リストの合計値を求めるプログラムは`fold`関数を使って次にように書けます。

```python
def add(x, y):
    return x + y

s = fold(add, 0, [1, 2, 3, 4, 5])
print(s)
```

## 練習問題２（map関数）

関数とリストを引数にとって、リストの各要素で関数を実行した結果のリストを返す関数を定義してください。

```python
def map(f, ls):
    ???
```

例えば、`map`関数は以下のような使い方ができます。

```python
ls = map(isEven, [0, 1, 2, 3, 4, 5])
print(ls) # [True, False, True, False, True, False]
```

ヒント：`for`文でリストをコピーするときは以下のようにします。

```python
r = []
for e in ls:
    r += [e]
```

## ラムダ式

Pythonでは以下の方法で関数を作ることもできます。

```python
lambda [引数１], [引数２], ...: [返り値]
```

例えば、足し算の関数`add`は以下のように定義できます。

```python
add = lambda x, y: x + y
```

ラムダ式は高階関数に渡すこともできます。

```python
fold(lambda x, y: x + y, 0, [1, 2, 3, 4, 5]) # 15
```

## 練習問題３

次の関数をラムダ式に書き直してください。

```python
def apply(f, x):
    return f(x)
```

## 引数いろいろ

### 実引数と仮引数

これまで引数とまとめて呼んでいたものは、正確には、実引数parameterと仮引数argumentと呼び分けます。

関数定義のときに設定する引数を仮引数、関数実行のときに渡す引数を実引数といいます。

例えば、以下の例では`x`は仮引数、`a`は実引数です。

```python
def inc(x):
    return x + 1

a = 1
inc(a)
```

### キーワード引数

関数に実引数を渡すときには、渡す先の仮引数名を指定できます。

```python
def sub(x, y):
    return x - y

sub(y=1, x=2) # 1
```

### デフォルト引数

関数の仮引数には既定値を設定することができます。既定値が設定された仮引数には、関数実行時に実引数を渡さなくてもよいです。

```python
def log(message, prefix=""):
    print(prefix + message)

log("start", "[06/01 12:00]") # [06/01 12:00]start
log("start") # start
```

なお、先程のキーワード引数はデフォルト引数と組み合わせて使われることがほとんどです。

### 可変長引数

関数は任意の数の引数を取るように定義することもできます。

関数の仮引数の前に`*`をつけると、実引数がリストとして渡されます。

```python
def prints(*args):
    for e in args:
        print(e)
```

関数の仮引数の前に`**`をつけると、キーワード引数が辞書として渡されます。

また同様にして、リストや辞書を、各要素が一つの引数に対応する形で、関数に渡すこともできます。

```python
def apply(f, *args, **kargs):
    f(*args, **kargs)
```

## 練習問題４

関数の実行記録を表示する関数`log`を作ってください。ただし、`log`は実行する関数`f`、可変長引数`args`、キーワード引数`kargs`、および実行タイプ`exec_type`を引数に取るようにしてください。また、返り値は、渡した関数の実行結果にしてください。

実行タイプには、`"production"`と`"development"`のいずれかを渡すものとし、既定値は`"production"`としてください。

実行タイプが`"production"`のときは、単に関数を実行するのみとし、`"development"`のときは、関数の実行前と実行後に、それぞれ`start`と`end`と表示するようにしてください。

以下は`log`関数の実行例です。

```python
def print_sub(x, y):
    r = x - y
    print(r)
    return r

log(print_add, args=[1, 2], exec_type="development")
# start
# -1 
# end

log(print_sub, kargs={"x": 2, "y":1}, exec_type="development")
# start
# 1
# end

log(print_add, args=[1, 2])
# start
# end
```

## 複数の返り値

関数から複数の値を返したい場合は、タプルを作って返り値とすることが多いです。

```python
def div(x, y):
    q = x // y
    r = x % y
    return (q, r)

q, r = div(5, 3)
```

## 自由変数と束縛変数

関数内部で使用される変数の内、関数内部で定義されたローカル変数や引数として渡された変数を束縛変数、関数外部で定義された変数を自由変数といいます。

例えば、以下の関数`func`において、`a`は自由変数、`b`と`x`は束縛変数です。

```python
a = 1

def func(x):
    b = x + 1
    return b
```

## クロージャー

関数は、内部で別の関数を定義して、その関数を返すこともできます。

```python
def map_gen(f):

    def func(ls):
        r = []
        for e in ls:
            r += [f(e)]
    
    return func

inc_map = map_gen(lambda x: x + 1)
inc_map([1, 2, 3]) # [2, 3, 4]
```

このとき、内部で定義された関数は、定義された環境の自由変数を保持します。このように、自由変数を記憶した関数のことをクロージャーといいます。

例えば、上の`map_gen`関数の内部で定義されている`func`関数は、自由変数`f`を内部に保持するのでクロージャーです。

クロージャー内に保持されている自由変数を書き換えるときは、ローカル変数定義と区別するために、`nonlocal`キーワードを使用します。

```python
x = 0

def func():
    nonlocal x
    x = 1
```

## 例題３

少し技巧的ですが、クロージャーを使うと複数の関数間で状態を共有することができます。

```python
def gen():
    x = 0

    def inc():
        nonlocal x
        x += 1
    
    def dec():
        nonlocal x
        x -=1
    
    def get():
        return x
    
    return (inc, dec, get)

inc, dec, get = gen()
inc()
inc()
print(get()) # 2
dec()
print(get()) # 1
```

## 練習問題５

関数合成を行う`comp`関数を定義してください。なお、引数`g`に渡される関数の引数は任意としたいので、可変長引数を使って定義してください。

```python
def comp(f, g):
    ???

inc = lambda x: x + 1
dbl = lambda x: 2 * x
add = lambda x, y: x + y

odd = comp(inc, dbl)
odd(3) # 7

comp(dbl, add)(1, 2) # 6
```
