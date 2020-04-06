from moneyonchain.manager import ConnectionManager

connection_manager = ConnectionManager()
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))
print("Gas price: {gas_price}".format(gas_price=connection_manager.gas_price))
