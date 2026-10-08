# Split audit — K2-subglacial-cavity

How this repository was carved out of the pristine **K** monorepo. Regenerate the classification with `python3 K-audit/classify.py K2-subglacial-cavity` and re-check the import graph with `python3 K-audit/verify_repo.py K2-subglacial-cavity`.

## Claim cluster

cavity and 3-D subglacial DNS, real-bed validation, and the field-analysis validation pipeline (§V/§H).

Source: `glaciers/**` minus the scallop-instability cluster (which went to K3) + `general_two_clocks/closure/**` and `compressible/**` (leaf solver dependencies) + one data cache from `general_two_clocks/data/**`.

## Composition

| | files |
|---|---|
| traced to a monorepo file | 298 |
| byte-identical copies | 293 |
| modified (see *Edits*) | 5 |
| new (not in the monorepo) | 1 |

Source directories, by file count:

- `glaciers/validation/reports/` — 75
- `glaciers/validation/synthetic/` — 39
- `glaciers/tests/` — 36
- `glaciers/validation/external/` — 34
- `glaciers/` — 29
- `glaciers/figures/` — 26
- `glaciers/subglacial/` — 24
- `glaciers/validation/external/data/measures0709/` — 8
- `general_two_clocks/closure/` — 7
- `glaciers/validation/external/data/` — 5
- `(monorepo root)`/ — 3
- `general_two_clocks/compressible/` — 3
- `glaciers/subglacial/data/` — 2
- `glaciers/subglacial/moving_boundary/` — 2
- `glaciers/validation/` — 2
- `glaciers/validation/validators/` — 2
- …plus 1 file(s) that sit alone in their source directory (top-level scripts, one-off reports)

## Vendored files

Copied byte-for-byte from the monorepo paths below (this is what makes the repo import-clean on its own):

- `repo root/*` (29 files)
- `closure/*` (7 files)
- `compressible/__init__.py`
- `compressible/ns.py`
- `compressible/solver.py`
- `figures/*` (26 files)
- `subglacial/*` (24 files)
- `subglacial/data/bedmap1_transect.csv`
- `subglacial/data/bushuk_raw_derived.json`
- `subglacial/moving_boundary/__init__.py`
- `subglacial/moving_boundary/stefan.py`
- `tests/*` (36 files)
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

## Excluded files

- none: every monorepo file belonging to this claim cluster was carried over.

## Test-suite accounting

`tests/` carries **36 test files** (glaciers/tests (51) − 15 that went to K3); the whole monorepo has 136 test files across the five repos (78+36+15+2+2 = 133, plus the 3 excluded in K1).

## Verification

`K-audit/verify_repo.py` walks the **AST import graph** of every Python file in this repo, expands each unqualified import against every `sys.path` root the file would actually see, and reports any import that resolves only outside the repository. Result:

```
OK K2-subglacial-cavity: no external edges
```

## Provenance

Pristine snapshot taken **before** any edit: `K-monorepo-archive.tar.gz` (SHA-256 `3c30c68b4d4287787af00539b2cbe75a47dc0536491ec0d1b17a0f61d80b5304`). `FUTURE_WORK.md` / `PAPER_OUTLINE.md` were deliberately left in the archive.
