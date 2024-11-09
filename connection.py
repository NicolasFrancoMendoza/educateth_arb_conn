import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

with open("artifacts/Saludo_metadata.json") as f:
    info_json = json.load(f)

ABI = info_json["output"]["abi"] # primer requisito para la conexion

CONTRACT = "0x46792D19FfC3c1eE3381aeEd692E107cFfaa04Ae" # segundo requisito, este contrato es el creado con funciones Saludo
WALLET = os.environ["WALLET"] # tercer requisito
PRIV_KEY = os.environ["PRIV_KEY"] # cuarto requisito

arbitrum_rpc = "https://endpoints.omniatech.io/v1/arbitrum/sepolia/public" #quinto requisito

w3 = Web3(Web3.HTTPProvider(arbitrum_rpc)) # establecemos la conexion con el RPC

if w3.is_connected():
    print("-" * 50)
    print("Connected to Arbitrum RPC endpoint")
else:
    print("Connection Failed")

contract_address = CONTRACT
contract_abi = ABI

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

account_address = WALLET
private_key = PRIV_KEY

result = contract.functions.leerSaludo().call() # lectura de función ya creada en contrato ya subido en la blockchain

print("-" * 50)
print(f"Ultimo saludo: {result}")


function_data = contract.functions.guardarSaludo("Hola desde python recargado II").build_transaction({ #estructura de transacción nueva que vamos a hacer
    'from': account_address,
    'gas': 5000000,
    'gasPrice': w3.to_wei('10', 'gwei'),
    'nonce': w3.eth.get_transaction_count(WALLET),
    'chainId': 421614, 
})

signed_transaction = w3.eth.account.sign_transaction(function_data, private_key) #subir la transacción
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction) #subir el hash

print(f"HASH: {transaction_hash.hex()}")

result2 = contract.functions.leerSaludo().call()

print("-" * 50)
print(f"Ultimo saludo: {result2}") #imprimir resultado de la función agregada

