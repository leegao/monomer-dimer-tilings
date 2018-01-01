# Tiling 3-by-N rectangles with Monomers and Dimers

Convoluted solution for the monomer-dimer tiling problem.

Suppose one is given pieces that may
be one of the three forms: monomers (<img alt="$m$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/0e51a2dede42189d77627c4d742822c3.svg?invert_in_darkmode" align=middle width="14.43321pt" height="14.15535pt"/>) that are <img alt="$1 \times 1$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/d12ef2fd91d2a991710509cae7229134.svg?invert_in_darkmode" align=middle width="36.52968pt" height="21.18732pt"/> squares, and dimers that are dominoes,
either vertically (<img alt="$v$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/6c4adbc36120d62b98deef2a20d5d303.svg?invert_in_darkmode" align=middle width="8.55789pt" height="14.15535pt"/>) oriented <img alt="$1 \times 2$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/6a178d559af5ef9cb672b85caf00d739.svg?invert_in_darkmode" align=middle width="36.52968pt" height="21.18732pt"/>, or horizontally (<img alt="$h$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/2ad9d098b937e46f9f58968551adac57.svg?invert_in_darkmode" align=middle width="9.471165pt" height="22.83138pt"/>) oriented <img alt="$2 \times 1$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/56cbb95ecc0b4e113e6fb1cd93b761b5.svg?invert_in_darkmode" align=middle width="36.52968pt" height="21.18732pt"/>. In how many ways can
a <img alt="$n \times 3$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/e13165a13b4e02249c42e972e74b4e17.svg?invert_in_darkmode" align=middle width="38.17737pt" height="21.18732pt"/> rectangle be covered completely and without overlap ("tiled") by such pieces?

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,0) rectangle (1,1) node[pos=0.5] {m};&#10;\draw (2,0) rectangle (4,1) node[pos=0.5] {h};&#10;\draw (5,1.5) rectangle (6,-0.5) node[pos=0.5] {v};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/11333ed87889acc204fd6107f7776597.svg?invert_in_darkmode" align=middle width="281.2953pt" height="94.207245pt"/></p>

------------------------

For example, here's a <img alt="$3 \times 2$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/d2a207b1ddb2c07906d819cec40e6c49.svg?invert_in_darkmode" align=middle width="36.52968pt" height="21.18732pt"/> rectangular tiling:

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,3) rectangle (2,2) node[pos=0.5] {h};&#10;\draw (0,2) rectangle (2,1) node[pos=0.5] {h};&#10;\draw (0,1) rectangle (1,0) node[pos=0.5] {m};&#10;\draw (1,1) rectangle (2,0) node[pos=0.5] {m};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/a9d3ff2c080871833fa3ac5b8d610d0a.svg?invert_in_darkmode" align=middle width="94.20081pt" height="140.98095pt"/></p>

or this <img alt="$3 \times 5$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/dd4efd8ab53bf4a40a0ee5e4c06cbdbf.svg?invert_in_darkmode" align=middle width="36.52968pt" height="21.18732pt"/> rectangular tiling:

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,3) rectangle (1,1) node[pos=0.5] {v};&#10;\draw (1,3) rectangle (3,2) node[pos=0.5] {h};&#10;\draw (3,3) rectangle (4,2) node[pos=0.5] {m};&#10;\draw (4,3) rectangle (5,1) node[pos=0.5] {v};&#10;\draw (1,2) rectangle (2,1) node[pos=0.5] {m};&#10;\draw (2,2) rectangle (4,1) node[pos=0.5] {h};&#10;\draw (0,1) rectangle (1,0) node[pos=0.5] {m};&#10;\draw (1,1) rectangle (3,0) node[pos=0.5] {h};&#10;\draw (3,1) rectangle (4,0) node[pos=0.5] {m};&#10;\draw (4,1) rectangle (5,0) node[pos=0.5] {m};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/dda00bb5c7ede5c37b4ae8b3b3b0350c.svg?invert_in_darkmode" align=middle width="234.5145pt" height="140.98095pt"/></p>

