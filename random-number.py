import collections
import copy
import sys
import random
import collections
import pandas as pd
import scipy.stats as ss
from scipy.stats import chi2_contingency


#標準的なゲームプレイヤにとって自然に見える疑似乱数列の生成法 (配列数50)
def evel_ary(ary):
    #全配列
    count_all = collections.Counter(ary)
    #  print(count_all)
    list_count_all = make_count_list(count_all)

    #1~15番目の配列
    ary_1_15 = ary[0:16]
    #print(ary_1_15)
    count_1_15 = collections.Counter(ary_1_15)
    #print(count_1_15)
    list_count_1_15 = make_count_list(count_1_15)

    #13~27番目の配列
    ary_13_27 = ary[12:28]
    #print(ary_13_27)
    count_13_27 = collections.Counter(ary_13_27)
    #print(count_13_27)
    list_count_13_27 = make_count_list(count_13_27)

    #25~39
    ary_25_39 = ary[24:40]
    #print(ary_25_39)
    count_25_39 = collections.Counter(ary_25_39)
    #print(count_25_39)
    list_count_25_39 = make_count_list(count_25_39)

    #36~50番目の配列
    ary_35_50 = ary[35:51]
    #print(ary_35_50)
    count_35_50 = collections.Counter(ary_35_50)
    #print(count_35_50)
    list_count_35_50 = make_count_list(count_35_50)

    #F1　特徴量1の計算 (F2以降も同様に特徴量を計算している）
    f1_value = make_chi2(list_count_all)

    #F2
    f2_value = make_chi2(list_count_1_15)

    #F3
    f3_value = make_chi2(list_count_13_27)

    #F4
    f4_value = make_chi2(list_count_25_39)

    #F5
    f5_value= make_chi2(list_count_35_50)

    #F6
    f6_temp = -1
    f6_counter = 0
    for i in ary:
        #print(i)
        if f6_temp == -1:
            #print("f6_temp_before" +str(f6_temp))
            f6_temp = i
            #print("f6_temp_after" +str(f6_temp))
            continue
        elif f6_temp % 2 == i % 2:
            f6_counter = f6_counter + 1

        f6_temp = i
    #print(f6_counter)
    f6_value = f6_counter

    #F7
    f7_temp = -1
    f7_counter = 0
    for i in ary:
        #print(i)
        if f7_temp == -1:
            #print("f7_temp_before" +str(f7_temp))
            f7_temp = i
            #print("f7_temp_after" +str(f7_temp))
            continue
        elif f7_temp == i:
            f7_counter = f7_counter + 1

        f7_temp = i

    #print(f7_counter)
    f7_value = f7_counter

    #F8
    f8_counter = 0
    for i in range(0,len(ary)-2):
        if ary[i] == ary[i+1] == ary[i+2]:
            f8_counter = f8_counter + 1

    #print(f8_counter)
    f8_value = f8_counter

    #F9
    f9_counter = 0
    for i in range(0,len(ary)-3):
        if ary[i] == ary[i+1] == ary[i+2] ==ary[i+3]:
            f9_counter = f9_counter + 1

    #print(f9_counter)
    f9_value = f9_counter

    #F10
    f10_counter = 0
    for i in range(0,len(ary)-3):
        local_ary = [ary[i],ary[i+1],ary[i+2],ary[i+3]]
        #print(local_ary)
        local_counter = collections.Counter(local_ary)
        local_vals ,local_counts = zip(*local_counter.most_common())
        if list(local_counts) == [2,2]:
            f10_counter = f10_counter + 1
            #print("OK")

    #print(f10_counter)
    f10_value = f10_counter

    #F11
    f11_counter = 0
    for i in range(0,len(ary)-4):
        local_ary = [ary[i],ary[i+1],ary[i+2],ary[i+3],ary[i+4]]
       # print(local_ary)
        local_counter = collections.Counter(local_ary)
        local_vals ,local_counts = zip(*local_counter.most_common())
        if list(local_counts) == [3,2]:
            f11_counter = f11_counter + 1
            #print("OK")

    #print(f11_counter)
    f11_value = f11_counter

    #F12
    f12_counter = 0
    for i in range(0,len(ary)-3):
        local_ary = [ary[i],ary[i+1],ary[i+2],ary[i+3]]
        #print(local_ary)
        local_counter = collections.Counter(local_ary)
        local_vals ,local_counts = zip(*local_counter.most_common())
        if list(local_counts) == [3,1]:
            f12_counter = f12_counter + 1
            #print("OK")

    #print(f12_counter)
    f12_value = f12_counter

    #F13
    #print("--F13--")
    f13_counter = 0
    for i in range(0,len(ary)-4):
        local_ary = [ary[i],ary[i+1],ary[i+2],ary[i+3],ary[i+4]]
        #print(local_ary)
        local_counter = collections.Counter(local_ary)
        local_vals ,local_counts = zip(*local_counter.most_common())
        if list(local_counts) == [3,2] or list(local_counts) == [3,1,1]:
            f13_counter = f13_counter + 1
           # print("OK")

    #print(f13_counter)
    f13_value = f13_counter

    #F14
    #print("--F14--")
    f14_counter = 0
    for i in range(0,len(ary)-5):
        local_ary = [ary[i],ary[i+1],ary[i+2],ary[i+3],ary[i+4],ary[i+5]]
        #print(local_ary)
        local_counter = collections.Counter(local_ary)
        local_vals ,local_counts = zip(*local_counter.most_common())
        if list(local_counts) == [4,2] or list(local_counts) == [4,1,1]:
            f14_counter = f14_counter + 1
            #print("OK")

    #print(f14_counter)
    f14_value = f14_counter

    #F15
    #print("--F15--")
    f15_counter = 0
    for i in range(0,len(ary)-6):
        local_ary = [ary[i],ary[i+1],ary[i+2],ary[i+3],ary[i+4],ary[i+5],ary[i+6]]
        #print(local_ary)
        local_counter = collections.Counter(local_ary)
        local_vals ,local_counts = zip(*local_counter.most_common())
        if list(local_counts) == [4,3] or list(local_counts) == [4,2,1] or list(local_counts) == [4,1,1,1]:
            f15_counter = f15_counter + 1
            #print("OK")

    #print(f15_counter)
    f15_value = f15_counter

    f_list = [f1_value,f2_value,f3_value,f4_value,f5_value,f6_value,f7_value,f8_value,f9_value,f10_value,f11_value,f12_value,f13_value,f14_value,f15_value]

    err_value = cal_err(f_list)

    return err_value

