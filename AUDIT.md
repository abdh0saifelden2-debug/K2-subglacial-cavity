# Split audit — K2-subglacial-cavity

How this repository was carved out of the pristine **K** monorepo. Regenerate the classification with [`K-audit` v1.0](https://github.com/abdh0saifelden2-debug/K-audit/tree/v1.0) — `python3 classify.py --mono K K2-subglacial-cavity` — and re-check the import graph with `python3 verify_repo.py --mono K K2-subglacial-cavity` (both run from a clone of `K-audit` against a clone of the monorepo).

## Claim cluster

cavity and 3-D subglacial DNS, real-bed validation, and the field-analysis validation pipeline (§V/§H).

Source: `glaciers/**` minus the scallop-instability cluster (which went to K3) + `general_two_clocks/closure/**` and `compressible/**` (leaf solver dependencies) + one data cache from `general_two_clocks/data/**`, plus the NR33–NR35 chains relocated from `general_two_clocks/` (scripts, reports, tests, figures) and `glaciers/GETTING_STARTED.md` (adapted).

## Composition

| | files |
|---|---|
| traced to a monorepo file | 314 |
| byte-identical copies | 299 |
| modified (see *Edits*) | 15 |
| new (not in the monorepo) | 6 |

Source directories, by file count:

- `glaciers/validation/reports/` — 75
- `glaciers/validation/synthetic/` — 39
- `glaciers/tests/` — 36
- `glaciers/validation/external/` — 34
- `glaciers/` — 30
- `glaciers/figures/` — 26
- `glaciers/subglacial/` — 24
- `glaciers/validation/external/data/measures0709/` — 8
- `general_two_clocks/closure/` — 7
- `general_two_clocks/` — 6
- `general_two_clocks/figures/` — 6
- `glaciers/validation/external/data/` — 5
- `(monorepo root)`/ — 3
- `general_two_clocks/compressible/` — 3
- `general_two_clocks/tests/` — 3
- `glaciers/subglacial/data/` — 2
- `glaciers/subglacial/moving_boundary/` — 2
- `glaciers/validation/` — 2
- `glaciers/validation/validators/` — 2
- …plus 1 file(s) that sit alone in their source directory (top-level scripts, one-off reports)

## Vendored files

Copied byte-for-byte from the monorepo paths below (this is what makes the repo import-clean on its own):

- `repo root/*` (30 files)
- `closure/*` (7 files)
- `compressible/__init__.py`
- `compressible/ns.py`
- `compressible/solver.py`
- `figures/*` (32 files)
- `subglacial/*` (24 files)
- `subglacial/data/bedmap1_transect.csv`
- `subglacial/data/bushuk_raw_derived.json`
- `subglacial/moving_boundary/__init__.py`
- `subglacial/moving_boundary/stefan.py`
- `tests/*` (37 files)
- `validation/README.md`
- `validation/REAL_DATA_RESULTS.md`
- `validation/external/*` (33 files)
- `validation/external/data/atl15_lake_dh_cache.json`
- `validation/external/data/lake_drainage_response_cache.json`
- `validation/external/data/lake_lag_matched.json`
- `validation/external/data/spatial_ews_field_cache.json`
- `validation/external/data/temporal_csd_field_cache.json`
- `validation/external/data/tidal_admittance_field_cache.json`
- `validation/external/data/measures0709/*` (8 files)
- `validation/reports/*` (75 files)
- `validation/synthetic/*` (38 files)
- `validation/validators/rtn_validator.py`
- `validation/validators/sliding_validator.py`

## Edits

- `validation/synthetic/creep_stefan_coupled.py` — `REPO` was computed as `dirname`×3 (assuming `glaciers/validation/synthetic/`, i.e. monorepo depth 3) and joined `"glaciers"` into two paths. In this repo the file is at `validation/synthetic/` (depth 2), so `REPO` is now `dirname`×2 and the `"glaciers"` path segments were dropped from `R14_JSON` and the `--out` default. Both targets resolve (`figures/56_scallop_amplitude_harmonics.json`, `validation/reports/creep_stefan_coupled.json`).
- `validation/external/lake_drainage_response_atl15.py` — `_ATL15` pointed at `../../../general_two_clocks/data/atl15_lake_dh_cache.json` (a monorepo-relative raw cache). It now points at the repo-local copy `validation/external/data/atl15_lake_dh_cache.json`, so the gated test block in `tests/test_lake_drainage_response.py` runs instead of skipping.
- `README.md` — rewritten to stand alone: no `../` links into sibling monorepo folders, run commands given from the repo root, and a Provenance section pointing at the archive.
- `pyproject.toml` — rewritten for this repo: `testpaths`/`pythonpath` scoped to this repo instead of all five monorepo domains, and the dependency list trimmed to the libraries this claim cluster imports.
- `requirements.txt` — rewritten for this repo: `testpaths`/`pythonpath` scoped to this repo instead of all five monorepo domains, and the dependency list trimmed to the libraries this claim cluster imports.
- `new_relationships10.py`, `new_relationships11.py`, `new_relationships12.py` — relocated from `general_two_clocks/` (previously excluded from every split; K2 is their home because their data applications read `validation/`): `sys.path` roots rewritten from `../glaciers/validation[*]` to the repo-local `validation/[*]`, availability-hint and docstring paths updated, run/test commands made repo-root-relative.
- `REPORT_NEW_RELATIONSHIPS10.md`, `REPORT_NEW_RELATIONSHIPS11.md`, `REPORT_NEW_RELATIONSHIPS12.md` — relocated from `general_two_clocks/`; run/test commands and in-text module paths made repo-root-relative; the `CROSS_RELATIONSHIPS_INDEX.md` link now points at the monorepo archive, since the index is deliberately not copied into any split.
- `tests/test_new_relationships11.py`, `tests/test_new_relationships12.py` — relocated from `general_two_clocks/tests/`; docstring and `sys.path` monorepo segments dropped. (`tests/test_new_relationships10.py` is a byte-identical copy, so it appears under *Vendored files*.)
- `GETTING_STARTED.md` — adapted from `glaciers/GETTING_STARTED.md`: run commands and paths made repo-root-relative; the theory-side pointers (`REPORT_CLOSURE.md`, `REPORT_THEORY.md`, `run_closure.py`) now link to `K1-two-clocks-theory`.
- `README.md`, `AUDIT.md`, `validation/REAL_DATA_RESULTS.md` — NR33–NR35 relocation noted; test counts updated (39 modules; `422 passed, 8 skipped` in CI); canonical archive SHA; `K-audit` v1.0 reference.

## Excluded files

- none: every monorepo file belonging to this claim cluster was carried over,
  plus the NR33–NR35 chains and `GETTING_STARTED.md` relocated here from K1
  (see K1 `AUDIT.md`).

## Test-suite accounting

`tests/` carries **39 test files** (glaciers/tests (51) − 15 that went to K3, plus the 3 NR33–NR35 modules relocated from K1); the whole monorepo has 136 test files across the five repos (78+39+15+2+2 = 136).

## Verification

[`K-audit`](https://github.com/abdh0saifelden2-debug/K-audit/tree/v1.0) `verify_repo.py` walks the **AST import graph** of every Python file in this repo, expands each unqualified import against every `sys.path` root the file would actually see, and reports any import that resolves only outside the repository (the relocated NR33–NR35 modules import only repo-local modules). Result:

```
OK K2-subglacial-cavity: no external edges
```

## Provenance

Pristine snapshot taken **before** any edit: `K-monorepo-archive.tar.gz` (SHA-256 `ef637ff55f912a5d1404f677429f9429eccc8102a8cab23cee79cf055bbf1220`). `FUTURE_WORK.md` / `PAPER_OUTLINE.md` were deliberately left in the archive.
