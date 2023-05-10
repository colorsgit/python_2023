<link rel="stylesheet" href="default.css" type="text/css">

# 環境構築

## Pythonのインストール

ブラウザで「python install」と検索してPythonのホームページを開きます。

Pythonのホームページにある「Download Python x.x.x」ボタンをクリックして、Pythonのインストーラーをダウンロードします。

<div class="note">
ダウンロード：パソコンにファイルを取り込むこと<br/>
インストール：ソフトウェアを使用できるようにする
</div>

<img src="assets/pythonHP.png">

インストーラーをダブルクリックで起動します。「Add python.exe to PATH」という項目に必ずチェックを入れて、「Install Now」ボタンを押します。

<img src="assets/pythonInstaller.png">

VSCodeを起動して、上部の「Terminal」タブから、「New Terminal」をクリックします。

<img src="assets/VSCodeNewTerminal.png">

すると、VSCodeの下部に新しくTerminalパネルが開きます。パネル内に、

```
$ python --version
```

と入力して、Enterキーを押します。正しくPythonがインストールできていれば、

```
> python x.x.x
```

と表示されます。

<img src="assets/VSCodeTerminal.png">

<div class="note">
ターミナルの入力と出力を区別するために、$と>を使います。<br/>
入力の場合は、「$＋空白」の後に入力内容を書きます。<br/>
出力の場合は、「>＋空白」の後に出力内容を書きます。
</div>

## VSCodeのセットアップ

VSCodeでは様々な拡張機能(Extension)を利用できます。今回は、Pythonのプログラムを書くときに便利な拡張機能を導入します。

VSCodeの左側からExtensionボタンをクリックして、拡張機能タブを開きます。検索欄に「python」と入力します。出てきた結果から、Microsoft社が提供している「Python」拡張機能を選びます。

<img src="assets/VSCodeExtension.png">

Python拡張機能のページが開くので、「Install」ボタンをクリックして拡張機能をインストールします。

<img src="assets/VSCodeExtensionPython.png">

「Uninstall」ボタンが表示されるようになれば、インストール完了です。

<img src="assets/VSCodeExtensionPythonInstalled.png">
