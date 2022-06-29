""" 
[txtファイルからグラフを描くプログラム]
2次元データを想定し、txtファイルに書き込まれているデータは
'x1,y1\n'
'x2,y2\n'
'x3,y3\n'
    :
    :
となる想定
 """

from matplotlib import pyplot as plt
# データのインプット
datanum = int(input('the number of data: '))
xmin,xmax,ymin,ymax = 0,0,0,0
for i in range(datanum):
    with open(input('input txt file: '), 'r') as rf:
        xlist = []
        ylist = []
        while True:
            line = rf.readline()
            if line == None or line == '':
                break
            x,y = line.replace('\n', '').split(',')
            xlist.append(int(x))
            ylist.append(float(y))
        plt.scatter(xlist, ylist, label=input('legend: '))
        if i == 0:
            xmin = min(xlist)
            xmax = max(xlist)
            ymin = min(ylist)
            ymax = max(ylist)
        else:
            xmin = xmin if xmin <= min(xlist) else min(xlist)
            xmax = xmax if xmax >= max(xlist) else max(xlist)
            ymin = ymin if ymin <= min(ylist) else min(ylist)
            ymax = ymax if ymax >= max(ylist) else max(ylist)

plt.title(input('title: '))
plt.xlabel(input('xlabel: '), fontname='MS Gothic')
plt.ylabel(input('ylabel: '), fontname='MS Gothic')
# plt.yscale('log')
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.legend()
plt.show()