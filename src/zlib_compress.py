from inspect import trace
import time
import zlib
import swoperator
import matplotlib.pyplot as plt
import openpyxl
import traceback

_level = 6
_wbits = -15
_memLevel = 8
_strategy = zlib.Z_FIXED
co = zlib.compressobj(level=_level, wbits=_wbits, memLevel=_memLevel, strategy=_strategy)
do = zlib.decompressobj(wbits=-zlib.MAX_WBITS)
for i in range(10):
    print(len(co.compress(b"! aaa authentication ppp ADMIN if-needed #STACK_AUTHEN_PPP_ADMIN_TYPE")
     + co.flush(zlib.Z_PARTIAL_FLUSH)))

# try:
#     while True:
#         print(len(co.compress(b"! aaa authentication ppp ADMIN if-needed #STACK_AUTHEN_PPP_ADMIN_TYPE")+co.flush(zlib.Z_PARTIAL_FLUSH)))
#         print(len('! aaa authentication ppp ADMIN if-needed #STACK_AUTHEN_PPP_ADMIN_TYPE'))
#         time.sleep(1)
# except Exception() as e:
#     quit()
quit()

so = swoperator.SWOperator()
# Dictionary for compression
commandDict = b''
for i in range(500):
    commandDict += (so.c.getCmd_zipf().replace(' <cr>', '\r\n')).encode()
isContinue = True
# allparameter
# _level_list = range(0, 10)
# _wbits_list = list(range(9,16)) + list(range(-15, -8))
# _memLevel_list = range(1, 10)
# _strategy_list = [zlib.Z_DEFAULT_STRATEGY, zlib.Z_FILTERED, zlib.Z_HUFFMAN_ONLY, zlib.Z_RLE, zlib.Z_FIXED]
_level_list = [6]
_wbits_list = [-15]
_memLevel_list = [8]
_strategy_list = [zlib.Z_FIXED]

progres_srate = 0
rlt_list = []
try:
    for _level in _level_list:
        for _wbits in _wbits_list:
            for _memLevel in _memLevel_list:
                for _strategy in _strategy_list:
                    co = zlib.compressobj(level=_level, wbits=_wbits, memLevel=_memLevel, strategy=_strategy, zdict=commandDict)
                    do = zlib.decompressobj(wbits=-zlib.MAX_WBITS, zdict=commandDict)

                    # raw_data = b''
                    # for i in range(10):
                    #     raw_data += so.c.getCmd_zipf().replace(' <cr>','\r\n').encode()
                    #     compress_data = co.compress(raw_data) + co.flush(zlib.Z_SYNC_FLUSH)
                    #     print(len(compress_data)/len(raw_data))
                    #     print(do.decompress(compress_data))
                    #     print('\r\n')
                    # print('-----')
                    ITER = 10000
                    SUM_comp = 0
                    SUM_raw = 0
                    _list = []
                    for i in range(ITER):
                        raw_data = so.c.getCmd_zipf().replace(' <cr>','\r\n').encode()
                        compress_data = co.compress(raw_data) + co.flush(zlib.Z_PARTIAL_FLUSH)
                        # print(do.decompress(compress_data))
                        SUM_comp += len(compress_data)
                        SUM_raw += len(raw_data)
                        _list.append(len(compress_data)/len(raw_data))
                    rlt_list.append((_level, _wbits, _memLevel, _strategy, SUM_comp/SUM_raw))
                    # _list.sort()
                    # plt.scatter(range(len(_list)),_list, marker='o')
                    # plt.hlines(SUM_comp/SUM_raw, 0, 10000, colors='red')
                    # plt.title('(level, wbits, memLevel, strategy) = (6, -15 8, 4)')
                    # plt.xlabel('圧縮に用いた累計コマンド数', fontname='MS Gothic')
                    # plt.ylabel('圧縮率(圧縮後のサイズ/元データのサイズ)', fontname='MS Gothic')
                    # plt.show()
                    print(SUM_comp/SUM_raw)
                    
                    del co, do
                    progres_srate += 1
                    print('{:3}'.format(progres_srate*100/5040))
                    # if progres_srate > 100:
                    #     isContinue = False
                    if not isContinue:
                        break
                if not isContinue:
                    break
            if not isContinue:
                break
        if not isContinue:
            break
except Exception as e:
    print("error occurs!!")
    print('now var is {},{},{},{}'.format(_level, _wbits, _memLevel, _strategy))
    print(traceback.format_exc())


# wb = openpyxl.Workbook()
# #2 grab the active worksheet(開いているワークシートを選択)
# ws = wb.active
# #3 Data can be assigned directly to cells(セルに直接データを挿入)
# ws.append(['level', 'wbits', 'memLevel', 'strategy'])
# #4 Rows can also be appended(行の追記)
# for i in rlt_list:
#     ws.append(i)
# #6 Save the file(ファイルを保存する)
# wb.save("zlib_compresstest_iter_nodict.xlsx")


with open('zlib_compress.txt', 'w') as f:
    for i, l in enumerate(_list):
        f.write(str(i+1) + ',' + str(l) + '\n')
