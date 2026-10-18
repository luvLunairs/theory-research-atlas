> Publication copy of a dated working document. Original source identifiers and
> line numbers below refer to the preserved source digest in [source-map.json](../../../source-map.json).
> Historical workflow/model-status notes are superseded by the current
> [assistance and submission record](../../../assistance-and-checks.md).

# Complete arithmetic tables for the three fixed first-seed-four cases

This is the literal arithmetic appendix to [the proof](f4-fixed.md).
Every lifetime is a set of nonnegative integer block indices. `empty` means
the empty set. In a source pair `a:b`, the carry is uniquely determined by
`a+b=r+cm`, with `c=0` or `1`; a repeated residue uses the strict
lifetime self-sum, never an unrestricted double. The proof explains these
operations. The identities below are mathematical assertions available
for direct arithmetic inspection, not pass flags from a hidden checker.

## Seeds 4,24; modulus 67

### Selected lifetimes

| Residues | Selected block indices |
| --- | --- |
| 3,18 | [3,infinity) |
| 4 | [0,4] |
| 10 | [9,infinity) |
| 17 | [4,infinity) |
| 24,27,35,42 | 0 |
| 25,26,32,33,40,48,54,55,63 | [0,infinity) |
| 34 | [0,6] |
| 41,43 | [0,1] |
| 47 | [6,infinity) |
| 62 | [1,infinity) |

Every residue not in this table has empty selected lifetime.

### Complete pair exclusion at supported residues

The sources column lists **all** unordered pairs of supported residues
whose sum has the target residue, even pairs whose lifetime self-sum
is empty. The last column is the union of their strict sum lifetimes.
It is disjoint from the selected lifetime and contains exactly its
complement above the second seed.

| Target r | All source pairs | Strict sum lifetime |
| --- | --- | --- |
| 3 | 27:43, 35:35 | [1,2] |
| 4 | 17:54, 24:47 | [5,infinity) |
| 10 | 34:43, 35:42 | [1,8] |
| 17 | 41:43, 42:42 | [1,3] |
| 18 | 42:43 | [1,2] |
| 24 | 43:48 | [1,infinity) |
| 25 | none | empty |
| 26 | none | empty |
| 27 | 3:24, 10:17, 32:62, 40:54, 47:47 | [1,infinity) |
| 32 | none | empty |
| 33 | none | empty |
| 34 | 10:24, 17:17, 47:54 | [7,infinity) |
| 35 | 3:32, 10:25, 17:18, 40:62, 47:55, 48:54 | [1,infinity) |
| 40 | none | empty |
| 41 | 17:24, 54:54 | [2,infinity) |
| 42 | 10:32, 17:25, 18:24, 47:62, 54:55 | [1,infinity) |
| 43 | 3:40, 10:33, 17:26, 18:25, 47:63, 48:62, 55:55 | [2,infinity) |
| 47 | 4:43 | [0,5] |
| 48 | 24:24 | empty |
| 54 | 27:27 | empty |
| 55 | none | empty |
| 62 | 27:35 | 0 |
| 63 | none | empty |

### Coverage at the other residues

Each row states actual source-pair lifetime identities. Their union
contains all `n>=0` when `r>g`, and all `n>=1` otherwise, precisely
the required positive candidates above the second seed. No exclusion
check is needed at these residues because none is selected.

