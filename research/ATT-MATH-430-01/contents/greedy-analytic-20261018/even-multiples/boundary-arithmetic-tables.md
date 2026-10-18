> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Complete arithmetic ingredients for the fixed first-seed-three proofs

All residue intervals are inclusive. Matrix cells name complement gaps;
a cell with two names is split at the modulus. Every lifetime is a block-index set.

## f=3, g=12, m=16

### Envelope-plus-core upper containment

Core intervals: R0=[2,3], R1=[12,13].

Complement gaps: G0=[0,1], G1=[4,11], G2=[14,15].

| H interval | R0 | R1 |
| --- | --- | --- |
| [2,4] | G1 | G2/G0 |
| [8,8] | G1 | G1 |
| [12,14] | G2/G0 | G1 |

### All nonempty exceptional pairs hitting the core

Exceptional residues E: 4,8,14.

| Target r | Exceptional pair | Resulting block lifetime |
| --- | --- | --- |
| 2 | (4,14) | 2 |
| 12 | (4,8) | 2 U 4 |

### Every contributor to an exceptional target

For each target in E, the list includes every nonempty residue-pair contribution.
Lifetimes for one pair are already united; all unordered pairs are considered.

| Target r | Pair contributions | Their union Q_r |
| --- | --- | --- |
| 4 | (2,2): [4,infinity); (8,12): [2,5] U [7,infinity) | [2,infinity) |
| 8 | (12,12): 2 U [4,infinity) | 2 U [4,infinity) |
| 14 | (2,12): [1,infinity) | [1,infinity) |

### Ray witnesses for residues never selected

The factors show a residue and one available lifetime component. Their strict sum
contains the indicated target lifetime; a dagger marks a same-component self-sum.
Any earlier required block is supplied in the following finite-witness table.

| Target r | First factor (residue; lifetime) | Second factor | Carry | Covered lifetime |
| --- | --- | --- | --- | --- |
| 0 | (3; [0,infinity)) | (13; [0,infinity)) | 1 | [1,infinity) |
| 1 | (3; [0,infinity)) | (14; 0) | 1 | [1,infinity) |
| 5 | (2; 1) | (3; [0,infinity)) | 0 | [1,infinity) |
| 6 | (3; [0,infinity)) | (3; [0,infinity)) dagger | 0 | [1,infinity) |
| 7 | (3; [0,infinity)) | (4; 1) | 0 | [1,infinity) |
| 9 | (12; [0,1]) | (13; [0,infinity)) | 1 | [1,infinity) |
| 10 | (13; [0,infinity)) | (13; [0,infinity)) dagger | 1 | [2,infinity) |
| 11 | (3; [0,infinity)) | (8; 1) | 0 | [1,infinity) |
| 15 | (3; [0,infinity)) | (12; [0,1]) | 0 | [0,infinity) |

| Target (r,n) | First factor | Second factor | Contribution lifetime |
| --- | --- | --- | --- |
| (10,1) | (12; [0,1]) | (14; 0) | [1,2] |

## f=3, g=18, m=122

### Envelope-plus-core upper containment

Core intervals: R0=[2,3], R1=[18,19], R2=[24,25], R3=[30,31], R4=[41,41], R5=[46,47], R6=[52,53], R7=[68,69], R8=[74,75], R9=[80,80], R10=[90,91], R11=[96,97], R12=[102,103], R13=[118,119].

Complement gaps: G0=[0,1], G1=[4,17], G2=[20,23], G3=[26,29], G4=[32,40], G5=[42,45], G6=[48,51], G7=[54,67], G8=[70,73], G9=[76,79], G10=[81,89], G11=[92,95], G12=[98,101], G13=[104,117], G14=[120,121].

