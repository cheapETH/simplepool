#!/usr/bin/env python3
import traceback
from web3.auto import w3
assert w3.isConnected()

# personal.unlockAccount('0xdF3097865fF3EA3EEC483Bb229322c255332A695')
print(w3.eth.coinbase)

ss = eval(input())
for k,v in ss.items():
  print("payout",k,v)
  try:
    ret = w3.eth.sendTransaction({'to': w3.toChecksumAddress(k.decode('utf-8')), 'from': w3.eth.coinbase, 'value': v*10**18, 'gasPrice': 1})
    print(ret)
  except Exception:
    print("PAYOUT FAILED")
    traceback.print_exc()

