data_dir=''
origin_data=''
pinghua_data_dir=''
wentai_data_dir=''

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

tar_names=['AM17CCS02A102_AV']
