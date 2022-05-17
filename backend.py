"""
This script is responsible for creating and implementing all the logic of the blockchain services for the supply chain, 
with different roles for the different actors, among other implementations, integrated with flask and Ganache.

Created by Mauro Cardoso, 23 of April 2022, 19:16    
"""

import json
from eth_utils import to_wei
from web3 import Web3
from solcx import compile_standard, install_solc
# Install Solidity compiler.
_solc_version = "0.6.6"
install_solc(_solc_version)

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
chain_id = 5777

# The keys that authorize transactions
private_key_pharma_manufacturer = "82ccaa6887277495d2777f250616f5661aad664c7de7e072f2746099e7ac6e65"
private_key_regulator = "34b19bf20fc9fedcd93da8b7153d2dbdde055fbc4f5956f4a36e97af023803b9"
private_key_hospital = "8e536588086a906b083570d3f5d7363836c160e1bbe962d9ed73a694b89e39b2"
private_key_distribuitor = "50f140b0b6ef5af32d8c3974e25d43cc17a5bb305b4df873f72995d1cdf04da1"

# Account addresses
wallet_pharma_manufacturer = "0xa0242e82a8D070fCD6376b1ACdC6335d93CC2101"
wallet_regulator = "0xbeD007e0a8E83ceE85fD3ed4D5Cc924Db7997D0e"
wallet_hospital = "0x29E486144A9BD0Ea750420843b163ed6f2D5F8b0"
wallet_distribuitor = "0x14a8cc5E3988eFaa2D1F15c2BE8aA1712FdbB948"


# Compile smart contract with solcx.
def compile_contract(contract_source_file):
    """
    Reads file, compiles, returns contract name and interface
    """
    with open(contract_source_file, "r") as f:
        contract_source_code = f.read()   
    compiled_sol = compile_standard(
        {
            "language": "Solidity",
            "sources": {"*": {"content": contract_source_code}, },
            "settings": {
                "outputSelection": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version=_solc_version,
    )
    compiled_sol_json = json.loads(json.dumps(compiled_sol, indent = 5))
    return compiled_sol_json

# Deploy contracts to ganache
def deploy_contract(acct,private, abi, bytecode, contract_args=None):
    """
    deploys contract using self-signed tx, waits for receipt, returns address
    """

    contract = web3.eth.contract(abi=abi, bytecode=bytecode)
    constructed = contract.constructor() if not contract_args else contract.constructor(*contract_args)
    tx = constructed.buildTransaction({
        'from': acct,
        'nonce': web3.eth.getTransactionCount(acct),
        "gasPrice": web3.eth.gas_price
    })
    # sign transactions
    print ("Signing and sending raw tx ...")
    signed = web3.eth.account.signTransaction(tx, private)
    
    # send transactions
    tx_hash = web3.eth.sendRawTransaction(signed.rawTransaction)
    print ("tx_hash = {} waiting for receipt ...".format(tx_hash.hex()))
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
    #print(tx_receipt)
    contractAddress = tx_receipt["contractAddress"]
    return contractAddress

#Execute contracts to ganache
def exec_contract(to_acct,private_key_sender, nonce, value):
    nonce = web3.eth.getTransactionCount(nonce)
    tx =  {
        'nonce': nonce,
        'to': to_acct,
        'value': web3.toWei(value, 'ether'),
        'gas': 2000000, # Act as miners ("Running the network") that need to be compensated, i.e. every time there is a transaction the network is compensated as PoW.
        "gasPrice": web3.eth.gas_price
    }
    # sign transactions
    signed_tx = web3.eth.account.signTransaction(tx, private_key_sender)
    # send transactions
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash, timeout=120)
    return tx_receipt


# Definition of the function to create the smart contract with a block adding for the pharma regulator
def create_regulator_contract():
    # Regulator Smart Contract
    compiled_sol = compile_contract('Arquitetura 2/sc_regulator.sol')
    compiled_sol_abi = compiled_sol["contracts"]["*"]["pharma_aproval"]["abi"]
    compiled_sol_bytecode = compiled_sol["contracts"]["*"]["pharma_aproval"]["evm"]["bytecode"]["object"]
    deploy_contract(wallet_regulator,private_key_regulator,compiled_sol_abi,compiled_sol_bytecode)

# Definition of the function to create a transaction with a block adding for the pharma manufacturer to the regulator
def create_transaction_regulator_to_manufacturer():
    exec_contract(wallet_regulator,private_key_pharma_manufacturer,wallet_pharma_manufacturer,0)
    

# Definition of the function to create the smart contract with a block adding for the distribuitor
def create_distribuitor_contract():
    # Regulator Smart Contract
    compiled_sol = compile_contract('Arquitetura 2/sc_distribuitor.sol')
    compiled_sol_abi = compiled_sol["contracts"]["*"]["distribuition"]["abi"]
    compiled_sol_bytecode = compiled_sol["contracts"]["*"]["distribuition"]["evm"]["bytecode"]["object"]
    deploy_contract(wallet_distribuitor,private_key_distribuitor,compiled_sol_abi,compiled_sol_bytecode)

# Definition of the function to create a transaction with a block adding for the pharma manufacturer with the distribuitor
def create_transaction_distribuitor(d_value):
    exec_contract(wallet_distribuitor,private_key_pharma_manufacturer,wallet_pharma_manufacturer,value = d_value)
    

# Definition of the function to create the smart contract with a block adding for the client (Hospital)
def create_hospital_contract():
    # Regulator Smart Contract
    compiled_sol = compile_contract('Arquitetura 2/sc_pharma.sol')
    compiled_sol_abi = compiled_sol["contracts"]["*"]["pharma"]["abi"]
    compiled_sol_bytecode = compiled_sol["contracts"]["*"]["pharma"]["evm"]["bytecode"]["object"]
    deploy_contract(wallet_hospital,private_key_hospital,compiled_sol_abi,compiled_sol_bytecode)

# Definition of the function to create a transaction with a block adding for the pharma manufacturer with the distribuitor
def create_transaction_hospital(h_value):
    exec_contract(wallet_pharma_manufacturer,private_key_hospital,wallet_hospital,value = h_value)