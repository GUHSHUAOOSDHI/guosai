# -*- coding: UTF-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

data1 = pd.read_excel(r".\1.xlsx")
keys1 = data1["分类名称"].tolist()
keys2 = data1["单品编码"].tolist()

LeiDict = {key: 0.0 for key in keys1}
#品类销量字典
MaLeiDict =dict(zip(data1["单品编码"], data1["分类名称"]))
#编码对应品类

# DanDict1 = {key: 0.0 for key in keys2}
# DanDict2 = {key: 0.0 for key in keys2}
# DanDict3 = {key: 0.0 for key in keys2}
# DanDict4 = {key: 0.0 for key in keys2}
# 分别对应春夏秋冬
#
# data2 = pd.read_excel(r"D:\sxjm\2.xlsx")
# for i in range(len(data2["销售日期"])):
#     a = data2["销售日期"][i].strftime('%Y-%m-%d %H:%M:%S')
#     if a[5:7] == "03" or a[5:7] == "04" or a[5:7] == "05":
#         DanDict1[data2["单品编码"][i]] += data2["销量(千克)"][i]
#     elif a[5:7] == "06" or a[5:7] == "07" or a[5:7] == "08":
#         DanDict2[data2["单品编码"][i]] += data2["销量(千克)"][i]
#     elif a[5:7] == "09" or a[5:7] == "10" or a[5:7] == "11":
#         DanDict3[data2["单品编码"][i]] += data2["销量(千克)"][i]
#     else:
#         DanDict4[data2["单品编码"][i]] += data2["销量(千克)"][i]
DanDict1 = {102900005115168: 453.7779999999989, 102900005115199: 323.3549999999996, 102900005115625: 0.0, 102900005115748: 503.4539999999991, 102900005115762: 2559.202000000008, 102900005115779: 3054.353999999997, 102900005115786: 2333.858999999959, 102900005115793: 239.75499999999997, 102900005115816: 0.0, 102900005115823: 2019.3239999999862, 102900005115854: 234.9849999999996, 102900005115861: 1.619, 102900005115878: 532.7619999999985, 102900005115885: 459.5869999999998, 102900005115908: 624.8220000000005, 102900005115946: 400.12799999999913, 102900005115960: 2838.6969999999874, 102900005115977: 15.144999999999998, 102900005115984: 2002.3449999999898, 102900005116639: 84.27799999999999, 102900005116776: 0.0, 102900005116790: 527.5369999999999, 102900005116806: 0.0, 102900005118572: 456.25799999999873, 102900005118817: 854.9849999999992, 102900005118831: 2161.0, 102900005119975: 998.3880000000014, 102900005122654: 105.80399999999997, 102900005128748: 1.7099999999999997, 102900011000175: 0.0, 102900011000571: 136.96499999999995, 102900011002414: 29.51399999999999, 102900011006689: 638.175000000001, 102900011006948: 191.4770000000001, 102900011006955: 0.0, 102900011007464: 15.20899999999999, 102900011007471: 4.943000000000001, 102900011007495: 3.056, 102900011008133: 4.322, 102900011008164: 1640.0590000000043, 102900011008485: 0.559, 102900011008492: 0.0, 102900011008515: 10.303000000000003, 102900011008522: 0.0, 102900011008676: 0.0, 102900011015384: 3.3899999999999997, 102900011015391: 0.9430000000000001, 102900011021644: 0.0, 102900011022849: 0.0, 102900011022924: 30.27499999999999, 102900011023464: 1462.5100000000084, 102900011026502: 0.0, 102900011026618: 0.0, 102900011027462: 0.0, 102900011027615: 0.0, 102900011029688: 0.0, 102900011030042: 0.0, 102900011030059: 3698.0, 102900011030097: 2273.0, 102900011030103: 170.0, 102900011030110: 2262.0, 102900011030134: 228.0, 102900011030141: 294.0, 102900011030158: 0.0, 102900011030400: 0.0, 102900011030417: 0.0, 102900011030905: 39.0, 102900011031216: 18.0, 102900011032176: 32.0, 102900011032282: 0.0, 102900011032480: 1.398, 102900011032589: 28.600999999999992, 102900011032787: 147.0, 102900011033081: 24.996000000000002, 102900011033173: 9.300000000000002, 102900011033234: 56.0, 102900011033241: 33.0, 102900011033531: 0.682, 102900011033562: 0.419, 102900011033586: 1.153, 102900011033906: 70.51199999999996, 102900011033920: 54.80299999999998, 102900011034200: 25.0, 102900011034217: 4.0, 102900011034224: 42.0, 102900011034231: 2516.0, 102900011034316: 9.381, 102900011034323: 5.529, 102900011034354: 37.0, 102900011035481: 0.0, 102900011035764: 0.0, 102900011035771: 0.0, 102900011035849: 16.538000000000004, 102900011036686: 5.0, 102900051000890: 0.0, 102900051009220: 36.38100000000001, 102900051010455: 1395.889000000004, 102900051010790: 17.70299999999999, 106971563780002: 8.0, 106972776821582: 27.0, 102900005116714: 5056.107000000086, 102900011000632: 1.267, 102900011009970: 1694.0229999999965, 102900011033913: 0.615, 102900011034026: 1063.2189999999987, 102900005116042: 0.0, 102900005116899: 3166.945999999989, 102900005118824: 359.7679999999994, 102900011001561: 0.0, 102900011001691: 10.519999999999998, 102900011007969: 46.935999999999986, 102900011009277: 0.0, 102900011010891: 275.4910000000001, 102900011018132: 0.0, 102900011021842: 779.0, 102900011023976: 0.0, 102900011024010: 21.0, 102900011032114: 0.0, 102900011032732: 32.85800000000001, 102900011034569: 0.0, 102900011035511: 0.0, 102900011035962: 0.0, 102900051000944: 102.43999999999998, 102900051006229: 0.0, 102900005116257: 4276.267000000015, 102900005116509: 697.2479999999998, 102900011000335: 2.2369999999999997, 102900011009444: 270.99599999999964, 102900011016909: 27.488000000000017, 102900011022764: 381.5669999999994, 102900011033975: 0.0, 102900011033982: 1.674, 102900011033999: 0.0, 102900051000463: 205.48099999999985, 102900005116219: 91.96499999999989, 102900005116226: 222.26200000000017, 102900005116233: 486.0499999999988, 102900005116905: 0.0, 102900005116943: 94.73099999999985, 102900005117056: 0.0, 102900005117209: 6.5280000000000005, 102900005119968: 0.9199999999999999, 102900005123880: 5.135, 102900005125808: 193.0619999999993, 102900011000328: 2581.266000000003, 102900011000861: 0.0, 102900011001219: 15.485999999999995, 102900011009772: 0.0, 102900011016701: 8881.837000000309, 102900011022030: 211.0, 102900011023648: 0.0, 102900011027479: 6.514, 102900011028407: 0.0, 102900011029176: 0.0, 102900011029275: 0.0, 102900011029299: 0.0, 102900011029305: 0.0, 102900011031100: 2901.0, 102900011031582: 207.0, 102900011031735: 0.0, 102900011031742: 0.0, 102900011031759: 0.0, 102900011032022: 1193.0, 102900011032145: 0.0, 102900011032206: 157.0, 102900011032213: 120.0, 102900011032220: 164.0, 102900011032237: 631.0, 102900011032244: 157.0, 102900011032251: 2623.0, 102900011032343: 167.80799999999988, 102900011032350: 28.128999999999998, 102900011032367: 27.349000000000007, 102900011032848: 636.0, 102900011034262: 0.0, 102900011034439: 365.0, 102900011035078: 284.37599999999935, 102900011036242: 43.0, 102900051004294: 411.8969999999999, 102900005115250: 1293.724000000004, 102900005116530: 1159.4909999999986, 102900005116547: 665.096000000002, 102900005116837: 336.74999999999994, 102900005116912: 13.366999999999997, 102900005117353: 18.0, 102900005119098: 161.80900000000005, 102900005119104: 46.0, 102900005119944: 53.326000000000064, 102900005125815: 280.2249999999997, 102900011001806: 102.0, 102900011001813: 16.0, 102900011007044: 61.0, 102900011008577: 2.0, 102900011009246: 49.720000000000034, 102900011010563: 0.0, 102900011011058: 0.638, 102900011011546: 15.0, 102900011011669: 0.0, 102900011011782: 0.0, 102900011012482: 0.0, 102900011012871: 0.0, 102900011012994: 195.0, 102900011013274: 633.0, 102900011018095: 77.0, 102900011021675: 2.388, 102900011021699: 0.0, 102900011023075: 1.0, 102900011026793: 0.0, 102900011030561: 0.0, 102900011030608: 13.0, 102900011030615: 0.0, 102900011030622: 0.0, 102900011030639: 0.0, 102900011030912: 0.0, 102900011030929: 0.0, 102900011031599: 0.0, 102900011031841: 0.0, 102900011031858: 0.0, 102900011031926: 296.0, 102900011031995: 0.0, 102900011032619: 2.9829999999999997, 102900011032626: 28.534999999999986, 102900011032633: 51.894999999999975, 102900011032640: 16.953, 102900011033937: 25.396000000000008, 102900011033944: 351.11600000000163, 102900011033968: 9.239999999999998, 102900011034330: 1282.0, 102900011034538: 0.0, 102900011034705: 0.0, 102900011035740: 196.0, 102900011035788: 0.0, 102900011036068: 0.0, 102900011036266: 0.0, 102900051009336: 15.302999999999999, 106930274220092: 107.0, 106930274620090: 0.0, 106931885000035: 2.0, 106931885000356: 2.0, 106949711300068: 827.0, 106949711300167: 545.0, 106949711300259: 3341.0, 106956146480197: 1.0, 106956146480203: 0.0, 106957634300010: 2.0, 106957634300058: 6.0, 106958851400125: 575.0, 106971533450003: 570.0, 106971533455008: 1018.0, 106973223300667: 0.0, 106973990980123: 0.0}
DanDict2 = {102900005115168: 62.34600000000001, 102900005115199: 0.0, 102900005115625: 0.0, 102900005115748: 0.0, 102900005115762: 2042.8720000000242, 102900005115779: 6478.055000000212, 102900005115786: 3913.158999999953, 102900005115793: 958.8820000000036, 102900005115816: 18.427999999999997, 102900005115823: 2672.7009999999827, 102900005115854: 0.0, 102900005115861: 0.964, 102900005115878: 0.0, 102900005115885: 0.0, 102900005115908: 1954.6889999999976, 102900005115946: 857.350999999999, 102900005115960: 2582.0170000000085, 102900005115977: 0.0, 102900005115984: 3969.3189999999345, 102900005116639: 10.036999999999997, 102900005116776: 0.0, 102900005116790: 826.991999999999, 102900005116806: 0.377, 102900005118572: 92.36800000000012, 102900005118817: 858.1230000000037, 102900005118831: 1707.0, 102900005119975: 3455.5300000000007, 102900005122654: 0.0, 102900005128748: 0.074, 102900011000175: 91.27200000000008, 102900011000571: 92.80799999999998, 102900011002414: 14.818999999999999, 102900011006689: 169.18699999999973, 102900011006948: 360.5359999999997, 102900011006955: 16.019, 102900011007464: 5.037999999999999, 102900011007471: 0.7460000000000001, 102900011007495: 0.056, 102900011008133: 4.408, 102900011008164: 1618.5230000000086, 102900011008485: 49.79400000000001, 102900011008492: 7.48, 102900011008515: 0.0, 102900011008522: 2447.052000000008, 102900011008676: 0.0, 102900011015384: 0.0, 102900011015391: 0.0, 102900011021644: 0.0, 102900011022849: 0.0, 102900011022924: 0.0, 102900011023464: 594.0209999999998, 102900011026502: 6.32, 102900011026618: 10.512, 102900011027462: 16.828999999999997, 102900011027615: 8.472, 102900011029688: 0.0, 102900011030042: 0.0, 102900011030059: 3054.0, 102900011030097: 2109.0, 102900011030103: 0.0, 102900011030110: 992.0, 102900011030134: 376.0, 102900011030141: 783.0, 102900011030158: 0.0, 102900011030400: 0.0, 102900011030417: 0.0, 102900011030905: 2.0, 102900011031216: 1.0, 102900011032176: 6.0, 102900011032282: 0.0, 102900011032480: 0.0, 102900011032589: 0.0, 102900011032787: 895.0, 102900011033081: 0.0, 102900011033173: 0.0, 102900011033234: 600.0, 102900011033241: 0.0, 102900011033531: 0.0, 102900011033562: 0.0, 102900011033586: 0.0, 102900011033906: 1289.784000000003, 102900011033920: 744.4039999999993, 102900011034200: 295.0, 102900011034217: 248.0, 102900011034224: 904.0, 102900011034231: 720.0, 102900011034316: 0.0, 102900011034323: 0.4799999999999999, 102900011034354: 163.0, 102900011035481: 0.0, 102900011035764: 0.0, 102900011035771: 0.0, 102900011035849: 0.0, 102900011036686: 22.0, 102900051000890: 0.671, 102900051009220: 0.0, 102900051010455: 3888.750999999953, 102900051010790: 1.53, 106971563780002: 0.0, 106972776821582: 101.0, 102900005116714: 7810.972000000008, 102900011000632: 0.0, 102900011009970: 2809.630000000007, 102900011033913: 0.0, 102900011034026: 1269.7379999999962, 102900005116042: 0.0, 102900005116899: 4842.794000000027, 102900005118824: 684.102000000001, 102900011001561: 1859.0, 102900011001691: 115.90199999999999, 102900011007969: 52.011000000000024, 102900011009277: 0.0, 102900011010891: 15.103000000000003, 102900011018132: 2.439, 102900011021842: 30.0, 102900011023976: 0.0, 102900011024010: 0.0, 102900011032114: 0.0, 102900011032732: 163.42499999999993, 102900011034569: 39.0, 102900011035511: 0.0, 102900011035962: 0.0, 102900051000944: 641.9100000000014, 102900051006229: 0.0, 102900005116257: 3830.9019999999564, 102900005116509: 1762.7810000000102, 102900011000335: 5.421, 102900011009444: 631.6450000000002, 102900011016909: 19.949, 102900011022764: 1327.7640000000044, 102900011033975: 157.0850000000004, 102900011033982: 233.2930000000002, 102900011033999: 0.0, 102900051000463: 236.06499999999997, 102900005116219: 184.96599999999955, 102900005116226: 357.7960000000004, 102900005116233: 588.3630000000013, 102900005116905: 0.339, 102900005116943: 206.5100000000004, 102900005117056: 2907.811000000035, 102900005117209: 62.89399999999998, 102900005119968: 104.87100000000001, 102900005123880: 68.84199999999998, 102900005125808: 490.8900000000013, 102900011000328: 2706.992000000012, 102900011000861: 27.713000000000026, 102900011001219: 77.34599999999993, 102900011009772: 0.0, 102900011016701: 6356.168000000074, 102900011022030: 178.0, 102900011023648: 0.0, 102900011027479: 94.946, 102900011028407: 0.0, 102900011029176: 0.0, 102900011029275: 0.0, 102900011029299: 1.161, 102900011029305: 13.868999999999994, 102900011031100: 2008.0, 102900011031582: 233.0, 102900011031735: 0.0, 102900011031742: 0.0, 102900011031759: 0.0, 102900011032022: 1364.0, 102900011032145: 0.0, 102900011032206: 263.0, 102900011032213: 209.0, 102900011032220: 64.0, 102900011032237: 577.0, 102900011032244: 202.0, 102900011032251: 887.0, 102900011032343: 115.48100000000008, 102900011032350: 0.0, 102900011032367: 67.55099999999999, 102900011032848: 412.0, 102900011034262: 91.0, 102900011034439: 303.0, 102900011035078: 110.835, 102900011036242: 0.0, 102900051004294: 627.2480000000046, 102900005115250: 310.28499999999974, 102900005116530: 2394.683000000011, 102900005116547: 1440.069999999992, 102900005116837: 14.252000000000004, 102900005116912: 216.828, 102900005117353: 4.0, 102900005119098: 224.05499999999992, 102900005119104: 0.0, 102900005119944: 251.1820000000001, 102900005125815: 1195.9629999999966, 102900011001806: 293.0, 102900011001813: 123.0, 102900011007044: 10.0, 102900011008577: 0.0, 102900011009246: 32.89900000000001, 102900011010563: 0.0, 102900011011058: 0.446, 102900011011546: 124.0, 102900011011669: 0.0, 102900011011782: 0.0, 102900011012482: 0.0, 102900011012871: 0.0, 102900011012994: 133.0, 102900011013274: 464.0, 102900011018095: 0.0, 102900011021675: 0.0, 102900011021699: 0.0, 102900011023075: 0.0, 102900011026793: 6.0, 102900011030561: 0.0, 102900011030608: 6.0, 102900011030615: 0.0, 102900011030622: 0.0, 102900011030639: 0.0, 102900011030912: 345.0, 102900011030929: 201.0, 102900011031599: 0.0, 102900011031841: 0.0, 102900011031858: 1.0, 102900011031926: 81.0, 102900011031995: 272.0, 102900011032619: 84.38999999999999, 102900011032626: 0.0, 102900011032633: 0.0, 102900011032640: 0.0, 102900011033937: 289.25199999999995, 102900011033944: 194.55399999999912, 102900011033968: 0.0, 102900011034330: 1245.0, 102900011034538: 0.0, 102900011034705: 0.0, 102900011035740: 35.0, 102900011035788: 0.0, 102900011036068: 0.0, 102900011036266: 0.0, 102900051009336: 9.674000000000001, 106930274220092: 0.0, 106930274620090: 0.0, 106931885000035: 0.0, 106931885000356: 0.0, 106949711300068: 358.0, 106949711300167: 0.0, 106949711300259: 2186.0, 106956146480197: 177.0, 106956146480203: 4.0, 106957634300010: 0.0, 106957634300058: 0.0, 106958851400125: 270.0, 106971533450003: 378.0, 106971533455008: 237.0, 106973223300667: 0.0, 106973990980123: 109.0}
DanDict3 = {102900005115168: 26.804000000000006, 102900005115199: 6.175999999999999, 102900005115625: 117.75499999999994, 102900005115748: 22.949999999999996, 102900005115762: 408.4579999999998, 102900005115779: 4111.212000000079, 102900005115786: 840.6830000000018, 102900005115793: 472.875, 102900005115816: 0.0, 102900005115823: 1466.9450000000024, 102900005115854: 114.32600000000019, 102900005115861: 1936.6439999999775, 102900005115878: 1996.8070000000125, 102900005115885: 248.60099999999966, 102900005115908: 1244.3789999999956, 102900005115946: 307.12699999999984, 102900005115960: 5212.366000000046, 102900005115977: 48.66699999999996, 102900005115984: 2013.036999999992, 102900005116639: 0.0, 102900005116776: 0.0, 102900005116790: 1076.009000000002, 102900005116806: 75.12700000000007, 102900005118572: 40.142999999999994, 102900005118817: 1476.3130000000067, 102900005118831: 1802.0, 102900005119975: 701.5860000000001, 102900005122654: 583.8949999999991, 102900005128748: 0.0, 102900011000175: 0.0, 102900011000571: 183.28599999999994, 102900011002414: 0.0, 102900011006689: 409.0140000000014, 102900011006948: 114.49999999999997, 102900011006955: 0.0, 102900011007464: 2.5879999999999996, 102900011007471: 0.0, 102900011007495: 0.0, 102900011008133: 0.0, 102900011008164: 1612.7939999999937, 102900011008485: 0.0, 102900011008492: 0.0, 102900011008515: 0.0, 102900011008522: 2099.301000000001, 102900011008676: 6.183000000000001, 102900011015384: 0.0, 102900011015391: 0.0, 102900011021644: 15.0, 102900011022849: 763.0279999999983, 102900011022924: 0.0, 102900011023464: 654.2500000000016, 102900011026502: 0.0, 102900011026618: 0.0, 102900011027462: 0.0, 102900011027615: 0.0, 102900011029688: 2.8859999999999997, 102900011030042: 0.0, 102900011030059: 4375.0, 102900011030097: 2566.0, 102900011030103: 0.0, 102900011030110: 1803.0, 102900011030134: 746.0, 102900011030141: 1089.0, 102900011030158: 0.0, 102900011030400: 0.0, 102900011030417: 0.0, 102900011030905: 224.0, 102900011031216: 0.0, 102900011032176: 0.0, 102900011032282: 0.0, 102900011032480: 0.0, 102900011032589: 0.0, 102900011032787: 34.0, 102900011033081: 0.0, 102900011033173: 0.0, 102900011033234: 71.0, 102900011033241: 32.0, 102900011033531: 0.0, 102900011033562: 0.0, 102900011033586: 0.0, 102900011033906: 1822.6839999999995, 102900011033920: 868.5849999999991, 102900011034200: 106.0, 102900011034217: 89.0, 102900011034224: 2000.0, 102900011034231: 2443.0, 102900011034316: 0.0, 102900011034323: 0.0, 102900011034354: 0.0, 102900011035481: 127.0, 102900011035764: 105.44099999999999, 102900011035771: 96.36700000000005, 102900011035849: 0.0, 102900011036686: 0.0, 102900051000890: 0.0, 102900051009220: 0.0, 102900051010455: 2053.0769999999998, 102900051010790: 3.484, 106971563780002: 0.0, 106972776821582: 0.0, 102900005116714: 7394.798000000085, 102900011000632: 0.798, 102900011009970: 1916.3449999999968, 102900011033913: 0.0, 102900011034026: 2063.2689999999784, 102900005116042: 0.0, 102900005116899: 9708.801000000054, 102900005118824: 124.56700000000004, 102900011001561: 236.0, 102900011001691: 0.0, 102900011007969: 1.522, 102900011009277: 25.752999999999986, 102900011010891: 14.345999999999998, 102900011018132: 16.998999999999995, 102900011021842: 1736.0, 102900011023976: 0.0, 102900011024010: 0.0, 102900011032114: 0.0, 102900011032732: 224.60699999999986, 102900011034569: 1.0, 102900011035511: 189.0369999999997, 102900011035962: 11.397999999999998, 102900051000944: 1.204, 102900051006229: 0.0, 102900005116257: 2025.5449999999978, 102900005116509: 591.5769999999998, 102900011000335: 0.0, 102900011009444: 218.92700000000005, 102900011016909: 13.991999999999999, 102900011022764: 414.37000000000035, 102900011033975: 24.457000000000015, 102900011033982: 62.19099999999995, 102900011033999: 4.981000000000001, 102900051000463: 498.47699999999907, 102900005116219: 37.66700000000001, 102900005116226: 275.061, 102900005116233: 689.7080000000009, 102900005116905: 0.302, 102900005116943: 147.1279999999999, 102900005117056: 3903.3710000000356, 102900005117209: 58.795, 102900005119968: 17.727, 102900005123880: 72.615, 102900005125808: 309.43200000000104, 102900011000328: 900.7940000000018, 102900011000861: 0.0, 102900011001219: 76.79199999999997, 102900011009772: 0.0, 102900011016701: 5409.491000000075, 102900011022030: 0.0, 102900011023648: 0.0, 102900011027479: 19.297000000000008, 102900011028407: 33.90699999999999, 102900011029176: 89.93799999999995, 102900011029275: 0.0, 102900011029299: 0.0, 102900011029305: 0.0, 102900011031100: 2225.0, 102900011031582: 448.0, 102900011031735: 0.0, 102900011031742: 0.0, 102900011031759: 0.0, 102900011032022: 1267.0, 102900011032145: 0.0, 102900011032206: 26.0, 102900011032213: 298.0, 102900011032220: 0.0, 102900011032237: 479.0, 102900011032244: 302.0, 102900011032251: 2132.0, 102900011032343: 33.08699999999999, 102900011032350: 0.0, 102900011032367: 62.758999999999936, 102900011032848: 463.0, 102900011034262: 2.0, 102900011034439: 346.0, 102900011035078: 177.6739999999999, 102900011036242: 0.0, 102900051004294: 543.7289999999997, 102900005115250: 263.1399999999997, 102900005116530: 4044.6960000000004, 102900005116547: 1405.4989999999796, 102900005116837: 674.1429999999987, 102900005116912: 85.69500000000002, 102900005117353: 0.0, 102900005119098: 67.42100000000009, 102900005119104: 56.0, 102900005119944: 127.83499999999981, 102900005125815: 588.653999999999, 102900011001806: 397.0, 102900011001813: 1612.0, 102900011007044: 23.0, 102900011008577: 1.0, 102900011009246: 51.95100000000006, 102900011010563: 1.2149999999999999, 102900011011058: 0.0, 102900011011546: 746.0, 102900011011669: 4.770000000000001, 102900011011782: 0.0, 102900011012482: 28.0, 102900011012871: 1.8619999999999997, 102900011012994: 522.0, 102900011013274: 827.0, 102900011018095: 243.0, 102900011021675: 0.0, 102900011021699: 4.268, 102900011023075: 0.0, 102900011026793: 4.0, 102900011030561: 0.0, 102900011030608: 0.0, 102900011030615: 0.0, 102900011030622: 0.0, 102900011030639: 0.0, 102900011030912: 706.0, 102900011030929: 345.0, 102900011031599: 0.0, 102900011031841: 2.0, 102900011031858: 0.0, 102900011031926: 219.0, 102900011031995: 385.0, 102900011032619: 326.213999999999, 102900011032626: 0.0, 102900011032633: 0.0, 102900011032640: 0.0, 102900011033937: 153.54700000000008, 102900011033944: 400.2509999999999, 102900011033968: 0.0, 102900011034330: 272.0, 102900011034538: 0.0, 102900011034705: 0.0, 102900011035740: 0.0, 102900011035788: 210.0, 102900011036068: 0.0, 102900011036266: 0.0, 102900051009336: 13.147999999999996, 106930274220092: 0.0, 106930274620090: 0.0, 106931885000035: 5.0, 106931885000356: 0.0, 106949711300068: 43.0, 106949711300167: 1422.0, 106949711300259: 4725.0, 106956146480197: 73.0, 106956146480203: 1.0, 106957634300010: 0.0, 106957634300058: 0.0, 106958851400125: 347.0, 106971533450003: 323.0, 106971533455008: 2.0, 106973223300667: 0.0, 106973990980123: 0.0}
DanDict4 = {102900005115168: 356.9090000000007, 102900005115199: 3.692, 102900005115625: 3.2649999999999997, 102900005115748: 192.27200000000005, 102900005115762: 89.52900000000001, 102900005115779: 2266.8399999999942, 102900005115786: 153.06299999999982, 102900005115793: 35.79100000000001, 102900005115816: 0.0, 102900005115823: 1447.785999999996, 102900005115854: 66.01399999999998, 102900005115861: 1897.3390000000095, 102900005115878: 1580.5930000000003, 102900005115885: 231.3869999999999, 102900005115908: 672.8270000000008, 102900005115946: 2.0340000000000003, 102900005115960: 8554.13799999999, 102900005115977: 21.235999999999994, 102900005115984: 2320.662999999991, 102900005116639: 0.0, 102900005116776: 0.0, 102900005116790: 480.76099999999957, 102900005116806: 25.621000000000006, 102900005118572: 7.928, 102900005118817: 2027.04, 102900005118831: 3312.0, 102900005119975: 3.9290000000000003, 102900005122654: 4272.755000000027, 102900005128748: 0.0, 102900011000175: 0.0, 102900011000571: 262.16199999999986, 102900011002414: 0.9189999999999999, 102900011006689: 327.102, 102900011006948: 66.10199999999999, 102900011006955: 0.318, 102900011007464: 7.337000000000002, 102900011007471: 1.8789999999999998, 102900011007495: 1.12, 102900011008133: 5.497000000000001, 102900011008164: 944.9320000000026, 102900011008485: 1.3820000000000001, 102900011008492: 0.0, 102900011008515: 2.633, 102900011008522: 138.90800000000004, 102900011008676: 9.703999999999999, 102900011015384: 0.0, 102900011015391: 0.0, 102900011021644: 10.0, 102900011022849: 612.0940000000004, 102900011022924: 0.0, 102900011023464: 557.2119999999987, 102900011026502: 0.0, 102900011026618: 0.0, 102900011027462: 0.0, 102900011027615: 0.0, 102900011029688: 0.0, 102900011030042: 313.0, 102900011030059: 3198.0, 102900011030097: 1900.0, 102900011030103: 417.0, 102900011030110: 1285.0, 102900011030134: 703.0, 102900011030141: 904.0, 102900011030158: 296.0, 102900011030400: 3.0, 102900011030417: 3.0, 102900011030905: 205.0, 102900011031216: 10.0, 102900011032176: 2.0, 102900011032282: 41.0, 102900011032480: 0.8260000000000001, 102900011032589: 0.0, 102900011032787: 0.0, 102900011033081: 0.0, 102900011033173: 0.0, 102900011033234: 0.0, 102900011033241: 0.0, 102900011033531: 0.0, 102900011033562: 0.0, 102900011033586: 0.0, 102900011033906: 3301.7559999999908, 102900011033920: 214.97599999999994, 102900011034200: 0.0, 102900011034217: 0.0, 102900011034224: 1111.0, 102900011034231: 1252.0, 102900011034316: 0.0, 102900011034323: 0.0, 102900011034354: 0.0, 102900011035481: 0.0, 102900011035764: 81.38999999999994, 102900011035771: 59.12900000000002, 102900011035849: 0.0, 102900011036686: 0.0, 102900051000890: 0.0, 102900051009220: 4.345000000000001, 102900051010455: 650.2730000000001, 102900051010790: 4.305000000000001, 106971563780002: 0.0, 106972776821582: 0.0, 102900005116714: 7275.351000000036, 102900011000632: 11.186, 102900011009970: 1973.7880000000036, 102900011033913: 0.0, 102900011034026: 1425.3450000000075, 102900005116042: 0.0, 102900005116899: 9430.89900000006, 102900005118824: 11.215000000000003, 102900011001561: 0.0, 102900011001691: 0.0, 102900011007969: 0.0, 102900011009277: 1645.6710000000003, 102900011010891: 143.91999999999996, 102900011018132: 31.37699999999999, 102900011021842: 3507.0, 102900011023976: 62.22100000000004, 102900011024010: 0.0, 102900011032114: 10.0, 102900011032732: 28.794000000000025, 102900011034569: 0.0, 102900011035511: 159.76299999999978, 102900011035962: 0.0, 102900051000944: 0.0, 102900051006229: 18.614, 102900005116257: 3469.287000000027, 102900005116509: 465.157, 102900011000335: 0.0, 102900011009444: 45.650000000000006, 102900011016909: 39.95000000000001, 102900011022764: 372.7120000000003, 102900011033975: 8.979999999999999, 102900011033982: 0.0, 102900011033999: 0.0, 102900051000463: 107.66600000000005, 102900005116219: 123.99499999999996, 102900005116226: 331.41200000000055, 102900005116233: 1693.7540000000076, 102900005116905: 1.176, 102900005116943: 210.19099999999958, 102900005117056: 2891.943000000008, 102900005117209: 134.97499999999988, 102900005119968: 4.981999999999999, 102900005123880: 65.45099999999998, 102900005125808: 453.96900000000005, 102900011000328: 1603.1290000000038, 102900011000861: 0.0, 102900011001219: 108.98799999999986, 102900011009772: 0.415, 102900011016701: 7516.835000000026, 102900011022030: 252.0, 102900011023648: 0.0, 102900011027479: 42.883000000000045, 102900011028407: 0.0, 102900011029176: 29.707000000000008, 102900011029275: 1.754, 102900011029299: 5.682000000000001, 102900011029305: 14.701999999999996, 102900011031100: 3699.0, 102900011031582: 44.0, 102900011031735: 18.0, 102900011031742: 6.0, 102900011031759: 13.0, 102900011032022: 1351.0, 102900011032145: 0.0, 102900011032206: 11.0, 102900011032213: 80.0, 102900011032220: 55.0, 102900011032237: 620.0, 102900011032244: 292.0, 102900011032251: 2593.0, 102900011032343: 53.65700000000001, 102900011032350: 48.46699999999999, 102900011032367: 57.15100000000001, 102900011032848: 357.0, 102900011034262: 0.0, 102900011034439: 243.0, 102900011035078: 196.32299999999972, 102900011036242: 2.0, 102900051004294: 636.9070000000022, 102900005115250: 943.5670000000003, 102900005116530: 4321.357, 102900005116547: 1186.8049999999942, 102900005116837: 1517.8139999999964, 102900005116912: 59.331999999999965, 102900005117353: 0.0, 102900005119098: 174.433, 102900005119104: 0.0, 102900005119944: 69.82199999999996, 102900005125815: 340.13499999999954, 102900011001806: 279.0, 102900011001813: 398.0, 102900011007044: 193.0, 102900011008577: 0.0, 102900011009246: 77.60099999999997, 102900011010563: 0.0, 102900011011058: 0.0, 102900011011546: 381.0, 102900011011669: 9.937999999999999, 102900011011782: 0.0, 102900011012482: 62.0, 102900011012871: 3.933, 102900011012994: 493.0, 102900011013274: 1003.0, 102900011018095: 658.0, 102900011021675: 0.0, 102900011021699: 2.3340000000000005, 102900011023075: 0.0, 102900011026793: 0.0, 102900011030561: 5.0, 102900011030608: 15.0, 102900011030615: 7.0, 102900011030622: 4.0, 102900011030639: 4.0, 102900011030912: 250.0, 102900011030929: 195.0, 102900011031599: 102.0, 102900011031841: 8.0, 102900011031858: 0.0, 102900011031926: 513.0, 102900011031995: 25.0, 102900011032619: 0.254, 102900011032626: 0.0, 102900011032633: 0.0, 102900011032640: 0.0, 102900011033937: 5.119999999999999, 102900011033944: 358.6310000000015, 102900011033968: 0.0, 102900011034330: 1430.0, 102900011034538: 3.0, 102900011034705: 8.0, 102900011035740: 140.0, 102900011035788: 169.0, 102900011036068: 13.0, 102900011036266: 3.0, 102900051009336: 1.8519999999999999, 106930274220092: 292.0, 106930274620090: 708.0, 106931885000035: 0.0, 106931885000356: 0.0, 106949711300068: 1321.0, 106949711300167: 1208.0, 106949711300259: 5344.0, 106956146480197: 0.0, 106956146480203: 90.0, 106957634300010: 166.0, 106957634300058: 75.0, 106958851400125: 957.0, 106971533450003: 32.0, 106971533455008: 518.0, 106973223300667: 1.0, 106973990980123: 0.0}

