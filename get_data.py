# 从表中取数据

import pandas as pd
import configparser
import time

start = time.time()
cf = configparser.ConfigParser()
cf.read('config.ini', encoding='UTF-8')

path1 = cf.get('xl_name1', 'xl')


def get_excel_data(excel_name, column_name):
    df = pd.read_excel(excel_name, keep_default_na=False)
    return [i for i in df[column_name]]


df1 = pd.read_excel(path1, keep_default_na=False)

base_id = []
sex = []
age = []
baby_age = []
in_days = []
hos_amount = []
main_diag_code = []
main_diag_name = []
other_diags_code = []
other_oper_code = []
mdc_code = []
adrg_code = []
drg_code = []
oper_code = []
error_log = []
log = []

for i in df1['BASE_ID']:
    base_id.append(i)
for i in df1['SEX']:
    sex.append(i)
for i in df1['AGE']:
    age.append(i)
for i in df1['BABY_AGE']:
    baby_age.append(i)
for i in df1['IN_DAYS']:
    in_days.append(i)
for i in df1['HOS_AMOUNT']:
    hos_amount.append(i)
for i in df1['MAIN_DIAG_CODE']:
    main_diag_code.append(i)
for i in df1['MAIN_DIAG_NAME']:
    main_diag_name.append(i)
for i in df1['OTHER_DIAGS_CODE']:
    other_diags_code.append(i)
for i in df1['OTHER_OPER_CODE']:
    other_oper_code.append(i)
for i in df1['MDC_CODE']:
    mdc_code.append(i)
for i in df1['ADRG_CODE']:
    adrg_code.append(i)
for i in df1['DRG_CODE']:
    drg_code.append(i)
for i in df1['OPER_CODE']:
    oper_code.append(i)
for i in df1['ERROR_LOG']:
    error_log.append(i)
for i in df1['LOG']:
    log.append(i)

# 分成五部分
# 9999

base_id11 = []
sex11 = []
age11 = []
baby_age11 = []
in_days11 = []
hos_amount11 = []
main_diag_code11 = []
main_diag_name11 = []
other_diags_code11 = []
other_oper_code11 = []
mdc_code11 = []
adrg_code11 = []
drg_code11 = []
oper_code11 = []
error_log11 = []
log11 = []
note11 = []

for i in range(len(base_id)):
    if drg_code[i] == '9999' and in_days[i] > 60:
        base_id11.append(base_id[i])
        sex11.append(sex[i])
        age11.append(age[i])
        baby_age11.append(baby_age[i])
        in_days11.append(in_days[i])
        hos_amount11.append(hos_amount[i])
        main_diag_code11.append(main_diag_code[i])
        main_diag_name11.append(main_diag_name[i])
        other_diags_code11.append(other_diags_code[i])
        other_oper_code11.append(other_oper_code[i])
        mdc_code11.append(mdc_code[i])
        adrg_code11.append(adrg_code[i])
        drg_code11.append(drg_code[i])
        # drg_code1.append()
        oper_code11.append(oper_code[i])
        error_log11.append(error_log[i])
        log11.append(log[i])
        note11.append('住院时长超过60天')


#
def data_9999_3(zd):
    return [zd[i] for i in range(len(base_id)) if
            (drg_code[i] == '9999' and in_days[i] != 0 and hos_amount[i] / in_days[i] < 5) or
            (drg_code[i] == '9999' and in_days[i] == 0)]


#
base_id12 = data_9999_3(base_id)
sex12 = data_9999_3(sex)
age12 = data_9999_3(age)
baby_age12 = data_9999_3(baby_age)
in_days12 = data_9999_3(in_days)
hos_amount12 = data_9999_3(hos_amount)
main_diag_code12 = data_9999_3(main_diag_code)
main_diag_name12 = data_9999_3(main_diag_name)
other_diags_code12 = data_9999_3(other_diags_code)
other_oper_code12 = data_9999_3(other_oper_code)
mdc_code12 = data_9999_3(mdc_code)
adrg_code12 = data_9999_3(adrg_code)
drg_code12 = data_9999_3(drg_code)
oper_code12 = data_9999_3(oper_code)
error_log12 = data_9999_3(error_log)
log12 = data_9999_3(log)
note12 = []

