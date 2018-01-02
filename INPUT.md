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
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};
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
\draw[draw=none] (3,2) rectangle (4,1) node[pos=0.5] {\(\times\)};
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
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {\(\times\)};
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
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {\(\times\)};
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

----------------------------------------

You may have noticed above, but there's a set of rules that governs these transformations. For example, suppose
we have a two-prong node, there are two transformations we can make. First, we could add a single monomer and get
a straight-line contour on the rightmost edge.

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw[fill=lightgray!40,draw=none] (1,3) rectangle (2,2);
\draw[fill=lightgray!40,draw=none] (2,3) rectangle (3,2);
\draw[fill=lightgray!40,draw=none] (3,3) rectangle (4,2);
\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);
\draw[fill=lightgray!40,draw=none] (8,3) rectangle (9,2);
\draw[fill=lightgray!40,draw=none] (9,3) rectangle (10,2);
\draw[fill=lightgray!40,draw=none] (10,3) rectangle (11,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[fill=lightgray!40,draw=none] (1,2) rectangle (2,1) node[pos=0.5] {before};
\draw[fill=lightgray!40,draw=none] (2,2) rectangle (3,1);
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {\(\times\)};
\draw (5,2) rectangle (6,1) node[pos=0.5] {m};
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);
\draw[fill=lightgray!40,draw=none] (8,2) rectangle (9,1) node[pos=0.5] {after};
\draw[fill=lightgray!40,draw=none] (9,2) rectangle (10,1);
\draw[fill=lightgray!40,draw=none] (10,2) rectangle (11,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw[fill=lightgray!40,draw=none] (1,1) rectangle (2,0);
\draw[fill=lightgray!40,draw=none] (2,1) rectangle (3,0);
\draw[fill=lightgray!40,draw=none] (3,1) rectangle (4,0);
\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);
\draw[fill=lightgray!40,draw=none] (8,1) rectangle (9,0);
\draw[fill=lightgray!40,draw=none] (9,1) rectangle (10,0);
\draw[fill=lightgray!40,draw=none] (10,1) rectangle (11,0);
\end{tikzpicture}
$$