There are various exact enumerations for this problem (e.g. see http://algo.inria.fr/libraries/autocomb/MonoDiMer-html/MonoDiMer.html),
but we'd like to approach this with a combination of enumerative combinatorics and computer programming to ease the tedious analysis.
In particular, we'd like to reduce this problem into finding the singularities of a complex rational function.

-----------------------------------------------------

In the <img alt="$3 \times 5$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/dd4efd8ab53bf4a40a0ee5e4c06cbdbf.svg?invert_in_darkmode" align=middle width="36.52968pt" height="21.18732pt"/> example above, we can consider the tiling process as a sequence of constructions. We start
with the <img alt="$3 \times 1$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/381872314d30ee5ea556f738a0875a68.svg?invert_in_darkmode" align=middle width="36.52968pt" height="21.18732pt"/> line at the beginning:

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,3) rectangle (1,1) node[pos=0.5] {v};&#10;\draw (0,1) rectangle (1,0) node[pos=0.5] {m};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/4541228356af488f7d8ade3126ebc02f.svg?invert_in_darkmode" align=middle width="47.43354pt" height="140.98095pt"/></p>

Next, the natural thing to do would be to add the horizontal block at the top of the second column. However,
for reasons that will become clear soon, let's artificially restrict our rules to allow the total gap at the
end of the blocks to be at most one-block wide. That is, we will always ensure that the contour edge of
our work-in-progress "rectangle" will only have holes that are "shallow" enough to be filled by a monomer.

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,3) rectangle (1,1) node[pos=0.5] {v};&#10;\draw[draw=none] (1,3) rectangle (2,2) node[pos=0.5] { };&#10;\draw[draw=none] (2,3) rectangle (3,2) node[pos=0.5] { };&#10;\draw[draw=none] (3,3) rectangle (4,2) node[pos=0.5] { };&#10;\draw (4,3) rectangle (6,2) node[pos=0.5] {h};&#10;\draw[draw=none] (6,3) rectangle (7,2) node[pos=0.5] { };&#10;\draw[draw=none] (7,3) rectangle (8,2) node[pos=0.5] { };&#10;\draw[draw=none] (8,3) rectangle (9,2) node[pos=0.5] { };&#10;\draw (9,3) rectangle (10,1) node[pos=0.5] {v};&#10;\draw (10,3) rectangle (12,2) node[pos=0.5] {h};&#10;\draw[draw=none] (1,2) rectangle (2,1) node[pos=0.5] { };&#10;\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};&#10;\draw[draw=none] (3,2) rectangle (4,1) node[pos=0.5] { };&#10;\draw (4,2) rectangle (5,1) node[pos=0.5] {m};&#10;\draw[draw=none] (5,2) rectangle (6,1) node[pos=0.5] { };&#10;\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] { };&#10;\draw[draw=none] (7,2) rectangle (8,1) node[pos=0.5] {=};&#10;\draw[draw=none] (8,2) rectangle (9,1) node[pos=0.5] { };&#10;\draw (10,2) rectangle (11,1) node[pos=0.5] {m};&#10;\draw (0,1) rectangle (1,0) node[pos=0.5] {m};&#10;\draw[draw=none] (1,1) rectangle (2,0) node[pos=0.5] { };&#10;\draw[draw=none] (2,1) rectangle (3,0) node[pos=0.5] { };&#10;\draw[draw=none] (3,1) rectangle (4,0) node[pos=0.5] { };&#10;\draw (4,1) rectangle (6,0) node[pos=0.5] {h};&#10;\draw[draw=none] (6,1) rectangle (7,0) node[pos=0.5] { };&#10;\draw[draw=none] (7,1) rectangle (8,0) node[pos=0.5] { };&#10;\draw[draw=none] (8,1) rectangle (9,0) node[pos=0.5] { };&#10;\draw (9,1) rectangle (10,0) node[pos=0.5] {m};&#10;\draw (10,1) rectangle (12,0) node[pos=0.5] {h};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/29f069b9ab250eb503543a23761e52d1.svg?invert_in_darkmode" align=middle width="561.9306pt" height="140.98095pt"/></p>

