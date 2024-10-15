# 五行相生相克 十神判断
# 甲乙丙丁戊己庚辛壬癸 木火土金水
listF = ["木", "火", "土", "金", "水"]
listT = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
# 十神名称列表
shishen = ["比肩", "劫财", "食神", "伤官", "偏财", "正财", "七杀", "正官", "偏印", "正印"]

def getIndexInListF(ele):
    if ele in listF:
        index = listF.index(ele)
        return index
    else:
        return -1

def getIndexInListT(ele):
    if ele in listT:
        index = listT.index(ele)
        return index
    else:
        return -1

def get_shishen_relation(rigan, biangan):
    # 通过计算索引差并取模来确定十神关系
    shishen_index = (biangan - rigan) % 10
    return f"{listT[rigan]}对于{listT[biangan]}的十神是：{shishen[shishen_index]}"

if __name__ == "__main__":
    # 输入两个五行/天干
    xing1 = input("请输入第一个五行/天干: ")
    xing2 = input("请输入第二个五行/天干: ")

    indexF1 = getIndexInListF(xing1)
    indexF2 = getIndexInListF(xing2)
    indexT1 = getIndexInListT(xing1)
    indexT2 = getIndexInListT(xing2)

    # 两个都是五行
    if indexF1 != -1 and indexF2 != -1:
        if indexF1 == indexF2:
            print(f"相同的五行：{indexF1}")
        elif indexF2 == (indexF1 + 1) % 5:
            print(f"{listF[indexF1]}生{listF[indexF2]}")
        elif indexF1 == (indexF2 + 1) % 5:
            print(f"{listF[indexF2]}生{listF[indexF1]}")
        elif indexF2 == (indexF1 + 2) % 5:
            print(f"{listF[indexF1]}克{listF[indexF2]}")
        elif indexF1 == (indexF2 + 2) % 5:
            print(f"{listF[indexF2]}克{listF[indexF1]}")
    # 两个都是天干
    elif indexT1 != -1 and indexT2 != -1:
        _r = get_shishen_relation(indexT1, indexT2)
        print(_r)
    # 无法识别
    else:
        print("天机不可泄露")
