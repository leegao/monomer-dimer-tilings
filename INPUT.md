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

There are various exact enumerations for this problem (e.g. see http://algo.inria.fr/libraries/autocomb/MonoDiMer-html/MonoDiMer.html),
but we'd like to approach this with a combination of enumerative combinatorics and computer programming to ease the tedious analysis.
In particular, we'd like to reduce this problem into finding the singularities of a complex rational function.

-----------------------------------------------------

In the $3 \times 5$ example above, we can consider the tiling process as a sequence of constructions. We start
with the $3 \times 1$ line at the beginning:

$$
\begin{tikzpicture}
\draw (0,3) rectangle (1,1) node[pos=0.5] {v};
\draw (0,1) rectangle (1,0) node[pos=0.5] {m};
\end{tikzpicture}
$$

Next, the natural thing to do would be to add the horizontal block at the top of the second column. However,
for reasons that will become clear soon, let's artificially restrict our rules to allow the total gap at the
end of the blocks to be at most one-block wide. That is, we will always ensure that the contour edge of
our work-in-progress "rectangle" will only have holes that are "shallow" enough to be filled by a monomer.

$$
\begin{tikzpicture}
\draw (0,3) rectangle (1,1) node[pos=0.5] {v};
\draw[draw=none] (1,3) rectangle (2,2) node[pos=0.5] { };
\draw[draw=none] (2,3) rectangle (3,2) node[pos=0.5] { };
\draw[draw=none] (3,3) rectangle (4,2) node[pos=0.5] { };
\draw (4,3) rectangle (6,2) node[pos=0.5] {h};
\draw[draw=none] (6,3) rectangle (7,2) node[pos=0.5] { };
\draw[draw=none] (7,3) rectangle (8,2) node[pos=0.5] { };
\draw[draw=none] (8,3) rectangle (9,2) node[pos=0.5] { };
\draw (9,3) rectangle (10,1) node[pos=0.5] {v};
\draw (10,3) rectangle (12,2) node[pos=0.5] {h};
\draw[draw=none] (1,2) rectangle (2,1) node[pos=0.5] { };
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {+};
\draw[draw=none] (3,2) rectangle (4,1) node[pos=0.5] { };
\draw (4,2) rectangle (5,1) node[pos=0.5] {m};
\draw[draw=none] (5,2) rectangle (6,1) node[pos=0.5] { };
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] { };
\draw[draw=none] (7,2) rectangle (8,1) node[pos=0.5] {=};
\draw[draw=none] (8,2) rectangle (9,1) node[pos=0.5] { };
\draw (10,2) rectangle (11,1) node[pos=0.5] {m};
\draw (0,1) rectangle (1,0) node[pos=0.5] {m};
\draw[draw=none] (1,1) rectangle (2,0) node[pos=0.5] { };
\draw[draw=none] (2,1) rectangle (3,0) node[pos=0.5] { };
\draw[draw=none] (3,1) rectangle (4,0) node[pos=0.5] { };
\draw (4,1) rectangle (6,0) node[pos=0.5] {h};
\draw[draw=none] (6,1) rectangle (7,0) node[pos=0.5] { };
\draw[draw=none] (7,1) rectangle (8,0) node[pos=0.5] { };
\draw[draw=none] (8,1) rectangle (9,0) node[pos=0.5] { };
\draw (9,1) rectangle (10,0) node[pos=0.5] {m};
\draw (10,1) rectangle (12,0) node[pos=0.5] {h};
\end{tikzpicture}
$$

Following that, we can add the horizontal block in the middle to get a contour with just a single protrusion in
the middle.

$$
\begin{tikzpicture}
\draw (0,3) rectangle (1,1) node[pos=0.5] {v};
\draw (1,3) rectangle (3,2) node[pos=0.5] {h};
\draw[draw=none] (3,3) rectangle (4,2) node[pos=0.5] { };
\draw[draw=none] (4,3) rectangle (5,2) node[pos=0.5] { };
\draw[draw=none] (5,3) rectangle (6,2) node[pos=0.5] { };
\draw[draw=none] (6,3) rectangle (7,2) node[pos=0.5] { };
\draw (7,3) rectangle (8,1) node[pos=0.5] {v};
\draw (8,3) rectangle (10,2) node[pos=0.5] {h};
\draw (1,2) rectangle (2,1) node[pos=0.5] {m};
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] { };
\draw[draw=none] (3,2) rectangle (4,1) node[pos=0.5] {+};
\draw (4,2) rectangle (6,1) node[pos=0.5] {h};
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {=};
\draw (8,2) rectangle (9,1) node[pos=0.5] {m};
\draw (9,2) rectangle (11,1) node[pos=0.5] {h};
\draw (0,1) rectangle (1,0) node[pos=0.5] {m};
\draw (1,1) rectangle (3,0) node[pos=0.5] {h};
\draw[draw=none] (3,1) rectangle (4,0) node[pos=0.5] { };
\draw[draw=none] (4,1) rectangle (5,0) node[pos=0.5] { };
\draw[draw=none] (5,1) rectangle (6,0) node[pos=0.5] { };
\draw[draw=none] (6,1) rectangle (7,0) node[pos=0.5] { };
\draw (7,1) rectangle (8,0) node[pos=0.5] {m};
\draw (8,1) rectangle (10,0) node[pos=0.5] {h};
\end{tikzpicture}
$$

