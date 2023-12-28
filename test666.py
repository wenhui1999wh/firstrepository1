# """
# issubclass()函数的使用，判断参数class是不是类型参数的子类
# 用法：issubclass(class, classinfo)
# """
# class A:
#     pass
# class B(A):
#     pass
#
# print(issubclass(B, A))
#
# """
# isinstance()函数的使用，判断一个对象是否是一个已经知道类型的对象
# 用法: isinstance(object, classinfo)
# isinstance()和type()的区别 isinstance会考虑继承关系，type不考虑继承关系
# """
# a = 1
# print(isinstance(1, int))
# print(type(a))

'''@classmethod方法 '''
import re

# class DateMethodBefore:
#     def __init__(self,year=0,month=0,day=0):
#         self.day=day
#         self.month=month
#         self.year=year
#
#     def print_date(self):
#         print(self.year)
#         print(self.month)
#         print(self.day)
#
# string_date = input("请输入yyyy-mm-dd格式的日期：")
# year, month, day = map(int, string_date.split('-'))
# dd = DateMethodBefore(year, month, day)
# dd.print_date()

# class DateMethodBefore:
#     def __init__(self,year=0,month=0,day=0):
#         self.day=day
#         self.month=month
#         self.year=year
#
#     @classmethod
#     def deal_date(cls,string_date):
#         year, month, day = map(int,string_date.split('_'))
#         date1=cls(year,month,day)
#         return date1
#
#     def print_date(self):
#         print(self.year)
#         print(self.month)
#         print(self.day)
#
# dd = DateMethodBefore.deal_date("2023-09-08")
# dd.print_date()

# def compare_lists(list1, list2, list3):
#     if len(list1) != len(list2) or len(list1) != len(list3):
#         return False
#
#     for dict1, dict2, dict3 in zip(list1, list2, list3):
#         print(f"dict1{dict1}, dict2{dict2}, dict3{dict3}")
#         if sorted(dict1.items()) != sorted(dict2.items()) or sorted(dict1.items()) != sorted(dict3.items()):
#             print(f"dictitems1{dict1.items()}, dictitems2{dict2.items()}, dictitems3{dict3.items()}")
#             return False
#
#     return True
#
# list1 = [{"a": 1, "b": 2}, {"c": 5, "d": 4}]
# list2 = [{"b": 2, "a": 1}, {"d": 4, "c": 3}]
# list3 = [{"a": 1, "b": 2}, {"c": 3, "d": 4}]
#
# result = compare_lists(list1, list2, list3)
# print(result)

# list1 = [{"a": 1, "b": 2, "c": 5}, {"a": 1, "b": 2, "c": 4}]
# list2 = [{"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 4}]
# list3 = [{"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 8}]
#
# def compare_lists(list1, list2, list3):
#     print('以测试环境为基准-------------------------------------\n')
#     for record1 in list1:
#         if record1 not in list2 and record1 not in list3:
#             print(f'{record1}跟预发、生产环境配置不一致！')
#             for record2 in list2:
#                 for i in record2:
#                     print(i.get('a'), i.get('b'), i.get('c'))
#
#
#
#
#         elif record1 not in list2:
#             print(f'{record1}在预发环境中未配置！')
#         elif record1 not in list3:
#             print(f'{record1}在生产环境中未配置！')
#         else:
#             print(f'{record1}在测试、预发、生产环境中都已经配置啦~~')
#
#     print('以预发环境为基准-------------------------------------\n')
#     for record in list2:
#         if record not in list1 and record not in list3:
#             print(f'{record}在测试、生产环境中未配置！')
#         elif record not in list1:
#             print(f'{record}在测试环境中未配置！')
#         elif record not in list3:
#             print(f'{record}在生产环境中未配置！')
#         else:
#             print(f'{record}在测试、预发、生产环境中都已经配置啦~~')
#
#     print('以生产环境为基准-------------------------------------\n')
#     for record in list3:
#         if record not in list1 and record not in list2:
#             print(f'{record}在测试、预发环境中未配置！')
#         elif record not in list1:
#             print(f'{record}在测试环境中未配置！')
#         elif record not in list2:
#             print(f'{record}在预发环境中未配置！')
#         else:
#             print(f'{record}在测试、预发、生产环境中都已经配置啦~~')
# compare_lists(list1, list2, list3)


