from moneyonchain.networks import network_manager
from moneyonchain.moc import MoCInrate

import logging
import logging.config

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='logs/inrate.log',
                    filemode='a')

# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
console.setFormatter(formatter)

log = logging.getLogger()
log.addHandler(console)


connection_network = 'rskTesnetPublic'
config_network = 'mocTestnetAlpha'

log.info('Connecting enviroment {0}...'.format(config_network))

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

moc_inrate = MoCInrate(network_manager).from_abi()

print("Bitpro rate: {0}".format(moc_inrate.bitpro_rate()))

print("DOC Freestable reedeem")
print("=======================")
info = moc_inrate.doc_inrate()
print(info)

print("Interest of reedeeming 1000 DOC")
interest_no_days = moc_inrate.doc_inrate_avg(0.020849)

for day_to_sett in reversed(range(0, 30)):
    print("Days to settlement: {0} Interest: {1}".format(day_to_sett, interest_no_days * day_to_sett))

print("BTCX Inrate")
print("===========")
info = moc_inrate.btcx_inrate()
print(info)

print("Interest of MINT 1.0 BTCX")
interest_no_days = moc_inrate.btc2x_inrate_avg(1.0, on_minting=True)

for day_to_sett in reversed(range(0, 30)):
    print("Days to settlement: {0} Interest: {1}".format(day_to_sett, interest_no_days * day_to_sett))

print("Interest of REEDEEM 1.0 BTCX")
interest_no_days = moc_inrate.btc2x_inrate_avg(1.0, on_minting=False)

for day_to_sett in reversed(range(0, 30)):
    print("Days to settlement: {0} Interest: {1}".format(day_to_sett, interest_no_days * day_to_sett))

info = moc_inrate.calc_mint_interest_value(1.0)
print(info)

# finally disconnect from network
network_manager.disconnect()
