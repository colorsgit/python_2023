# 関数

## 練習問題１の解答例

```python
def has(x, ls):
    for e in ls:
        if x == e:
            return True
    return False
```

## 練習問題２の解答例

```python
def map(f, ls):
    r = []
    for e in ls:
        r += [f(e)]
    return r
```

## 練習問題３の解答例

```python
apply = lambda f, x: f(x)
```

## 練習問題４の解答例

```python
def log(f, args=[], kargs={}, exec_type="production"):
    is_prod = exec_type == "production"

    if not is_prod:
        print("start")

    r = f(*args, **kargs)

    if not is_prod:
        print("end")
       
    return r
```

## 練習問題５の解答例

```python
def comp(f, g):
    def func(*args, **kargs):
        return f(g(*args, **kargs))
    return func
```
