from moneyonchain.networks import network_manager
from moneyonchain.rdoc import RDOCMoCState


connection_network = 'rskTestnetPublic'
config_network = 'rdocTestnetAlpha'


# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

moc_state = RDOCMoCState(network_manager).from_abi()

print("State: {0}".format(moc_state.state()))

print("Day Block Span: {0}".format(moc_state.day_block_span()))
print("Smoothing Factor: {0}".format(moc_state.smoothing_factor()))
print("RIF in system: {0}".format(moc_state.rbtc_in_system()))
print("Cobj: {0}".format(moc_state.cobj()))
print("Cobj X2: {0}".format(moc_state.cobj_X2()))
#print("Max mint riskpro avail: {0}".format(moc_state.max_mint_bpro_available()))
#print("Max mint riskpro: {0}".format(moc_state.max_mint_bpro()))
print("Absolute max doc: {0}".format(moc_state.absolute_max_doc()))
print("Max RISKPROx: {0}".format(moc_state.max_bprox(str.encode('X2'))))
#print("Max RISKPROx btc value: {0}".format(moc_state.max_bprox_btc_value()))
print("Absolute max bpro: {0}".format(moc_state.absolute_max_bpro()))
print("Free doc: {0}".format(moc_state.free_doc()))
print("Leverage: {0}".format(moc_state.leverage(str.encode('X2'))))


print("RIF Price in USD: {0}".format(moc_state.bitcoin_price()))
print("RIF Moving Average in USD: {0}".format(moc_state.bitcoin_moving_average()))
print("Days to settlement: {0}".format(moc_state.days_to_settlement()))
print("Global Coverage: {0}".format(moc_state.global_coverage()))
print("RIFP Total Supply: {0}".format(moc_state.bitpro_total_supply()))
print("RDOC Total Supply: {0}".format(moc_state.doc_total_supply()))
print("Implementation: {0}".format(moc_state.implementation()))

print("Max RISKPRO dicount {0}".format(moc_state.max_bpro_with_discount()))
print("RiskPro discount price {0}".format(moc_state.bpro_discount_price()))
print("RIFP Discount: {0}".format(moc_state.bpro_discount_rate()))
print("RiskPro price {0}".format(moc_state.bpro_price()))
print("RIFP Tec Price: {0}".format(moc_state.bpro_tec_price()))

print("RISKPROX Price: {0}".format(moc_state.bprox_price()))
print("RISKPROX Tec Price: {0}".format(moc_state.btc2x_tec_price()))

print("Inrate bag: {0}".format(moc_state.get_inrate_bag(str.encode('X2'))))


print("X2")
print("Bucket NBTC: {0}".format(moc_state.bucket_nbtc(str.encode('X2'))))
print("Bucket NDOC: {0}".format(moc_state.bucket_ndoc(str.encode('X2'))))
print("Bucket NBPRO: {0}".format(moc_state.bucket_nbpro(str.encode('X2'))))
print("Coverage RISKPROX: {0}".format(moc_state.coverage(str.encode('X2'))))

print("C0")
print("Bucket NBTC: {0}".format(moc_state.bucket_nbtc(str.encode('C0'))))
print("Bucket NDOC: {0}".format(moc_state.bucket_ndoc(str.encode('C0'))))
print("Bucket NBPRO: {0}".format(moc_state.bucket_nbpro(str.encode('C0'))))
print("Coverage RISKPROX: {0}".format(moc_state.coverage(str.encode('C0'))))


print("Is liquidation: {0}".format(moc_state.is_liquidation()))
print("Is calculate ema: {0}".format(moc_state.is_calculate_ema()))
print("Price provider: {0}".format(moc_state.price_provider()))

print("Liquidation price: {0}".format(moc_state.liquidation_price()))

print("Global locked reserve: {0}".format(moc_state.global_locked_reserve_tokens()))
print("Reserves remainder: {0}".format(moc_state.reserves_remainder()))
print("Liq: {0}".format(moc_state.liq()))

print("Current_abundance_ratio: {0}".format(moc_state.current_abundance_ratio()))  #block_identifier=1233780
print("abundance_ratio: {0}".format(moc_state.abundance_ratio(int(2.242807702008664948*10*18)))) #, block_identifier=1233780


print("Bucket NDOC: {0}".format(moc_state.bucket_ndoc(str.encode('C0'), formatted=False)))
print("RDOC Totaly: {0}".format(moc_state.doc_total_supply(formatted=False)))
print("Bucket NBTC: {0}".format(moc_state.bucket_nbtc(str.encode('C0'), formatted=False)))
print("RIF in sysm: {0}".format(moc_state.rbtc_in_system(formatted=False)))


# finally disconnect from network
network_manager.disconnect()