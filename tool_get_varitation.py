import datetime
import csv
import pandas as pd

def read_file(file_path, out_filename, formname):
    data_dict = {}
    try:
        # 读取Excel文件
        excel_file = pd.ExcelFile(file_path)

        # 读取第一个工作表的数据
        sheet_data = pd.read_excel(excel_file, sheet_name='チェック条件表（単項目）', header=None)

        # print("Sheet Data:")
        # print(sheet_data)

        for index, row in sheet_data.iterrows():
            if index > 2 and pd.notnull(row[0]) and pd.notnull(row[2]):
                key = row[2]
                value = row[1:]
                data_dict[key] = value

        print(data_dict)
        print(out_filename)

        with open(out_filename, 'a+', encoding="utf8") as f_output:
            _line = f"""\t$("{formname}").validationEngine('attach',{{
		// 以下のパラメータは任意
		promptPosition: "bottomLeft",//エラー文の表示位置
		showArrowOnRadioAndCheckbox: true,//エラー箇所の図示
		focusFirstField: true,//エラー時に一番文頭の入力フィールドにフォーカスさせるかどうか
		maxErrorsPerField: 1,
		scroll: false,
		'custom_error_messages': {{"""
            f_output.write(_line)
            for k, v in data_dict.items():
                line = f"\n\t\t\t#'{k}': {{"
                # 必須
                if v.loc[3] == '○':
                    line += f"""\n\t\t\t\t'required': {{
					'message': getMessage(ERROR_CODE.E0002, ['{v.loc[16]}'])
				}},"""
                
                # 半角数字
                if v.loc[4] == '○':
                    line += f"""\n\t\t\t\t'custom[halfwidthNumbers]' : {{
					'message': getMessage(ERROR_CODE.E0003, ['{v.loc[16]}'])
				}},"""

                # 半角英数字+全角文字+全角カタカナ
                if v.loc[6] == '○' and v.loc[7] == '○' and v.loc[8] == '○':
                    line += f"""\n\t\t\t\t'custom2[prohibitionCharacter]' : {{
					'message': getMessage(ERROR_CODE.E0015, ['{v.loc[16]}'])
				}},"""
                # 半角英数字
                elif v.loc[6] == '○':
                    line += f"""\n\t\t\t\t'custom[halfwidthAlphanumeric]' : {{
					'message': getMessage(ERROR_CODE.E0005, ['{v.loc[16]}'])
				}},"""
                # 全角文字
                elif v.loc[7] == '○':
                    line += f"""\n\t\t\t\t'custom[fullwidthCharacters]' : {{
					'message': getMessage(ERROR_CODE.E0006, ['{v.loc[16]}'])
				}},"""
                # 全角カタカナ
                elif v.loc[8] == '○':
                    line += f"""\n\t\t\t\t'custom[kana]' : {{
					'message': getMessage(ERROR_CODE.E0007, ['{v.loc[16]}'])
				}},"""

                # 日付
                if v.loc[9] == '○':
                    line += f"""\n\t\t\t\t'custom[date]' : {{
	        		'message': getMessage(ERROR_CODE.E0008, ['{v.loc[16]}'])
	        	}}"""


                # 桁数関連
                if pd.notnull(v.loc[13]):
                    if pd.notnull(v.loc[14]):
                        # 指定桁数
                        if v.loc[13] == v.loc[14]:
                            line += f"""\n\t\t\t\t'minSize' : {{
					'message': getMessage(ERROR_CODE.E0017, ['{v.loc[16]}', '{v.loc[13]}'])
				}},"""
                            line += f"""\n\t\t\t\t'maxSize' : {{
					'message': getMessage(ERROR_CODE.E0017, ['{v.loc[16]}', '{v.loc[14]}'])
				}},"""
                        # 最小桁数&最大桁数
                        else:
                            line += f"""\n\t\t\t\t'minSize' : {{\n\t\t\t\t\t'message': getMessage(ERROR_CODE.E0013, ['{v.loc[16]}', '{v.loc[13]}'])
				}},"""
                            line += f"""\n\t\t\t\t'maxSize' : {{\n\t\t\t\t\t'message': getMessage(ERROR_CODE.E0012, ['{v.loc[16]}', '{v.loc[14]}'])
				}},"""
                    # 最小桁数のみ
                    else:
                        line += f"""\n\t\t\t\t'minSize' : {{\n\t\t\t\t\t'message': getMessage(ERROR_CODE.E0013, ['{v.loc[16]}', '{v.loc[13]}'])
				}},"""
                # 最大桁数のみ
                elif pd.notnull(v.loc[14]):
                    line += f"""\n\t\t\t\t'maxSize' : {{
					'message': getMessage(ERROR_CODE.E0012, ['{v.loc[16]}', '{v.loc[14]}'])
				}},"""
  

                line += "\n\t\t\t},"
                f_output.write(line)
            _line = f"""\n\t\t}},
		onValidationComplete: function(form, status){{
			return status;
		}}\n\t}});"""
            f_output.write(_line)
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")

# テスト用のファイルパス
file_path = r'C:\ning\doc'
file_name = '.xlsx'
out_filename = file_name[:8]+datetime.datetime.now().strftime('%H%M%S')+".txt"
formname = ".a-form"

# 関数の呼び出し
read_file(f"{file_path}\\{file_name}", out_filename, formname)
