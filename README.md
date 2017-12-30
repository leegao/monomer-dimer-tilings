# Tiling 3-by-N rectangles with Monomers and Dimers

Convoluted solution for the monomer-dimer tiling problem.

Suppose one is given pieces that may
be one of the three forms: monomers (<img alt="$m$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/0e51a2dede42189d77627c4d742822c3.svg?invert_in_darkmode" align=middle width="14.43321pt" height="14.15535pt"/>) that are <img alt="$1 \times 1$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/d12ef2fd91d2a991710509cae7229134.svg?invert_in_darkmode" align=middle width="36.52968pt" height="21.18732pt"/> squares, and dimers that are dominoes,
either vertically (<img alt="$v$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/6c4adbc36120d62b98deef2a20d5d303.svg?invert_in_darkmode" align=middle width="8.55789pt" height="14.15535pt"/>) oriented <img alt="$1 \times 2$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/6a178d559af5ef9cb672b85caf00d739.svg?invert_in_darkmode" align=middle width="36.52968pt" height="21.18732pt"/>, or horizontally (<img alt="$h$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/2ad9d098b937e46f9f58968551adac57.svg?invert_in_darkmode" align=middle width="9.471165pt" height="22.83138pt"/>) oriented <img alt="$2 \times 1$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/56cbb95ecc0b4e113e6fb1cd93b761b5.svg?invert_in_darkmode" align=middle width="36.52968pt" height="21.18732pt"/>. In how many ways can
a <img alt="$n \times 3$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/e13165a13b4e02249c42e972e74b4e17.svg?invert_in_darkmode" align=middle width="38.17737pt" height="21.18732pt"/> rectangle be covered completely and without overlap ("tiled") by such pieces?

<p align="center"><img alt="$$&#10;\begin{tikzpicture}&#10;\draw (0,0) rectangle (1,1) node[draw, inner sep=5pt, pos=0.5, anchor=south] {m};&#10;\end{tikzpicture}&#10;$$" src="https://rawgit.com/leegao/monomer-dimer-tilings/svgs/svgs/d036560c8e772d68cc7fb174582f0fd5.svg?invert_in_darkmode" align=middle width="47.43354pt" height="47.891085pt"/></p>