Following that, we can add the horizontal block in the middle to get a contour with just a single protrusion in
the middle.

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,3) rectangle (1,1) node[pos=0.5] {v};&#10;\draw (1,3) rectangle (3,2) node[pos=0.5] {h};&#10;\draw[draw=none] (3,3) rectangle (4,2) node[pos=0.5] { };&#10;\draw[draw=none] (4,3) rectangle (5,2) node[pos=0.5] { };&#10;\draw[draw=none] (5,3) rectangle (6,2) node[pos=0.5] { };&#10;\draw[draw=none] (6,3) rectangle (7,2) node[pos=0.5] { };&#10;\draw (7,3) rectangle (8,1) node[pos=0.5] {v};&#10;\draw (8,3) rectangle (10,2) node[pos=0.5] {h};&#10;\draw (1,2) rectangle (2,1) node[pos=0.5] {m};&#10;\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] { };&#10;\draw[draw=none] (3,2) rectangle (4,1) node[pos=0.5] {\(\times\)};&#10;\draw (4,2) rectangle (6,1) node[pos=0.5] {h};&#10;\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {=};&#10;\draw (8,2) rectangle (9,1) node[pos=0.5] {m};&#10;\draw (9,2) rectangle (11,1) node[pos=0.5] {h};&#10;\draw (0,1) rectangle (1,0) node[pos=0.5] {m};&#10;\draw (1,1) rectangle (3,0) node[pos=0.5] {h};&#10;\draw[draw=none] (3,1) rectangle (4,0) node[pos=0.5] { };&#10;\draw[draw=none] (4,1) rectangle (5,0) node[pos=0.5] { };&#10;\draw[draw=none] (5,1) rectangle (6,0) node[pos=0.5] { };&#10;\draw[draw=none] (6,1) rectangle (7,0) node[pos=0.5] { };&#10;\draw (7,1) rectangle (8,0) node[pos=0.5] {m};&#10;\draw (8,1) rectangle (10,0) node[pos=0.5] {h};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/96d6a4e13305596b7673eae38318048c.svg?invert_in_darkmode" align=middle width="515.1564pt" height="140.98095pt"/></p>

Adding the two monomers on the top and the bottom corners results in a smooth contour:

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,3) rectangle (1,1) node[pos=0.5] {v};&#10;\draw (1,3) rectangle (3,2) node[pos=0.5] {h};&#10;\draw[draw=none] (3,3) rectangle (4,2) node[pos=0.5] { };&#10;\draw[draw=none] (4,3) rectangle (5,2) node[pos=0.5] { };&#10;\draw (5,3) rectangle (6,2) node[pos=0.5] {m};&#10;\draw[draw=none] (6,3) rectangle (7,2) node[pos=0.5] { };&#10;\draw (7,3) rectangle (8,1) node[pos=0.5] {v};&#10;\draw (8,3) rectangle (10,2) node[pos=0.5] {h};&#10;\draw (10,3) rectangle (11,2) node[pos=0.5] {m};&#10;\draw (1,2) rectangle (2,1) node[pos=0.5] {m};&#10;\draw (2,2) rectangle (4,1) node[pos=0.5] {h};&#10;\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {\(\times\)};&#10;\draw[draw=none] (5,2) rectangle (6,1) node[pos=0.5] { };&#10;\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {=};&#10;\draw (8,2) rectangle (9,1) node[pos=0.5] {m};&#10;\draw (9,2) rectangle (11,1) node[pos=0.5] {h};&#10;\draw (0,1) rectangle (1,0) node[pos=0.5] {m};&#10;\draw (1,1) rectangle (3,0) node[pos=0.5] {h};&#10;\draw[draw=none] (3,1) rectangle (4,0) node[pos=0.5] { };&#10;\draw[draw=none] (4,1) rectangle (5,0) node[pos=0.5] { };&#10;\draw (5,1) rectangle (6,0) node[pos=0.5] {m};&#10;\draw[draw=none] (6,1) rectangle (7,0) node[pos=0.5] { };&#10;\draw (7,1) rectangle (8,0) node[pos=0.5] {m};&#10;\draw (8,1) rectangle (10,0) node[pos=0.5] {h};&#10;\draw (10,1) rectangle (11,0) node[pos=0.5] {m};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/a71eb302a120806870fd6f9553dba012.svg?invert_in_darkmode" align=middle width="515.1564pt" height="140.98095pt"/></p>