def cal_err(f_list):
    #最終的なErr値の代入先
    err_value = 0

    #F1 特徴量1の計算 (F2以降も同様）
    f1_err = 0
    if f_list[0] < 2: #下限
        f1_err = 2 - f_list[0]
    elif 5 < f_list[0]: #上限
        f1_err = f_list[0] - 5
    f1_err = f1_err * 3 # 重みγ

    #F2
    f2_err = 0
    if f_list[1] < 2: #下限
        f2_err = 2 - f_list[1]
    elif 5 < f_list[1]: #上限
        f2_err = f_list[1] - 5
    f2_err = f2_err * 3 # 重みγ

    #F3
    f3_err = 0
    if f_list[2] < 2: #下限
        f3_err = 2 - f_list[2]
    elif 5 < f_list[2]: #上限
        f3_err = f_list[2] - 5
    f3_err = f3_err * 3 # 重みγ

    #F4
    f4_err = 0
    if f_list[3] < 2: #下限
        f4_err = 2 - f_list[3]
    elif 5 < f_list[3]: #上限
        f4_err = f_list[3] - 5
    f4_err = f4_err * 3 # 重みγ

    #F5
    f5_err = 0
    if f_list[4] < 2: #下限
        f5_err = 2 - f_list[4]
    elif 5 < f_list[4]: #上限
        f5_err = f_list[4] - 5
    f5_err = f5_err * 3 # 重みγ

    #F6
    f6_err = 0
    if f_list[5] < 27: #下限
        f6_err = 27 - f_list[5]
    elif 30 < f_list[5]: #上限
        f6_err = f_list[5] - 30
    f6_err = f6_err * 1 # 重みγ

    #F7
    f7_err = 0
    if f_list[6] < 5: #下限
        f7_err = 5 - f_list[6]
    elif 8 < f_list[6]: #上限
        f7_err = f_list[6] - 8
    f7_err = f7_err * 1 # 重みγ

    #F8
    f8_err = 0
    if f_list[7] < 0: #下限
        f8_err = 0 - f_list[7]
    elif 1 < f_list[7]: #上限
        f8_err = f_list[7] - 1
    f8_err = f8_err * 3 # 重みγ

    #F9
    f9_err = 0
    if f_list[8] < 0: #下限
        f9_err = 0 - f_list[8]
    elif 0 < f_list[8]: #上限
        f9_err = f_list[8] - 0
    f9_err = f9_err * 10 # 重みγ

    #F10
    f10_err = 0
    if f_list[9] < 1: #下限
        f10_err = 1 - f_list[9]
    elif 3 < f_list[9]: #上限
        f10_err = f_list[9] - 3
    f10_err = f10_err * 4 # 重みγ

    #F11
    f11_err = 0
    if f_list[10] < 0: #下限
        f11_err = 0 - f_list[10]
    elif 0 < f_list[10]: #上限
        f11_err = f_list[10] - 0
    f11_err = f11_err * 4 # 重みγ

    #F12
    f12_err = 0
    if f_list[11] < 0: #下限
        f12_err = 0 - f_list[11]
    elif 1 < f_list[11]: #上限
        f12_err = f_list[11] - 1
    f12_err = f12_err * 4 # 重みγ

    #F13
    f13_err = 0
    if f_list[12] < 1: #下限
        f13_err = 1 - f_list[12]
    elif 2 < f_list[12]: #上限
        f13_err = f_list[12] - 2
    f13_err = f13_err * 4 # 重みγ

    #F14
    f14_err = 0
    if f_list[13] < 0: #下限
        f14_err = 0 - f_list[13]
    elif 0 < f_list[13]: #上限
        f14_err = f_list[13] - 0
    f14_err = f14_err * 4 # 重みγ

    #F15
    f15_err = 0
    if f_list[14] < 0: #下限
        f15_err = 0 - f_list[14]
    elif 0 < f_list[14]: #上限
        f15_err = f_list[14] - 0
    f15_err = f15_err * 4 # 重みγ

    err_value = f1_err+f2_err+f3_err+f4_err+f5_err+f6_err+f7_err+f8_err+f9_err+f10_err+f11_err+f12_err+f13_err+f14_err+f15_err
    #print(err_value)

    return err_value

