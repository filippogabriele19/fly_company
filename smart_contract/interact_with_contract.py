from lib2to3.pgen2.pgen import generate_grammar
import json
import string
from app.models import Ticket
from web3 import Web3
from .setting import *
from datetime import datetime

# for connetting to 
w3 = Web3(Web3.HTTPProvider(RPC_SERVER))
my_address = w3.eth.accounts[0]

# read the json after compile conctract with truffle
info_json = json.load(open('smart_contract/build/contracts/MyCompanyFlightTickets.json'))
abi = info_json["abi"]
bytecode = info_json["bytecode"]
contract_address = info_json["networks"]["5777"]["address"]
my_company_tickets = w3.eth.contract(address=contract_address, abi=abi)
nonce = w3.eth.getTransactionCount(my_address) 


def get_all():
    #get all registered tickets
    print(my_company_tickets.functions.getAllTickets().call())


def add_new (name:string,last_name:string,ticket:Ticket):
    print("Updating contract...")
    store_transaction = my_company_tickets.functions.addTicket(
        name,
        last_name,
        ticket.date_purchase.strftime("%d/%m/%Y"),
        ticket.date_departure.strftime("%d/%m/%Y"),
        ticket.departure_city,
        ticket.arrival_city,
        ticket.price,
        ticket.airplane_code,
        ticket.code
    ).buildTransaction(
        {
            "chainId": w3.eth.chain_id,
            "gasPrice": w3.eth.gas_price,
            "from": my_address,
            "nonce": w3.eth.getTransactionCount(my_address),
        }
    )

    signed_store_txn = w3.eth.account.sign_transaction(
        store_transaction, private_key=PRIVATE_KEY_1
    )
    send_add_ticket_tx = w3.eth.send_raw_transaction(signed_store_txn.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(send_add_ticket_tx)
    print("Updated contract...")
    return True


def search_from_code(_code:string):
    # do a search with mapping 
    serched_ticket = my_company_tickets.functions.getTicketFromCode(_code).call()
    #prob not the best way to compare if the code is the same
    if( len(serched_ticket) >0 ):
        if(serched_ticket[8] == _code):
            return(serched_ticket)
        else:
            return None
    else:
        return None