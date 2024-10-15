# 导入所需的库
import datetime
import os
from lunarcalendar import Converter, Solar

# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 卦象文件所在目录
filename = 'guaName64.txt'

# 定义八卦字典，每个卦象用3个爻表示，0为阴，1为阳
gua_dict = {
    "乾": [1, 1, 1],  # ☰ 三阳爻
    "坤": [0, 0, 0],  # ☷ 六阴爻
    "离": [1, 0, 1],  # ☲ 中虚
    "坎": [0, 1, 0],  # ☵ 中满
    "震": [0, 0, 1],  # ☳ 仰盂
    "艮": [1, 0, 0],  # ☶ 覆碗
    "兑": [0, 1, 1],  # ☱ 上缺
    "巽": [1, 1, 0],  # ☴ 下断
}
list_gua = ['坤', '震', '坎', '兑', '艮', '离', '巽', '乾']

def binary_to_decimal(binary_list):
    # Convert the binary list to a string
    binary_str = ''.join(map(str, binary_list))
    # Convert the binary string to a decimal integer
    decimal_value = int(binary_str, 2)
    return decimal_value

# 输入年份、月份、日期和时辰
def get_gua(year, month, day, hour):
    # 计算上卦（年、月、日之和 % 8）
    upper_trigram = (year + month + day - 1) % 8

    # 计算下卦（年、月、日、时之和 % 8）
    lower_trigram = (year + month + day + hour - 1) % 8

    # 上下卦的组合
    trigrams = ["乾", "兑", "离", "震", "巽", "坎", "艮", "坤"]

    # 输出卦象
    upper_gua = trigrams[upper_trigram]
    lower_gua = trigrams[lower_trigram]

    return upper_gua, lower_gua

# 将阳历日期转换为阴历
def solar_to_lunar(year, month, day):
    solar = Solar(year, month, day)  # 创建阳历对象
    lunar = Converter.Solar2Lunar(solar)
    return lunar.year, lunar.month, lunar.day

# 计算动爻
def calculate_dongyao(year, month, day, hour):
    # 计算年份、月份、日期、时辰之和
    total_sum = year + month + day + hour
    
    # 除以6，取余数，得到动爻
    dongyao = total_sum % 6
    
    return dongyao

# 根据给定的爻阵判断卦名
def get_gua_name(gua_combination):
    for gua, combination in gua_dict.items():
        if combination == gua_combination:
            return gua
    return "未找到匹配的卦象"

# 计算变卦
def get_change_gua(upper_gua, lower_gua, moving_yao):
    # 获取上卦和下卦的数值
    upper_gua_values = gua_dict[upper_gua]
    lower_gua_values = gua_dict[lower_gua]

    # 动爻改变的爻，具体根据动爻的数值来确定
    if moving_yao == 1:  # 下卦第3爻
        lower_gua_values[2] = 1 - lower_gua_values[2]
    elif moving_yao == 2:  # 下卦第2爻
        lower_gua_values[1] = 1 - lower_gua_values[1]
    elif moving_yao == 3:  # 下卦第1爻
        lower_gua_values[0] = 1 - lower_gua_values[0]
    elif moving_yao == 4:  # 上卦第3爻
        upper_gua_values[2] = 1 - upper_gua_values[2]
    elif moving_yao == 5:  # 上卦第2爻
        upper_gua_values[1] = 1 - upper_gua_values[1]
    elif moving_yao == 6:  # 上卦第1爻
        upper_gua_values[0] = 1 - upper_gua_values[0]


    # 返回变卦
    return get_gua_name(upper_gua_values), get_gua_name(lower_gua_values)

def find_line_in_file(filename, upper_gua, lower_gua):
    """
    在指定的文件中查找包含特定文字的行，并返回该行内容及行号。
    
    :param filename: 文件名
    :param search_text: 要查找的文字
    :return: 包含指定文字的行及行号
    """
    filename = os.path.join(script_dir, filename)
    search_text = f'上{upper_gua}下{lower_gua}'  # 假设我们要查找的文字
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        for index, line in enumerate(lines, start=1):
            if search_text in line:
                next_line = lines[index + 1] if index + 1 < len(lines) else None
                return index, line.strip(), next_line  # 返回行号和内容
    return None, None, None  # 如果没找到

# 测试：2024年10月15日，9点（巳时）
dt = datetime.datetime.now()
year = dt.year
month = dt.month
day = dt.day
hour = dt.hour
print(f"阳历日期：{year}年 {month}月 {day}日 {hour}时")

# 转换为阴历
lunar_year, lunar_month, lunar_day = solar_to_lunar(year, month, day)
print(f"阴历日期：{lunar_year}年 {lunar_month}月 {lunar_day}日 {hour}时")

# 计算卦象
upper_gua, lower_gua = get_gua(lunar_year, lunar_month, lunar_day, hour)

# 打印卦象
print(f"上卦: {upper_gua}, 下卦: {lower_gua}")
line_num, line_content, next_line = find_line_in_file(filename, upper_gua, lower_gua)
if line_num:
    print(f'No {line_num}, 内容: {line_content}')
    if next_line:
        print(next_line)
else:
    print("天机不可泄露， 找不到该卦象")

# 计算动爻
dongyao = calculate_dongyao(lunar_year, lunar_month, lunar_day, hour)

# 输出动爻数值
print(f"动爻数值：{dongyao}")

# 计算变卦
change_gua = get_change_gua(upper_gua, lower_gua, dongyao)
print(f"变卦为：上卦:{change_gua[0]} 下卦:{change_gua[1]}")

line_num, line_content, next_line = find_line_in_file(filename, change_gua[0], change_gua[1])
if line_num:
    print(f'No {line_num}, 内容: {line_content}')
    if next_line:
        print(next_line)
else:
    print("天机不可泄露， 找不到该卦象")
