# Tiling 3-by-N rectangles with Monomers and Dimers

Convoluted solution for the monomer-dimer tiling problem.

Suppose one is given pieces that may
be one of the three forms: monomers ($m$) that are $1 \times 1$ squares, and dimers that are dominoes,
either vertically ($v$) oriented $1 \times 2$, or horizontally ($h$) oriented $2 \times 1$. In how many ways can
a $n \times 3$ rectangle be covered completely and without overlap ("tiled") by such pieces?

$$
\begin{tikzpicture}
\draw (0,0) rectangle (1,1) node[pos=0.5] {m};
\draw (3,0) rectangle (5,1) node[pos=0.5] {h};
\draw (7,0) rectangle (7,2) node[pos=0.5] {v};
\end{tikzpicture}
$$