import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

with open("artifacts/Saludo_metadata.json") as f:
    info_json = json.load(f)

ABI = info_json["output"]["abi"] # primer requisito para la conexion

CONTRACT = "0x46792D19FfC3c1eE3381aeEd692E107cFfaa04Ae" # segundo requisito
WALLET = os.environ["WALLET"] # tercer requisito
PRIV_KEY = os.environ["PRIV_KEY"] # cuarto requisito

arbitrum_rpc = "https://endpoints.omniatech.io/v1/arbitrum/sepolia/public" #quinto requisito

w3 = Web3(Web3.HTTPProvider(arbitrum_rpc)) # establecemos la conexion con el RPC

if w3.is_connected():
    print("-" * 50)
    print("Connected to Arbitrum RPC endpoint")
else:
    print("Connection Failed")