| Target r | Pair and its exact strict sum lifetime |
| --- | --- |
| 0 | 4:63: [1,infinity) |
| 1 | 25:43: [1,infinity) |
| 2 | 26:43: [1,infinity) |
| 5 | 24:48: [1,infinity) |
| 6 | 25:48: [1,infinity) |
| 7 | 26:48: [1,infinity) |
| 8 | 27:48: [1,infinity) |
| 9 | 33:43: [1,infinity) |
| 11 | 24:54: [1,infinity) |
| 12 | 24:55: [1,infinity) |
| 13 | 25:55: [1,infinity) |
| 14 | 26:55: [1,infinity) |
| 15 | 27:55: [1,infinity) |
| 16 | 35:48: [1,infinity) |
| 19 | 32:54: [1,infinity) |
| 20 | 24:63: [1,infinity) |
| 21 | 25:63: [1,infinity) |
| 22 | 26:63: [1,infinity) |
| 23 | 27:63: [1,infinity) |
| 28 | 4:24: [0,4]; 3:25: [3,infinity) |
| 29 | 4:25: [0,infinity) |
| 30 | 4:26: [0,infinity) |
| 31 | 4:27: [0,4]; 35:63: [1,infinity) |
| 36 | 4:32: [0,infinity) |
| 37 | 4:33: [0,infinity) |
| 38 | 4:34: [0,10]; 3:35: [3,infinity) |
| 39 | 4:35: [0,4]; 43:63: [1,infinity) |
| 44 | 4:40: [0,infinity) |
| 45 | 4:41: [0,5]; 3:42: [3,infinity) |
| 46 | 4:42: [0,4]; 3:43: [3,infinity) |
| 49 | 24:25: [0,infinity) |
| 50 | 24:26: [0,infinity) |
| 51 | 25:26: [0,infinity) |
| 52 | 4:48: [0,infinity) |
| 53 | 26:27: [0,infinity) |
| 56 | 24:32: [0,infinity) |
| 57 | 24:33: [0,infinity) |
| 58 | 4:54: [0,infinity) |
| 59 | 4:55: [0,infinity) |
| 60 | 25:35: [0,infinity) |
| 61 | 26:35: [0,infinity) |
| 64 | 24:40: [0,infinity) |
| 65 | 25:40: [0,infinity) |
| 66 | 25:41: [0,infinity) |

## Seeds 4,32; modulus 91

### Selected lifetimes

| Residues | Selected block indices |
| --- | --- |
| 2 | [7,infinity) |
| 3,18,25 | [3,infinity) |
| 4,87 | [0,3] |
| 10 | [6,infinity) |
| 17,63 | [4,infinity) |
| 26,86 | [2,infinity) |
| 32,35,43,50,58,59 | 0 |
| 33,40,41,48,56,64,70,71,79 | [0,infinity) |
| 34 | [0,5] |
| 42 | [0,4] |
| 49,51,57 | [0,1] |
| 55 | [5,infinity) |
| 78 | [1,infinity) |

Every residue not in this table has empty selected lifetime.

### Complete pair exclusion at supported residues

The sources column lists **all** unordered pairs of supported residues
whose sum has the target residue, even pairs whose lifetime self-sum
is empty. The last column is the union of their strict sum lifetimes.
It is disjoint from the selected lifetime and contains exactly its
complement above the second seed.

| Target r | All source pairs | Strict sum lifetime |
| --- | --- | --- |
| 2 | 34:59, 35:58, 42:51, 43:50 | [1,6] |
| 3 | 35:59, 43:51 | [1,2] |
| 4 | 2:2, 17:78, 25:70, 32:63, 40:55 | [4,infinity) |
| 10 | 42:59, 43:58, 50:51 | [1,5] |
| 17 | 49:59, 50:58, 51:57 | [1,3] |
| 18 | 50:59, 51:58 | [1,2] |
| 25 | 57:59, 58:58 | [1,2] |
| 26 | 58:59 | 1 |
| 32 | 59:64 | [1,infinity) |
| 33 | none | empty |
| 34 | 2:32, 17:17, 55:70 | [6,infinity) |
| 35 | 2:33, 3:32, 10:25, 17:18, 40:86, 48:78, 55:71, 56:70, 63:63 | [1,infinity) |
| 40 | none | empty |
| 41 | none | empty |
| 42 | 2:40, 10:32, 17:25, 55:78, 63:70 | [5,infinity) |
| 43 | 2:41, 3:40, 10:33, 17:26, 18:25, 48:86, 55:79, 56:78, 63:71, 64:70 | [1,infinity) |
| 48 | none | empty |
| 49 | 17:32, 70:70 | [2,infinity) |
| 50 | 2:48, 10:40, 17:33, 18:32, 25:25, 55:86, 63:78, 70:71 | [1,infinity) |
| 51 | 2:49, 3:48, 10:41, 17:34, 18:33, 25:26, 55:87, 56:86, 63:79, 64:78, 71:71 | [2,infinity) |
| 55 | 4:51, 59:87 | [0,4] |
| 56 | none | empty |
| 57 | 2:55, 17:40, 25:32, 70:78 | [2,infinity) |
| 58 | 2:56, 3:55, 10:48, 17:41, 18:40, 25:33, 26:32, 63:86, 70:79, 71:78 | [1,infinity) |
| 59 | 2:57, 3:56, 4:55, 10:49, 17:42, 18:41, 25:34, 26:33, 63:87, 64:86, 71:79 | [1,infinity) |
| 63 | 4:59 | [0,3] |
| 64 | 32:32 | empty |
| 70 | 35:35 | empty |
| 71 | none | empty |
| 78 | 35:43 | 0 |
| 79 | none | empty |
| 86 | 35:51, 43:43 | [0,1] |
| 87 | 17:70, 32:55 | [4,infinity) |

