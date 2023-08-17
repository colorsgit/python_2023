# sqlite

## データベースとは

Webアプリではデータを保存しておきたいことがよくあります。例えば、ユーザーのメールアドレスとパスワードなどです。こうしたデータの保存先がデータベースです。

データベースには様々な種類があります。そのなかで最もよく使われるのがRDB(Relational DataBase)です。RDBにも幾つも製品がありますが、今回は最も手軽に扱えるsqliteというソフトを使います。

RDBではテーブルという単位でデータを管理します。例えば、SNSサービスに使うデータベースには、ユーザーテーブルや投稿テーブルがあるでしょう。テーブルはExcelの表のような構造をしています。

例えば、ユーザーテーブルは次のような構造です。

|ID|name|email|password|
|-|-|-|-|
|1|Tanaka|tanaka@example.com|tanakapw|
|2|Sato|sato@example.com|satopw|
|3|Suzuki|suzuki@example.com|suzukipw|

RDBはSQL(Structured Query Language)を使用して操作します。この資料では主にSQLの使い方を見ていきます。

## SQLの種類

SQLは次の三種類に分けられます。

- DDL(Data Definition Language)
- DML(Data Manipulation Language)
- DCL(Data Control Language)

DDLはテーブルの作成や削除といったデータベースオブジェクトの操作に用います。

DMLはデータの追加や削除といったテーブルに対する操作に用います。

DCLはトランザクション管理に用います。トランザクションについては、この資料では説明を省略します。

## DDL

- テーブルの追加

```sql
create table user (id integer, name text, email text, password text);
```

- テーブルの削除

```sql
drop table user;
```

## DML

- データの取得

```sql
select name from user;
select name, email from user;
select * from user;
```

データ取得時に条件を指定することができます。

```sql
select name from user where id=1;
```

- データの追加

```sql
insert into user (id, name, email, password)
values (4, 'Ueno', 'ueno@example.com', 'uenopw');
```

- データの削除

```sql
delete from user where id=4;
```

### テーブル結合

userテーブル
|id|name|email|password|
|-|-|-|-|
|1|Tanaka|tanaka@example.com|tanakapw|
|2|Sato|sato@example.com|satopw|
|3|Suzuki|suzuki@example.com|suzukipw|

postテーブル
|id|message|author|
|-|-|-|
|1|hello|2|
|2|how are you?|1|
|3|i am fine|2|

- 内部結合

```sql
select user.name, post.message from user
inner join post
on user.id=post.auther
```

|name|message|
|-|-|
|Tanaka|how are you?|
|Sato|hello|
|Sato|i am fine|

- 左外部結合

```sql
select user.name, post.message from user
left outer join post
on user.id=post.auther
```

|name|message|
|-|-|
|Tanaka|how are you?|
|Sato|hello|
|Sato|i am fine|
|Suzuki||

## Pythonライブラリ

sqliteはPythonで操作することができます。

```python
import sqlite3

dbname = 'test.db'
conn = sqlite3.connect(dbname)
cur = conn.cursor()

cur.execute('CREATE TABLE user (...)')

cur.execute('INSERT INTO user (...) values (...)')
cur.execute('INSERT INTO user (...) values (...)')
cur.execute('INSERT INTO user (...) values (...)')

conn.commit()

cur.close()
conn.close()
```

データ取得

```python
cur.execute('SELECT * FROM user')
print(cur.fetchall())
```

```
[(1, "Tanaka", "tanaka@example.com", "tanakapw")]
```

## 練習問題

次のユーザーテーブルと投稿テーブルを作ってください。

ユーザーテーブル

|id|name|password|
|-|-|-|
|1|Tanaka|tanakapw|
|2|Sato|satopw|
|3|Suzuki|suzukipw|

投稿テーブル

|id|message|auther|
|-|-|-|
|1|I found an interesting object on morning.|3|
|2|How is its shape like?|1|
|3|It's like an egg, but made of metal.|3|
|4|Hey, it must be part of my artwork.|2|
|5|I dropped it somewhere last night.|2|

1. ユーザー名`Tanaka`、パスワード`wrongpw`でのログインが成功するかどうかSQLを使って調べてください。
1. 投稿idが4番の投稿の投稿主の名前をSQLを使って調べてください。

<!--
```sql
create table user (id integer, name text, password text);

create table post (id integer, message text, auther integer);

insert into user (id, name, password)
values (1, 'Tanaka', 'tanakapw'),
       (2, 'Sato','satopw'),
       (3, 'Suzuki', 'suzukipw');

insert into post (id, message, author)
values (1, 'I found an interesting object on morning', 3),
       (2, 'How is its shape like?', 1),
       (3, 'It''s like an egg, but made of metal.', 3),
       (4, 'Hey, it must be part of my artwork.', 2),
       (5, 'I dropped it somewhare last night.', 2);

select name from user
inner join on post
on user.id=post.author
where post.id=4;
```
-->