Finally, adding in the final line completes the rectangle

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,3) rectangle (1,1) node[pos=0.5] {v};&#10;\draw (1,3) rectangle (3,2) node[pos=0.5] {h};&#10;\draw (3,3) rectangle (4,2) node[pos=0.5] {m};&#10;\draw (5,3) rectangle (6,1) node[pos=0.5] {v};&#10;\draw (7,3) rectangle (8,1) node[pos=0.5] {v};&#10;\draw (8,3) rectangle (10,2) node[pos=0.5] {h};&#10;\draw (10,3) rectangle (11,2) node[pos=0.5] {m};&#10;\draw (11,3) rectangle (12,1) node[pos=0.5] {v};&#10;\draw (1,2) rectangle (2,1) node[pos=0.5] {m};&#10;\draw (2,2) rectangle (4,1) node[pos=0.5] {h};&#10;\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {\(\times\)};&#10;\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {=};&#10;\draw (8,2) rectangle (9,1) node[pos=0.5] {m};&#10;\draw (9,2) rectangle (11,1) node[pos=0.5] {h};&#10;\draw (0,1) rectangle (1,0) node[pos=0.5] {m};&#10;\draw (1,1) rectangle (3,0) node[pos=0.5] {h};&#10;\draw (3,1) rectangle (4,0) node[pos=0.5] {m};&#10;\draw (5,1) rectangle (6,0) node[pos=0.5] {m};&#10;\draw (7,1) rectangle (8,0) node[pos=0.5] {m};&#10;\draw (8,1) rectangle (10,0) node[pos=0.5] {h};&#10;\draw (10,1) rectangle (11,0) node[pos=0.5] {m};&#10;\draw (11,1) rectangle (12,0) node[pos=0.5] {m};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/9c2735a3bdb97b4e67450efd44de1d7a.svg?invert_in_darkmode" align=middle width="561.9306pt" height="140.98095pt"/></p>

----------------------------------------

You may have noticed above, but there's a set of rules that governs these transformations. For example, suppose
we have a two-prong node, there are two transformations we can make. First, we could add a single monomer and get
a straight-line contour on the rightmost edge.

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);&#10;\draw[fill=lightgray!40,draw=none] (1,3) rectangle (2,2);&#10;\draw[fill=lightgray!40,draw=none] (2,3) rectangle (3,2);&#10;\draw[fill=lightgray!40,draw=none] (3,3) rectangle (4,2);&#10;\draw[fill=lightgray!40,draw=none] (7,3) rectangle (8,2);&#10;\draw[fill=lightgray!40,draw=none] (8,3) rectangle (9,2);&#10;\draw[fill=lightgray!40,draw=none] (9,3) rectangle (10,2);&#10;\draw[fill=lightgray!40,draw=none] (10,3) rectangle (11,2);&#10;\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);&#10;\draw[fill=lightgray!40,draw=none] (1,2) rectangle (2,1) node[pos=0.5] {before};&#10;\draw[fill=lightgray!40,draw=none] (2,2) rectangle (3,1);&#10;\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {\(\times\)};&#10;\draw (5,2) rectangle (6,1) node[pos=0.5] {m};&#10;\draw[draw=none] (6,2) rectangle (7,1) node[pos=0.5] {=};&#10;\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);&#10;\draw[fill=lightgray!40,draw=none] (8,2) rectangle (9,1) node[pos=0.5] {after};&#10;\draw[fill=lightgray!40,draw=none] (9,2) rectangle (10,1);&#10;\draw[fill=lightgray!40,draw=none] (10,2) rectangle (11,1);&#10;\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);&#10;\draw[fill=lightgray!40,draw=none] (1,1) rectangle (2,0);&#10;\draw[fill=lightgray!40,draw=none] (2,1) rectangle (3,0);&#10;\draw[fill=lightgray!40,draw=none] (3,1) rectangle (4,0);&#10;\draw[fill=lightgray!40,draw=none] (7,1) rectangle (8,0);&#10;\draw[fill=lightgray!40,draw=none] (8,1) rectangle (9,0);&#10;\draw[fill=lightgray!40,draw=none] (9,1) rectangle (10,0);&#10;\draw[fill=lightgray!40,draw=none] (10,1) rectangle (11,0);&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/46b68fccb6cb9a62fa6a3e052c367668.svg" align=middle width="514.4964pt" height="140.32095pt"/></p>

