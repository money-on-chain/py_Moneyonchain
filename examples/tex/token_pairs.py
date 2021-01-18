from moneyonchain.manager import ConnectionManager
from moneyonchain.dex import MoCDecentralizedExchange


network = 'dexMainnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCDecentralizedExchange")
dex = MoCDecentralizedExchange(connection_manager)
print(dex.token_pairs())

"""

[
['0xe700691dA7b9851F2F35f8b8182c69c53CcaD9Db', '0x967F8799aF07dF1534d48A95a5C9FEBE92c53AE0'], 
['0xe700691dA7b9851F2F35f8b8182c69c53CcaD9Db', '0x2d919F19D4892381D58edeBeca66D5642Cef1a1f'], 
['0xe700691dA7b9851F2F35f8b8182c69c53CcaD9Db', '0x440CD83C160De5C96Ddb20246815eA44C7aBBCa8'], 
['0x967F8799aF07dF1534d48A95a5C9FEBE92c53AE0', '0x440CD83C160De5C96Ddb20246815eA44C7aBBCa8'], 
['0xe700691dA7b9851F2F35f8b8182c69c53CcaD9Db', '0x2AcC95758f8b5F583470ba265EB685a8F45fC9D5'], 
['0x2d919F19D4892381D58edeBeca66D5642Cef1a1f', '0xf4d27c56595Ed59B66cC7F03CFF5193e4bd74a61'], 
['0x2AcC95758f8b5F583470ba265EB685a8F45fC9D5', '0xf4d27c56595Ed59B66cC7F03CFF5193e4bd74a61']
]




"""