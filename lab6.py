import hashlib
import json
from flask import Flask


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash=0, current_hash=0)

    def create_block(self, proof, previous_hash, current_hash):
        block = {
            'index': len(self.chain)+1,
            'proof': proof,
            'previous_hash': previous_hash,
            'current_hash': current_hash,
        }
        self.chain.append(block)
        return block

    def hash(self, block):
        encoded_block = json.dumps(block).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_value = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_value[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return [new_proof, hash_value]


app = Flask(__name__)
blk = Blockchain()


@app.route('/mine_block')
def mine_block():
    previous_block = blk.get_previous_block()

    previous_proof = previous_block['proof']

    proof = blk.proof_of_work(previous_proof)
    previous_hash = blk.hash(previous_block)

    block = blk.create_block(proof[0], previous_hash, proof[1])

    response = {
        'Message': 'Your block is mined',
        'index': block['index'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
        'current_hash': block['current_hash'],
    }
    return response


@app.route('/get_chain')
def get_chain():
    response = {
        'chain': blk.chain,
        'length': len(blk.chain)
    }

    return response


app.run()
