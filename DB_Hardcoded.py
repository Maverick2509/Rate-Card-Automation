tier_glid_mapping = {
'Tier1':'1000001',
'Tier2':'1000002',
'Tier3':'1000003',
'Tier4':'1000004',
'Tier5':'1000005',
'Tier6':'1000006',
'Tier7':'1000007',
'Tier8':'1000008',
'Tier9':'1000009',
'Tier10':'1000010',
'Tier11':'1000011',
'Tier12':'1000012',
'Tier13':'1000013',
'Tier14':'1000014',
'Tier15':'1000015',
'Tier16':'1000016',
'Tier17':'1000017',
'Tier18':'1000018',
'Tier19':'1000019',
'Tier20':'1000020'
}

currencyName_currencyCode_mapping = {
'CAD':'124',
'CNY':'156',
'CZK':'203',
'DKK':'208',
'HKD':'344',
'INR':'356',
'AUD':'36',
'IDR':'360',
'ILS':'376',
'JPY':'392',
'KRW':'410',
'MYR':'458',
'NZD':'554',
'NOK':'578',
'RUB':'643',
'SGD':'702',
'ZAR':'710',
'SEK':'752',
'CHF':'756',
'THB':'764',
'TRY':'792',
'GBP':'826',
'USD':'840',
'TWD':'901',
'EUR':'978',
'PLN':'985'
}

evenName_atributeCode_mapping = {
'/event/billing/product/fee/cycle/cycle_forward_monthly/tofino/storage':'StoragePerformance',
'/event/billing/product/fee/cycle/cycle_forward_monthly/tofino/network':'OFFAddiMul',
'/event/billing/product/fee/cycle/cycle_forward_monthly/tofino/vpn':'OFFVPNSer',
'/event/billing/product/fee/cycle/cycle_forward_monthly/tofino/connector':'OFFDataCen',
'/event/billing/product/fee/cycle/cycle_forward_monthly/tofino/host':'OFFHostType',
'/event/billing/product/fee/cycle/cycle_forward_monthly/tofino/vm':'OFFVMType'
}

newDict = {
'StoragePerformance': 'EVENT.PIN_FLD_INHERITED_INFO.DELL_FLD_STORAGE_PERFORMANCE',
'OFFAddiMul': 'EVENT.PIN_FLD_INHERITED_INFO.DELL_FLD_OFF_ADDI_MULTI_CLOUD',
'OFFVPNSer' : 'EVENT.PIN_FLD_INHERITED_INFO.DELL_FLD_OFF_VPN_SERVICES',
'OFFDataCen': 'EVENT.PIN_FLD_INHERITED_INFO.DELL_FLD_OFF_DATA_CENTER',
'OFFHostType': 'EVENT.PIN_FLD_INHERITED_INFO.DELL_FLD_OFF_HOST_TYPE',
'OFFVMType': 'EVENT.PIN_FLD_INHERITED_INFO.DELL_FLD_OFF_VM_TYPE'

}