def make_count_list(counter):
    """
    配列の1~6の要素数を数え、それをlistとして返す
    :param counter: collections.Counter
    :return:
    """
    list_count = []
    for i in range(1, 7):
        count = counter[i]
        #print(count)
        list_count.append(count)
    #print(list_count)
    return list_count


def make_chi2(list_count_all):
    """
    1D6を振った際のΧ^2値を返す
    :param list_count_all:
    :return:
    """

    chi2 , p = ss.chisquare(list_count_all) #chisquareで簡単に

    return chi2

def no_adjusted_random_int(seed, num_start, num_stop, num):
    """
    random.randint()で乱数配列を返す
　　　　　　
    :param seed: seed値
    :param num_start:
    :param num_stop:
    :param num:
    :return:
    """
    random.seed(seed)  # seed値の固定
    num_array = []
    for i in range(0, num):
        num_array.append(random.randint(num_start, num_stop))
    return num_array


def adjusted_random_int(seed, num_start, num_stop,num):
    """
    random.randint()で乱数配列を返す
    ただし調整を加える

    :param seed: seed値
    :param num_start:
    :param num_stop:
    :param num:
    :return:
    """
    random.seed(seed)  # seed値の固定
    num_array = []
    for i in range(0, num):
        num_array.append(random.randint(num_start, num_stop))

    err_val = evel_ary(num_array)
    for i in range(0,1000):

        #乱数で変更するindexとその値を決める
        index = random.randint(0,len(num_array)-1)
        change_val = random.randint(num_start, num_stop)

        #deepcopyで参照関係を持たないように
        num_array_deepcopy = copy.deepcopy(num_array)
        #値を1つ入れ替える
        num_array_deepcopy[index] = change_val

        #新しい乱数列の評価
        change_err_val = evel_ary(num_array_deepcopy)
        #print("err_val: " +str(err_val))
        #print("change_err_val: " +str(change_err_val))

        #Err値の比較
        if change_err_val < err_val:
            num_array = num_array_deepcopy
            err_val = change_err_val

        if err_val == 0:
            break

    return num_array