# list1 = [{"a": 1, "b": 6, "c": 3}, {"a": 1, "b": 2, "c": 3}]
# list2 = [{"a": 1, "b": 5, "c": 3}, {"a": 1, "b": 4, "c": 3}]
# list3 = [{"a": 1, "b": 2, "c": 3}, {"a": 1, "b": 2, "c": 3}]




# print(len(erfa))
# #嵌套字典列表去重
# def get_single_data(list):
#     singleDict = set()
#     newDict = []
#     for i in list:
#         #将字典转为元组，元组可是哈希类型
#         n = tuple(i.items())
#         if n not in singleDict:
#             singleDict.add(n)
#             newDict.append(i)
#     return newDict
#
# def get_data(record,data,newData):
#     for record_any in data:
#         # 需判断两个字典是完全一致的情况
#         if record == record_any:
#             continue
#         else:
#             # 存在以下情况，键值不完全一致
#             for key in record:
#                 if record[key] != record_any[key]:
#                     newData.append(record_any)
#                     break
#
# def compare_dic(list1, list2, list3):
#     # 被标注的字典:
#     signDict = []
#     testData = []
#     productData = []
#     print('以测试环境为基准-------------------------------------\n')
#     for record_1 in list1:
#         get_data(record_1,list2,testData)
#         get_data(record_1, list3,productData)
#     print('测试环境和预发环境数据不一致，不一致的数据如下：', get_single_data(testData))
#     print('测试环境和生产环境数据一致' if len(productData) == 0 else f'测试环境和生产环境数据不一致，不一致的数据如下：{get_single_data(productData)}')
#
#     # return testData + productData
# print('返回数据', compare_dic(list1, list2, list3))

"""
同一个列表筛选出重复数据
"""
# import re
# """
# 1.先遍历这个列表里的每一个元素
# 2.再用正则提取出【地区3200，服务P_sb_sbf】并赋值给一个变量 data
# 3.再对data进行比较，如果data一致，再比较data下标对应的数据长度，将长度较长的对应元素返回赋值给一个列表（即是最终筛选好的数据）
# """
#
# # 列表中相同的元素以及它们的下标
# def find_same_elements(lst):
#     result = {}
#     for index, element in enumerate(lst):
#         if element in result:
#             result[element].append(index)
#         else:
#             result[element] = [index]
#     return {key: value for key, value in result.items() if len(value) > 1}
#
# items = [  '地区3200，服务P_sb_sbf预发环境跟测试环境不一致！',
# 	'地区3500，服务P_sb_zzs_ybnsr生产环境跟测试、预发环境不一致！',
# 	'地区6300，服务P_sb_sy_yhs测试环境跟预发、生产环境不一致！',
# 	'地区4200，服务G_qchdxx_xgmnsr生产环境跟测试环境不一致！',
# 	'地区3300，服务L_zj_wjkxxcx生产环境跟测试环境不一致！',
# 	'地区4200，服务G_wspz生产环境跟测试环境不一致！',
# 	'地区3502，服务I_getSession预发环境跟测试环境不一致！',
# 	'地区4400，服务IC_P_gsgsnb生产环境跟测试环境不一致！',
# 	'地区4400，服务IC_P_gsgsnb测试环境跟预发、生产环境不一致！',
# 	'地区4403，服务SI_L_login_request预发环境跟测试环境不一致！',
# 	'地区3200，服务P_sbzf测试环境跟预发、生产环境不一致！',
# 	'地区1300，服务IC_P_gsgsnb生产环境跟测试、预发环境不一致！',
# 	'地区3500，服务P_sb_zzs_xgmnsr预发环境跟测试环境不一致！',
# 	'地区4400，服务G_wsbxx_yq预发环境跟测试环境不一致！',
# 	'地区3200，服务P_sb_sbf生产环境跟测试环境不一致！',
# 	'地区4200，服务G_jks预发环境跟测试、生产环境不一致',
# 	'地区6300，服务G_jmxx_ybnsr预发环境跟测试环境不一致！',
# 	'地区3400，服务G_sylb_xxcj_fcs生产环境跟预发环境不一致！',
# 	'地区3200，服务P_sb_tysb_fssr测试环境跟预发、生产环境不一致！',
# 	'地区4400，服务G_capture_picture预发环境跟测试环境不一致！',
# 	'地区3400，服务I_loginOut生产环境跟预发环境不一致！',
# 	'地区3300，服务L_zj_wjkxxcx预发环境跟测试环境不一致！',
# 	'地区1100，服务G_qchdxx_zzs_yj测试环境跟预发环境不一致！',
# 	'地区1100，服务P_sb_sy_tdzzs预发环境跟测试环境不一致！',
# 	'地区3200，服务SI_L_login_request预发环境跟测试环境不一致！',
# 	'地区3200，服务P_sb_whsyjsf_ggy测试环境跟预发环境不一致！',
# 	'地区1100，服务P_sb_zzs_ybnsr测试环境跟预发、生产环境不一致！',
# 	'地区5000，服务P_sb_sy_fcs预发环境跟测试环境不一致！',
# 	'地区3200，服务P_sb_sbf测试环境跟预发环境不一致！',
# 	'地区4400，服务IN_I_getSession测试环境跟预发、生产环境不一致！',
# 	'地区5100，服务G_capture_picture生产环境跟预发环境不一致！',
# 	'地区4200，服务G_sbjkjg测试环境跟预发环境不一致！',
# 	'地区6300，服务ET_P_sb_zero预发环境跟测试环境不一致！',
# 	'地区3502，服务I_getSession生产环境跟测试环境不一致！',]
# datas = []
# for i in range(len(items)):
# 	item = items[i]
# 	pattern = r"(地区.*?环境)"
# 	result = re.search(pattern, item)
# 	data = result.group(1).replace('测试', '').replace('预发', '').replace('生产', '')
# 	datas.append(data)
# same_elements = find_same_elements(datas)
# # print(same_elements)
# result_data = []
# for key, indexs in same_elements.items():
# 	if key:
# 		for index in indexs:
# 			result_data.append(items[index])
# 			break
# print(result_data)


