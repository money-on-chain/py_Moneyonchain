from moneyonchain.manager import ConnectionManager
from moneyonchain.moc import MoCInrate


network = 'mocTestnetAlpha'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

print("Connecting to MoCInrate")
moc_inrate = MoCInrate(connection_manager)

"""
Commissions for different transaction types
"""
tx_type_mint_bpro_fees_rbtc = moc_inrate.tx_type_mint_bpro_fees_rbtc()
tx_type_redeem_bpro_fees_rbtc = moc_inrate.tx_type_redeem_bpro_fees_rbtc()
tx_type_mint_doc_fees_rbtc = moc_inrate.tx_type_mint_doc_fees_rbtc()
tx_type_redeem_doc_fees_rbtc = moc_inrate.tx_type_redeem_doc_fees_rbtc()
tx_type_mint_btcx_fees_rbtc = moc_inrate.tx_type_mint_btcx_fees_rbtc()
tx_type_redeem_btcx_fees_rbtc = moc_inrate.tx_type_redeem_btcx_fees_rbtc()
tx_type_mint_bpro_fees_moc = moc_inrate.tx_type_mint_bpro_fees_moc()
tx_type_redeem_bpro_fees_moc = moc_inrate.tx_type_redeem_bpro_fees_moc()
tx_type_mint_doc_fees_moc = moc_inrate.tx_type_mint_doc_fees_moc()
tx_type_redeem_doc_fees_moc = moc_inrate.tx_type_redeem_doc_fees_moc()
tx_type_mint_btcx_fees_moc = moc_inrate.tx_type_mint_btcx_fees_moc()
tx_type_redeem_btcx_fees_moc = moc_inrate.tx_type_redeem_btcx_fees_moc()
print("Commission rate - Mint BPRO with fees in RBTC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_mint_bpro_fees_rbtc)))
print("Commission rate - Redeem BPRO with fees in RBTC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_redeem_bpro_fees_rbtc)))
print("Commission rate - Mint DOC with fees in RBTC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_mint_doc_fees_rbtc)))
print("Commission rate - Redeem DOC with fees in RBTC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_redeem_doc_fees_rbtc)))
print("Commission rate - Mint BTCx with fees in RBTC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_mint_btcx_fees_rbtc)))
print("Commission rate - Redeem BTCx with fees in RBTC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_redeem_btcx_fees_rbtc)))
print("Commission rate - Mint BPRO with fees in MoC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_mint_bpro_fees_moc)))
print("Commission rate - Redeem BPRO with fees in MoC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_redeem_bpro_fees_moc)))
print("Commission rate - Mint DOC with fees in MoC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_mint_doc_fees_moc)))
print("Commission rate - Redeem DOC with fees in MoC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_redeem_doc_fees_moc)))
print("Commission rate - Mint BTCx with fees in MoC: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_mint_btcx_fees_moc)))
print("Commission rate - Redeem BTCx with fees in MoC	: {0}".format(moc_inrate.commission_rate_by_transaction_type(tx_type_redeem_btcx_fees_moc)))


"""
0.25% Annual
"""

print("Bitpro rate: {0}".format(moc_inrate.bitpro_rate()))
print("Bitpro holders interest: {0}".format(moc_inrate.calc_bitpro_holders_interest()))
print("Bitpro interest address: {0}".format(moc_inrate.bitpro_interest_address()))
print("Bitpro interest block span: {0}".format(moc_inrate.bitpro_interest_blockspan()))
print("Bitpro interest last payed block: {0}".format(moc_inrate.last_bitpro_interest_block()))

print("Daily inrate: {0}".format(moc_inrate.daily_inrate()))

print("Calc commission value - Mint BPRO with fees in RBTC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_mint_bpro_fees_rbtc)))
print("Calc commission value - Redeem BPRO with fees in RBTC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_redeem_bpro_fees_rbtc)))
print("Calc commission value - Mint DOC with fees in RBTC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_mint_doc_fees_rbtc)))
print("Calc commission value - Redeem DOC with fees in RBTC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_redeem_doc_fees_rbtc)))
print("Calc commission value - Mint BTCx with fees in RBTC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_mint_btcx_fees_rbtc)))
print("Calc commission value - Redeem BTCx with fees in RBTC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_redeem_btcx_fees_rbtc)))
print("Calc commission value - Mint BPRO with fees in MoC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_mint_bpro_fees_moc)))
print("Calc commission value - Redeem BPRO with fees in MoC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_redeem_bpro_fees_moc)))
print("Calc commission value - Mint DOC with fees in MoC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_mint_doc_fees_moc)))
print("Calc commission value - Redeem DOC with fees in MoC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_redeem_doc_fees_moc)))
print("Calc commission value - Mint BTCx with fees in MoC: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_mint_btcx_fees_moc)))
print("Calc commission value - Redeem BTCx with fees in MoC	: {0}".format(moc_inrate.calc_commission_value(10.0, tx_type_redeem_btcx_fees_moc)))