for i in range(len(base_id12)):
    note12.append('费用异常:住院费用/住院时长<5')


# # 0000

def data_0000_1(zd):
    return [zd[i] for i in range(len(base_id)) if drg_code[i] == '0000']


base_id2 = data_0000_1(base_id)
sex2 = data_0000_1(sex)
age2 = data_0000_1(age)
baby_age2 = data_0000_1(baby_age)
in_days2 = data_0000_1(in_days)
hos_amount2 = data_0000_1(hos_amount)
main_diag_code2 = data_0000_1(main_diag_code)
main_diag_name2 = data_0000_1(main_diag_name)
other_diags_code2 = data_0000_1(other_diags_code)
other_oper_code2 = data_0000_1(other_oper_code)
mdc_code2 = data_0000_1(mdc_code)
adrg_code2 = data_0000_1(adrg_code)
drg_code2 = data_0000_1(drg_code)
oper_code2 = data_0000_1(oper_code)
error_log2 = data_0000_1(error_log)
log2 = data_0000_1(log)

# # 诊断详情
path2 = cf.get('xl_name2', 'xl')
diag_detail_id = get_excel_data(path2, 'BASE_ID')
diag_detail_diag_code = get_excel_data(path2, 'SICKNESS_CODE')

def diag_detail(zd):
    return [zd[i] for i in range(len(base_id2)) for j in range(len(diag_detail_id)) if base_id2[i] == diag_detail_id[j]]

base_id21 = diag_detail(base_id2)
sex21 = diag_detail(sex2)
age21 = diag_detail(age2)
baby_age21 = diag_detail(baby_age2)
in_days21 = diag_detail(in_days2)
hos_amount21 = diag_detail(hos_amount2)
main_diag_code21 = diag_detail(main_diag_code2)
main_diag_name21 = diag_detail(main_diag_name2)
other_diags_code21 = diag_detail(other_diags_code2)
other_oper_code21 = diag_detail(other_oper_code2)
mdc_code21 = diag_detail(mdc_code2)
adrg_code21 = diag_detail(adrg_code2)
drg_code21 = diag_detail(drg_code2)
oper_code21 = diag_detail(oper_code2)
error_log21 = diag_detail(error_log2)
log21 = diag_detail(log2)
diag_code21 = []  # 在诊断详情中匹配出来的诊断编码
for i in base_id2:
    for j in range(len(diag_detail_id)):
        if i == diag_detail_id[j]:
            diag_code21.append(diag_detail_diag_code[j])
            break

