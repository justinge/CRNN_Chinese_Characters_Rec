import os
import cv2
import glob
import pathlib
import random

data_path = "D:\\BaiduNetdiskDownload\\icdar2017rctw\\recognition"
save_path = "D:\\BaiduNetdiskDownload\\icdar2017rctw\\recognition"
std_chinese_label = "../lib/dataset/txt/char_std_5990.txt"
test_file = data_path + "\\contest.txt"
train_file = data_path + "\\contrain.txt"
test_file_handler = open(test_file, "a", encoding="utf-8")
train_file_handler = open(train_file, "a", encoding="utf-8")

raw_char_set = open(std_chinese_label, 'r', encoding='GB18030').readlines()
char_det = [x.strip() for x in raw_char_set]

fileHandler = open(data_path + "/train.txt", "r", encoding="utf-8")
cnt = 0
while True:
    # Get next line from file
    raw_line = fileHandler.readline()
    # If line is empty then end of file reached
    if not raw_line:
        break
    line = raw_line.strip()
    list_line = line.split("\t")
    if len(list_line) < 3:
        continue
    image_path = pathlib.Path(list_line[0])

    image_name = os.path.basename(image_path)
    if os.path.exists(data_path + "\\train" + "\\" + image_name):
        # print(data_path + " exist")
        pass
    else:
        print(data_path + " not exist")
        continue
    str_val = list_line[1]
    char_idx_str = ""
    char_idx = -1
    for i in str_val:
        if i in char_det:
            char_idx = char_det.index(i)
        if char_idx == -1:
            print(i + "字不存在")
            continue
        else:
            char_idx_str = char_idx_str + str(char_idx) + " "
    if len(char_idx_str) == 0 or len(char_idx_str) >= 20:
        print("xxxxx", image_name)
        continue

    to_write_line = image_name + " " + char_idx_str.strip() + "\n"
    if cnt % 13 == 0:
        test_file_handler.write(to_write_line)
    else:
        train_file_handler.write(to_write_line)
    # test_file_handler.write(to_write_line)
    # train_file_handler.write(to_write_line)
    cnt = cnt + 1

    # Close Close
test_file_handler.close()
train_file_handler.close()
fileHandler.close()