### Coverage at the other residues

Each row states actual source-pair lifetime identities. Their union
contains all `n>=0` when `r>g`, and all `n>=1` otherwise, precisely
the required positive candidates above the second seed. No exclusion
check is needed at these residues because none is selected.

| Target r | Pair and its exact strict sum lifetime |
| --- | --- |
| 0 | 33:58: [1,infinity) |
| 1 | 33:59: [1,infinity) |
| 5 | 32:64: [1,infinity) |
| 6 | 33:64: [1,infinity) |
| 7 | 34:64: [1,infinity) |
| 8 | 35:64: [1,infinity) |
| 9 | 41:59: [1,infinity) |
| 11 | 32:70: [1,infinity) |
| 12 | 32:71: [1,infinity) |
| 13 | 33:71: [1,infinity) |
| 14 | 34:71: [1,infinity) |
| 15 | 35:71: [1,infinity) |
| 16 | 43:64: [1,infinity) |
| 19 | 40:70: [1,infinity) |
| 20 | 32:79: [1,infinity) |
| 21 | 33:79: [1,infinity) |
| 22 | 34:79: [1,infinity) |
| 23 | 35:79: [1,infinity) |
| 24 | 51:64: [1,infinity) |
| 27 | 48:70: [1,infinity) |
| 28 | 40:79: [1,infinity) |
| 29 | 33:87: [1,infinity) |
| 30 | 42:79: [1,infinity) |
| 31 | 43:79: [1,infinity) |
| 36 | 4:32: [0,3]; 3:33: [3,infinity) |
| 37 | 4:33: [0,infinity) |
| 38 | 4:34: [0,8]; 3:35: [3,infinity) |
| 39 | 4:35: [0,3]; 51:79: [1,infinity) |
| 44 | 4:40: [0,infinity) |
| 45 | 4:41: [0,infinity) |
| 46 | 4:42: [0,7]; 3:43: [3,infinity) |
| 47 | 4:43: [0,3]; 59:79: [1,infinity) |
| 52 | 4:48: [0,infinity) |
| 53 | 4:49: [0,4]; 3:50: [3,infinity) |
| 54 | 4:50: [0,3]; 3:51: [3,infinity) |
| 60 | 4:56: [0,infinity) |
| 61 | 4:57: [0,4]; 3:58: [3,infinity) |
| 62 | 4:58: [0,3]; 3:59: [3,infinity) |
| 65 | 32:33: [0,infinity) |
| 66 | 32:34: [0,5]; 10:56: [6,infinity) |
| 67 | 33:34: [0,infinity) |
| 68 | 4:64: [0,infinity) |
| 69 | 34:35: [0,5]; 10:59: [6,infinity) |
| 72 | 32:40: [0,infinity) |
| 73 | 32:41: [0,infinity) |
| 74 | 4:70: [0,infinity) |
| 75 | 4:71: [0,infinity) |
| 76 | 33:43: [0,infinity) |
| 77 | 34:43: [0,5]; 18:59: [3,infinity) |
| 80 | 32:48: [0,infinity) |
| 81 | 33:48: [0,infinity) |
| 82 | 33:49: [0,infinity) |
| 83 | 4:79: [0,infinity) |
| 84 | 33:51: [0,infinity) |
| 85 | 34:51: [0,6]; 26:59: [2,infinity) |
| 88 | 32:56: [0,infinity) |
| 89 | 33:56: [0,infinity) |
| 90 | 33:57: [0,infinity) |

## Seeds 4,40; modulus 115

### Selected lifetimes

| Residues | Selected block indices |
| --- | --- |
| 2,10,109 | [7,infinity) |
| 3,18 | [3,infinity) |
| 4,103 | [0,4] |
| 17,71,79 | [5,infinity) |
| 25,33 | [4,infinity) |
| 26,102,110 | [2,infinity) |
| 34 | [2,6] |
| 40 | 0 union [9,infinity) |
| 41,48,49,56,64,72,86,87,95 | [0,infinity) |
| 42,50 | [0,5] |
| 43,51,58,66,67,74,75 | 0 |
| 57,59,65 | [0,1] |
| 63 | [6,infinity) |
| 73 | [0,2] |
| 80 | [0,7] |
| 94 | [1,infinity) |
| 111 | [0,3] |

