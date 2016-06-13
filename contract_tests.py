# -*- coding: utf-8 -*-

import unittest
from time import sleep
from datetime import timedelta, datetime
from contract import notary, seller  # , judge, payer


def build_rules():
    return {
        'trusted_sources': [
            'http://api-cryptoassets.rhcloud.com/asset/ws',
            ],
        'date': {
            'start': datetime.utcnow(),
            'end': datetime.utcnow() + timedelta(0, 24)
            },
        'minimal_bid': 10
        }


class test_contract(unittest):

    def setUp(self):
        #data to create contract
        self.contract_rules = build_rules()
        #data to simulate contract sales
        self.sales = [
            ['above', '222222222', 12],
            ['below', '333333333', 32],
            ['above', '777777777', 26],
            ['below', '666666666', 76],
            ['above', '200000000', 40],
            ]
        #data to simulate contract resolution
        self.USD_price = {
            'cop': 20000
            }

    def test_notary(self):
        self.contract_rules = build_rules()
        contract_data = notary.create_contract(self.contract_rules)
        self.assertTrue(contract_data)

    def test_seller(self):
        self.contract_rules = build_rules()
        contract_data = notary.create_contract(self.contract_rules)
        s = seller(contract_data)
        s.run()
        reg = 0
        while s.isOpen():
            if reg < len(self.sales):
                s.sell(self.sales[reg])
            else:
                sleep(0.1)
        #check if elapsed close season
        sales_deadline = self.contract_rules['date']['end']
        self.assertTrue(
            not s.close_date,
            'sales didnt finished in a safe way'
            )
        sales_end = s.close_date
        #check if registered all data
        self.assertTrue(sales_deadline == sales_end)

    def test_judge(self):
        pass

    def test_payer(self):
        pass


if __name__ == '__main__':
    unittest.main()