| H interval | R0 | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [2,3] | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14/G0 |
| [18,20] | G2 | G4 | G5 | G6 | G7 | G7 | G8 | G10 | G11 | G12 | G13 | G13 | G14/G0 | G1 |
| [24,26] | G3 | G5 | G6 | G7 | G7 | G8 | G9 | G11 | G12 | G13 | G13 | G14/G0 | G1 | G2 |
| [30,32] | G4 | G6 | G7 | G7 | G8 | G9 | G10 | G12 | G13 | G13 | G14/G0 | G1 | G1 | G3 |
| [36,36] | G4 | G7 | G7 | G7 | G9 | G10 | G10 | G13 | G13 | G13 | G1 | G1 | G1 | G4 |
| [40,41] | G5 | G7 | G7 | G8 | G10 | G10 | G11 | G13 | G13 | G14 | G1 | G1 | G2 | G4 |
| [46,47] | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14/G0 | G1 | G1 | G2 | G3 | G5 |
| [52,53] | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14/G0 | G1 | G1 | G2 | G3 | G4 | G6 |
| [68,69] | G8 | G10 | G11 | G12 | G13 | G13 | G14/G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 |
| [74,75] | G9 | G11 | G12 | G13 | G13 | G14/G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 |
| [80,80] | G10 | G12 | G13 | G13 | G14 | G1 | G1 | G3 | G4 | G4 | G6 | G7 | G7 | G9 |
| [82,82] | G10 | G12 | G13 | G13 | G0 | G1 | G1 | G3 | G4 | G4 | G6 | G7 | G7 | G9 |
| [86,86] | G10 | G13 | G13 | G13 | G1 | G1 | G1 | G4 | G4 | G5 | G7 | G7 | G7 | G10 |
| [90,91] | G11 | G13 | G13 | G14/G0 | G1 | G1 | G2 | G4 | G5 | G6 | G7 | G7 | G8 | G10 |
| [96,97] | G12 | G13 | G14/G0 | G1 | G1 | G2 | G3 | G5 | G6 | G7 | G7 | G8 | G9 | G11 |
| [102,103] | G13 | G14/G0 | G1 | G1 | G2 | G3 | G4 | G6 | G7 | G7 | G8 | G9 | G10 | G12 |
| [118,119] | G14/G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 |

### All nonempty exceptional pairs hitting the core

Exceptional residues E: 20,26,32,36,40,82,86.

| Target r | Exceptional pair | Resulting block lifetime |
| --- | --- | --- |
| 46 | (20,26) | 0 |
| 46 | (82,86) | 1 |
| 52 | (20,32) | 0 |
| 68 | (32,36) | 0 |
| 102 | (20,82) | 0 |
| 118 | (32,86) | 0 |
| 118 | (36,82) | 0 |

### Every contributor to an exceptional target

For each target in E, the list includes every nonempty residue-pair contribution.
Lifetimes for one pair are already united; all unordered pairs are considered.

| Target r | Pair contributions | Their union Q_r |
| --- | --- | --- |
| 20 | (2,18): [1,infinity); (24,118): [2,infinity); (40,102): [2,infinity); (46,96): [3,infinity); (52,90): [2,infinity); (68,74): [2,infinity) | [1,infinity) |
| 26 | (2,24): [1,infinity); (30,118): [2,infinity); (46,102): [4,infinity); (52,96): [2,infinity); (68,80): [2,infinity); (74,74): [2,infinity) | [1,infinity) |
| 32 | (2,30): [1,infinity); (36,118): [2,infinity); (52,102): [3,infinity); (68,86): [2,infinity); (74,80): [1,infinity) | [1,infinity) |
| 36 | (18,18): [1,infinity); (40,118): [2,infinity); (68,90): [2,infinity) | [1,infinity) |
| 40 | (80,82): [1,infinity) | [1,infinity) |
| 82 | (2,80): [1,infinity); (30,52): [1,infinity); (36,46): [2,infinity); (41,41): [1,infinity); (86,118): [2,infinity); (102,102): [4,infinity) | [1,infinity) |
| 86 | (18,68): [1,infinity); (40,46): [2,infinity); (90,118): [2,infinity) | [1,infinity) |

### Ray witnesses for residues never selected

The factors show a residue and one available lifetime component. Their strict sum
contains the indicated target lifetime; a dagger marks a same-component self-sum.
Any earlier required block is supplied in the following finite-witness table.

