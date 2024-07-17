import os
import warnings
import traceback
import pandas as pd

SKIP_SHEET = []#['画面処理定義書', '画面レイアウト', '画面項目定義書', 'チェック条件表（単項目）']

def list_files_in_directory(directory_path):
    try:
        # 指定したディレクトリのファイル名を取得
        files = os.listdir(directory_path)
        # フォルダ内のファイルのみを抽出（ディレクトリを除外）
        files = [f for f in files if os.path.isfile(os.path.join(directory_path, f))]
        return files
    except Exception as e:
        return str(e)

def check_file(file_path, table, in_col):
    try:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)

            # Excelファイルを読み込む
            xls = pd.ExcelFile(file_path, engine='openpyxl')
            
            found_positions = []
            
            # すべてのシートをループ
            for sheet_name in xls.sheet_names:
                if sheet_name in SKIP_SHEET:
                    continue

                df = pd.read_excel(xls, sheet_name=sheet_name)
                
                # 指定されたテキストを含むセルを検索
                result = df.map(lambda x: table in str(x))

                r_col = False
                r_num = 0
                if result.values.sum() > 0:
                    _text_list = []
                    result_col = df.map(lambda x: in_col in str(x))
                    if result_col.values.any():
                        r_col = True
                        r_num = result_col.values.sum()
                
                        # 検索結果がTrueのセルの原始テキストを取得
                        for row in range(result.shape[0]):
                            for col in range(result.shape[1]):
                                if result_col.iat[row, col]:
                                    _text_list.append(df.iat[row, col])
            
                    found_positions.append([file_path, sheet_name, r_col, (result.values.sum()),r_num, _text_list])
            return found_positions
    except Exception as e:
        print(file_path)
        traceback.print_exc()
        print(str(e))
        return []

# 使用例
# directory_path = r'C:\ning\doc\'
# directory_path = r'C:\ning\doc\'
directory_path = r'C:\ning\doc\'
# directory_path = r'C:\ning\doc\'

file_names = list_files_in_directory(directory_path)
# select_tble_num = '200'
select_col = '地域の町会・自治会へ'

# print('全角')

n=[]
for f in file_names:
    # ＴＢＬ ＴＢＲ
    # if '処理' not in f:
    #     continue
    n += check_file(directory_path+'\\'+f, '地域の町会・自治会へ', select_col)

for d in n:
    print(d)

# print('半角')

# n=[]
# for f in file_names:
#     if '編集' not in f:
#         continue
    
#     n += check_file(directory_path+'\\'+f, 'TBL'+select_tble_num, select_col)

# for d in n:
#     print(d)

# print(check_file(directory_path, 'TBL105', '受信希望区分'))
