from decimal import Decimal

from moneyonchain.networks import network_manager
from moneyonchain.moc import MoCInrate, MoCState

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


connection_network = 'rskTestnetPublic'
config_network = 'mocTestnetAlpha'

log.info('Connecting enviroment {0}...'.format(config_network))

# Connect to network
network_manager.connect(connection_network=connection_network, config_network=config_network)

moc_inrate = MoCInrate(network_manager).from_abi()
moc_state = MoCState(network_manager).from_abi()

print("Bitpro rate: {0}".format(moc_inrate.bitpro_rate()))

print("DOC Freestable reedeem")
print("=======================")
info = moc_inrate.doc_inrate()
print(info)

info = moc_inrate.spot_inrate()
print("Spot Inrate: {0}".format(info))

info = moc_state.current_abundance_ratio()
print("Current Abundance ratio: {0}".format(info))

print("Interest of reedeeming 1000 DOC")
interest_no_days = moc_inrate.doc_inrate_avg(1000)
print(interest_no_days)

for day_to_sett in reversed(range(0, 30)):
    print("Days to settlement: {0} Interest: {1}".format(day_to_sett, interest_no_days * day_to_sett))

print("BTCX Inrate")
print("===========")
info = moc_inrate.btcx_inrate()
print(info)


info = dict()
info['btcx'] = dict()
info['btcx']['redeem'] = dict()
info['btcx']['mint'] = dict()
info['btcx']['mint']['amount'] = Decimal(0.001)
info['btcx']['redeem']['amount'] = Decimal(0.001)

print("BTCX Mint Amount: {0:.6f}".format(info['btcx']['mint']['amount']))
print("BTCX Redeem Amount: {0:.6f}".format(info['btcx']['redeem']['amount']))

print("BTCX On Mint (Inrate Avg...)")
interest_no_days = moc_inrate.btc2x_inrate_avg(info['btcx']['mint']['amount'], on_minting=True)
for day_to_sett in reversed(range(0, 30)):
    interest_perc = interest_no_days * day_to_sett * 100
    interest_amount = interest_perc * info['btcx']['mint']['amount'] / 100
    print("... Days to settl: {0} Int. Perc: {1:.2f} % Int Amount. {2:.7f}".format(day_to_sett, interest_perc,
                                                                                   interest_amount))
# Mint BTCX
info['btcx']['mint']['interest'] = Decimal(moc_inrate.calc_mint_interest_value(info['btcx']['mint']['amount']))
info['btcx']['mint']['percent'] = info['btcx']['mint']['interest'] * 100 / info['btcx']['mint']['amount']

print("BTCX Mint Interest: {0:.7f}".format(info['btcx']['mint']['interest']))
print("BTCX Mint Interest perc: {0:.2f} %".format(info['btcx']['mint']['percent']))


print("BTCX On redeem (Inrate Avg...)")
interest_no_days = Decimal(moc_inrate.btc2x_inrate_avg(info['btcx']['redeem']['amount'], on_minting=False))
for day_to_sett in reversed(range(0, 30)):
    interest_perc = interest_no_days * day_to_sett * 100
    interest_amount = interest_perc * info['btcx']['redeem']['amount'] / 100
    print("... Days to settl: {0} Int. Perc: {1:.2f} % Int Amount. {2:.7f}".format(day_to_sett, interest_perc,
                                                                                   interest_amount))

# Redeem BTCX
info['btcx']['redeem']['interest'] = Decimal(moc_inrate.calc_final_redeem_interest(info['btcx']['redeem']['amount']))
info['btcx']['redeem']['percent'] = info['btcx']['redeem']['interest'] * 100 / info['btcx']['redeem']['amount']

print("BTCX Redeem Interest: {0:.7f}".format(info['btcx']['redeem']['interest']))
print("BTCX Redeem Interest perc: {0:.2f} %".format(info['btcx']['redeem']['percent']))

# finally disconnect from network
network_manager.disconnect()
