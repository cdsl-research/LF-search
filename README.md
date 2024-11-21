# LF-search
ログファイルを探すソフトウェア

## 主な機能の概要
### main.py
- プログラムのエントリーポイント
- コマンドライン引数の検証
- 全体の実行フロー制御

### file_processor.py
- ファイルの読み込みと処理
- パスの検証とフィルタリング
- ログファイル検出の実行

### entropy.py
- エントロピー計算のコア機能
- ファイルのバイナリデータ解析
- チャンク単位のエントロピー計算

### utils.py
- タイムアウト処理
- 非ログファイル拡張子の定義と判定
- ユーティリティ関数

## 実行方法
プログラムを実行する際に，調査するディレクトリの指定をしてください．
また，ルートユーザーで実行するようにしてください．
```
# python3 main.py /var/log
```

## 実行結果
実行すると検出したログファイルのファイルパスが表示されます．
```
スキャン開始: /var/log

処理対象: 81ファイル
除外: 拡張子フィルタ 21件, 空/リンク 12件

検出したログファイル（19件）：
/var/log/lastlog
/var/log/wtmp
/var/log/sysstat/sa20
/var/log/sysstat/sa19
/var/log/sysstat/sa17
/var/log/sysstat/sa18
/var/log/sysstat/sa13
/var/log/sysstat/sa14
/var/log/sysstat/sa15
/var/log/sysstat/sa16
/var/log/sysstat/sa21
/var/log/journal/93414f62599b4f97abca6fe97ffc40ff/system.journal
/var/log/journal/93414f62599b4f97abca6fe97ffc40ff/user-1000@6d93242b09d34fae827dbdfb79d215cb-0000000000000e1a-0006262f2d627a16.journal
/var/log/journal/93414f62599b4f97abca6fe97ffc40ff/system@6d93242b09d34fae827dbdfb79d215cb-00000000000003b3-0006262f2ade0058.journal
/var/log/journal/93414f62599b4f97abca6fe97ffc40ff/system@88455b2d345f41279d4a5aae22341862-00000000000039d7-000626c0008d3e74.journal
/var/log/journal/93414f62599b4f97abca6fe97ffc40ff/system@241e7cd7e6bd486eac0feaf3f021923d-000000000000470c-000626d5328b6ef7.journal
/var/log/journal/93414f62599b4f97abca6fe97ffc40ff/user-1000.journal
/var/log/journal/93414f62599b4f97abca6fe97ffc40ff/system@880d4c50dccd48b58a998dcca920375b-0000000000002ec9-000626b8cfe24c29.journal
/var/log/journal/93414f62599b4f97abca6fe97ffc40ff/system@40538de0e34344c1a47585a33f45292b-0000000000005347-000626dcdad0b204.journal

処理時間: 5.8秒
```
