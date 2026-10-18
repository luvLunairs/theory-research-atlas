> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Proposed exact lifetime-sum tables

Intervals refer to nonnegative block indices. All intervals are inclusive;
`[a,infinity)` is the ray starting at a; `-` is empty.

## f=3, g=12, m=16

| Residues r | Selected lifetime L_r | Distinct-sum lifetime Q_r |
| --- | --- | --- |
| 0,1,5,6,7,9,10,11 | - | [1,infinity) |
| 2 | 1 U [3,infinity) | 2 |
| 3,13 | [0,infinity) | - |
| 4 | 1 | [2,infinity) |
| 8 | 1 U 3 | 2 U [4,infinity) |
| 12 | [0,1] U 3 U [5,infinity) | 2 U 4 |
| 14 | 0 | [1,infinity) |
| 15 | - | [0,infinity) |

## f=3, g=18, m=122

| Residues r | Selected lifetime L_r | Distinct-sum lifetime Q_r |
| --- | --- | --- |
| 0,1,4,5,6,7,8,9,10,11,12,13,14,15,16,17 | - | [1,infinity) |
| 2 | [1,infinity) | - |
| 3,18,19,24,25,30,31,41,47,53,69,74,75,80,90,91,96,97,103,119 | [0,infinity) | - |
| 20,26,32,36,40,82,86 | 0 | [1,infinity) |
| 21,22,23,27,28,29,33,34,35,37,38,39,42,43,44,45,48,49,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,70,71,72,73,76,77,78,79,81,83,84,85,87,88,89,92,93,94,95,98,99,100,101,104,105,106,107,108,109,110,111,112,113,114,115,116,117,120,121 | - | [0,infinity) |
| 46 | [2,infinity) | [0,1] |
| 52,68,102,118 | [1,infinity) | 0 |

## f=3, g=24, m=96

| Residues r | Selected lifetime L_r | Distinct-sum lifetime Q_r |
| --- | --- | --- |
| 0,1,4,5,6,7,11,12,13,15,16,17,18,19,21,22,23 | - | [1,infinity) |
| 2 | [1,2] | [3,infinity) |
| 3,25,31,37,43,59,65,71,93 | [0,infinity) | - |
| 8,14 | [1,infinity) | - |
| 9 | [2,infinity) | 1 |
| 10 | 1 | [2,infinity) |
| 20 | 1 U [5,infinity) | [2,4] |
| 24,30 | [0,1] | [2,infinity) |
| 26,32,38,44,52,53 | 0 | [1,infinity) |
| 27,28,29,33,34,35,39,40,41,45,46,47,49,50,51,55,56,57,58,60,61,62,63,66,67,68,69,72,73,74,75,77,78,79,80,81,83,84,85,86,87,89,90,91,94,95 | - | [0,infinity) |
| 36 | 0 U [3,infinity) | [1,2] |
| 42 | 0 U [2,infinity) | 1 |
| 48 | 0 U [4,infinity) | [1,3] |
| 54 | [3,infinity) | [0,2] |
| 64 | [2,3] | [0,1] U [4,infinity) |
| 70 | [1,infinity) | 0 |
| 76,82 | [2,infinity) | [0,1] |
| 88 | 1 | 0 U [2,infinity) |
| 92 | [1,2] | 0 U [3,infinity) |

