# MyConfig - custom\_config

## 用法

指定したディレクトリの `default` と `local` ディレクトリを検索して、設定ファイル(INI形式)を読み込む。

* default は、固定設定、local は、固有設定。
* default に設定されていて、local に設定されているパラメータは、local の値で置き換わります。
* default に設定されていて、local に設定されていないパラメータは、default の値のままです。
* default/ 設定ファイル名と local/ 設定ファイル名は同じである必要があります。

現在は、`[defaults]` セクションのみ読み込みます。


```
from custom_config import Config

config = Config()

config = Config( config_file="myconfig.conf" )

config = Config( default_config={ "test1": "arg test1 message" } )
```

### 環境変数

|環境変数|未設定時のデフォルト値|用途|用例|
|:--|:--|:--|:--|
|MY_MODULE_PATH|カレントディレクトリ|ライブラリを読み込むディレクトリの存在するディレクトリ| ${HOME}/lib |
|CUSTOM\_CONFIG\_DIR|カレントディレクトリ|default/local ディレクトリを検索するディレクトリ| ${HOME}/mydir|
|CUSTOM\_CONFIG\_FILE|`custom_config.conf`|設定ファイルの名前。|myconfig.conf|


## Test

### 準備

```
eval `setup_MyConfigEnv.sh`
```

### テスト実施

```
python -m unittest discover tests
```

## ディレクトリ/ファイル構成

```
./
|-- README.md ……………………… このファイル
|-- custom_config ………………… custom_config モジュールディレクトリ
|   |-- __init__.py ……………… custom_config モジュール __init__.py
|   |-- __main__.py ……………… custom_config モジュール __main__.py
|   `-- _custom_config.py ……… custom_config モジュール本体
|-- default ………………………… default 設定ディレクトリ
|   |-- custom_config.conf  …… 設定ファイル名省略時の default 設定ファイル
|   `-- sample.conf ……………… サンプル設定ファイル
|-- local …………………………… local 設定ディレクトリ
|   |-- custom_config.conf  …… 設定ファイル名省略時の local 設定ファイル
|   `-- sample.conf ……………… サンプル設定ファイル
|-- setup_MyConfigEnv.sh  ……… テスト用環境変数設定ファイル
`-- tests …………………………… テストディレクトリ
    `-- test_custom_config.py … テストファイル
```
