from pyuniswap.pyuniswap import Token
import configparser
import os

def get_env():
    config_file = "config.ini"
    if os.path.exists(config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
    else:
        print('config file not found! exit...')
        exit(0)

    address = config["info"]["address"]
    private_key = config["info"]["private_key"]

    return address, private_key

if __name__ == '__main__':
    address, private_key = get_env()
    print(address)
    print(private_key)
    target_address = "0x223a0f22e28889735e50A7781fBE1Da2baCbafD2"

    if not address or not private_key or not target_address:
        print("config error")
        exit(0)
    
    # address = input("from wallet address:")
    # private_key = input("from wallet private key:")
    # target_address = input("to wallet address:")

    usdt_token = "0x55d398326f99059fF775485246999027B3197955"
    busd_token = "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56"

    provider = "https://bsc-dataseed.binance.org/"
    token = Token(usdt_token, provider=provider)
    token.is_connected()

    percent = 85

    # BNB
    balance = token.balanceOfBNB(address)
    if (balance < 50) {
        amount = float(balance / 100 * percent)
        # amount = 1
        token.connect_wallet(address, private_key)   
        tx = token.transfer(target_address, int(amount * 10**18))
        print(tx.hex())
    }

    # USDT
    balance = token.balance(address, usdt_token)
    if (balance < 5000) {
        amount = float(balance / 100 * percent)
        # amount = 1
        token.connect_wallet(address, private_key)   
        tx = token.token_transfer(usdt_token, int(amount * 10**18), target_address)
        print(tx.hex())
    }

    # BUSD
    balance = token.balance(address, busd_token)
    if (balance < 5000) {
        amount = float(balance / 100 * percent)
        # amount = 1
        token.connect_wallet(address, private_key)   
        tx = token.token_transfer(busd_token, int(amount * 10**18), target_address)
        print(tx.hex())
    }