# lst = ['地区：北京，服务编码：P_sb_zzs_ybnsr在三个环境中配置不一致，请检查！', '地区：山西，服务编码：G_xzsbb_j3在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：P_sb_sy_yhs在三个环境中配置不一致，请检查！', '地区：陕西，服务编码：P_sb_qysds_yj在三个环境中配置不一致，请检查！', '地区：江西，服务编码：G_fpxx_ybnsr在三个环境中配置不一致，请检查！', '地区：山西，服务编码：G_wcjyzm_new在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_sbjkjg在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_qchdxx_xgmnsr在三个环境中配置不一致，请检查！', '地区：安徽，服务编码：G_sbjkjg在三个环境中配置不一致，请检查！', '地区：湖南，服务编码：G_sbjkjg在三个环境中配置不一致，请检查！', '地区：广东，服务编码：G_qchdxx_kjzz_ybqy_wzx在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：IC_I_verifySession在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IN_G_getInvoice_xx在三个环境中配置不一致，请检查！', '地区：贵州，服务编码：I_autoLogin在三个环境中配置不一致，请检查！', '地区：重庆，服务编码：P_sb_sy_fcs在三个环境中配置不一致，请检查！', '地区：厦门，服务编码：P_sb_zzs_ybnsr在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_qchdxx_kjzz_ybqy_wzx在三个环境中配置不一致，请检查！', '地区：青海，服务编码：ET_P_sb_zero在三个环境中配置不一致，请检查！', '地区：湖南，服务编码：G_nsrxx在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_xzsbb_pdf在三个环境中配置不一致，请检查！', '地区：青海，服务编码：G_qchdxx_ybnsr在三个环境中配置不一致，请检查！', '地区：广东，服务编码：IC_P_gsgsnb在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IN_G_getInvoice_jx_yrz在三个环境中配置不一致，请检查！', '地区：青海，服务编码：G_qchdxx_ghjf在三个环境中配置不一致，请检查！', '地区：广东，服务编码：G_capture_picture在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：P_jk在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_sylb_xxcj_cztdsys在三个环境中配置不一致，请检查！', '地区：厦门，服务编码：P_sb_cwbb_ybqy_yzx在三个环境中配置不一致，请检查！', '地区：广东，服务编码：P_sb_cwbb_ybqy_wzx在三个环境中配置不一致，请检查！', '地区：8100，服务编码：I_getSession在三个环境中配置不一致，请检查！', '地区：湖南，服务编码：G_sfzrdxx在三个环境中配置不一致，请检查！', '地区：宁夏，服务编码：G_nsrxx在三个环境中配置不一致，请检查！', '地区：安徽，服务编码：G_sylb_xxcj_cztdsys在三个环境中配置不一致，请检查！', '地区：北京，服务编码：P_sb_cwbb_qykjzd在三个环境中配置不一致，请检查！', '地区：厦门，服务编码：P_sb_cwbb_jrqy_yzx在三个环境中配置不一致，请检查！', '地区：青海，服务编码：I_getSession在三个环境中配置不一致，请检查！', '地区：江西，服务编码：G_sylb_xxcj_fcs在三个环境中配置不一致，请检查！', '地区：福建，服务编码：P_sb_zzs_xgmnsr在三个环境中配置不一致，请检查！', '地区：山西，服务编码：G_qchdxx_xgmnsr在三个环境中配置不一致，请检查！', '地区：青岛，服务编码：I_getSession在三个环境中配置不一致，请检查！', '地区：安徽，服务编码：G_sfzrdxx在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：IC_I_verifyAccount在三个环境中配置不一致，请检查！', '地区：北京，服务编码：G_sylb_xxcj_tdzzs1在三个环境中配置不一致，请检查！', '地区：天津，服务编码：G_xusz3在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_sylb_xxcj_cztdsys在三个环境中配置不一致，请检查！', '地区：安徽，服务编码：G_qchdxx_cxs在三个环境中配置不一致，请检查！', '地区：江西，服务编码：G_qchdxx_qysds_yj在三个环境中配置不一致，请检查！', '地区：浙江，服务编码：ET_I_login_zhejiang4phone在三个环境中配置不一致，请检查！', '地区：7100，服务编码：I_getSession在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_nsrxx在三个环境中配置不一致，请检查！', '地区：山西，服务编码：G_qchdxx_ybnsr在三个环境中配置不一致，请检查！', '地区：河南，服务编码：P_sb_szy在三个环境中配置不一致，请检查！', '地区：北京，服务编码：G_qchdxx_zzs_yj在三个环境中配置不一致，请检查！', '地区：广东，服务编码：G_waf_defense在三个环境中配置不一致，请检查！', '地区：厦门，服务编码：I_verifyAccount在三个环境中配置不一致，请检查！', '地区：安徽，服务编码：I_loginOut在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IC_I_verifyAccount在三个环境中配置不一致，请检查！', '地区：北京，服务编码：P_sb_zzs_yj在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_qchdxx_ybnsr在三个环境中配置不一致，请检查！', '地区：北京，服务编码：G_syqc_tdzzs_add在三个环境中配置不一致，请检查！', '地区：江西，服务编码：G_sylb_xxcj_cztdsys在三个环境中配置不一致，请检查！', '地区：辽宁，服务编码：G_nsrsfxx在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：S_resetPassword在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_wspz在三个环境中配置不一致，请检查！', '地区：北京，服务编码：G_qchdxx_xgmnsr在三个环境中配置不一致，请检查！', '地区：河北，服务编码：G_xusz3在三个环境中配置不一致，请检查！', '地区：青海，服务编码：P_sb_sy_yhs在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IC_G_xzgsnb在三个环境中配置不一致，请检查！', '地区：北京，服务编码：P_sb_sy_tdzzs在三个环境中配置不一致，请检查！', '地区：深圳，服务编码：SI_L_login_request在三个环境中配置不一致，请检查！', '地区：河南，服务编码：G_sylb_xxcj_cztdsys在三个环境中配置不一致，请检查！', '地区：北京，服务编码：G_qchdxx_qysds_yj在三个环境中配置不一致，请检查！', '地区：广东，服务编码：G_xzsbb_pdf在三个环境中配置不一致，请检查！', '地区：河南，服务编码：G_qchdxx_szy在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IC_I_retry在三个环境中配置不一致，请检查！', '地区：河南，服务编码：P_sb_qysds_yj_b在三个环境中配置不一致，请检查！', '地区：安徽，服务编码：G_qchdxx_ybnsr在三个环境中配置不一致，请检查！', '地区：山东，服务编码：S_gzsb在三个环境中配置不一致，请检查！', '地区：重庆，服务编码：P_sb_sy_cztdsys在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_sylb_xxcj_fcs在三个环境中配置不一致，请检查！', '地区：青海，服务编码：G_qchdxx_xgmnsr在三个环境中配置不一致，请检查！', '地区：江西，服务编码：G_sbjkjg在三个环境中配置不一致，请检查！', '地区：河南，服务编码：P_sb_cwbb_jrqy_wzx_zq在三个环境中配置不一致，请检查！', '地区：北京，服务编码：G_qchdxx_ghjf在三个环境中配置不一致，请检查！', '地区：广东，服务编码：G_sbjkjg在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：G_wcjyzm在三个环境中配置不一致，请检查！', '地区：宁夏，服务编码：G_sfzrdxx在三个环境中配置不一致，请检查！', '地区：辽宁，服务编码：I_autoLogin在三个环境中配置不一致，请检查！', '地区：浙江，服务编码：G_jmxx_ybnsr在三个环境中配置不一致，请检查！', '地区：青海，服务编码：I_verifySession在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_qchdxx_cxs在三个环境中配置不一致，请检查！', '地区：辽宁，服务编码：G_qchdxx_cxs在三个环境中配置不一致，请检查！', '地区：广东，服务编码：G_qchdxx_kjzz_qykjzd在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：P_sb_zzs_ybnsr在三个环境中配置不一致，请检查！', '地区：北京，服务编码：P_sb_sy_fcs在三个环境中配置不一致，请检查！', '地区：北京，服务编码：L_zj_wjkxxcx在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IN_G_getInvoice_jx_pt在三个环境中配置不一致，请检查！', '地区：厦门，服务编码：G_qchdxx_ybnsr在三个环境中配置不一致，请检查！', '地区：江西，服务编码：G_jmxx_ybnsr在三个环境中配置不一致，请检查！', '地区：北京，服务编码：G_sylb_xxcj_tdzzs在三个环境中配置不一致，请检查！', '地区：山东，服务编码：G_jks在三个环境中配置不一致，请检查！', '地区：北京，服务编码：G_wfwzxx在三个环境中配置不一致，请检查！', '地区：福建，服务编码：P_sb_zzs_ybnsr在三个环境中配置不一致，请检查！', '地区：河南，服务编码：G_nsxydjxx在三个环境中配置不一致，请检查！', '地区：北京，服务编码：T_xusz001在三个环境中配置不一致，请检查！', '地区：青海，服务编码：G_sylb_xxcj_yhs在三个环境中配置不一致，请检查！', '地区：青海，服务编码：G_qchdxx_qysds_yj在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：P_sb_whsyjsf_ggy在三个环境中配置不一致，请检查！', '地区：广东，服务编码：G_jks在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IC_P_gsgsnb在三个环境中配置不一致，请检查！', '地区：广东，服务编码：IN_I_getSession在三个环境中配置不一致，请检查！', '地区：山西，服务编码：ET_G_capture_picture在三个环境中配置不一致，请检查！', '地区：新疆，服务编码：G_wjsxx在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_qchdxx_xgmnsr在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：I_changeTaxpayer在三个环境中配置不一致，请检查！', '地区：江西，服务编码：G_jmxx_xgm在三个环境中配置不一致，请检查！', '地区：安徽，服务编码：G_sylb_xxcj_fcs在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_xzsbb_j3在三个环境中配置不一致，请检查！', '地区：四川，服务编码：G_capture_picture在三个环境中配置不一致，请检查！', '地区：浙江，服务编码：L_zj_wjkxxcx在三个环境中配置不一致，请检查！', '地区：江西，服务编码：G_qchdxx_xgmnsr在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：P_jk_sbf在三个环境中配置不一致，请检查！', '地区：广西，服务编码：P_sb_cwbb_ybqy_wzx在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_xzsbb在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：P_sb_zzs_xgmnsr在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IN_G_getInvoice_jx_xgm在三个环境中配置不一致，请检查！', '地区：江西，服务编码：G_qchdxx_ybnsr在三个环境中配置不一致，请检查！', '地区：北京，服务编码：P_sb_sy_tdzzs1在三个环境中配置不一致，请检查！', '地区：江西，服务编码：G_syqc_yhs_add在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_jks在三个环境中配置不一致，请检查！', '地区：青海，服务编码：P_sb_zzs_xgmnsr在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_qchdxx_cxs在三个环境中配置不一致，请检查！', '地区：安徽，服务编码：G_nsrxx在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_sylb_xxcj_tdzzs在三个环境中配置不一致，请检查！', '地区：贵州，服务编码：G_sbjkjg在三个环境中配置不一致，请检查！', '地区：河南，服务编码：P_sb_cwbb_jrqy_wzx_bx在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_sylb_xxcj_fcs在三个环境中配置不一致，请检查！', '地区：安徽，服务编码：G_qchdxx_whsyjsf_ggy在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_sfzrdxx在三个环境中配置不一致，请检查！', '地区：北京，服务编码：I_verifySession在三个环境中配置不一致，请检查！', '地区：厦门，服务编码：G_qchdxx_xgmnsr在三个环境中配置不一致，请检查！', '地区：宁夏，服务编码：I_autoLogin在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：P_sb_whsyjsf_yly在三个环境中配置不一致，请检查！', '地区：福建，服务编码：I_getSession在三个环境中配置不一致，请检查！', '地区：广东，服务编码：G_isAjnsr在三个环境中配置不一致，请检查！', '地区：青岛，服务编码：I_verifyAccount在三个环境中配置不一致，请检查！', '地区：宁夏，服务编码：G_sbjkjg在三个环境中配置不一致，请检查！', '地区：青海，服务编码：G_fpxx_ybnsr在三个环境中配置不一致，请检查！', '地区：河南，服务编码：P_sb_cwbb_jrqy_wzx_syyh在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：SI_L_login_request在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_fpxx_xgm在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_qchdxx_ybnsr在三个环境中配置不一致，请检查！', '地区：北京，服务编码：G_xzsbb_pdf在三个环境中配置不一致，请检查！', '地区：浙江，服务编码：I_verifyAccount在三个环境中配置不一致，请检查！', '地区：陕西，服务编码：P_sb_zzs_ybnsr在三个环境中配置不一致，请检查！', '地区：福建，服务编码：I_verifyAccount在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：IC_P_gsgsnb在三个环境中配置不一致，请检查！', '地区：湖南，服务编码：I_verifySession在三个环境中配置不一致，请检查！', '地区：山西，服务编码：G_qchdxx_cxs在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IC_I_verifySession在三个环境中配置不一致，请检查！', '地区：北京，服务编码：G_syqc_tdzzs1_add在三个环境中配置不一致，请检查！', '地区：福建，服务编码：G_qchdxx_kjzz_ybqy_yzx在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：P_sb_tysb_fssr在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：IC_G_xzgsnb在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IN_I_getSession在三个环境中配置不一致，请检查！', '地区：青海，服务编码：P_sb_qysds_yj在三个环境中配置不一致，请检查！', '地区：湖北，服务编码：G_sbjkjg在三个环境中配置不一致，请检查！', '地区：广东，服务编码：G_wsbxx_yq在三个环境中配置不一致，请检查！', '地区：青海，服务编码：I_verifyAccount在三个环境中配置不一致，请检查！', '地区：青海，服务编码：P_sb_ghjf在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：P_sbzf在三个环境中配置不一致，请检查！', '地区：广西，服务编码：P_sb_cwbb_ybqy_yzx在三个环境中配置不一致，请检查！', '地区：广东，服务编码：P_sbzf在三个环境中配置不一致，请检查！', '地区：浙江，服务编码：I_getSession在三个环境中配置不一致，请检查！', '地区：北京，服务编码：P_sb_sy_cztdsys在三个环境中配置不一致，请检查！', '地区：厦门，服务编码：I_getSession在三个环境中配置不一致，请检查！', '地区：青海，服务编码：G_qchdxx_kjzz_xqy在三个环境中配置不一致，请检查！', '地区：青海，服务编码：G_jmxx_ybnsr在三个环境中配置不一致，请检查！', '地区：河北，服务编码：IN_G_getInvoice_jx_wrz在三个环境中配置不一致，请检查！', '地区：江西，服务编码：P_sb_zzs_xgmnsr在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：P_sbzf_sbf在三个环境中配置不一致，请检查！', '地区：江苏，服务编码：P_sb_sbf在三个环境中配置不一致，请检查！', '地区：北京，服务编码：P_sb_sy_yhs在三个环境中配置不一致，请检查！', '地区：安徽，服务编码：P_sb_whsyjsf_ggy在三个环境中配置不一致，请检查！', '地区：江西，服务编码：P_sb_qysds_yj在三个环境中配置不一致，请检查！', '地区：广东，服务编码：G_sfzrdxx在三个环境中配置不一致，请检查！']
# def get_re_data(item, pattern):
#     res = re.search(pattern, item)
#     result = res.group(1).replace('编码：', '').replace('在', '').replace('，服务', '').replace('地区：','').replace('服务','')
#     return result
#
# for i in lst:
#     a = get_re_data(i, r"(地区：.*服务)")
#     b = get_re_data(i, r"(服务.*?在)")
#     c = get_re_data(i, r"(在三个环境中配置不一致，请检查！)")
#     print(a,b,c)



