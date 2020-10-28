"""
Get BPRO Price
Get Bitcoin Price
Get BTCX Price
"""

from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoC

network = 'mocMainnet2'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

contract = MoC(connection_manager)
print("Bitcoin price in usd: {0}".format(contract.bitcoin_price()))
print("BPRO price in usd: {0}".format(contract.bpro_price()))
print("BTC2X price in usd: {0}".format(contract.btc2x_tec_price() * contract.bitcoin_price()))
print("MoC price in usd: {0}".format(contract.moc_price()))