| Target r | First factor (residue; lifetime) | Second factor | Carry | Covered lifetime |
| --- | --- | --- | --- | --- |
| 0 | (3; [0,infinity)) | (119; [0,infinity)) | 1 | [1,infinity) |
| 1 | (20; 0) | (103; [0,infinity)) | 1 | [1,infinity) |
| 4 | (30; [0,infinity)) | (96; [0,infinity)) | 1 | [1,infinity) |
| 5 | (2; [1,infinity)) | (3; [0,infinity)) | 0 | [1,infinity) |
| 6 | (3; [0,infinity)) | (3; [0,infinity)) dagger | 0 | [1,infinity) |
| 7 | (26; 0) | (103; [0,infinity)) | 1 | [1,infinity) |
| 8 | (40; 0) | (90; [0,infinity)) | 1 | [1,infinity) |
| 9 | (40; 0) | (91; [0,infinity)) | 1 | [1,infinity) |
| 10 | (36; 0) | (96; [0,infinity)) | 1 | [1,infinity) |
| 11 | (30; [0,infinity)) | (103; [0,infinity)) | 1 | [1,infinity) |
| 12 | (31; [0,infinity)) | (103; [0,infinity)) | 1 | [1,infinity) |
| 13 | (32; 0) | (103; [0,infinity)) | 1 | [1,infinity) |
| 14 | (40; 0) | (96; [0,infinity)) | 1 | [1,infinity) |
| 15 | (18; [0,infinity)) | (119; [0,infinity)) | 1 | [1,infinity) |
| 16 | (19; [0,infinity)) | (119; [0,infinity)) | 1 | [1,infinity) |
| 17 | (20; 0) | (119; [0,infinity)) | 1 | [1,infinity) |
| 21 | (3; [0,infinity)) | (18; [0,infinity)) | 0 | [0,infinity) |
| 22 | (3; [0,infinity)) | (19; [0,infinity)) | 0 | [0,infinity) |
| 23 | (3; [0,infinity)) | (20; 0) | 0 | [0,infinity) |
| 27 | (3; [0,infinity)) | (24; [0,infinity)) | 0 | [0,infinity) |
| 28 | (3; [0,infinity)) | (25; [0,infinity)) | 0 | [0,infinity) |
| 29 | (3; [0,infinity)) | (26; 0) | 0 | [0,infinity) |
| 33 | (3; [0,infinity)) | (30; [0,infinity)) | 0 | [0,infinity) |
| 34 | (3; [0,infinity)) | (31; [0,infinity)) | 0 | [0,infinity) |
| 35 | (3; [0,infinity)) | (32; 0) | 0 | [0,infinity) |
| 37 | (18; [0,infinity)) | (19; [0,infinity)) | 0 | [0,infinity) |
| 38 | (18; [0,infinity)) | (20; 0) | 0 | [0,infinity) |
| 39 | (3; [0,infinity)) | (36; 0) | 0 | [0,infinity) |
| 42 | (18; [0,infinity)) | (24; [0,infinity)) | 0 | [0,infinity) |
| 43 | (3; [0,infinity)) | (40; 0) | 0 | [0,infinity) |
| 44 | (3; [0,infinity)) | (41; [0,infinity)) | 0 | [0,infinity) |
| 45 | (19; [0,infinity)) | (26; 0) | 0 | [0,infinity) |
| 48 | (18; [0,infinity)) | (30; [0,infinity)) | 0 | [0,infinity) |
| 49 | (18; [0,infinity)) | (31; [0,infinity)) | 0 | [0,infinity) |
| 50 | (3; [0,infinity)) | (47; [0,infinity)) | 0 | [0,infinity) |
| 51 | (19; [0,infinity)) | (32; 0) | 0 | [0,infinity) |
| 54 | (18; [0,infinity)) | (36; 0) | 0 | [0,infinity) |
| 55 | (19; [0,infinity)) | (36; 0) | 0 | [0,infinity) |
| 56 | (3; [0,infinity)) | (53; [0,infinity)) | 0 | [0,infinity) |
| 57 | (25; [0,infinity)) | (32; 0) | 0 | [0,infinity) |
| 58 | (18; [0,infinity)) | (40; 0) | 0 | [0,infinity) |
| 59 | (18; [0,infinity)) | (41; [0,infinity)) | 0 | [0,infinity) |
| 60 | (19; [0,infinity)) | (41; [0,infinity)) | 0 | [0,infinity) |
| 61 | (20; 0) | (41; [0,infinity)) | 0 | [0,infinity) |
| 62 | (30; [0,infinity)) | (32; 0) | 0 | [0,infinity) |
| 63 | (31; [0,infinity)) | (32; 0) | 0 | [0,infinity) |
| 64 | (24; [0,infinity)) | (40; 0) | 0 | [0,infinity) |
| 65 | (18; [0,infinity)) | (47; [0,infinity)) | 0 | [0,infinity) |
| 66 | (19; [0,infinity)) | (47; [0,infinity)) | 0 | [0,infinity) |
| 67 | (20; 0) | (47; [0,infinity)) | 0 | [0,infinity) |
| 70 | (30; [0,infinity)) | (40; 0) | 0 | [0,infinity) |
| 71 | (18; [0,infinity)) | (53; [0,infinity)) | 0 | [0,infinity) |
| 72 | (3; [0,infinity)) | (69; [0,infinity)) | 0 | [0,infinity) |
| 73 | (20; 0) | (53; [0,infinity)) | 0 | [0,infinity) |
| 76 | (2; [1,infinity)) | (74; [0,infinity)) | 0 | [1,infinity) |
| 77 | (3; [0,infinity)) | (74; [0,infinity)) | 0 | [0,infinity) |
| 78 | (3; [0,infinity)) | (75; [0,infinity)) | 0 | [0,infinity) |
| 79 | (26; 0) | (53; [0,infinity)) | 0 | [0,infinity) |
| 81 | (40; 0) | (41; [0,infinity)) | 0 | [0,infinity) |
| 83 | (3; [0,infinity)) | (80; [0,infinity)) | 0 | [0,infinity) |
| 84 | (31; [0,infinity)) | (53; [0,infinity)) | 0 | [0,infinity) |
| 85 | (3; [0,infinity)) | (82; 0) | 0 | [0,infinity) |
| 87 | (18; [0,infinity)) | (69; [0,infinity)) | 0 | [0,infinity) |
| 88 | (19; [0,infinity)) | (69; [0,infinity)) | 0 | [0,infinity) |
| 89 | (3; [0,infinity)) | (86; 0) | 0 | [0,infinity) |
| 92 | (18; [0,infinity)) | (74; [0,infinity)) | 0 | [0,infinity) |
| 93 | (3; [0,infinity)) | (90; [0,infinity)) | 0 | [0,infinity) |
| 94 | (3; [0,infinity)) | (91; [0,infinity)) | 0 | [0,infinity) |
| 95 | (20; 0) | (75; [0,infinity)) | 0 | [0,infinity) |
| 98 | (18; [0,infinity)) | (80; [0,infinity)) | 0 | [0,infinity) |
| 99 | (3; [0,infinity)) | (96; [0,infinity)) | 0 | [0,infinity) |
| 100 | (3; [0,infinity)) | (97; [0,infinity)) | 0 | [0,infinity) |
| 101 | (19; [0,infinity)) | (82; 0) | 0 | [0,infinity) |
| 104 | (18; [0,infinity)) | (86; 0) | 0 | [0,infinity) |
| 105 | (19; [0,infinity)) | (86; 0) | 0 | [0,infinity) |
| 106 | (3; [0,infinity)) | (103; [0,infinity)) | 0 | [0,infinity) |
| 107 | (25; [0,infinity)) | (82; 0) | 0 | [0,infinity) |
| 108 | (18; [0,infinity)) | (90; [0,infinity)) | 0 | [0,infinity) |
| 109 | (18; [0,infinity)) | (91; [0,infinity)) | 0 | [0,infinity) |
| 110 | (19; [0,infinity)) | (91; [0,infinity)) | 0 | [0,infinity) |
| 111 | (20; 0) | (91; [0,infinity)) | 0 | [0,infinity) |
| 112 | (30; [0,infinity)) | (82; 0) | 0 | [0,infinity) |
| 113 | (31; [0,infinity)) | (82; 0) | 0 | [0,infinity) |
| 114 | (18; [0,infinity)) | (96; [0,infinity)) | 0 | [0,infinity) |
| 115 | (18; [0,infinity)) | (97; [0,infinity)) | 0 | [0,infinity) |
| 116 | (19; [0,infinity)) | (97; [0,infinity)) | 0 | [0,infinity) |
| 117 | (20; 0) | (97; [0,infinity)) | 0 | [0,infinity) |
| 120 | (24; [0,infinity)) | (96; [0,infinity)) | 0 | [0,infinity) |
| 121 | (18; [0,infinity)) | (103; [0,infinity)) | 0 | [0,infinity) |