# diag_code21是0000837能在诊断详情中找到的诊断编码共797 拿797去与国临2.0编码去比较
# 国临2.0
# 匹配不到国临2.0编码
base_id22 = []
sex22 = []
age22 = []
baby_age22 = []
in_days22 = []
hos_amount22 = []
main_diag_code22 = []
main_diag_name22 = []
other_diags_code22 = []
other_oper_code22 = []
mdc_code22 = []
adrg_code22 = []
drg_code22 = []
oper_code22 = []
error_log22 = []
log22 = []
diag_code22 = []  # 在诊断详情中匹配出来的诊断编码
note22 = []
# 匹配到国临2.0编码，再与映射关系进行匹配
base_id23 = []
sex23 = []
age23 = []
baby_age23 = []
in_days23 = []
hos_amount23 = []
main_diag_code23 = []
main_diag_name23 = []
other_diags_code23 = []
other_oper_code23 = []
mdc_code23 = []
adrg_code23 = []
drg_code23 = []
oper_code23 = []
error_log23 = []
log23 = []
diag23 = []
# diag_code23 = [] # 在诊断详情中匹配出来的诊断编码
note23 = []
path3 = cf.get('xl_name3', 'xl')
icd_code = get_excel_data(path3, 'ICD_CODE')
for i in range(len(diag_code21)):
    if diag_code21[i] not in icd_code:  # 匹配不到国临2.0编码
        base_id22.append(base_id21[i])
        sex22.append(sex21[i])
        age22.append(age21[i])
        baby_age22.append(baby_age21[i])
        in_days22.append(in_days21[i])
        hos_amount22.append(hos_amount21[i])
        main_diag_code22.append(main_diag_code21[i])
        main_diag_name22.append(main_diag_name21[i])
        other_diags_code22.append(other_diags_code21[i])
        other_oper_code22.append(other_oper_code21[i])
        mdc_code22.append(mdc_code21[i])
        adrg_code22.append(adrg_code21[i])
        drg_code22.append(drg_code21[i])
        oper_code22.append(oper_code21[i])
        error_log22.append(error_log21[i])
        log22.append(log21[i])
        note22.append('诊断编码非国临2.0编码')
    else:
        base_id23.append(base_id21[i])
        sex23.append(sex21[i])
        age23.append(age21[i])
        baby_age23.append(baby_age21[i])
        in_days23.append(in_days21[i])
        hos_amount23.append(hos_amount21[i])
        main_diag_code23.append(main_diag_code21[i])
        main_diag_name23.append(main_diag_name21[i])
        other_diags_code23.append(other_diags_code21[i])
        other_oper_code23.append(other_oper_code21[i])
        mdc_code23.append(mdc_code21[i])
        adrg_code23.append(adrg_code21[i])
        drg_code23.append(drg_code21[i])
        oper_code23.append(oper_code21[i])
        error_log23.append(error_log21[i])
        diag23.append(diag_code21[i])
        log23.append(log21[i])
# 742(base_id23)与2.0到CHS直接映射  （在跑结果的时候问一遍映射关系是否都已经更改好了）
# 国临2.0-CHS直接映射的国临2.0编码
path4 = cf.get('xl_name4', 'xl')
glTchs = get_excel_data(path4, 'GL2_CODE')
for i in range(len(base_id23)):
    if base_id23[i] not in glTchs:
        note23.append('无国临2.0到CHS分组方案编码映射')


#
def non_name(zd):
    return [zd[i] for i in range(len(base_id)) if drg_code[i] == '0000' and main_diag_name[i] == '']


base_id24 = non_name(base_id)
sex24 = non_name(sex)
age24 = non_name(age)
baby_age24 = non_name(baby_age)
in_days24 = non_name(in_days)
hos_amount24 = non_name(hos_amount)
main_diag_code24 = non_name(main_diag_code)
main_diag_name24 = non_name(main_diag_name)
other_diags_code24 = non_name(other_diags_code)
other_oper_code24 = non_name(other_oper_code)
mdc_code24 = non_name(mdc_code)
adrg_code24 = non_name(adrg_code)
drg_code24 = non_name(drg_code)
oper_code24 = non_name(oper_code)
error_log24 = non_name(error_log)
log24 = non_name(log)
note24 = []
for i in range(len(base_id24)):
    note24.append('无主诊断编码，主诊断名称')