LeiDict1 = {'花叶类': 0.0, '花菜类': 0.0, '水生根茎类': 0.0, '茄类': 0.0, '辣椒类': 0.0, '食用菌': 0.0}
LeiDict2 = {'花叶类': 0.0, '花菜类': 0.0, '水生根茎类': 0.0, '茄类': 0.0, '辣椒类': 0.0, '食用菌': 0.0}
LeiDict3 = {'花叶类': 0.0, '花菜类': 0.0, '水生根茎类': 0.0, '茄类': 0.0, '辣椒类': 0.0, '食用菌': 0.0}
LeiDict4 = {'花叶类': 0.0, '花菜类': 0.0, '水生根茎类': 0.0, '茄类': 0.0, '辣椒类': 0.0, '食用菌': 0.0}
for key, value in DanDict1.items():
    LeiDict1[MaLeiDict[key]] += value
for key, value in DanDict2.items():
    LeiDict2[MaLeiDict[key]] += value
for key, value in DanDict3.items():
    LeiDict3[MaLeiDict[key]] += value
for key, value in DanDict4.items():
    LeiDict4[MaLeiDict[key]] += value
print(LeiDict1)
print(LeiDict2)
print(LeiDict3)
print(LeiDict4)

# 提取键和值
x = list(LeiDict4.keys())
y = list(LeiDict4.values())
print(y)

plt.figure(figsize=(12, 8))
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.xticks(rotation=45)

# 绘制柱状图
plt.bar(x, y)

# 添加标题和标签
plt.title('蔬菜各品类销售量冬季分布图')
plt.xlabel('品类名称')
plt.ylabel('销量(千克)')

plt.subplots_adjust(bottom=0.2)
# 显示图形
plt.show()