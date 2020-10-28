from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCState


network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCState")
moc_state = MoCState(connection_manager)
print("Bitcoin Price in USD: {0}".format(moc_state.bitcoin_price()))
print("Bitcoin Moving Average in USD: {0}".format(moc_state.bitcoin_moving_average()))
print("Days to settlement: {0}".format(moc_state.days_to_settlement()))
print("Global Coverage: {0}".format(moc_state.global_coverage()))
print("Bitpro Total Supply: {0}".format(moc_state.bitpro_total_supply()))
print("DOC Total Supply: {0}".format(moc_state.doc_total_supply()))
print("Implementation: {0}".format(moc_state.implementation()))
print("BPro Discount: {0}".format(moc_state.bpro_discount_rate()))
print("BPro Tec Price: {0}".format(moc_state.bpro_tec_price()))
print("MoC Price in USD: {0}".format(moc_state.moc_price()))



"""
Connecting to mocMainnet2...
Connected: True
Connecting to MoCState
Bitcoin Price in USD: 9192.25
Bitcoin Moving Average in USD: 8691.773665743441728397

Connecting to mocTestnet...
Connected: True
Connecting to MoCState
Bitcoin Price in USD: 9194.28
Bitcoin Moving Average in USD: 8881.279549746037722543
"""

