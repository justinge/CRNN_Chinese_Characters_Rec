data_path = "D:\\BaiduNetdiskDownload\\icdar2017rctw\\recognition"
save_path = "D:\\BaiduNetdiskDownload\\icdar2017rctw\\recognition"
test_file = data_path + "\\contest.txt"
train_file = data_path + "\\contrain.txt"

fileHandler = open(train_file, "r", encoding="utf-8")

while True:
    # Get next line from file
    raw_line = fileHandler.readline()
    if not raw_line:
        break
    imgname = raw_line.split(' ')[0]
    indices = raw_line.split(' ')[1:]
    if len(indices) < 3:
        print(indices, imgname)