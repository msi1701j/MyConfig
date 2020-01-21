# MyConfig - custom\_config

See the description in English below.

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
|CUSTOM\_CONFIG\_DIR|カレントディレクトリ|`default` および `local` ディレクトリを検索するディレクトリ| ${HOME}/mydir|
|CUSTOM\_CONFIG\_FILE|`custom_config.conf`|設定ファイルの名前。|myconfig.conf|


## Test

### 準備

```
eval `./setup_MyConfigEnv.sh`
```

あるいは

```
eval $(./setup_MyConfigEnv.sh)
```


### テスト実施

```
python -m unittest discover tests
```

## ディレクトリ/ファイル構成

```
./
├─ README.md ........................... このファイル
├─ custom_config/ ...................... custom_config モジュールディレクトリ
│    ├─ __init__.py ................... custom_config モジュール __init__.py
│    ├─ __main__.py ................... custom_config モジュール __main__.py
│    └─ _custom_config.py ............. custom_config モジュール本体
├─ default/ ............................ default 設定ディレクトリ
│    ├─ custom_config.conf ............ 設定ファイル名省略時の default 設定ファイル
│    └─ sample.conf ................... サンプル設定ファイル
├─ local/ .............................. local 設定ディレクトリ
│    ├─ custom_config.conf ............ 設定ファイル名省略時の local 設定ファイル
│    └─ sample.conf ................... サンプル設定ファイル
├─ setup_MyConfigEnv.sh ................ テスト用環境変数設定ファイル
└─ tests/ .............................. テストディレクトリ
      └─ unit/ ......................... Unit テスト用ディレクトリ
            ├─ __init__.py ............. ディレクトリマーカー
            └─ test_custom_config.py ... テストファイル
```

---
**English description**

# MyConfig - custom\_config

## Usage

Search the `default` and `local` directories in the specified directory and read the configuration file (INI format).

* `default` configuration is fixed, `local` configuration is as you like.
* Parameters that are set to default and set to local are replaced with the value of local.
* Parameters that are set to default but not set to local retain their default values.
* The name of the default/configuration file and the name of the local/configuration file must be the same.

Currently it only reads the `[defaults]` section.


```
from custom_config import Config

config = Config ()

config = Config (config_file = "myconfig.conf")

config = Config (default_config = {"test1": "arg test1 message"})
```

### Environment variable

| Environment variable | Default value when not set | Use | Example |
|:-|:-|:-|:-|
| MY_MODULE_PATH | Current directory | Directory where library is loaded is located | ${HOME}/lib |
| CUSTOM\_CONFIG\_DIR | Current directory | Directory to search `default` and `local` directory | $ {HOME} / mydir |
| CUSTOM\_CONFIG\_FILE | `custom_config.conf` | Name of the configuration file. | myconfig.conf |


## Test

### Preparation

```
eval `./setup_MyConfigEnv.sh`
```

or

```
eval $(./setup_MyConfigEnv.sh)
```


### Test execution

```
python -m unittest discover tests
```

## Directory / File structure

```
./
|-README.md ................... This file
|-custom_config ............... custom_config module directory
| |-__init__.py ............... custom_config module __init__.py
| |-__main__.py ............... custom_config module __main__.py
| `-_custom_config.py ......... The custom_config module body
|-default ..................... default configuration directory
| |-custom_config.conf ........ Default configuration file when the configuration file name is omitted
| `-sample.conf ............... Sample configuration file
|-local ....................... local configuration directory
| |-custom_config.conf ........ Local configuration file when the configuration file name is omitted
| `-sample.conf ............... Sample configuration file
|-setup_MyConfigEnv.sh ........ Environment variable setting file for test
`-tests ....................... Test directory
    `-test_custom_config.py ... test file
```
