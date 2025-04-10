# bitcoin-p2sh-p2wsh-multisig
This repository contains a Bitcoin transaction implementation that demonstrates how to build, sign, and serialize a P2SH-P2WSH 2-of-2 multisig transaction using raw scripting and witness data.

# Bitcoin P2SH-P2WSH Multisig Transaction

This project demonstrates how to build and sign a Bitcoin transaction that spends from a 2-of-2 multisig using a P2SH-wrapped P2WSH structure.

## Overview

- Constructs a raw Bitcoin transaction manually
- Signs the transaction with two private keys
- Builds the correct scriptSig and witness stack
- Outputs the final signed transaction in hex format

## Details

- Script type: P2SH-P2WSH 2-of-2 Multisig
- One input, one output
- Signatures created using ECDSA
- Final transaction written to `out.txt`

## How to Run

1. Uncomment your language in `run.sh`
2. Make `test.sh` executable:
   ```bash
   chmod +x test.sh
   ./test.sh
