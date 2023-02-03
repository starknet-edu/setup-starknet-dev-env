# How to setup on mac
This is my personal best practise to setup the local starknet dev env. There are lots of tutorials out there, I will keep it updated if possible.
Please raise PR if you find anything wrong.

It consists of
 - latest cairo-lang
 - latest starknet-devnet
 - latest protostar and toml file.
 - protostar cheatsheet.

# install build tools
```
xcode-select --install
```

# install brew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

# install python3.9
```
brew install python@3.9 git gmp
```

# install cairo
You might encounter some issues while installing `fastecdsa` on M1 Chip, please refer to this [thread](https://github.com/AntonKueltz/fastecdsa/issues/74)

```
python3.9 -m venv ~/cairo_venv
source ~/cairo_venv/bin/activate
pip3 install ecdsa fastecdsa sympy cairo-lang
```

# install starknet-devnet
```
pip3 install starknet-devnet
```

# start your local dev env
```
starknet-devnet --seed 1234
```

# install protostar
```
curl -L https://raw.githubusercontent.com/software-mansion/protostar/master/install.sh | bash
```
# init your protostar project
```
protostar init $your-project-name
```
# protostar build
```
protostar build
```

# protostar declare
```
protostar -p devnet declare ./build/main.json --account-address ${ACCT_ADDR} --private-key-path ./.pkey --max-fee auto
```

# protostar deployment
```
protostar -p devnet deploy ${CLASS_HASH} --account-address ${ACCT_ADDR} --private-key-path ./.pkey --max-fee auto
```

# protostar call smartcontract
```
protostar -p devnet call --contract-address ${CONTRACT_ADDR} --function "get_balance"
```

# protostar invoke smartcontract
```
protostar -p devnet invoke --contract-address ${CONTRACT_ADDR} --function "increase_balance" --account-address ${ACCT_ADDR} --max-fee auto --inputs 3 --private-key-path ./.pkey
```

# protostar.toml
```
[project]
protostar-version = "0.9.1"
lib-path = "lib"

[contracts]
main = ["src/main.cairo"]

[profile.devnet.project]
gateway-url = "http://127.0.0.1:5050/"
chain-id = 1536727068981429685321

["profile.devnet.protostar.deploy"]
gateway-url="http://127.0.0.1:5050/"

["profile.testnet.protostar.deploy"]
network="testnet"

["profile.mainnet.protostar.deploy"]
network="mainnet"
```



