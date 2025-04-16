## Scripting with Moccasin:

├── README.md
├── moccasin.toml
├── script
│   └── deploy.py
├── src
│   └── Counter.vy
└── tests
    ├── conftest.py
    └── test_counter.py
    
## RUN
You can run the deploy.py script with either:


mox run deploy 


OR


mox run ./script/deploy.py


OR


mox run deploy --network anvil --account anvil1

## Networking:


If you have networks defined in your moccasin.toml, 
you can directly work with the network in your scripts. 


For example, if you have a anvil network defined in your moccasin.toml:


mox run deploy --network anvil

## Encrypting a private key
You can encrypt a private key using the wallet import ACCOUNT_NAME command. This will create a keystore file in the default keystore directory.
It will prompt you to enter your private key and password.


mox wallet import my_account

Running wallet command...
Importing private key...
Enter your private key:  ...



Once you have an account, you can view it with the wallet list command.

$ mox wallet list

Running wallet command...
Found 1 accounts:
my_account



This will encrypt your key and store it at ~/.moccasin/keystore/my_account.json. 

You can view the contents of the keystore file with the wallet view command.

You can then use these in scripts!



mox run deploy --account my_account