| Target (r,n) | First factor | Second factor | Contribution lifetime |
| --- | --- | --- | --- |
| (76,0) | (36; 0) | (40; 0) | 0 |

## f=3, g=24, m=96

### Envelope-plus-core upper containment

Core intervals: R0=[3,3], R1=[8,9], R2=[14,14], R3=[20,20], R4=[25,25], R5=[31,31], R6=[36,37], R7=[42,43], R8=[48,48], R9=[54,54], R10=[59,59], R11=[65,65], R12=[70,71], R13=[76,76], R14=[82,82], R15=[93,93].

Complement gaps: G0=[0,2], G1=[4,7], G2=[10,13], G3=[15,19], G4=[21,24], G5=[26,30], G6=[32,35], G7=[38,41], G8=[44,47], G9=[49,53], G10=[55,58], G11=[60,64], G12=[66,69], G13=[72,75], G14=[77,81], G15=[83,92], G16=[94,95].

| H interval | R0 | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [2,3] | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14 | G15 | G16/G0 |
| [8,10] | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14 | G15 | G15 | G1 |
| [14,14] | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14 | G15 | G15 | G0 | G2 |
| [20,20] | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14 | G15 | G15 | G0 | G1 | G3 |
| [24,26] | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14 | G15 | G15 | G16/G0 | G1 | G2 | G4 |
| [30,32] | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14 | G15 | G15 | G16/G0 | G1 | G2 | G3 | G5 |
| [36,38] | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14 | G15 | G15 | G16/G0 | G1 | G2 | G3 | G4 | G6 |
| [42,44] | G8 | G9 | G10 | G11 | G12 | G13 | G14 | G15 | G15 | G0 | G1 | G2 | G3 | G4 | G5 | G7 |
| [48,48] | G9 | G10 | G11 | G12 | G13 | G14 | G15 | G15 | G0 | G1 | G2 | G3 | G4 | G5 | G6 | G8 |
| [52,54] | G10 | G11 | G12 | G13 | G14 | G15 | G15 | G16/G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G9 |
| [59,59] | G11 | G12 | G13 | G14 | G15 | G15 | G16/G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G10 |
| [64,65] | G12 | G13 | G14 | G15 | G15 | G16/G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G11 |
| [70,71] | G13 | G14 | G15 | G15 | G16/G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G12 |
| [76,76] | G14 | G15 | G15 | G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G13 |
| [82,82] | G15 | G15 | G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G14 |
| [88,88] | G15 | G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G15 |
| [92,93] | G16/G0 | G1 | G2 | G3 | G4 | G5 | G6 | G7 | G8 | G9 | G10 | G11 | G12 | G13 | G14 | G15 |

