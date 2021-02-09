import xlsxwriter
import xlwt
from xlwt import Workbook
import random
#####################################################################
#variable list
e = 2.718281828459045 #Natural constant
alpht = 0.02
beta = 0
j = 1
##########################################
wb = Workbook('shuju.xls')

sheet1 = wb.add_sheet('sheet1',cell_overwrite_ok=True)

weight = [0.36,0.26,0.24,0.32,0.26,0.18,0.60,0.60,0.68,1.28,0.99,3.70,1.90,3.31,3.06,1.10,5.85,6.50,5.70,7.40,1.53,1.26,1.25,
          1.52,1.24,7.40,7.40,3.21,3.32,1.64,3.37,1.00]
for w in weight:
    K = 1 / 34
    m = 1
    y = 0
    
    for i in range(1, 150):  # i is time
        # r = random.random()
        sheet1.write(i, j, K)
        # if r < 0.32:
        #     rate = 0.5
        # elif r>0.32 and r<0.9:
        #     rate = 0
        # elif r>0.9:
        #     rate = -0.5
        if(K >= 4/34):
            y = 1 / (1 + 0.0002 * e ** (alpht * (w-beta) * i))
            z = 0.15 * (m - y) # + rate
            K = z + K
            m = y
        else:
            y = 1 / (1 + 0.0002 * e ** (alpht * w * i))
            z = 0.15 * (m - y)
            K = z + K
            m = y
    j = j + 1
wb.save('F:/AI/shuju6.xls')  # save excel
print('保存完成')