# Tiling 3-by-N rectangles with Monomers and Dimers

Convoluted solution for the monomer-dimer tiling problem.

Suppose one is given pieces that may
be one of the three forms: monomers ($m$) that are $1 \times 1$ squares, and dimers that are dominoes,
either vertically ($v$) oriented $1 \times 2$, or horizontally ($h$) oriented $2 \times 1$. In how many ways can
a $n \times 3$ rectangle be covered completely and without overlap ("tiled") by such pieces?

$$
\begin{tikzpicture}
\draw (0,0) rectangle (1,1) node[pos=0.5] {m};
\draw (2,0) rectangle (4,1) node[pos=0.5] {h};
\draw (5,1.5) rectangle (6,-0.5) node[pos=0.5] {v};
\end{tikzpicture}
$$

------------------------

For example, here's a $3 \times 2$ rectangular tiling:

$$
\begin{tikzpicture}
\draw (0,3) rectangle (2,2) node[pos=0.5] {h};
\draw (0,2) rectangle (2,1) node[pos=0.5] {h};
\draw (0,1) rectangle (1,0) node[pos=0.5] {m};
\draw (1,1) rectangle (2,0) node[pos=0.5] {m};
\end{tikzpicture}
$$

or this $3 \times 5$ rectangular tiling:

$$
\begin{tikzpicture}
\draw (0,3) rectangle (1,1) node[pos=0.5] {v};
\draw (1,3) rectangle (3,2) node[pos=0.5] {h};
\draw (3,3) rectangle (4,2) node[pos=0.5] {m};
\draw (4,3) rectangle (5,1) node[pos=0.5] {v};
\draw (1,2) rectangle (2,1) node[pos=0.5] {m};
\draw (2,2) rectangle (4,1) node[pos=0.5] {h};
\draw (0,1) rectangle (1,0) node[pos=0.5] {m};
\draw (1,1) rectangle (3,0) node[pos=0.5] {h};
\draw (3,1) rectangle (4,0) node[pos=0.5] {m};
\draw (4,1) rectangle (5,0) node[pos=0.5] {m};
\end{tikzpicture}
$$
