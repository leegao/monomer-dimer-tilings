# Tiles a particular 3 x N block with monomers and dimers

# blocks = '''
# g  v g g  m gg g    g
# g *v=gtg * =g tg *m=gg
# gg   g gg   gg gg   gg
# '''.strip().splitlines()
blocks = '''
g  m g g  hh gg 
g *m=gtg *hh=gg
gg   g gg    g 
'''.strip().splitlines()
# blocks = '''
# gg   g gg    g
# g *m=gtg *hh=gg
# g  m g g  hh gg
# '''.strip().splitlines()
# blocks = '''
# g hh g   g
# g*hh=gt =g
# g hh g   g
# '''.strip().splitlines()

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
parse_blocks(blocks, c=['or', 'or', 'or'])
print r'''\end{tikzpicture}
$$
'''