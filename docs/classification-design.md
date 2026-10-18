# Classification design

The taxonomy is a navigation system for theoretical research. Each node defines a subject, its boundaries, representative objects and connections to other fields. Method and validation tags describe possible tasks within a subject; they do not assign one research method or resource requirement to an entire discipline.

## Classification references

| Reference | Useful structure | Local adaptation and limits |
| --- | --- | --- |
| [MSC2020 introduction](https://msc2020.org/) and [classification list](https://msc2020.org/MSC_2020.pdf) | Mathematical hierarchy and cross-references | The top-level list and selected logic, Markov-process and lattice-model entries were inspected; local branches remain an editorial grouping, with no exhaustive code-level crosswalk |
| [APS PhySH design](https://physh-alpha.aps.org/about) | Separate subject, system and technique facets; related concepts | One primary problem record with cross-domain links; no claim of an exact PhySH ontology mapping |
| [OECD Frascati Manual 2015](https://www.oecd.org/content/dam/oecd/en/publications/reports/2015/10/frascati-manual-2015_g1g57dcb/9789264239012-en.pdf), Table 2.2 | Broad coverage across natural sciences, engineering and social sciences | A dated reference for breadth, rather than a detailed classification of theoretical tasks or a claim about the latest FORD release |
| [AEA JEL codes](https://www.aeaweb.org/econlit/jelCodes.php?view=jel) | Distinct game, equilibrium, decision, social-choice and econometric subjects | Formal tasks are included; empirical and policy claims require their own evidence |
| [arXiv category taxonomy](https://arxiv.org/category_taxonomy) | Literature-discovery vocabulary across fields | Categories do not establish peer-review acceptance or problem status |
| [ACM-hosted CCS mapping](https://ccecc.acm.org/guidance/information-technology-applied/classification-mappings/acm-computing-classification-system-2012) | Separation of theoretical computation from broader software topics | The referenced curriculum mapping is partial; full code-level alignment remains unverified |

The [source directory](sources.md) includes field-specific reviews, problem sets, research communities and papers. Similar labels do not establish equivalence to an external classification code. Local node IDs remain stable when external schemes change.

The atlas uses its own descriptions and organization. The MSC classification has separate CC BY-NC-SA terms; linking to it does not relicense it under the atlas's licenses. Reuse of external classification text or structure must comply with its own terms and attribution requirements.

## Primary subject and cross-links

Place a problem according to its target claim, then link relevant methods and applications. A finite game equilibrium certificate belongs in game theory, with links to algorithms and optimization. A theorem about a physical model may belong in mathematical physics and link to its physical application. Entropy inequalities connect information theory, probability and convex geometry through one problem record.

Candidate and card identity is independent of placement. Problem relations refer to existing IDs and state the assumptions needed for any claimed equivalence. Subject cross-links support discovery; they do not assert that the subjects or problems are equivalent.

## Scope

The map includes mathematics, logic, computation, probability, statistics and learning, information, theoretical and mathematical physics, chemistry and materials, biology, economics and games, networks, Earth and climate science, astrophysics, control and engineering, and formal cognition and language.

Formal medical, epidemiological and agricultural models may fit within biology, statistics or control. Clinical recommendations, field trials and descriptive studies fall outside the research scope. Robotics, operations research and theoretical signal processing connect control, algorithms and information. A problem needs a defined statement and a means of evaluating results.

Experiment dependence is assessed per task. A node's `validation_options` lists possible forms of evidence; individual cards specify the requirements. A formal model problem may be studied independently while its empirical interpretation still requires substantial data or experiments. See the [scope decisions](../data/scope-decisions.json).

## Coverage

The [coverage matrix](coverage.md) separates classification references, research entry points, candidates, cards and cross-linked problems. Counts aggregate explicitly mapped descendants. Cross-links do not multiply a problem's primary record, while one source may serve several subjects.

A journal or society directory provides an entry point but does not establish detailed problem coverage. Branch depth varies with the available detail. Coverage is selective and favors accessible English-language sources; source and problem counts cannot estimate the fraction of all research that has been covered.
