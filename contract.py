# -*- coding: utf-8 -*-

from datetime import datetime, timedelta


def calculate_USD_price(source):
    """calculate a price of USD in COP given a source"""
    return 10000


class notary():
    """
    creates the smart contract, that means:
    - set market opening and closing date
    - set limit for USD price in COP
    - get intial ether for smart-contract to work
    - set official source of information to decide smart-contract result
    - set minimal amount of ether to buy in a contract
    - get any other initial condition will be used
    - start smart contract adresses and tokens
    """
    def __init__(self):
        super(notary, self).__init__()
        self.trusted_sources = [
            'http://api-cryptoassets.rhcloud.com/asset/ws',
            ]

    def default_price_boundary(self):
        """calculate default price boundary"""
        opt = 0
        succeded = False
        while not succeded:
            try:
                price_boundary = calculate_USD_price(
                    self.trusted_sources[opt]
                    )
                succeded = True
            except:
                if opt < len(self.trusted_sources):
                    opt += 1
                else:
                    raise Exception('all sources checked, all failed')


class contract_rules():
    """
    represents contract rules
    """
    def __init__(self):
        super(contract_rules, self).__init__()
        self.trusted_sources = [
            'http://api-cryptoassets.rhcloud.com/asset/ws',
            ]
        self.price_boundary = 0
        self.date = {
            'start': datetime.utcnow(),
            'end': datetime.utcnow() + timedelta(0, 24)
            }


class payer():
    """
    calculate and do payments

    - list all ethereum address of the ones that bought the good result
    - calculate payment for every address that bought good result
    - calculate payment comissions
    - make payments to addresses
    """
    def __init__(self, result):
        pass


class judge():
    """
        decide the correct result of the contract based on the official source
        - get data from official source
        - choose the good result of smart-contract
        - show results of smart contract
        - enable smart-contracts payment
    """
    def __init__(self, contract_rules):
       self.rules = contract_rules
       self.payer = payer()

    def run(self):
        """start judge labor"""
        #calculate time to start working
        t = self.calculate_rest()
        #sleep while not working
        sleep(t)
        #choose good result
        result = self.choose_good_result()
        #send payer the correct result
        self.payer.start(result)

    def calculate_rest():
        """calculate time until judge must work"""
        pass

    def choose_good_result(self):
        """choose good results"""
        #get current price
        result = self.get_current_price()
        #return good result
        return result