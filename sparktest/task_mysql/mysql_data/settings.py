# -*- coding: utf-8 -*-
ip="192.168.1.245"
port = 3307
mysql_user="admin"
mysql_passwd="admin"
database="test"
# start_time =1462032001
# end_time =  1462118398
tablename = "sfhd_test32"
tablename_2 = "test_upgrade_2"
timespan = 600
split_file_number = 0
columns =('time', 'B06LT02AA_AV', 'B06M07ABIT_AV', 'B03M01BIT_AV', 'B03CV03EZT_AV', 'B03CV04EZT_AV', 'B03CV04BZT_AV', 'B06CV01AZT_AV', 'AMB05CQ04AM_AV', 'B06M07BAIT_AV', 'AMB26AGCI002M_AV', 'AMB06FT05A_AV', 'AM17CCS06A701_AV', 'AMB01FT01A_AV', 'B03PDT15A_AV', 'B03CV04CZT_AV', 'B03M02EAFT_AV', 'B03M01FIT_AV', 'AMB05CQ04BM_AV', 'AMB03FT02EM_AV', 'AM23SIG0201_AV', 'AM17CCS02A105_AV', 'B03PT02DA_AV', 'B03M02AAFT_AV', 'B26DEHI004_AV', 'B06M07BBIT_AV', 'B03M01AIT_AV', 'AMB03FT02BM_AV', 'AMT31PT03M_AV', 'B06M02AIT_AV', 'B03CV03DZT_AV', 'B03M02CAFT_AV', 'B06LT02BB_AV', 'B03M05BIT_AV', 'AMB03FT02DM_AV', 'AMT31PT01M_AV', 'B03M05CIT_AV', 'B06M01BIT_AV', 'AMB01FT01C_AV', 'AM17CCS06A504_AV', 'AMB05CQ04AV_AV', 'B03PDT15D_AV', 'AMB03FT02AM_AV', 'B07ST03BA_AV', 'B07FT10BO_AV', 'B03M02FAFT_AV', 'AMB01FT01M_AV', 'B06LT02AB_AV', 'B06LT02BA_AV', 'B03CV04AZT_AV', 'B03CV03CZT_AV', 'B03M05FIT_AV', 'AMB02PT01B_AV', 'B03CV04DZT_AV', 'B03PDT15F_AV', 'B03M02BAFT_AV', 'B07FT10AAO_AV', 'B06M07AAIT_AV', 'AMB02PT01A_AV', 'B03PT02FA_AV', 'E91GE01HZ_AV', 'B06CV02AZT_AV', 'AM17CCS03A101_AV', 'B05PT01A_AV', 'AM17CCS06A506_AV', 'B03PDT15B_AV', 'AMB05CQ05AM_AV', 'AM24MCS0203_AV', 'B07CV01BZT_AV', 'E91GE01RP_AV', 'B06CV01BZT_AV', 'B06CV02BZT_AV', 'B03M02DAFT_AV', 'B03PT02BA_AV', 'B03CV03AZT_AV', 'AMB05PT01PV_AV', 'B03CV03FZT_AV', 'B03PT02AA_AV', 'B03CV03BZT_AV', 'B03M01CIT_AV', 'AM17CCS02A102_AV', 'B03PT02CA_AV', 'AMB02PT03A_AV', 'B03PT02EA_AV', 'AMB05PT01BIA_AV', 'AMB03FT02FM_AV', 'B03M05AIT_AV', 'AMB03FT02CM_AV', 'B03M01EIT_AV', 'B03M05EIT_AV', 'AMB03TE04EM_AV', 'B03M01DIT_AV', 'B07ST03AA_AV', 'B03PDT15E_AV', 'B07CV01AZT_AV', 'T39ST01A_AV', 'B03PDT15C_AV', 'AMB02PT23AM_AV', 'B03CV04FZT_AV', 'AMB11PT01M_AV', 'T31PT04B_AV', 'B06M01AIT_AV', 'AMB01FT01B_AV', 'AMB01PT31M_AV', 'B03M05DIT_AV', 'B06M02BIT_AV', 'B03TE02CA_AV', 'AMB03TE04AM_AV', 'B07TE11BA_AV', 'B03TE02DA_AV', 'AM23SIG0202_AV', 'B03TE02AA_AV', 'B07TE01AA_AV', 'T58TE01A_AV', 'AM23SIG0205_AV', 'AM23SIG0204_AV', 'AM24SIG0305_AV', 'B03TE02BA_AV', 'AM24SIG0309_AV', 'AM24SIG0303_AV', 'AM24SIG0307_AV', 'AMB03TE04FM_AV', 'B06TE10AA_AV', 'AMB03TE04DM_AV', 'AMSIG0301_AV', 'AMB01TE01M_AV', 'B03TE02EA_AV', 'AMB03TE04BM_AV', 'B06TE10BA_AV', 'AM23SIG0203_AV', 'B03TE02FA_AV', 'AM24SIG0304_AV', 'B07TE11AA_AV', 'AMB03TE04CM_AV', 'AM24SIG0306_AV', 'AMT37TE05M_AV', 'AM23SIG0206_AV')


# _*_ coding:utf-8 _*_
__author__ = 'llj'
#-----io相关---------------
data_dir=''
models_dir=''
power_sample_dir=''
fit_summary_file = ''

#-----columns相关---------
mmj_colums={
    "tar_wind_quality":[],
    "tar_wind_temp":[],
    "tar_outwind_temp":[],
    "real_wind_quelity":[],
    "real_wind_temp":[],
    "real_outwind":[],
    "real_coldwind":[],
    "real_hotwind":[],
    "real_motor_current":[],
    "real_dynmic_current":[],
}
boiler_columns = {
    "tar_power":['AM17CCS02A102_AV'],
    "real_power":['B26DEHI004_AV'],
    "real_gross_incoal":['AM17CCS06A701_AV'],
    "real_mainsteam_press":['AMB02PT03A_AV'],
    "real_reheatsteam_press":['T31PT04B_AV'],
    "real_coldsteam_press":['AMB02PT23AM_AV'],
    "real_boiler_water_flow":['AMB01FT01M_AV'],
    "real_boiler_water_temp":['AMB01TE01M_AV'],
    "read_boiler_water_press":['AMB01PT31M_AV'],
    "real_boiler_induced_wind":['B07FT10AAO_AV','B07FT10BO_AV'],
    "real_boiler_gross_wind":['AMB06FT05A_AV'],
    "real_boiler_outsmoke_oxyrate":[ 'AMB05CQ05AM_AV','AMB05CQ04BM_AV'],
    "real_oxygen":['AMB05CQ05AM_AV'],
    "real_deaerator_temp":['T58TE01A_AV'],
    "real_manual_oxygen":['AMB05CQ04AV_AV'],
    "real_superheat":['AMSIG0301_AV'],
    "real_gross_fuel":['AM17CCS06A504_AV'],
    "real_blower":['B06LT02BA_AV','B06LT02BB_AV','B06LT02AA_AV','B06LT02AB_AV',],
}
#----------子模型样本相关-----------------------------
#是否只对每个稳态单独建模
only_wentai = ''
flag_columns = ['real_power']
skip_columns = ['tar_power']
delay_pos = -11
delay_interval = 5
pinghua_file_prename='pinghua'
sample_file_prename='power_sample'
tar_names=['AM17CCS02A102_AV']
