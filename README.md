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
with the singular vertical block:

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,3) rectangle (1,1) node[pos=0.5] {v};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/481e997d914bcd7d51a16bc6104e4628.svg?invert_in_darkmode" align=middle width="47.43354pt" height="94.20741pt"/></p>

We can complete this column by adding a single monomer:

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,3) rectangle (1,1) node[pos=0.5] {v};&#10;\draw (0,1) rectangle (1,0) node[pos=0.5] {m};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/4541228356af488f7d8ade3126ebc02f.svg?invert_in_darkmode" align=middle width="47.43354pt" height="140.98095pt"/></p>

