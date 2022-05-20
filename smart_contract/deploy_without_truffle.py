from lib2to3.pgen2.pgen import generate_grammar
from solcx import compile_standard, install_solc
import json
from web3 import Web3
from setting import *



with open("./contracts/MyCompanyFlightTickets.sol", "r") as file:
    my_company_flight_tickets_file = file.read()

# COmpile our solidity
install_solc("0.8.7")
compiled_sol = compile_standard(
    {
        "language": "Solidity",
        "sources": {
            "MyCompanyFlightTickets.sol": {"content": my_company_flight_tickets_file}
        },
        "settings": {
            "outputSelection": {
                "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
            }
        },
    },
    solc_version="0.8.7",
)

#write .json file
with open("./build/contracts/MyCompanyFlightTickets.json", "w") as file:
    json.dump(compiled_sol, file)

# get bytecode
bytecode = compiled_sol["contracts"]["MyCompanyFlightTickets.sol"][
    "MyCompanyFlightTickets"
]["evm"]["bytecode"]["object"]

# get abi
abi = compiled_sol["contracts"]["MyCompanyFlightTickets.sol"]["MyCompanyFlightTickets"]["abi"]



# for connetting to 
w3 = Web3(Web3.HTTPProvider(RPC_SERVER))
print(w3.isConnected())

#fist accounts is my account for develop the contract
my_address = w3.eth.accounts[0]
#my private key
private_key = PRIVATE_KEY_1


# create the contract in python
contract = w3.eth.contract(abi=abi, bytecode=bytecode)
# get the latestest transaction
nonce = w3.eth.getTransactionCount(my_address)
print(nonce)

#build a transaction
transaction = contract.constructor().buildTransaction(
    {
        "chainId": w3.eth.chain_id,
        "gasPrice": w3.eth.gas_price,
        "from": my_address,
        "nonce": nonce,
    }
)
signed_txn = w3.eth.account.sign_transaction(transaction, private_key=private_key)

# send his signed transaction
print("Deploying contract...")
tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Deployed!")

# working with the contract
# contract addeess
# contract ABI
print(tx_receipt.contractAddress)