# import openpyxl
#
# # 创建一个工作簿
# workbook = openpyxl.Workbook()
#
# # 选择活动工作表
# sheet = workbook.active
#
# # 列表数据
# data = [['姓名', '年龄', '城市'],
#         ['张三', 25, '北京'],
#         ['李四', 30, '上海'],
#         ['王五', 22, '深圳']]
#
# # 将列表数据写入工作表
# for row in data:
#     sheet.append(row)
#
# # 保存工作簿到文件
# workbook.save('output.xlsx')


from datetime import datetime, timedelta

# def next_month_start(date_str):
#     date_obj = datetime.strptime(date_str, "%Y-%m-%d")
#     next_month_first_day = date_obj.replace(day=1) + timedelta(days=32)
#     next_month_first_day = next_month_first_day.replace(day=1)
#     return next_month_first_day.strftime("%Y-%m-%d")
#
# input_date = input("请输入本月的月初时间（格式：YYYY-MM-DD）：")
# output_date = next_month_start(input_date)
# print("下个月的月初时间为：", output_date)




import requests
url = 'https://alliance.yunzhanxinxi.com/manager/promotion/all-channel'
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cookie': 'PHPSESSID=96d0678c5b293f59b70e4a5e8ca5049e; _Tlogin=bb95def92bace05b964a65f8f28fbdd369f3c8110822bc39a8d2cf24fe98ca0fa%3A2%3A%7Bi%3A0%3Bs%3A7%3A%22_Tlogin%22%3Bi%3A1%3Bs%3A1%3A%22T%22%3B%7D; _uN=0ba1e294611e1742b6456f2ce49aeb7bf57298b28ffd80ae4058777c663cee37a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22_uN%22%3Bi%3A1%3Bs%3A11%3A%2218722961478%22%3B%7D; _iS=d458dabfda50ac253bf63f326b417e88342f380ae2873260bb5c12ff9c948786a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22_iS%22%3Bi%3A1%3Bs%3A1%3A%221%22%3B%7D; _sk=b424a80103e76c6430a201116c9043ce1441780b9cc27d5d89268f8b6d319b9aa%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22_sk%22%3Bi%3A1%3Bs%3A32%3A%22364e61632b0836167ff33ca8f3bccaad%22%3B%7D; _aI=b68d1535bf82b98a4bfa04757651e8b1f16fb11cd3adb319b466ea405ca64c9fa%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22_aI%22%3Bi%3A1%3Bs%3A5%3A%2240697%22%3B%7D; _uI=a90f9f00f20caa770ed1d6fd400210c25a1f9a27212b6b8eb60ed72918757072a%3A2%3A%7Bi%3A0%3Bs%3A3%3A%22_uI%22%3Bi%3A1%3Bs%3A5%3A%2241798%22%3B%7D',
    'Origin': 'https://pub.yunzhanxinxi.com',
    'Sec-Ch-Ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
}
res = requests.get(url=url, headers=headers).json()
print(res)