import os
#长宽参数
width = 1224.00
height = 370.00

#readline 逐行读取数据
path = 'D:\AI\label_2'
files = os.listdir(path)
for file in files:
    #print('文件名称是：' + str(file) )
    path_all = os.path.join(path , file)
    #print('文件完整目录是 ：' + str(path_all))

    with open(path_all , 'r+', encoding = 'UTF-8') as stream:
        line = stream.readline()
        while line:
            print("读取到的字符是：" + line )
            #拆分字符串
            line_split = line.split()
            frist_class = line_split[0]
            print('首字段' + str(frist_class))
            area_class = line_split[4:8]
            area_float = []

            #print(line_split)
            if frist_class == 'DontCare':
                line_split =  line_split.clear()
                frist_class = frist_class.clear()
                #line = stream.readline()
                print("判断一未通过：\n" + line)
                break

            elif frist_class == []:
                line_split = line_split.clear()
                frist_class = frist_class.clear()
                #line = stream.readline()
                print("判断二未通过：\n" + line)
                break

            else:
                print('分支三:' + line)
                #提取有用信息 ，索引 + 切片 ，
                # area_class  = line_split[4:8]
                # area_float = []
                #把列表中所有的字符串改写为浮点数
                for num in area_class:
                    area_float.append(float(num))

                area_class_new = [area_float[0]/width , area_float[1]/height , area_float[2]/width , area_float[3]/height]

                #将字符串整合
                area_class_new.insert(0 , frist_class)
                print(type(frist_class))

                print('新字符串为：' + str(area_class_new) + '\n')
                print('***********************************************************************************\n')
                #清空文件

                #按行写入文件
                stream.truncate(0)
                stream.writelines(str(area_class_new))
                print('写入完成')
                line = stream.readline()

    stream.close()









