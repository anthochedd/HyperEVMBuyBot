import time
from web3 import Web3
from eth_account import Account
from decimal import Decimal
import json

# ===================== CONFIGURATION =====================
# Private wallet key (NEVER SHARE IT!)
PRIVATE_KEY = ""
# HyperswapRouter address (to complete)
ROUTER_ADDRESS = "0xb4a9C4e6Ea8E2191d2FA5B380452a634Fb21240A"  # To complete
# Token address to buy
TOKEN_ADDRESS = ""  # To complete
# Amount of HYPE to use for each purchase (in HYPE, ex: 0.00000001)
AMOUNT_HYPE = Decimal("0.00000001")
# RPC HyperEVM
RPC_URL = "https://rpc.hyperliquid.xyz/evm"
# Purchase frequency (in seconds)
FREQUENCY = 5
# Tolerated slippage (in %)
SLIPPAGE = 1

ROUTER_ABI = json.loads('[{"inputs":[{"internalType":"uint256","name":"amountOutMin","type":"uint256"},{"internalType":"address[]","name":"path","type":"address[]"},{"internalType":"address","name":"to","type":"address"},{"internalType":"address","name":"referrer","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"}],"name":"swapExactETHForTokensSupportingFeeOnTransferTokens","outputs":[],"stateMutability":"payable","type":"function"}]')

w3 = Web3(Web3.HTTPProvider(RPC_URL))
if not w3.is_connected():
    print("Error connecting to HyperEVM RPC!")
    exit(1)

account = Account.from_key(PRIVATE_KEY)
print(f"Bot connected with address: {account.address}")

router = w3.eth.contract(address=Web3.to_checksum_address(ROUTER_ADDRESS), abi=ROUTER_ABI)

def buy_token(gas_price, nonce):
    amount_in_wei = w3.to_wei(AMOUNT_HYPE, 'ether')
    amount_out_min = 1
    path = [w3.to_checksum_address("0x5555555555555555555555555555555555555555"), w3.to_checksum_address(TOKEN_ADDRESS)]
    to = account.address
    referrer = "0x0000000000000000000000000000000000000000"
    deadline = int(time.time()) + 60

    tx = router.functions.swapExactETHForTokensSupportingFeeOnTransferTokens(
        amount_out_min,
        path,
        to,
        referrer,
        deadline
    ).build_transaction({
        'from': account.address,
        'value': amount_in_wei,
        'gas': 300000,
        'gasPrice': gas_price,
        'nonce': nonce,
        'chainId': 999
    })

    signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"Transaction sent: {w3.to_hex(tx_hash)} | Gas price: {gas_price / 1e9:.3f} Gwei | Nonce: {nonce}")
    return tx_hash

if __name__ == "__main__":
    gas_price = 200_000_000
    nonce = w3.eth.get_transaction_count(account.address, 'pending')
    while True:
        try:
            buy_token(gas_price, nonce)
            nonce += 1
        except Exception as e:
            print(f"Error during purchase: {e}")
        time.sleep(FREQUENCY) 