import pyroaman

if __name__ == "__main__":
    db = pyroaman.load('Ryenet.json')

# print(db.pages)
some_blocks = db.lookup('testcard')
# print(some_blocks)

for blocks in some_blocks:
    print(blocks)
    print(blocks.children)
# print(some_blocks[0].text)
# print(dir(some_blocks[0]))

# print(some_blocks[0].children)

# print(some_blocks[0].links)

# print(some_blocks[0].backlinks)

# print(some_blocks[0].metadata)
# print(some_blocks[1])