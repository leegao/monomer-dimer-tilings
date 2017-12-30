# Tiles a particular 3 x N block with monomers and dimers

blocks = '''
hh
hh
mm
'''.strip().splitlines()

def parse_blocks(blocks):
    seen = set()
    output = []
    for v, line in enumerate(blocks):
        for h, token in enumerate(line):
            if (v, h) in seen:
                continue
            token = blocks[v][h]
            output.append((token, h, v))
            seen.add((v, h))
            if token == 'v':
                assert blocks[v + 1][h] == 'v'
                seen.add((v + 1, h))
            elif token == 'h':
                assert blocks[v][h + 1] == 'h'
                seen.add((v, h + 1))
    return print_blocks(output)


def print_blocks(parsed_blocks):
    for token, h, v in parsed_blocks:
        if token == 'v':
            print '\draw (%s,%s) rectangle (%s,%s) node[pos=0.5] {v};' % (h, 3-v, h + 1, 3-(v + 2))
        elif token == 'h':
            print '\draw (%s,%s) rectangle (%s,%s) node[pos=0.5] {h};' % (h, 3-v, h + 2, 3-(v + 1))
        else:
            print '\draw (%s,%s) rectangle (%s,%s) node[pos=0.5] {m};' % (h, 3-v, h + 1, 3-(v + 1))

print r'''
$$
\begin{tikzpicture}'''
parse_blocks(blocks)
print r'''\end{tikzpicture}
$$
'''