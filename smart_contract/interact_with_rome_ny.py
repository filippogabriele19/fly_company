from lib2to3.pgen2.pgen import generate_grammar
import json
import string
from app.models import Ticket
from web3 import Web3
from .setting import *
from datetime import datetime
import asyncio

# for connetting to
w3 = Web3(Web3.HTTPProvider(RPC_SERVER))
my_address = w3.eth.accounts[0]

# read the json after compile conctract with truffle
info_json = json.load(open("smart_contract/build/contracts/FlightRomeNYNFT.json"))
abi = info_json["abi"]
bytecode = info_json["bytecode"]
contract_address = info_json["networks"]["5777"]["address"]
contract = w3.eth.contract(address=contract_address, abi=abi)
nonce = w3.eth.getTransactionCount(my_address)


def get_data_from_event():
    result = contract.events.TicketBought()
    print(result)


def return_contract_address():
    return contract_address


def buy_nft():
    print("Updating contract...")
    print(w3.eth.chain_id)
    store_transaction = contract.functions.safeMint().buildTransaction(
        {
            "chainId": w3.eth.chain_id,
            "value": 1000000000000000000,
            "gasPrice": w3.eth.gas_price,
            "from": w3.eth.accounts[1],
            "nonce": w3.eth.getTransactionCount(w3.eth.accounts[1]),
        }
    )

    signed_store_txn = w3.eth.account.sign_transaction(
        store_transaction, private_key=PRIVATE_KEY_2
    )
    send_add_ticket_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_add_ticket_tx)
    print("Updated contract!")
    return True
