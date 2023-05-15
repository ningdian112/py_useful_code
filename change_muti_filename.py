import os

ori_txt = "average"
new_txt = 'original'


aim_add = r"C:\Users\Ning\...\original"
# 替换文件夹内的所有文件夹的名字个别关键词
# car_average_0 》》 car_original_0



aim_list  = os.listdir(aim_add)
s = []
for file in aim_list:
    if os.path.isdir(aim_add +'\\'+ file):
        if ori_txt in file:
            print("yes")
            new_file = file
            new_file = new_file.replace(ori_txt, new_txt)
            new_file_num = aim_list.index(file)
            ori_address = os.rename(aim_add +'\\'+ file,aim_add +'\\'+ new_file)

            # aim_list[new_file_num] = new_file