On the other hand, we could also add in a horizontal block to get a single central hump on the rightmost edge.

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw[fill=lightgray!40,draw=none] (1,3) rectangle (2,2);
\draw[fill=lightgray!40,draw=none] (2,3) rectangle (3,2);
\draw[fill=lightgray!40,draw=none] (3,3) rectangle (4,2);
\draw[fill=lightgray!40,draw=none] (8,3) rectangle (9,2);
\draw[fill=lightgray!40,draw=none] (9,3) rectangle (10,2);
\draw[fill=lightgray!40,draw=none] (10,3) rectangle (11,2);
\draw[fill=lightgray!40,draw=none] (11,3) rectangle (12,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[fill=lightgray!40,draw=none] (1,2) rectangle (2,1) node[pos=0.5] {before};
\draw[fill=lightgray!40,draw=none] (2,2) rectangle (3,1);
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {\(\times\)};
\draw (5,2) rectangle (7,1) node[pos=0.5] {h};
\draw[draw=none] (7,2) rectangle (8,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (8,2) rectangle (9,1);
\draw[fill=lightgray!40,draw=none] (9,2) rectangle (10,1) node[pos=0.5] {after};
\draw[fill=lightgray!40,draw=none] (10,2) rectangle (11,1);
\draw[fill=lightgray!40,draw=none] (11,2) rectangle (12,1);
\draw[fill=lightgray!40,draw=none] (12,2) rectangle (13,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw[fill=lightgray!40,draw=none] (1,1) rectangle (2,0);
\draw[fill=lightgray!40,draw=none] (2,1) rectangle (3,0);
\draw[fill=lightgray!40,draw=none] (3,1) rectangle (4,0);
\draw[fill=lightgray!40,draw=none] (8,1) rectangle (9,0);
\draw[fill=lightgray!40,draw=none] (9,1) rectangle (10,0);
\draw[fill=lightgray!40,draw=none] (10,1) rectangle (11,0);
\draw[fill=lightgray!40,draw=none] (11,1) rectangle (12,0);
\end{tikzpicture}
$$

If we don't care about what the blocks on the right-most side are, we can actually characterize these
operational rules by just specifying transformations of the right-most contours. The above rules generates
the following operational equations for the contours:

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw[fill=lightgray!40,draw=none] (1,3) rectangle (2,2);
\draw[fill=lightgray!40,draw=none] (6,3) rectangle (7,2);
\draw[fill=lightgray!40,draw=none] (9,3) rectangle (10,2);
\draw[fill=lightgray!40,draw=none] (10,3) rectangle (11,2);
\draw[fill=lightgray!40,draw=none] (14,3) rectangle (15,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};
\draw (3,2) rectangle (5,1) node[pos=0.5] {h};
\draw[draw=none] (5,2) rectangle (6,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (6,2) rectangle (7,1);
\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);
\draw[draw=none] (8,2) rectangle (9,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (9,2) rectangle (10,1);
\draw[draw=none] (11,2) rectangle (12,1) node[pos=0.5] {\(\times\)};
\draw (12,2) rectangle (13,1) node[pos=0.5] {m};
\draw[draw=none] (13,2) rectangle (14,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (14,2) rectangle (15,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw[fill=lightgray!40,draw=none] (1,1) rectangle (2,0);
\draw[fill=lightgray!40,draw=none] (6,1) rectangle (7,0);
\draw[fill=lightgray!40,draw=none] (9,1) rectangle (10,0);
\draw[fill=lightgray!40,draw=none] (10,1) rectangle (11,0);
\draw[fill=lightgray!40,draw=none] (14,1) rectangle (15,0);
\end{tikzpicture}
$$

As an another example, here are all of the equations that governs the behavior of L-shaped edges.

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw (3,3) rectangle (4,1) node[pos=0.5] {v};
\draw[fill=lightgray!40,draw=none] (5,3) rectangle (6,2);
\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);
\draw (10,3) rectangle (11,2) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (12,3) rectangle (13,2);
\draw[fill=lightgray!40,draw=none] (13,3) rectangle (14,2);
\draw[fill=lightgray!40,draw=none] (15,3) rectangle (16,2);
\draw[fill=lightgray!40,draw=none] (20,3) rectangle (21,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (5,2) rectangle (6,1);
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);
\draw[draw=none] (9,2) rectangle (10,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (11,2) rectangle (12,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (12,2) rectangle (13,1);
\draw[draw=none] (14,2) rectangle (15,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (15,2) rectangle (16,1);
\draw[draw=none] (17,2) rectangle (18,1) node[pos=0.5] {\(\times\)};
\draw (18,2) rectangle (19,1) node[pos=0.5] {m};
\draw[draw=none] (19,2) rectangle (20,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (20,2) rectangle (21,1);
\draw[fill=lightgray!40,draw=none] (21,2) rectangle (22,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw[fill=lightgray!40,draw=none] (1,1) rectangle (2,0);
\draw[fill=lightgray!40,draw=none] (5,1) rectangle (6,0);
\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);
\draw[fill=lightgray!40,draw=none] (8,1) rectangle (9,0);
\draw[fill=lightgray!40,draw=none] (12,1) rectangle (13,0);
\draw[fill=lightgray!40,draw=none] (13,1) rectangle (14,0);
\draw[fill=lightgray!40,draw=none] (15,1) rectangle (16,0);
\draw[fill=lightgray!40,draw=none] (16,1) rectangle (17,0);
\draw[fill=lightgray!40,draw=none] (20,1) rectangle (21,0);
\draw[fill=lightgray!40,draw=none] (21,1) rectangle (22,0);
\end{tikzpicture}
$$

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw (3,3) rectangle (4,2) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (5,3) rectangle (6,2);
\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);
\draw (10,3) rectangle (12,2) node[pos=0.5] {h};
\draw[fill=lightgray!40,draw=none] (13,3) rectangle (14,2);
\draw[fill=lightgray!40,draw=none] (14,3) rectangle (15,2);
\draw[fill=lightgray!40,draw=none] (16,3) rectangle (17,2);
\draw (19,3) rectangle (20,2) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (22,3) rectangle (23,2);
\draw[fill=lightgray!40,draw=none] (25,3) rectangle (26,2);
\draw (28,3) rectangle (30,2) node[pos=0.5] {h};
\draw[fill=lightgray!40,draw=none] (31,3) rectangle (32,2);
\draw[fill=lightgray!40,draw=none] (32,3) rectangle (33,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};
\draw (3,2) rectangle (4,1) node[pos=0.5] {m};
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (5,2) rectangle (6,1);
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);
\draw[draw=none] (9,2) rectangle (10,1) node[pos=0.5] {\(\times\)};
\draw (10,2) rectangle (12,1) node[pos=0.5] {h};
\draw[draw=none] (12,2) rectangle (13,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (13,2) rectangle (14,1);
\draw[fill=lightgray!40,draw=none] (14,2) rectangle (15,1);
\draw[draw=none] (15,2) rectangle (16,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (16,2) rectangle (17,1);
\draw[draw=none] (18,2) rectangle (19,1) node[pos=0.5] {\(\times\)};
\draw (19,2) rectangle (21,1) node[pos=0.5] {h};
\draw[draw=none] (21,2) rectangle (22,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (22,2) rectangle (23,1);
\draw[fill=lightgray!40,draw=none] (23,2) rectangle (24,1);
\draw[draw=none] (24,2) rectangle (25,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (25,2) rectangle (26,1);
\draw[draw=none] (27,2) rectangle (28,1) node[pos=0.5] {\(\times\)};
\draw (28,2) rectangle (29,1) node[pos=0.5] {m};
\draw[draw=none] (30,2) rectangle (31,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (31,2) rectangle (32,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw[fill=lightgray!40,draw=none] (1,1) rectangle (2,0);
\draw[fill=lightgray!40,draw=none] (5,1) rectangle (6,0);
\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);
\draw[fill=lightgray!40,draw=none] (8,1) rectangle (9,0);
\draw[fill=lightgray!40,draw=none] (13,1) rectangle (14,0);
\draw[fill=lightgray!40,draw=none] (16,1) rectangle (17,0);
\draw[fill=lightgray!40,draw=none] (17,1) rectangle (18,0);
\draw[fill=lightgray!40,draw=none] (22,1) rectangle (23,0);
\draw[fill=lightgray!40,draw=none] (25,1) rectangle (26,0);
\draw[fill=lightgray!40,draw=none] (26,1) rectangle (27,0);
\draw[fill=lightgray!40,draw=none] (31,1) rectangle (32,0);
\end{tikzpicture}
$$

The above L-contour generalizes for its reflection, and the C shaped contour generalizes to all contours with
a single hole:

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw[fill=lightgray!40,draw=none] (1,3) rectangle (2,2);
\draw[fill=lightgray!40,draw=none] (5,3) rectangle (6,2);
\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);
\draw[fill=lightgray!40,draw=none] (8,3) rectangle (9,2);
\draw[fill=lightgray!40,draw=none] (12,3) rectangle (13,2);
\draw[fill=lightgray!40,draw=none] (13,3) rectangle (14,2);
\draw[fill=lightgray!40,draw=none] (15,3) rectangle (16,2);
\draw[fill=lightgray!40,draw=none] (16,3) rectangle (17,2);
\draw[fill=lightgray!40,draw=none] (20,3) rectangle (21,2);
\draw[fill=lightgray!40,draw=none] (21,3) rectangle (22,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};
\draw (3,2) rectangle (4,0) node[pos=0.5] {v};
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (5,2) rectangle (6,1);
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);
\draw[draw=none] (9,2) rectangle (10,1) node[pos=0.5] {\(\times\)};
\draw (10,2) rectangle (11,1) node[pos=0.5] {m};
\draw[draw=none] (11,2) rectangle (12,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (12,2) rectangle (13,1);
\draw[fill=lightgray!40,draw=none] (13,2) rectangle (14,1);
\draw[draw=none] (14,2) rectangle (15,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (15,2) rectangle (16,1);
\draw[draw=none] (17,2) rectangle (18,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (19,2) rectangle (20,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (20,2) rectangle (21,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw[fill=lightgray!40,draw=none] (5,1) rectangle (6,0);
\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);
\draw[fill=lightgray!40,draw=none] (12,1) rectangle (13,0);
\draw[fill=lightgray!40,draw=none] (15,1) rectangle (16,0);
\draw (18,1) rectangle (19,0) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (20,1) rectangle (21,0);
\draw[fill=lightgray!40,draw=none] (21,1) rectangle (22,0);
\end{tikzpicture}
$$

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw[fill=lightgray!40,draw=none] (1,3) rectangle (2,2);
\draw[fill=lightgray!40,draw=none] (5,3) rectangle (6,2);
\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);
\draw[fill=lightgray!40,draw=none] (8,3) rectangle (9,2);
\draw[fill=lightgray!40,draw=none] (13,3) rectangle (14,2);
\draw[fill=lightgray!40,draw=none] (16,3) rectangle (17,2);
\draw[fill=lightgray!40,draw=none] (17,3) rectangle (18,2);
\draw[fill=lightgray!40,draw=none] (22,3) rectangle (23,2);
\draw[fill=lightgray!40,draw=none] (25,3) rectangle (26,2);
\draw[fill=lightgray!40,draw=none] (26,3) rectangle (27,2);
\draw[fill=lightgray!40,draw=none] (31,3) rectangle (32,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};
\draw (3,2) rectangle (4,1) node[pos=0.5] {m};
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (5,2) rectangle (6,1);
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);
\draw[draw=none] (9,2) rectangle (10,1) node[pos=0.5] {\(\times\)};
\draw (10,2) rectangle (12,1) node[pos=0.5] {h};
\draw[draw=none] (12,2) rectangle (13,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (13,2) rectangle (14,1);
\draw[fill=lightgray!40,draw=none] (14,2) rectangle (15,1);
\draw[draw=none] (15,2) rectangle (16,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (16,2) rectangle (17,1);
\draw[draw=none] (18,2) rectangle (19,1) node[pos=0.5] {\(\times\)};
\draw (19,2) rectangle (21,1) node[pos=0.5] {h};
\draw[draw=none] (21,2) rectangle (22,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (22,2) rectangle (23,1);
\draw[fill=lightgray!40,draw=none] (23,2) rectangle (24,1);
\draw[draw=none] (24,2) rectangle (25,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (25,2) rectangle (26,1);
\draw[draw=none] (27,2) rectangle (28,1) node[pos=0.5] {\(\times\)};
\draw (28,2) rectangle (29,1) node[pos=0.5] {m};
\draw[draw=none] (30,2) rectangle (31,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (31,2) rectangle (32,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw (3,1) rectangle (4,0) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (5,1) rectangle (6,0);
\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);
\draw (10,1) rectangle (12,0) node[pos=0.5] {h};
\draw[fill=lightgray!40,draw=none] (13,1) rectangle (14,0);
\draw[fill=lightgray!40,draw=none] (14,1) rectangle (15,0);
\draw[fill=lightgray!40,draw=none] (16,1) rectangle (17,0);
\draw (19,1) rectangle (20,0) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (22,1) rectangle (23,0);
\draw[fill=lightgray!40,draw=none] (25,1) rectangle (26,0);
\draw (28,1) rectangle (30,0) node[pos=0.5] {h};
\draw[fill=lightgray!40,draw=none] (31,1) rectangle (32,0);
\draw[fill=lightgray!40,draw=none] (32,1) rectangle (33,0);
\end{tikzpicture}
$$

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw[fill=lightgray!40,draw=none] (1,3) rectangle (2,2);
\draw[fill=lightgray!40,draw=none] (6,3) rectangle (7,2);
\draw[fill=lightgray!40,draw=none] (9,3) rectangle (10,2);
\draw[fill=lightgray!40,draw=none] (10,3) rectangle (11,2);
\draw[fill=lightgray!40,draw=none] (14,3) rectangle (15,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[fill=lightgray!40,draw=none] (1,2) rectangle (2,1);
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (5,2) rectangle (6,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (6,2) rectangle (7,1);
\draw[draw=none] (8,2) rectangle (9,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (9,2) rectangle (10,1);
\draw[fill=lightgray!40,draw=none] (10,2) rectangle (11,1);
\draw[draw=none] (11,2) rectangle (12,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (13,2) rectangle (14,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (14,2) rectangle (15,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw (3,1) rectangle (5,0) node[pos=0.5] {h};
\draw[fill=lightgray!40,draw=none] (6,1) rectangle (7,0);
\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);
\draw[fill=lightgray!40,draw=none] (9,1) rectangle (10,0);
\draw (12,1) rectangle (13,0) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (14,1) rectangle (15,0);
\end{tikzpicture}
$$

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw (3,3) rectangle (5,2) node[pos=0.5] {h};
\draw[fill=lightgray!40,draw=none] (6,3) rectangle (7,2);
\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);
\draw[fill=lightgray!40,draw=none] (9,3) rectangle (10,2);
\draw (12,3) rectangle (13,2) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (14,3) rectangle (15,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[fill=lightgray!40,draw=none] (1,2) rectangle (2,1);
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (5,2) rectangle (6,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (6,2) rectangle (7,1);
\draw[draw=none] (8,2) rectangle (9,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (9,2) rectangle (10,1);
\draw[fill=lightgray!40,draw=none] (10,2) rectangle (11,1);
\draw[draw=none] (11,2) rectangle (12,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (13,2) rectangle (14,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (14,2) rectangle (15,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw[fill=lightgray!40,draw=none] (1,1) rectangle (2,0);
\draw[fill=lightgray!40,draw=none] (6,1) rectangle (7,0);
\draw[fill=lightgray!40,draw=none] (9,1) rectangle (10,0);
\draw[fill=lightgray!40,draw=none] (10,1) rectangle (11,0);
\draw[fill=lightgray!40,draw=none] (14,1) rectangle (15,0);
\end{tikzpicture}
$$

We couldn't generalize the single-hump in the middle contour in the above example, but we can enumerate
their equations explicitly.

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw (3,3) rectangle (4,2) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (5,3) rectangle (6,2);
\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);
\draw (10,3) rectangle (12,2) node[pos=0.5] {h};
\draw[fill=lightgray!40,draw=none] (13,3) rectangle (14,2);
\draw[fill=lightgray!40,draw=none] (14,3) rectangle (15,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[fill=lightgray!40,draw=none] (1,2) rectangle (2,1);
\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (5,2) rectangle (6,1);
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);
\draw[fill=lightgray!40,draw=none] (8,2) rectangle (9,1);
\draw[draw=none] (9,2) rectangle (10,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (12,2) rectangle (13,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (13,2) rectangle (14,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw (3,1) rectangle (4,0) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (5,1) rectangle (6,0);
\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);
\draw (10,1) rectangle (12,0) node[pos=0.5] {h};
\draw[fill=lightgray!40,draw=none] (13,1) rectangle (14,0);
\draw[fill=lightgray!40,draw=none] (14,1) rectangle (15,0);
\end{tikzpicture}
$$

Finally, let's enumerate the set of equations that starts off from the smooth contour.

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw (2,3) rectangle (3,2) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (4,3) rectangle (5,2);
\draw[fill=lightgray!40,draw=none] (5,3) rectangle (6,2);
\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);
\draw[fill=lightgray!40,draw=none] (11,3) rectangle (12,2);
\draw[fill=lightgray!40,draw=none] (14,3) rectangle (15,2);
\draw[fill=lightgray!40,draw=none] (18,3) rectangle (19,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[draw=none] (1,2) rectangle (2,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (3,2) rectangle (4,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (4,2) rectangle (5,1);
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);
\draw[draw=none] (8,2) rectangle (9,1) node[pos=0.5] {\(\times\)};
\draw (9,2) rectangle (10,1) node[pos=0.5] {m};
\draw[draw=none] (10,2) rectangle (11,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (11,2) rectangle (12,1);
\draw[fill=lightgray!40,draw=none] (12,2) rectangle (13,1);
\draw[draw=none] (13,2) rectangle (14,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (14,2) rectangle (15,1);
\draw[draw=none] (15,2) rectangle (16,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (17,2) rectangle (18,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (18,2) rectangle (19,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw[fill=lightgray!40,draw=none] (4,1) rectangle (5,0);
\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);
\draw[fill=lightgray!40,draw=none] (11,1) rectangle (12,0);
\draw[fill=lightgray!40,draw=none] (14,1) rectangle (15,0);
\draw (16,1) rectangle (17,0) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (18,1) rectangle (19,0);
\draw[fill=lightgray!40,draw=none] (19,1) rectangle (20,0);
\end{tikzpicture}
$$

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw (2,3) rectangle (3,2) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (4,3) rectangle (5,2);
\draw[fill=lightgray!40,draw=none] (5,3) rectangle (6,2);
\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);
\draw[fill=lightgray!40,draw=none] (11,3) rectangle (12,2);
\draw[fill=lightgray!40,draw=none] (14,3) rectangle (15,2);
\draw (16,3) rectangle (17,2) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (18,3) rectangle (19,2);
\draw[fill=lightgray!40,draw=none] (19,3) rectangle (20,2);
\draw[fill=lightgray!40,draw=none] (21,3) rectangle (22,2);
\draw (23,3) rectangle (24,2) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (25,3) rectangle (26,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[draw=none] (1,2) rectangle (2,1) node[pos=0.5] {\(\times\)};
\draw (2,2) rectangle (3,1) node[pos=0.5] {m};
\draw[draw=none] (3,2) rectangle (4,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (4,2) rectangle (5,1);
\draw[fill=lightgray!40,draw=none] (5,2) rectangle (6,1);
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);
\draw[draw=none] (8,2) rectangle (9,1) node[pos=0.5] {\(\times\)};
\draw (9,2) rectangle (10,1) node[pos=0.5] {m};
\draw[draw=none] (10,2) rectangle (11,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (11,2) rectangle (12,1);
\draw[fill=lightgray!40,draw=none] (12,2) rectangle (13,1);
\draw[draw=none] (13,2) rectangle (14,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (14,2) rectangle (15,1);
\draw[draw=none] (15,2) rectangle (16,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (17,2) rectangle (18,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (18,2) rectangle (19,1);
\draw[draw=none] (20,2) rectangle (21,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (21,2) rectangle (22,1);
\draw[draw=none] (22,2) rectangle (23,1) node[pos=0.5] {\(\times\)};
\draw (23,2) rectangle (24,1) node[pos=0.5] {m};
\draw[draw=none] (24,2) rectangle (25,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (25,2) rectangle (26,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw[fill=lightgray!40,draw=none] (4,1) rectangle (5,0);
\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);
\draw (9,1) rectangle (10,0) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (11,1) rectangle (12,0);
\draw[fill=lightgray!40,draw=none] (12,1) rectangle (13,0);
\draw[fill=lightgray!40,draw=none] (14,1) rectangle (15,0);
\draw (16,1) rectangle (17,0) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (18,1) rectangle (19,0);
\draw[fill=lightgray!40,draw=none] (19,1) rectangle (20,0);
\draw[fill=lightgray!40,draw=none] (21,1) rectangle (22,0);
\draw (23,1) rectangle (24,0) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (25,1) rectangle (26,0);
\end{tikzpicture}
$$

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw (2,3) rectangle (3,1) node[pos=0.5] {v};
\draw[fill=lightgray!40,draw=none] (4,3) rectangle (5,2);
\draw[fill=lightgray!40,draw=none] (5,3) rectangle (6,2);
\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);
\draw[fill=lightgray!40,draw=none] (11,3) rectangle (12,2);
\draw[fill=lightgray!40,draw=none] (14,3) rectangle (15,2);
\draw (16,3) rectangle (17,1) node[pos=0.5] {v};
\draw[fill=lightgray!40,draw=none] (18,3) rectangle (19,2);
\draw[fill=lightgray!40,draw=none] (20,3) rectangle (21,2);
\draw (22,3) rectangle (23,2) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (24,3) rectangle (25,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[draw=none] (1,2) rectangle (2,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (3,2) rectangle (4,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (4,2) rectangle (5,1);
\draw[fill=lightgray!40,draw=none] (5,2) rectangle (6,1);
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);
\draw[draw=none] (8,2) rectangle (9,1) node[pos=0.5] {\(\times\)};
\draw (9,2) rectangle (10,0) node[pos=0.5] {v};
\draw[draw=none] (10,2) rectangle (11,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (11,2) rectangle (12,1);
\draw[fill=lightgray!40,draw=none] (12,2) rectangle (13,1);
\draw[draw=none] (13,2) rectangle (14,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (14,2) rectangle (15,1);
\draw[draw=none] (15,2) rectangle (16,1) node[pos=0.5] {\(\times\)};
\draw[draw=none] (17,2) rectangle (18,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (18,2) rectangle (19,1);
\draw[draw=none] (19,2) rectangle (20,1) node[pos=0.5] {or};
\draw[fill=lightgray!40,draw=none] (20,2) rectangle (21,1);
\draw[draw=none] (21,2) rectangle (22,1) node[pos=0.5] {\(\times\)};
\draw (22,2) rectangle (23,0) node[pos=0.5] {v};
\draw[draw=none] (23,2) rectangle (24,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (24,2) rectangle (25,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw[fill=lightgray!40,draw=none] (4,1) rectangle (5,0);
\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);
\draw[fill=lightgray!40,draw=none] (11,1) rectangle (12,0);
\draw[fill=lightgray!40,draw=none] (12,1) rectangle (13,0);
\draw[fill=lightgray!40,draw=none] (14,1) rectangle (15,0);
\draw (16,1) rectangle (17,0) node[pos=0.5] {m};
\draw[fill=lightgray!40,draw=none] (18,1) rectangle (19,0);
\draw[fill=lightgray!40,draw=none] (20,1) rectangle (21,0);
\draw[fill=lightgray!40,draw=none] (24,1) rectangle (25,0);
\end{tikzpicture}
$$

$$
\begin{tikzpicture}
\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);
\draw (2,3) rectangle (4,2) node[pos=0.5] {h};
\draw[fill=lightgray!40,draw=none] (5,3) rectangle (6,2);
\draw[fill=lightgray!40,draw=none] (9,3) rectangle (10,2);
\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);
\draw[draw=none] (1,2) rectangle (2,1) node[pos=0.5] {\(\times\)};
\draw (2,2) rectangle (4,1) node[pos=0.5] {h};
\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (5,2) rectangle (6,1);
\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {or};
\draw[draw=none] (8,2) rectangle (9,1) node[pos=0.5] {=};
\draw[fill=lightgray!40,draw=none] (9,2) rectangle (10,1);
\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);
\draw (2,1) rectangle (4,0) node[pos=0.5] {h};
\draw[fill=lightgray!40,draw=none] (5,1) rectangle (6,0);
\draw[fill=lightgray!40,draw=none] (9,1) rectangle (10,0);
\end{tikzpicture}
$$