# # #无mdc
base_id3 = [base_id[i] for i in range(len(base_id)) if mdc_code[i] == '']
sex3 = [sex[i] for i in range(len(base_id)) if mdc_code[i] == '']
age3 = [age[i] for i in range(len(base_id)) if mdc_code[i] == '']
baby_age3 = [baby_age[i] for i in range(len(base_id)) if mdc_code[i] == '']
in_days3 = [in_days[i] for i in range(len(base_id)) if mdc_code[i] == '']
hos_amount3 = [hos_amount[i] for i in range(len(base_id)) if mdc_code[i] == '']
main_diag_code3 = [main_diag_code[i] for i in range(len(base_id)) if mdc_code[i] == '']
main_diag_name3 = [main_diag_name[i] for i in range(len(base_id)) if mdc_code[i] == '']
other_diags_code3 = [other_diags_code[i] for i in range(len(base_id)) if mdc_code[i] == '']
other_oper_code3 = [other_oper_code[i] for i in range(len(base_id)) if mdc_code[i] == '']
mdc_code3 = [mdc_code[i] for i in range(len(base_id)) if mdc_code[i] == '']
adrg_code3 = [adrg_code[i] for i in range(len(base_id)) if mdc_code[i] == '']
drg_code3 = [drg_code[i] for i in range(len(base_id)) if mdc_code[i] == '']
oper_code3 = [oper_code[i] for i in range(len(base_id)) if mdc_code[i] == '']
error_log3 = [error_log[i] for i in range(len(base_id)) if mdc_code[i] == '']
log3 = [log[i] for i in range(len(base_id)) if mdc_code[i] == '']

# MDC与诊断编码对应表：
path6 = cf.get('xl_name6', 'xl')
mdc_code_dic = get_excel_data(path6, 'MDC_CODE')
diag_code_dic = get_excel_data(path6, 'DIAG_CODE')
# 查看没有MDC的main_diag_code 是否存在于MDC_DIC中，如果不存在，那么没有mdc
base_id31 = []
sex31 = []
age31 = []
baby_age31 = []
in_days31 = []
hos_amount31 = []
main_diag_code31 = []
main_diag_name31 = []
other_diags_code31 = []
other_oper_code31 = []
mdc_code31 = []
adrg_code31 = []
drg_code31 = []
oper_code31 = []
error_log31 = []
log31 = []
note31 = []
for i in range(len(base_id3)):
    if main_diag_code3[i] not in diag_code_dic:
        base_id31.append(base_id3[i])
        sex31.append(sex3[i])
        age31.append(age3[i])
        baby_age31.append(baby_age3[i])
        in_days31.append(in_days3[i])
        hos_amount31.append(hos_amount3[i])
        main_diag_code31.append(main_diag_code3[i])
        main_diag_name31.append(main_diag_name3[i])
        other_diags_code31.append(other_diags_code3[i])
        other_oper_code31.append(other_oper_code3[i])
        mdc_code31.append(mdc_code3[i])
        adrg_code31.append(adrg_code3[i])
        drg_code31.append(drg_code3[i])
        oper_code31.append(oper_code3[i])
        error_log31.append(error_log3[i])
        log31.append(log3[i])
        note31.append("该病例诊断编码无对应的MDC组")

