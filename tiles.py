# Tiles a particular 3 x N block with monomers and dimers

# blocks = '''
# g  v g g  m gg g    g
# g *v=gtg * =g tg *m=gg
# gg   g gg   gg gg   gg
# '''.strip().splitlines()
# blocks = '''
# g  hh gg
# g *hh=gg
# gg    g
# '''.strip().splitlines()
# blocks = '''
# gg    g
# g *hh=gg
# g  hh gg
# '''.strip().splitlines()
# blocks = '''
# g hh g   g
# g*hh=gt =g
# g hh g   g
# '''.strip().splitlines()
# blocks = '''
# g  m gg g    g  g  hh gg
# gg* =ggtgg* =ggtgg*  =g
# g    g  g  m gg g  hh gg
# '''.strip().splitlines()
# blocks = '''
# g v gg g   g  g hh g
# g*v=ggtg*v=ggtg*hh=g
# g   g  g v gg g hh g
# '''.strip().splitlines()
blocks = '''
g
gg
g
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

ablocks = [
    zip('ggg', block) for block in ('   ', 'g  ', ' g ', '  g', 'gg ', ' gg', 'g g')
]

rules = [
    #000    100    010    001    110  011  101
    ['h^3', 'v'  , ''   , 'v'  , 'm', 'm', 'm'], # 000 ->
    ['m'  , ''   , ''   , ''   , '' , 'h', '' ], # 100 ->
    ['m'  , ''   , ''   , ''   , '' , '' , 'h'], # 010 ->
    ['m'  , ''   , ''   , ''   , 'h', '' , '' ], # 001 ->
    ['v'  , 'm'  , 'm'  , 'h^2', '' , '' , '' ], # 110 ->
    ['v'  , 'h^2', 'm'  , 'm'  , '' , '' , '' ], # 011 ->
    [''   , 'm'  , 'h^2', 'm'  , '' , '' , '' ], # 101 ->
]

def fmt(block):
    print r'''\begin{tikzpicture}[scale = 0.3]'''
    parse_blocks(block, c=['or', 'or', 'or'])
    print r'''\end{tikzpicture}'''

print '~'
for b in ablocks:
    print '&'
    fmt(b)

print r'\\'
for j, b in enumerate(ablocks):
    fmt(b)
    for i in range(7):
        print r'& \vspace*{-0.65cm} ' + (r'\(%s\)'%rules[i][j] if rules[i][j] else '')
    print r'\\'
