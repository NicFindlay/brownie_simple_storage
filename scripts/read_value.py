from brownie import SimpleStorage, accounts, config


def read_contract():
    # printing first contract address from deployment
    # print(SimpleStorage[0])

    simple_storage = SimpleStorage[-1]  # -1 most recent
    print(simple_storage.retrieve())


def main():
    read_contract()