def worst_seed(num_start, num_stop, num):
    """
    関数evel_aryが最も悪くでるseed値を求める

    :param num_start: 乱数列の最小値
    :param num_stop: 乱数列の最大値
    :param num: 乱数列の数
    :return: 最も悪いevel_aryとなった時のseed
    """
    cal_seed = -1
    cal_evel = -1
    for i in range(0,100000):#64580
        no_adjusted_int_ary = no_adjusted_random_int(i,num_start, num_stop, num)
        temp_evel = evel_ary(no_adjusted_int_ary)

        if cal_evel < temp_evel:
            cal_seed = i
            cal_evel = temp_evel

    print(cal_seed)
    return cal_seed

def average_evel(num_start, num_stop, num):
    """
    複数生成したno_adjusted_random_intをevel_aryに渡して帰ってくる値の平均を計算して返す

    :param num_start: 乱数列の最小値
    :param num_stop: 乱数列の最大値
    :param num: 乱数列の数
    :return: 乱数列の平均値
    """
    ave_evel = 0
    count = 0

    for i in range(0,100000):
        no_adjusted_int_ary = no_adjusted_random_int(i,num_start, num_stop, num)
        temp_evel = evel_ary(no_adjusted_int_ary)
        ave_evel = ave_evel + temp_evel
        count = count + 1
    ave_evel = ave_evel / count
    print(str(count)+":average: " + str(ave_evel))

if __name__ == "__main__":
    """
    　このコードの反省点
    　・配列で実装したほうが、コード行数の大幅削減につながる部分があるにもかかわらず単一の値で実装したこと：def cal_err や　evel_ary　など
    　・print文デバック
    　・マジックナンバー多数
    　・コメントが少ない。
    """

    # seed値と乱数配列の固定
    seed = 64580
    #seed 1021 連続した値が多い
    num = 50
    num_start = 1
    num_stop = 6

    no_adjusted_int_ary = no_adjusted_random_int(seed,num_start, num_stop, num)
    adjusted_int_ary = adjusted_random_int(seed,num_start, num_stop, num)

    teuchi = [1 ,5 ,4 ,3 ,2 ,2 ,6 ,1 ,5 ,5 ,4 ,2 ,3 ,1 ,3 ,6 ,2 ,5 ,4 ,2 ,1 ,3 ,2 ,5 ,4 ,6 ,1 ,1 ,3 ,1 ,4 ,6 ,5 ,5 ,5 ,2 ,3 ,1 ,1 ,2 ,4 ,3 ,6 ,1 ,5 ,5 ,1 ,3 ,5 ,2]

    print("no_adjusted: " + str(no_adjusted_int_ary) +" evel: " + str(evel_ary(no_adjusted_int_ary)))
    print("   adjusted: " + str(adjusted_int_ary) + " evel: " + str(evel_ary(adjusted_int_ary)))
    print("     teuchi: " + str(teuchi) + " evel: " + str(evel_ary(teuchi)))

