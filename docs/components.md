# components of smart contract

smart contract is based on following components that intends to be individual modules:

##1. notary

creates the smart contract, that means:

- set market opening and closing date
- set limit for USD price in COP
- get intial ether for smart-contract to work
- set official source of information to decide smart-contract result
- set minimal amount of ether to buy in a contract
- get any other initial condition will be used
- start smart contract adresses and tokens

##2. seller

sell results, that means:

- register all income transactions to smart contract adresses
- show results about results selling

##3.judge

decide the correct result of the contract based on the official source

- get data from official source
- choose the good result of smart-contract
- show results of smart contract
- enable smart-contracts payment

##4. payer

calculate and do payments

- list all ethereum address of the ones that bought the good result
- calculate payment for every address that bought good result
- calculate payment comissions
- make payments to addresses

# components interaction

smart contract is created by giving information and gas to notary, minimal information
for notary to work is:

- selling start date (yyyy/mm/dd-HH:MM:SS)
- selling close date (yyyy/mm/dd-HH:MM:SS)
- lowest smart-contract price, transactions below this price will not be accounted and will not be returned to sender

then it must return the addresses for other people to send ether to their favorite result, results are only
two:

- above the limit
- below the limit

then, when starts selling date, seller starts to sell results and have a register of sales until close date is reached

when smart contract finish, judge get information from official source and chooses the wining result and order payer
to split collected funds into the addresses that bought correct result and divide full budget into addreses paying
a proportional amount to the funds sent by those addresses, calculation also considers transaction fees, so payment per address
include fees to make transaction