Adding the two monomers on the top and the bottom corners results in a smooth contour:

$$
\begin{tikzpicture}
\draw (0,3) rectangle (1,1) node[pos=0.5] {v};
\draw (1,3) rectangle (3,2) node[pos=0.5] {h};
\draw[draw=none] (3,3) rectangle (4,2) node[pos=0.5] { };
\draw[draw=none] (4,3) rectangle (5,2) node[pos=0.5] { };
\draw (5,3) rectangle (6,2) node[pos=0.5] {m};
\draw[draw=none] (6,3) rectangle (7,2) node[pos=0.5] { };
\draw (7,3) rectangle (8,1) node[pos=0.5] {v};
\draw (8,3) rectangle (10,2) node[pos=0.5] {h};
\draw (10,3) rectangle (11,2) node[pos=0.5] {m};
\draw (1,2) rectangle (2,1) node[pos=0.5] {m};
\draw (2,2) rectangle (4,1) node[pos=0.5] {h};
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {+};
\draw[draw=none] (5,2) rectangle (6,1) node[pos=0.5] { };
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {=};
\draw (8,2) rectangle (9,1) node[pos=0.5] {m};
\draw (9,2) rectangle (11,1) node[pos=0.5] {h};
\draw (0,1) rectangle (1,0) node[pos=0.5] {m};
\draw (1,1) rectangle (3,0) node[pos=0.5] {h};
\draw[draw=none] (3,1) rectangle (4,0) node[pos=0.5] { };
\draw[draw=none] (4,1) rectangle (5,0) node[pos=0.5] { };
\draw (5,1) rectangle (6,0) node[pos=0.5] {m};
\draw[draw=none] (6,1) rectangle (7,0) node[pos=0.5] { };
\draw (7,1) rectangle (8,0) node[pos=0.5] {m};
\draw (8,1) rectangle (10,0) node[pos=0.5] {h};
\draw (10,1) rectangle (11,0) node[pos=0.5] {m};
\end{tikzpicture}
$$

Finally, adding in the final line completes the rectangle

$$
\begin{tikzpicture}
\draw (0,3) rectangle (1,1) node[pos=0.5] {v};
\draw (1,3) rectangle (3,2) node[pos=0.5] {h};
\draw (3,3) rectangle (4,2) node[pos=0.5] {m};
\draw (5,3) rectangle (6,1) node[pos=0.5] {v};
\draw (7,3) rectangle (8,1) node[pos=0.5] {v};
\draw (8,3) rectangle (10,2) node[pos=0.5] {h};
\draw (10,3) rectangle (11,2) node[pos=0.5] {m};
\draw (11,3) rectangle (12,1) node[pos=0.5] {v};
\draw (1,2) rectangle (2,1) node[pos=0.5] {m};
\draw (2,2) rectangle (4,1) node[pos=0.5] {h};
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {+};
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {=};
\draw (8,2) rectangle (9,1) node[pos=0.5] {m};
\draw (9,2) rectangle (11,1) node[pos=0.5] {h};
\draw (0,1) rectangle (1,0) node[pos=0.5] {m};
\draw (1,1) rectangle (3,0) node[pos=0.5] {h};
\draw (3,1) rectangle (4,0) node[pos=0.5] {m};
\draw (5,1) rectangle (6,0) node[pos=0.5] {m};
\draw (7,1) rectangle (8,0) node[pos=0.5] {m};
\draw (8,1) rectangle (10,0) node[pos=0.5] {h};
\draw (10,1) rectangle (11,0) node[pos=0.5] {m};
\draw (11,1) rectangle (12,0) node[pos=0.5] {m};
\end{tikzpicture}
$$