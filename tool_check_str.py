import datetime
import csv
import pandas as pd

def read_file(file_path, out_filename):
    out_str = ""
    out_str2 = ""
    try:
        # ファイルを読み込み、行ごとにリストに格納
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 各行を表示
        for line in lines:
            # print(line.strip())
            if "レイアウト" in line :
                out_str += line
            elif "項目定義" in line:
                out_str2 += line

        with open(out_filename, 'a+', encoding="utf8") as f_output:
            f_output.write(out_str)
        with open(out_filename[:-4]+"_1.txt", 'a+', encoding="utf8") as f_output:
            f_output.write(out_str2)

    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")

# テスト用のファイルパス
file_path = r'C:\ning\dev\tool'
file_name = 'file_names.txt'
out_filename = file_name[:8]+datetime.datetime.now().strftime('%H%M%S')+".txt"

# 関数の呼び出し
read_file(f"{file_path}\\{file_name}", out_filename)