Every residue not in this table has empty selected lifetime.

### Complete pair exclusion at supported residues

The sources column lists **all** unordered pairs of supported residues
whose sum has the target residue, even pairs whose lifetime self-sum
is empty. The last column is the union of their strict sum lifetimes.
It is disjoint from the selected lifetime and contains exactly its
complement above the second seed.

| Target r | All source pairs | Strict sum lifetime |
| --- | --- | --- |
| 2 | 42:75, 43:74, 50:67, 51:66, 58:59 | [1,6] |
| 3 | 43:75, 51:67, 59:59 | [1,2] |
| 4 | 2:2, 10:109, 17:102, 25:94, 33:86, 40:79, 48:71, 56:63 | [5,infinity) |
| 10 | 50:75, 51:74, 58:67, 59:66 | [1,6] |
| 17 | 57:75, 58:74, 59:73, 65:67, 66:66 | [1,4] |
| 18 | 58:75, 59:74, 66:67 | [1,2] |
| 25 | 65:75, 66:74, 67:73 | [1,3] |
| 26 | 66:75, 67:74 | 1 |
| 33 | 73:75, 74:74 | [1,3] |
| 34 | 17:17, 40:109, 63:86, 74:75 | 1 union [7,infinity) |
| 40 | 75:80 | [1,8] |
| 41 | none | empty |
| 42 | 2:40, 17:25, 48:109, 63:94, 71:86 | [6,infinity) |
| 43 | 2:41, 3:40, 10:33, 17:26, 18:25, 48:110, 49:109, 56:102, 63:95, 64:94, 71:87, 72:86, 79:79 | [1,infinity) |
| 48 | none | empty |
| 49 | none | empty |
| 50 | 2:48, 10:40, 17:33, 25:25, 56:109, 63:102, 71:94, 79:86 | [6,infinity) |
| 51 | 2:49, 3:48, 10:41, 17:34, 18:33, 25:26, 56:110, 57:109, 63:103, 64:102, 71:95, 72:94, 79:87, 80:86 | [1,infinity) |
| 56 | none | empty |
| 57 | 17:40, 63:109, 86:86 | [2,infinity) |
| 58 | 2:56, 10:48, 17:41, 18:40, 25:33, 63:110, 64:109, 71:102, 79:94, 86:87 | [1,infinity) |
| 59 | 2:57, 3:56, 10:49, 17:42, 18:41, 25:34, 26:33, 63:111, 64:110, 65:109, 71:103, 72:102, 79:95, 80:94, 87:87 | [2,infinity) |
| 63 | 4:59, 67:111, 75:103 | [0,5] |
| 64 | none | empty |
| 65 | 2:63, 17:48, 25:40, 71:109, 86:94 | [2,infinity) |
| 66 | 2:64, 3:63, 10:56, 17:49, 18:48, 25:41, 26:40, 33:33, 71:110, 72:109, 79:102, 86:95, 87:94 | [1,infinity) |
| 67 | 2:65, 3:64, 4:63, 10:57, 17:50, 18:49, 25:42, 26:41, 33:34, 71:111, 72:110, 73:109, 79:103, 80:102, 87:95 | [1,infinity) |
| 71 | 4:67, 75:111 | [0,4] |
| 72 | none | empty |
| 73 | 2:71, 10:63, 17:56, 25:48, 33:40, 79:109, 86:102, 94:94 | [3,infinity) |
| 74 | 2:72, 3:71, 10:64, 17:57, 18:56, 25:49, 26:48, 33:41, 34:40, 79:110, 80:109, 86:103, 87:102, 94:95 | [1,infinity) |
| 75 | 2:73, 3:72, 4:71, 10:65, 17:58, 18:57, 25:50, 26:49, 33:42, 34:41, 79:111, 80:110, 87:103, 95:95 | [1,infinity) |
| 79 | 4:75 | [0,4] |
| 80 | 17:63, 40:40, 86:109 | [8,infinity) |
| 86 | 43:43 | empty |
| 87 | none | empty |
| 94 | 43:51 | 0 |
| 95 | none | empty |
| 102 | 43:59, 51:51 | [0,1] |
| 103 | 17:86, 40:63, 109:109 | [5,infinity) |
| 109 | 34:75, 42:67, 43:66, 50:59, 51:58 | [0,6] |
| 110 | 43:67, 51:59 | [0,1] |
| 111 | 2:109, 17:94, 25:86, 40:71, 48:63 | [4,infinity) |

