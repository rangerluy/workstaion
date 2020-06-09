# 从表中取数据
s = """
BASE_ID
SEX	
AGE	
BABY_AGE	
IN_DAYS	
HOS_AMOUNT	
MAIN_DIAG_CODE	
MAIN_DIAG_NAME	
OTHER_DIAGS_CODE	
OTHER_OPER_CODE	
MDC_CODE	
ADRG_CODE	
DRG_CODE	
OPER_CODE	
ERROR_LOG	
LOG
"""
import pandas as pd
path = '未入组.xlsx'

def get_excel_data(excel_name, column_name):
    df = pd.read_excel(excel_name,keep_default_na=False)
    return [i for i in df[column_name]]

base_id =  get_excel_data(path,'BASE_ID')

sex = get_excel_data(path,'SEX')
age = get_excel_data(path,'AGE')
baby_age = get_excel_data(path,'BABY_AGE')
in_days = get_excel_data(path,'IN_DAYS')
hos_amout = get_excel_data(path,'HOS_AMOUNT')
main_diag_code = get_excel_data(path,'MAIN_DIAG_CODE')
main_diag_name = get_excel_data(path,'MAIN_DIAG_NAME')
other_diags_code = get_excel_data(path,'OTHER_DIAGS_CODE')
other_oper_code = get_excel_data(path,'OTHER_OPER_CODE')
mdc_code = get_excel_data(path,'MDC_CODE')
adrg_code = get_excel_data(path,'ADRG_CODE')
drg_code = get_excel_data(path,'DRG_CODE')
oper_code = get_excel_data(path,'OPER_CODE')
error_log = get_excel_data(path,'ERROR_LOG')
log = get_excel_data(path,'LOG')


#分成五部分
#9999
base_id11 = [base_id[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
sex11 = [sex[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
age11 = [age[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
baby_age11 = [baby_age[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
in_days11 = [in_days[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
hos_amout11 = [hos_amout[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
main_diag_code11 = [main_diag_code[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
main_diag_name11 = [main_diag_name[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
other_diags_code11 = [other_diags_code[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
other_oper_code11 = [other_oper_code[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
mdc_code11 = [mdc_code[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
adrg_code11 = [adrg_code[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
drg_code11 = [drg_code[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
oper_code11 = [oper_code[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
error_log11 = [error_log[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
log11 = [log[i] for i in range(len(base_id)) if drg_code[i] == '9999' and in_days[i]>60]
note11 = []
for i in range(len(base_id11)):
    note11.append('住院时长超过60天')
base_id12 = [base_id[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0) ]
sex12 = [sex[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
age12 = [age[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
baby_age12 = [baby_age[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
in_days12 = [in_days[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
hos_amout12 = [hos_amout[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
main_diag_code12 = [main_diag_code[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
main_diag_name12 = [main_diag_name[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
other_diags_code12 = [other_diags_code[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
other_oper_code12 = [other_oper_code[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
mdc_code12 = [mdc_code[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
adrg_code12 = [adrg_code[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
drg_code12 = [drg_code[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
oper_code12 = [oper_code[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
error_log12 = [error_log[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
log12 = [log[i] for i in range(len(base_id)) if (drg_code[i] == '9999' and in_days[i]!=0 and hos_amout[i]/in_days[i]<5) or (drg_code[i] == '9999' and in_days == 0)]
for  i in range(len(base_id12)):
    note11.append("费用异常：住院费用/住院时长<5")



#0000
base_id2 = [base_id[i] for i in range(len(base_id)) if drg_code[i] == '0000']
sex2 = [sex[i] for i in range(len(base_id)) if drg_code[i] == '0000']
age2 = [age[i] for i in range(len(base_id)) if drg_code[i] == '0000']
baby_age2 = [baby_age[i] for i in range(len(base_id)) if drg_code[i] == '0000']
in_days2 = [in_days[i] for i in range(len(base_id)) if drg_code[i] == '0000']
hos_amout2 = [hos_amout[i] for i in range(len(base_id)) if drg_code[i] == '0000']
main_diag_code2 = [main_diag_code[i] for i in range(len(base_id)) if drg_code[i] == '0000']
main_diag_name2 = [main_diag_name[i] for i in range(len(base_id)) if drg_code[i] == '0000']
other_diags_code2 = [other_diags_code[i] for i in range(len(base_id)) if drg_code[i] == '0000']
other_oper_code2 = [other_oper_code[i] for i in range(len(base_id)) if drg_code[i] == '0000']
mdc_code2 = [mdc_code[i] for i in range(len(base_id)) if drg_code[i] == '0000']
adrg_code2 = [adrg_code[i] for i in range(len(base_id)) if drg_code[i] == '0000']
drg_code2 = [drg_code[i] for i in range(len(base_id)) if drg_code[i] == '0000']
oper_code2 = [oper_code[i] for i in range(len(base_id)) if drg_code[i] == '0000']
error_log2 = [error_log[i] for i in range(len(base_id)) if drg_code[i] == '0000']
log2 = [log[i] for i in range(len(base_id)) if drg_code[i] == '0000']

#无mdc
base_id3 = [base_id[i] for i in range(len(base_id)) if mdc_code[i] == '']
sex3 = [sex[i] for i in range(len(base_id)) if mdc_code[i] == '']
age3 = [age[i] for i in range(len(base_id)) if mdc_code[i] == '']
baby_age3 = [baby_age[i] for i in range(len(base_id)) if mdc_code[i] == '']
in_days3 = [in_days[i] for i in range(len(base_id)) if mdc_code[i] == '']
hos_amout3 = [hos_amout[i] for i in range(len(base_id)) if mdc_code[i] == '']
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

# 有mdc，无adrg,无drg
base_id4 = [base_id[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code == '']
sex4 = [sex[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
age4 = [age[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
baby_age4 = [baby_age[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
in_days4 = [in_days[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
hos_amout4 = [hos_amout[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
main_diag_code4 = [main_diag_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
main_diag_name4 = [main_diag_name[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
other_diags_code4 = [other_diags_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
other_oper_code4 = [other_oper_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
mdc_code4 = [mdc_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
adrg_code4 = [adrg_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
drg_code4 = [drg_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
oper_code4 = [oper_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
error_log4 = [error_log[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
log4 = [log[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code == '']
# 有mdc  有adrg 无drg

base_id5 = [base_id[i] for i in range(len(base_id)) if mdc_code[i] != '' and adrg_code != '' and drg_code == '']
sex5 = [sex[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
age5 = [age[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
baby_age5 = [baby_age[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
in_days5 = [in_days[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
hos_amout5 = [hos_amout[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
main_diag_code5 = [main_diag_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
main_diag_name5 = [main_diag_name[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
other_diags_code5 = [other_diags_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
other_oper_code5 = [other_oper_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
mdc_code5 = [mdc_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
adrg_code5 = [adrg_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
drg_code5 = [drg_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
oper_code5 = [oper_code[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
error_log5 = [error_log[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']
log5 = [log[i] for i in range(len(base_id)) if mdc_code[i] == '' and adrg_code != '' and drg_code == '']