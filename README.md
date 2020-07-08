# submitt-file-to-web-site
PythonでWebサイトへエクセルファイルを提出するスクリプトです

このスクリプトをwindows10のタスクスケジューラーに登録し，自動送信を実現しました．

用いたライブラリは以下の二つです．
- glob
- os
- datetime
- selenium
- time

この中でseleniumは，サードパーティー製ライブラリなので

pip install selenium

でインストールする必要があります．

また，実際に操作するブラウザである，Chromeドライバーをインストールが必要です．

https://chromedriver.storage.googleapis.com/index.html?path=83.0.4103.39/

上のサイトから

chromedriver_win32.zip

をダウンロードして，解凍してください．

その解凍先をスクリプト内で用います．

# タスクスケジューラーへのPythonスクリプトの登録方法
- ctrl + Rを押す
- 出てきたボックスに，Taskschd.msc，を入力する(タスクスケジューラーが起動される)
- フォルダをタスクスケジューラーライブラリに変える
- 基本タスクの生成
- 名前と説明をわかるように入力
- 次へ
- いつタスクを開始するか指定(毎日，毎週，毎週，1回限り，コンピューターの起動時，ログオン時，特定のイベントへのログの記録時)
- 次へ
- いつやるかを具体的に指定
- 次へ
- プログラムの開始
- 次へ
- プログラム/スクリプトの欄へ，python.exeを指定する
- 引数の追加の欄へ，pythonスクリプトのファイル名を指定する
- 開始(オプション)の欄へ，pythonスクリプトのある場所(パス)を指定する
- 次へ
- 完了

参考サイト

https://rdk.me/anaconda/

https://tonari-it.com/windows-task-schdeuler/