### Coverage at the other residues

Each row states actual source-pair lifetime identities. Their union
contains all `n>=0` when `r>g`, and all `n>=1` otherwise, precisely
the required positive candidates above the second seed. No exclusion
check is needed at these residues because none is selected.

| Target r | Pair and its exact strict sum lifetime |
| --- | --- |
| 0 | 41:74: [1,infinity) |
| 1 | 41:75: [1,infinity) |
| 5 | 48:72: [1,infinity) |
| 6 | 41:80: [1,infinity) |
| 7 | 48:74: [1,infinity) |
| 8 | 48:75: [1,infinity) |
| 9 | 49:75: [1,infinity) |
| 11 | 40:86: [1,infinity) |
| 12 | 40:87: [1,infinity) |
| 13 | 41:87: [1,infinity) |
| 14 | 42:87: [1,infinity) |
| 15 | 43:87: [1,infinity) |
| 16 | 56:75: [1,infinity) |
| 19 | 48:86: [1,infinity) |
| 20 | 40:95: [1,infinity) |
| 21 | 41:95: [1,infinity) |
| 22 | 42:95: [1,infinity) |
| 23 | 43:95: [1,infinity) |
| 24 | 64:75: [1,infinity) |
| 27 | 56:86: [1,infinity) |
| 28 | 48:95: [1,infinity) |
| 29 | 41:103: [1,infinity) |
| 30 | 50:95: [1,infinity) |
| 31 | 51:95: [1,infinity) |
| 32 | 72:75: [1,infinity) |
| 35 | 64:86: [1,infinity) |
| 36 | 48:103: [1,infinity) |
| 37 | 41:111: [1,infinity) |
| 38 | 58:95: [1,infinity) |
| 39 | 59:95: [1,infinity) |
| 44 | 4:40: [0,4] union [9,infinity); 3:41: [3,infinity) |
| 45 | 4:41: [0,infinity) |
| 46 | 4:42: [0,9]; 3:43: [3,infinity) |
| 47 | 4:43: [0,4]; 67:95: [1,infinity) |
| 52 | 4:48: [0,infinity) |
| 53 | 4:49: [0,infinity) |
| 54 | 4:50: [0,9]; 3:51: [3,infinity) |
| 55 | 4:51: [0,4]; 75:95: [1,infinity) |
| 60 | 4:56: [0,infinity) |
| 61 | 4:57: [0,5]; 3:58: [3,infinity) |
| 62 | 4:58: [0,4]; 3:59: [3,infinity) |
| 68 | 4:64: [0,infinity) |
| 69 | 4:65: [0,5]; 3:66: [3,infinity) |
| 70 | 4:66: [0,4]; 3:67: [3,infinity) |
| 76 | 4:72: [0,infinity) |
| 77 | 4:73: [0,6]; 2:75: [7,infinity) |
| 78 | 4:74: [0,4]; 3:75: [3,infinity) |
| 81 | 40:41: [0,infinity) |
| 82 | 40:42: [0,5] union [9,infinity); 17:65: [5,infinity) |
| 83 | 41:42: [0,infinity) |
| 84 | 41:43: [0,infinity) |
| 85 | 42:43: [0,5]; 18:67: [3,infinity) |
| 88 | 40:48: [0,infinity) |
| 89 | 40:49: [0,infinity) |
| 90 | 4:86: [0,infinity) |
| 91 | 4:87: [0,infinity) |
| 92 | 41:51: [0,infinity) |
| 93 | 42:51: [0,5]; 18:75: [3,infinity) |
| 96 | 40:56: [0,infinity) |
| 97 | 41:56: [0,infinity) |
| 98 | 41:57: [0,infinity) |
| 99 | 4:95: [0,infinity) |
| 100 | 41:59: [0,infinity) |
| 101 | 42:59: [0,6]; 26:75: [2,infinity) |
| 104 | 40:64: [0,infinity) |
| 105 | 41:64: [0,infinity) |
| 106 | 41:65: [0,infinity) |
| 107 | 41:66: [0,infinity) |
| 108 | 41:67: [0,infinity) |
| 112 | 40:72: [0,infinity) |
| 113 | 41:72: [0,infinity) |
| 114 | 41:73: [0,infinity) |

