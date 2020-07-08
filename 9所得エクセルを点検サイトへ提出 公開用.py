# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:40:33 2020

実行した日と同じexcelファイルを提出するスクリプト

"""

# エクセルファイル名所得用モジュールインポート部分
import glob
import os
from datetime import datetime
# エクセルファイル提出用モジュールインポート部分
from selenium import webdriver
import time


# エクセルファイルの親パスを変数に宣言しとく
excel_path = '提出したいexcelファイルのディレクトリ名'

# ChromeDriverのフルパスを変数に宣言しとく
ChromeDriver_path = 'ChromeDriverのフルパス'

# ログインIDとパスワードを先に変数で宣言しとく
ID = 'サイトへのログインID'
password_var = 'サイトへのログインパスワード'

# 今日の年月日を年．月．日の形式で所得できるようにする
now_date = datetime.now().strftime("%y.%m.%d")

# glob関数を使って親パスの中のエクセルファイルのフルパスすべてを変数に代入する
excel_filename_fulls = glob.glob(excel_path + '*xlsx')

# 変数はフルパスのリストになっているのでforで取り出して拡張子を除いたファイル名にする
for excel_filename_full in excel_filename_fulls:
    # splitext関数を使ってフルパスを拡張子を除いたファイル名に変換して変数に代入する
    excel_filename = os.path.splitext(os.path.basename(excel_filename_full))[0]
    # 変数に代入したやつをコンソール上に表示する
    print(excel_filename, end=' ')
    # print(type(excel_filename))
    # 条件分岐で今日の年月日と上で直接変数に代入されてる年月日を比較する
    # 日付が一致した時 エクセルファイルを自主点検のほうにコピーする
    if excel_filename == now_date:
        print("日付が一致しました")
        # 点検担当のサイトにログインする
        # ブラウザを開く。
        driver = webdriver.Chrome(executable_path=ChromeDriver_path)
        # 点検担当のサイトを開く
        driver.get("提出したいサイトのURL")
        # 3秒待機
        time.sleep(5)
        # ログインIDを入力
        login_id = driver.find_element_by_name("username")
        login_id.send_keys(ID)
        # 2秒待機
        time.sleep(2)
        # パスワードを入力
        password = driver.find_element_by_name("password")
        password.send_keys(password_var)
        # 2秒待機
        time.sleep(2)
        # ログインボタンをクリックする
        login_btn = driver.find_element_by_xpath('//*[@id="login"]/form/input[4]')
        login_btn.click()
        # 10秒待機
        time.sleep(5)

        # ログインした点検担当のサイト上でエクセルファイルを提出する
        # ファイル選択テキストボックスを指定するオブジェクトを生成する
        file_select = driver.find_element_by_name('upfile')
        # オブジェクトのsecd_keysを使って提出するエクセルファイルのフルパスを入力する
        file_select.send_keys(excel_filename_full)
        # ファイル提出の送信ボタンを押す
        file_upload = driver.find_element_by_xpath('//*[@id="upload"]/form/input[3]')
        file_upload.click()
        # エクセルファイルをちゃんと提出したことがわかるようにわざとchromeは終了させない

    # 日付が一致しない時 falseをコンソール上に表示
    else:
        print("false")