On the other hand, we could also add in a horizontal block to get a single central hump on the rightmost edge.

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);&#10;\draw[fill=lightgray!40,draw=none] (1,3) rectangle (2,2);&#10;\draw[fill=lightgray!40,draw=none] (2,3) rectangle (3,2);&#10;\draw[fill=lightgray!40,draw=none] (3,3) rectangle (4,2);&#10;\draw[fill=lightgray!40,draw=none] (8,3) rectangle (9,2);&#10;\draw[fill=lightgray!40,draw=none] (9,3) rectangle (10,2);&#10;\draw[fill=lightgray!40,draw=none] (10,3) rectangle (11,2);&#10;\draw[fill=lightgray!40,draw=none] (11,3) rectangle (12,2);&#10;\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);&#10;\draw[fill=lightgray!40,draw=none] (1,2) rectangle (2,1) node[pos=0.5] {before};&#10;\draw[fill=lightgray!40,draw=none] (2,2) rectangle (3,1);&#10;\draw[draw=none] (4,2) rectangle (5,1) node[pos=0.5] {\(\times\)};&#10;\draw (5,2) rectangle (7,1) node[pos=0.5] {h};&#10;\draw[draw=none] (7,2) rectangle (8,1) node[pos=0.5] {=};&#10;\draw[fill=lightgray!40,draw=none] (8,2) rectangle (9,1);&#10;\draw[fill=lightgray!40,draw=none] (9,2) rectangle (10,1) node[pos=0.5] {after};&#10;\draw[fill=lightgray!40,draw=none] (10,2) rectangle (11,1);&#10;\draw[fill=lightgray!40,draw=none] (11,2) rectangle (12,1);&#10;\draw[fill=lightgray!40,draw=none] (12,2) rectangle (13,1);&#10;\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);&#10;\draw[fill=lightgray!40,draw=none] (1,1) rectangle (2,0);&#10;\draw[fill=lightgray!40,draw=none] (2,1) rectangle (3,0);&#10;\draw[fill=lightgray!40,draw=none] (3,1) rectangle (4,0);&#10;\draw[fill=lightgray!40,draw=none] (8,1) rectangle (9,0);&#10;\draw[fill=lightgray!40,draw=none] (9,1) rectangle (10,0);&#10;\draw[fill=lightgray!40,draw=none] (10,1) rectangle (11,0);&#10;\draw[fill=lightgray!40,draw=none] (11,1) rectangle (12,0);&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/c420edb88cf3d829786bc6689bec1bc8.svg" align=middle width="608.0382pt" height="140.31435pt"/></p>

If we don't care about what the blocks on the right-most side are, we can actually characterize these
operational rules by just specifying transformations of the right-most contours. The above rules generates
the following operational equations for the contours:

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw[fill=lightgray!40,draw=none] (0,3) rectangle (1,2);&#10;\draw[fill=lightgray!40,draw=none] (1,3) rectangle (2,2);&#10;\draw[fill=lightgray!40,draw=none] (6,3) rectangle (7,2);&#10;\draw[fill=lightgray!40,draw=none] (9,3) rectangle (10,2);&#10;\draw[fill=lightgray!40,draw=none] (10,3) rectangle (11,2);&#10;\draw[fill=lightgray!40,draw=none] (14,3) rectangle (15,2);&#10;\draw[fill=lightgray!40,draw=none] (0,2) rectangle (1,1);&#10;\draw[draw=none] (2,2) rectangle (3,1) node[pos=0.5] {\(\times\)};&#10;\draw (3,2) rectangle (5,1) node[pos=0.5] {h};&#10;\draw[draw=none] (5,2) rectangle (6,1) node[pos=0.5] {=};&#10;\draw[fill=lightgray!40,draw=none] (6,2) rectangle (7,1);&#10;\draw[fill=lightgray!40,draw=none] (7,2) rectangle (8,1);&#10;\draw[draw=none] (8,2) rectangle (9,1) node[pos=0.5] {or};&#10;\draw[fill=lightgray!40,draw=none] (9,2) rectangle (10,1);&#10;\draw[draw=none] (11,2) rectangle (12,1) node[pos=0.5] {\(\times\)};&#10;\draw (12,2) rectangle (13,1) node[pos=0.5] {m};&#10;\draw[draw=none] (13,2) rectangle (14,1) node[pos=0.5] {=};&#10;\draw[fill=lightgray!40,draw=none] (14,2) rectangle (15,1);&#10;\draw[fill=lightgray!40,draw=none] (0,1) rectangle (1,0);&#10;\draw[fill=lightgray!40,draw=none] (1,1) rectangle (2,0);&#10;\draw[fill=lightgray!40,draw=none] (6,1) rectangle (7,0);&#10;\draw[fill=lightgray!40,draw=none] (9,1) rectangle (10,0);&#10;\draw[fill=lightgray!40,draw=none] (10,1) rectangle (11,0);&#10;\draw[fill=lightgray!40,draw=none] (14,1) rectangle (15,0);&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/59487950f939f54a90a550a5f2713b0b.svg" align=middle width="701.58495pt" height="140.31435pt"/></p>

