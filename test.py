import json
from eth_utils import to_wei
from web3 import Web3
from brownie import sc_raw_material, sc_distribuitor

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# chave que autoriza as transações
private_key_raw_manufacturer = "13d20f193a5afa9908881d9506aabfea55db4b9541ba8a7a649a003eae315e5c"
private_key_pharma_manufacturer = "cd4ddd830b5531c1fc444c96572c73ab12537ccf3a53fd64241dbbefb1fff00d"
private_key_regulator = "e5c18734e231f48a76c66c08e71ca5902239494911e1c9e77e21e1c0a28e0171"
private_key_warehouse = "669214fc033c591d3b54011ffccf6dd7d3593b039793cdb93c74de63c0bd5405"
private_key_hospital = "42c418e98b0595f6e4eaa82761248145a52b06e5eb7364e5e10d3ae216cf80bc"
private_key_distribuitor = "98fbfee901721a7b148b6073e928590e23912664655e709d89f3434d1f7238c5"

# endereços das contas
wallet_raw_manufacturer = "0xA7fff0149449c9f5e468d8DC6d793342170F9088"
wallet_pharma_manufacturer = "0x931aF97Bad351732E935270019ACb225f32Ce763"
wallet_regulator = "0x2ec80273c33E1A7A101a677166e8F69f7793a71e"
wallet_warehouse = "0x7556e026028d761D682aee8A907847d548FE3B41"
wallet_hospital = "0x212D741fF92D25d91944111732354251429ACEC3"
wallet_distribuitor = "0x40b644C30eD556a8424d63615998321e7854bd9a"

# get the nonce
nonce = web3.eth.getTransactionCount(wallet_raw_manufacturer) # previne que uma transação seja realizada mais que uma vez
# create transactions
tx =  {
    'nonce': nonce,
    'to': wallet_distribuitor,
    'value': web3.toWei(100, 'ether'),
    'gas': 2000000, # Age como mineradores("Running the network") que precisam de ser compensados, ou seja, sempre que existe uma transação a rede é compensada como PoW.
    'gasPrice': web3.toWei('50', 'gwei')
}
# sign transactions
signed_tx = web3.eth.account.signTransaction(tx, private_key_raw_manufacturer)
# send transactions
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
#get transaction hashes
print(web3.toHex(tx_hash))

