# Tiles a particular 3 x N block with monomers and dimers

blocks = '''
g m gg g   g  g m gg g m g
g*m=ggtg*m=ggtg* =g tg*m=g
g   g  g m gg g m gg g m g
'''.strip().splitlines()

def parse_blocks(blocks, c = ()):
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
    return print_blocks(output, c)


def get_str(c):
    if not c:
        return 'c'
    else:
        return c.pop(0)

def print_blocks(parsed_blocks, c = ()):
    for token, h, v in parsed_blocks:
        if token == 'v':
            print '\draw (%s,%s) rectangle (%s,%s) node[pos=0.5] {v};' % (h, 3-v, h + 1, 3-(v + 2))
        elif token == 'h':
            print '\draw (%s,%s) rectangle (%s,%s) node[pos=0.5] {h};' % (h, 3-v, h + 2, 3-(v + 1))
        elif token == 'm':
            print '\draw (%s,%s) rectangle (%s,%s) node[pos=0.5] {m};' % (h, 3-v, h + 1, 3-(v + 1))
        elif token == 't':
            print '\draw[draw=none] (%s,%s) rectangle (%s,%s) node[pos=0.5] {%s};' % (h, 3-v, h + 1, 3-(v + 1), get_str(c))
        elif token == 'g':
            print '\draw[fill=lightgray!40,draw=none] (%s,%s) rectangle (%s,%s);' % (h, 3-v, h + 1, 3-(v + 1))
        elif token == 'c':
            print '\draw[fill=lightgray!40,draw=none] (%s,%s) rectangle (%s,%s) node[pos=0.5] {%s};' % (h, 3-v, h + 1, 3-(v + 1), get_str(c))
        elif token == '*':
            print r'\draw[draw=none] (%s,%s) rectangle (%s,%s) node[pos=0.5] {\(\times\)};' % (h, 3-v, h + 1, 3-(v + 1))
        elif token != ' ':
            print '\draw[draw=none] (%s,%s) rectangle (%s,%s) node[pos=0.5] {%s};' % (h, 3-v, h + 1, 3-(v + 1), token)

print r'''
$$
\begin{tikzpicture}'''
parse_blocks(blocks, c=['or', 'or'])
print r'''\end{tikzpicture}
$$
'''