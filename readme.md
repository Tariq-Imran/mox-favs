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

## Networking:
If you have networks defined in your moccasin.toml, 
you can directly work with the network in your scripts. 
For example, if you have a anvil network defined in your moccasin.toml:
mox run deploy --network anvil
