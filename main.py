from pyuniswap.pyuniswap import Token

if __name__ == '__main__':
    address = input("from wallet address:")
    private_key = input("from wallet primary key:")
    #target_address = input("to wallet address:")
    target_address = "0x198294CEE14776ee126B98875C26d49f9B7f28E4"
    amount = float(input("amount to send:"))

    usdt = "0x55d398326f99059ff775485246999027b3197955"
    provider = "https://bsc-dataseed.binance.org/"
    token = Token(usdt, provider=provider)
    token.connect_wallet(address, private_key)
    tx = token.transfer(target_address, int(amount * 10**18))
    print(tx.hex())
