#future COP smart-contract

##1. summary

this smart-contract is a future market that allows user to buy results over an above a price fixed by
the contract for USD (united states dollar) in COP (colombian peso)

USD price in COP could be obtained from this ticker that takes official sources: ```http://api-cryptoassets.rhcloud.com/asset/ws```

##2. functionalities

1. allows to buy two results in a limited pre-defined lapsus (hard deadline to buy results):
    - price will be above limit
    - price will be below limit
2. get information from official sources about USD value in COP and decide winning outuput
3. divide amount of money between the addresses that bought winning result proportional to its positions

for full description of its components, please watch [components section](docs/components.md)

##3. environment setup

environment setup can be described on [install pyethereum section](docs/setup_pyethereum.md)

##4. documentation

available documentation is on ```/docs``` folder

##5. get involved

fork it and share, please follow (PEP8)[https://www.python.org/dev/peps/pep-0008/], for further information
contact us at (pedrorivera@emdyp.me)[mailto:pedrorivera@emdyp.me], or (oscaros73@gmail.com)[mailto:oscaros73@gmail.com]