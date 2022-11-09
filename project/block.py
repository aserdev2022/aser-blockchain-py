import time
from crypto_hash import crypto_hash


class Block:

    def __init__(self, timestamp, last_hash, hash, data):
        self.data = data
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash

    def __repr__(self):
        return (
            'Block('
            f'timestamp: {self.timestamp},'
            f'last_hash: {self.last_hash},'
            f'hash: {self.hash},'
            f'data: {self.data})'
        )

    @staticmethod
    def mine_block(last_block, data):
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, data)

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        return Block(1, 'genesis', 'genesis_hash', [])


def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)


if __name__ == '__main__':
    main()
