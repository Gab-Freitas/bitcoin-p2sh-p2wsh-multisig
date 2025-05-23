from bitcoinutils.setup import setup
from bitcoinutils.keys import PrivateKey, P2wshAddress, P2shAddress
from bitcoinutils.script import Script
from bitcoinutils.transactions import Transaction, TxInput, TxOutput, TxWitnessInput
from bitcoinutils.utils import to_satoshis

setup("mainnet")


def main():
    # Private keys
    priv1 = PrivateKey(b=bytes.fromhex(
        "39dc0a9f0b185a2ee56349691f34716e6e0cda06a7f9707742ac113c4e2317bf"))
    priv2 = PrivateKey(b=bytes.fromhex(
        "5077ccd9c558b7d04a81920d38aa11b4a9f9de3b23fab45c3ef28039920fdd6d"))

    # Corresponding public keys
    pub1 = priv1.get_public_key()
    print(pub1.to_hex())
    pub2 = priv2.get_public_key()

    # Multisig redeem script
    redeem_script = Script(
        ["OP_2", pub2.to_hex(), pub1.to_hex(), "OP_2", "OP_CHECKMULTISIG"])
    p2wsh_script = redeem_script.to_p2wsh_script_pub_key()
    p2sh_address = P2shAddress.from_script(p2wsh_script)

    # UTXO details
    outpoint_txid = "0000000000000000000000000000000000000000000000000000000000000000"
    outpoint_index = 0
    amount = 100000  # 0.001 BTC in satoshis

    # Destination address and output
    destination_address = "325UUecEQuyrTd28Xs2hvAxdAjHM7XzqVF"
    txout = TxOutput(amount, P2shAddress(
        destination_address).to_script_pub_key())

    # Create transaction
    txin = TxInput(outpoint_txid, outpoint_index, sequence=b'\xff\xff\xff\xff')

    tx = Transaction([txin], [txout], has_segwit=True)
    print(dir(tx.inputs))
    # Signatures
    sighash1 = priv1.sign_segwit_input(tx, 0, redeem_script, amount)
    sighash2 = priv2.sign_segwit_input(tx, 0, redeem_script, amount)

    # ScriptSig & Witness
    txin.script_sig = Script(["220020" + p2wsh_script.to_hex()[4:]])
    tx.witnesses.append(TxWitnessInput(
        ["", sighash2, sighash1, redeem_script.to_hex()]))

    # Serialize and save transaction
    signed_tx = tx.serialize()
    with open("out.txt", "w") as f:
        f.write(signed_tx)

    print("Transaction Hex:", signed_tx)


if __name__ == "__main__":
    main()