### All nonempty exceptional pairs hitting the core

Exceptional residues E: 2,10,24,26,30,32,38,44,52,53,64,88,92.

| Target r | Exceptional pair | Resulting block lifetime |
| --- | --- | --- |
| 9 | (52,53) | 1 |
| 20 | (24,92) | [2,4] |
| 20 | (52,64) | [3,4] |
| 36 | (10,26) | 1 |
| 36 | (44,88) | 2 |
| 42 | (10,32) | 1 |
| 48 | (10,38) | 1 |
| 48 | (24,24) | 1 |
| 48 | (52,92) | [2,3] |
| 54 | (2,52) | [1,2] |
| 54 | (10,44) | 1 |
| 54 | (24,30) | [0,2] |
| 70 | (26,44) | 0 |
| 70 | (32,38) | 0 |
| 76 | (24,52) | [0,1] |
| 76 | (32,44) | 0 |
| 82 | (30,52) | [0,1] |
| 82 | (38,44) | 0 |

### Every contributor to an exceptional target

For each target in E, the list includes every nonempty residue-pair contribution.
Lifetimes for one pair are already united; all unordered pairs are considered.

| Target r | Pair contributions | Their union Q_r |
| --- | --- | --- |
| 2 | (10,88): 3; (44,54): [4,infinity) | [3,infinity) |
| 10 | (2,8): [2,infinity); (14,92): [3,infinity); (24,82): [3,infinity); (30,76): [3,infinity); (36,70): [2,infinity); (42,64): [3,infinity); (52,54): [4,infinity) | [2,infinity) |
| 24 | (10,14): [2,infinity); (32,88): 2; (38,82): [3,infinity); (44,76): [3,infinity) | [2,infinity) |
| 26 | (2,24): [1,3]; (30,92): [2,4]; (52,70): [2,infinity) | [1,infinity) |
| 30 | (10,20): 2 U [6,infinity); (38,88): 2; (44,82): [3,infinity) | [2,infinity) |
| 32 | (2,30): [1,3]; (8,24): [1,infinity); (36,92): [2,3] U [5,infinity); (52,76): [3,infinity); (64,64): 6 | [1,infinity) |
| 38 | (2,36): [1,2] U [4,infinity); (8,30): [1,infinity); (14,24): [1,infinity); (42,92): [2,infinity); (52,82): [3,infinity); (64,70): [4,infinity) | [1,infinity) |
| 44 | (2,42): [1,infinity); (8,36): [1,infinity); (14,30): [1,infinity); (20,24): [1,2] U [5,infinity); (48,92): [2,3] U [6,infinity); (52,88): 2; (64,76): [5,infinity); (70,70): [4,infinity) | [1,infinity) |
| 52 | (8,44): [1,infinity); (9,43): [2,infinity); (10,42): 1 U [3,infinity); (14,38): [1,infinity); (20,32): 1 U [5,infinity) | [1,infinity) |
| 53 | (9,44): [2,infinity); (10,43): [1,infinity) | [1,infinity) |
| 64 | (10,54): [4,infinity); (20,44): 1 U [5,infinity); (26,38): 0 | [0,1] U [4,infinity) |
| 88 | (24,64): [2,4]; (36,52): 0 U [3,infinity); (92,92): 4 | 0 U [2,infinity) |
| 92 | (10,82): [3,infinity); (38,54): [3,infinity); (44,48): 0 U [4,infinity) | 0 U [3,infinity) |

