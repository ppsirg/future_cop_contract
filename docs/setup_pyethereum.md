#install pyethereum, the one that let us to communicate with blockchain


- [serpent: start site](https://mc2-umd.github.io/ethereumlab/)
- [serpent tutorial](https://mc2-umd.github.io/ethereumlab/docs/serpent_tutorial.pdf)

this guide was made and tested only for ubuntu 16.04 LTS and ubuntu 14.04 LTS, it should
work in most of debian-based os

1- create a folder to save all you're going to download

```
mkdir ethereum
cd ethereum
```
- make python 2.7 virtualenv

```
mkvirtualenv -p /usr/bin/python2
```

2- install dependencies

```
sudo apt-get install libssl-dev autoconf libtool libffi-dev libgmp-dev build-essential automake
git clone https://github.com/bitcoin/secp256k1.git
cd secp256k1
./autogen.sh
./configure
make
./tests
sudo make install
```

3- clone pyethereum and install it

```
cd ..
git clone https://github.com/ethereum/pyethereum
cd pyethereum
pip install -r requirements.txt
pip install pytest
```

4- install serpent

```
cd ..
git clone https://github.com/ethereum/serpent.git
cd serpent
git checkout develop
python setup.py install
```

5- check if all is ok

```
py.test -m test_contracts.py
```