# #
# # 有mdc，无adrg,无drg
base_id4 = [base_id[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
sex4 = [sex[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
age4 = [age[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
baby_age4 = [baby_age[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
in_days4 = [in_days[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
hos_amount4 = [hos_amount[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
main_diag_code4 = [main_diag_code[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
main_diag_name4 = [main_diag_name[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
other_diags_code4 = [other_diags_code[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
other_oper_code4 = [other_oper_code[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
mdc_code4 = [mdc_code[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
adrg_code4 = [adrg_code[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
drg_code4 = [drg_code[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
oper_code4 = [oper_code[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
error_log4 = [error_log[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
log4 = [log[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] == '']
note41 = []
for i in range(len(base_id4)):
    note41.append("符合入MDC的条件，但没有入到ADRG组")

# # drg_adrg_dic
path7 = cf.get('xl_name7', 'xl')
diag_code_adrg_dic = get_excel_data(path7, "DIAG_CODE")


# 有mdc,有adrg，没有drg
def non_drg(zd):
    return [zd[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code[i] != '' and drg_code[i] == '']


base_id5 = non_drg(base_id)
sex5 = non_drg(sex)
age5 = non_drg(age)
baby_age5 = non_drg(baby_age)
in_days5 = non_drg(in_days)
hos_amount5 = non_drg(hos_amount)
main_diag_code5 = non_drg(main_diag_code)
main_diag_name5 = non_drg(main_diag_name)
other_diags_code5 = non_drg(other_diags_code)
other_oper_code5 = non_drg(other_oper_code)
mdc_code5 = non_drg(mdc_code)
adrg_code5 = non_drg(adrg_code)
drg_code5 = non_drg(drg_code)
oper_code5 = non_drg(oper_code)
error_log5 = non_drg(error_log)
log5 = non_drg(log)

note51 = []
for i in range(len(base_id5)):
    note51.append('该ADRG组没有细化到DRG组')

# #
base_id_all = []
sex_all = []
age_all = []
in_days_all = []
hos_amount_all = []
main_diag_code_all = []
main_diag_name_all = []
other_diags_code_all = []
other_oper_code_all = []
mdc_code_all = []
adrg_code_all = []
drg_code_all = []
oper_code_all = []
error_log_all = []
log_all = []
note_all = []
for i in range(len(base_id11)):
    base_id_all.append(base_id11[i])
    sex_all.append(sex11[i])
    age_all.append(age11[i])
    in_days_all.append(in_days11[i])
    hos_amount_all.append(hos_amount11[i])
    main_diag_code_all.append(main_diag_code11[i])
    main_diag_name_all.append(main_diag_name11[i])
    other_diags_code_all.append(other_diags_code11[i])
    other_oper_code_all.append(other_oper_code11[i])
    mdc_code_all.append(mdc_code11[i])
    adrg_code_all.append(adrg_code11[i])
    drg_code_all.append(drg_code11[i])
    oper_code_all.append(oper_code11[i])
    error_log_all.append(error_log11[i])
    log_all.append(log11[i])
    note_all.append(note11[i])

for i in range(len(base_id12)):
    base_id_all.append(base_id12[i])
    sex_all.append(sex12[i])
    age_all.append(age12[i])
    in_days_all.append(in_days12[i])
    hos_amount_all.append(hos_amount12[i])
    main_diag_code_all.append(main_diag_code12[i])
    main_diag_name_all.append(main_diag_name12[i])
    other_diags_code_all.append(other_diags_code12[i])
    other_oper_code_all.append(other_oper_code12[i])
    mdc_code_all.append(mdc_code12[i])
    adrg_code_all.append(adrg_code12[i])
    drg_code_all.append(drg_code12[i])
    oper_code_all.append(oper_code12[i])
    error_log_all.append(error_log12[i])
    log_all.append(log12[i])
    note_all.append(note12[i])

for i in range(len(base_id22)):
    base_id_all.append(base_id22[i])
    sex_all.append(sex22[i])
    age_all.append(age22[i])
    in_days_all.append(in_days22[i])
    hos_amount_all.append(hos_amount22[i])
    main_diag_code_all.append(main_diag_code22[i])
    main_diag_name_all.append(main_diag_name22[i])
    other_diags_code_all.append(other_diags_code22[i])
    other_oper_code_all.append(other_oper_code22[i])
    mdc_code_all.append(mdc_code22[i])
    adrg_code_all.append(adrg_code22[i])
    drg_code_all.append(drg_code22[i])
    oper_code_all.append(oper_code22[i])
    error_log_all.append(error_log22[i])
    log_all.append(log22[i])
    note_all.append(note22[i])

for i in range(len(base_id23)):
    base_id_all.append(base_id23[i])
    sex_all.append(sex23[i])
    age_all.append(age23[i])
    in_days_all.append(in_days23[i])
    hos_amount_all.append(hos_amount23[i])
    main_diag_code_all.append(main_diag_code23[i])
    main_diag_name_all.append(main_diag_name23[i])
    other_diags_code_all.append(other_diags_code23[i])
    other_oper_code_all.append(other_oper_code23[i])
    mdc_code_all.append(mdc_code23[i])
    adrg_code_all.append(adrg_code23[i])
    drg_code_all.append(drg_code23[i])
    oper_code_all.append(oper_code23[i])
    error_log_all.append(error_log23[i])
    log_all.append(log23[i])
    note_all.append(note23[i])

for i in range(len(base_id24)):
    base_id_all.append(base_id24[i])
    sex_all.append(sex24[i])
    age_all.append(age24[i])
    in_days_all.append(in_days24[i])
    hos_amount_all.append(hos_amount24[i])
    main_diag_code_all.append(main_diag_code24[i])
    main_diag_name_all.append(main_diag_name24[i])
    other_diags_code_all.append(other_diags_code24[i])
    other_oper_code_all.append(other_oper_code24[i])
    mdc_code_all.append(mdc_code24[i])
    adrg_code_all.append(adrg_code24[i])
    drg_code_all.append(drg_code24[i])
    oper_code_all.append(oper_code24[i])
    error_log_all.append(error_log24[i])
    log_all.append(log24[i])
    note_all.append(note24[i])

for i in range(len(base_id31)):
    base_id_all.append(base_id31[i])
    sex_all.append(sex31[i])
    age_all.append(age31[i])
    in_days_all.append(in_days31[i])
    hos_amount_all.append(hos_amount31[i])
    main_diag_code_all.append(main_diag_code31[i])
    main_diag_name_all.append(main_diag_name31[i])
    other_diags_code_all.append(other_diags_code31[i])
    other_oper_code_all.append(other_oper_code31[i])
    mdc_code_all.append(mdc_code31[i])
    adrg_code_all.append(adrg_code31[i])
    drg_code_all.append(drg_code31[i])
    oper_code_all.append(oper_code31[i])
    error_log_all.append(error_log31[i])
    log_all.append(log31[i])
    note_all.append(note31[i])

for i in range(len(base_id4)):
    base_id_all.append(base_id4[i])
    sex_all.append(sex4[i])
    age_all.append(age4[i])
    in_days_all.append(in_days4[i])
    hos_amount_all.append(hos_amount4[i])
    main_diag_code_all.append(main_diag_code4[i])
    main_diag_name_all.append(main_diag_name4[i])
    other_diags_code_all.append(other_diags_code4[i])
    other_oper_code_all.append(other_oper_code4[i])
    mdc_code_all.append(mdc_code4[i])
    adrg_code_all.append(adrg_code4[i])
    drg_code_all.append(drg_code4[i])
    oper_code_all.append(oper_code4[i])
    error_log_all.append(error_log4[i])
    log_all.append(log4[i])
    note_all.append(note41[i])

for i in range(len(base_id5)):
    base_id_all.append(base_id5[i])
    sex_all.append(sex5[i])
    age_all.append(age5[i])
    in_days_all.append(in_days5[i])
    hos_amount_all.append(hos_amount5[i])
    main_diag_code_all.append(main_diag_code5[i])
    main_diag_name_all.append(main_diag_name5[i])
    other_diags_code_all.append(other_diags_code5[i])
    other_oper_code_all.append(other_oper_code5[i])
    mdc_code_all.append(mdc_code5[i])
    adrg_code_all.append(adrg_code5[i])
    drg_code_all.append(drg_code5[i])
    oper_code_all.append(oper_code5[i])
    error_log_all.append(error_log5[i])
    log_all.append(log5[i])
    note_all.append(note51[i])

dic = {}
dic['base_id'] = base_id_all
dic['sex'] = sex_all
dic['age'] = age_all
dic['in_days'] = in_days_all
dic['hos_amount'] = hos_amount_all
dic['main_diag_code'] = main_diag_code_all
dic['main_diag_name'] = main_diag_name_all
dic['other_diags_code'] = other_diags_code_all
dic['other_oper_code'] = other_oper_code_all
dic['mdc_code'] = mdc_code_all
dic['adrg_code'] = adrg_code_all
dic['drg_code'] = drg_code_all
dic['oper_code'] = oper_code_all
dic['error_log'] = error_log_all
dic['log'] = log_all
dic['note'] = note_all
df4 = pd.DataFrame(dic)
df4.to_excel('test2.xlsx')
end = time.time()
print((end - start) / 60, '分')