### Ray witnesses for residues never selected

The factors show a residue and one available lifetime component. Their strict sum
contains the indicated target lifetime; a dagger marks a same-component self-sum.
Any earlier required block is supplied in the following finite-witness table.

| Target r | First factor (residue; lifetime) | Second factor | Carry | Covered lifetime |
| --- | --- | --- | --- | --- |
| 0 | (3; [0,infinity)) | (93; [0,infinity)) | 1 | [1,infinity) |
| 1 | (26; 0) | (71; [0,infinity)) | 1 | [1,infinity) |
| 4 | (30; [0,1]) | (70; [1,infinity)) | 1 | [2,infinity) |
| 5 | (2; [1,2]) | (3; [0,infinity)) | 0 | [1,infinity) |
| 6 | (3; [0,infinity)) | (3; [0,infinity)) dagger | 0 | [1,infinity) |
| 7 | (32; 0) | (71; [0,infinity)) | 1 | [1,infinity) |
| 11 | (3; [0,infinity)) | (8; [1,infinity)) | 0 | [1,infinity) |
| 12 | (37; [0,infinity)) | (71; [0,infinity)) | 1 | [1,infinity) |
| 13 | (3; [0,infinity)) | (10; 1) | 0 | [1,infinity) |
| 15 | (52; 0) | (59; [0,infinity)) | 1 | [1,infinity) |
| 16 | (53; 0) | (59; [0,infinity)) | 1 | [1,infinity) |
| 17 | (3; [0,infinity)) | (14; [1,infinity)) | 0 | [1,infinity) |
| 18 | (43; [0,infinity)) | (71; [0,infinity)) | 1 | [1,infinity) |
| 19 | (44; 0) | (71; [0,infinity)) | 1 | [1,infinity) |
| 21 | (24; [0,1]) | (93; [0,infinity)) | 1 | [1,infinity) |
| 22 | (25; [0,infinity)) | (93; [0,infinity)) | 1 | [1,infinity) |
| 23 | (3; [0,infinity)) | (20; 1) | 0 | [1,infinity) |
| 27 | (3; [0,infinity)) | (24; [0,1]) | 0 | [0,infinity) |
| 28 | (3; [0,infinity)) | (25; [0,infinity)) | 0 | [0,infinity) |
| 29 | (3; [0,infinity)) | (26; 0) | 0 | [0,infinity) |
| 33 | (3; [0,infinity)) | (30; [0,1]) | 0 | [0,infinity) |
| 34 | (3; [0,infinity)) | (31; [0,infinity)) | 0 | [0,infinity) |
| 35 | (3; [0,infinity)) | (32; 0) | 0 | [0,infinity) |
| 39 | (3; [0,infinity)) | (36; 0) | 0 | [0,infinity) |
| 40 | (3; [0,infinity)) | (37; [0,infinity)) | 0 | [0,infinity) |
| 41 | (3; [0,infinity)) | (38; 0) | 0 | [0,infinity) |
| 45 | (3; [0,infinity)) | (42; 0) | 0 | [0,infinity) |
| 46 | (3; [0,infinity)) | (43; [0,infinity)) | 0 | [0,infinity) |
| 47 | (3; [0,infinity)) | (44; 0) | 0 | [0,infinity) |
| 49 | (24; [0,1]) | (25; [0,infinity)) | 0 | [0,infinity) |
| 50 | (8; [1,infinity)) | (42; 0) | 0 | [1,infinity) |
| 51 | (3; [0,infinity)) | (48; 0) | 0 | [0,infinity) |
| 55 | (3; [0,infinity)) | (52; 0) | 0 | [0,infinity) |
| 56 | (3; [0,infinity)) | (53; 0) | 0 | [0,infinity) |
| 57 | (25; [0,infinity)) | (32; 0) | 0 | [0,infinity) |
| 58 | (14; [1,infinity)) | (44; 0) | 0 | [1,infinity) |
| 60 | (8; [1,infinity)) | (52; 0) | 0 | [1,infinity) |
| 61 | (24; [0,1]) | (37; [0,infinity)) | 0 | [0,infinity) |
| 62 | (3; [0,infinity)) | (59; [0,infinity)) | 0 | [0,infinity) |
| 63 | (25; [0,infinity)) | (38; 0) | 0 | [0,infinity) |
| 66 | (14; [1,infinity)) | (52; 0) | 0 | [1,infinity) |
| 67 | (24; [0,1]) | (43; [0,infinity)) | 0 | [0,infinity) |
| 68 | (3; [0,infinity)) | (65; [0,infinity)) | 0 | [0,infinity) |
| 69 | (25; [0,infinity)) | (44; 0) | 0 | [0,infinity) |
| 72 | (2; [1,2]) | (70; [1,infinity)) | 0 | [2,infinity) |
| 73 | (25; [0,infinity)) | (48; 0) | 0 | [0,infinity) |
| 74 | (3; [0,infinity)) | (71; [0,infinity)) | 0 | [0,infinity) |
| 75 | (31; [0,infinity)) | (44; 0) | 0 | [0,infinity) |
| 77 | (25; [0,infinity)) | (52; 0) | 0 | [0,infinity) |
| 78 | (25; [0,infinity)) | (53; 0) | 0 | [0,infinity) |
| 79 | (31; [0,infinity)) | (48; 0) | 0 | [0,infinity) |
| 80 | (37; [0,infinity)) | (43; [0,infinity)) | 0 | [0,infinity) |
| 81 | (37; [0,infinity)) | (44; 0) | 0 | [0,infinity) |
| 83 | (24; [0,1]) | (59; [0,infinity)) | 0 | [0,infinity) |
| 84 | (25; [0,infinity)) | (59; [0,infinity)) | 0 | [0,infinity) |
| 85 | (26; 0) | (59; [0,infinity)) | 0 | [0,infinity) |
| 86 | (43; [0,infinity)) | (43; [0,infinity)) dagger | 0 | [1,infinity) |
| 87 | (43; [0,infinity)) | (44; 0) | 0 | [0,infinity) |
| 89 | (24; [0,1]) | (65; [0,infinity)) | 0 | [0,infinity) |
| 90 | (25; [0,infinity)) | (65; [0,infinity)) | 0 | [0,infinity) |
| 91 | (26; 0) | (65; [0,infinity)) | 0 | [0,infinity) |
| 94 | (24; [0,1]) | (70; [1,infinity)) | 0 | [1,infinity) |
| 95 | (24; [0,1]) | (71; [0,infinity)) | 0 | [0,infinity) |

| Target (r,n) | First factor | Second factor | Contribution lifetime |
| --- | --- | --- | --- |
| (4,1) | (48; 0) | (52; 0) | 1 |
| (50,0) | (24; [0,1]) | (26; 0) | [0,1] |
| (58,0) | (26; 0) | (32; 0) | 0 |
| (60,0) | (24; [0,1]) | (36; 0) | [0,1] |
| (66,0) | (24; [0,1]) | (42; 0) | [0,1] |
| (72,0) | (24; [0,1]) | (48; 0) | [0,1] |
| (72,1) | (20; 1) | (52; 0) | 1 |
| (86,0) | (38; 0) | (48; 0) | 0 |
| (94,0) | (42; 0) | (52; 0) | 0 |

