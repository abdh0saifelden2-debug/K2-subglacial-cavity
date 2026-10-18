# Subglacial cavity — the closure verdict in a cavity, and real-bed validation

The largest cluster of the program: the two-clocks closure tested in a
penalized **subglacial cavity DNS** over synthetic *and* real BEDMAP1 beds
(Parts 9–10g), the 3-D a-posteriori LES that makes basal melt rate
closure-dependent, and the §V/§H **validation pipeline** that takes the
framework's [HYP] predictions to real Antarctic data (Bedmap2, BedMachine,
active lakes, ITS_LIVE velocities).

The two-clocks *observation* and the closure benchmarks it rests on live in
**`K1-two-clocks-theory`**; the scallop instability family and channelisation
live in **`K3-scallop-migration`** (both split from the same monorepo — see
Provenance).

## What was found so far

**Cavity benchmark and melt**
- **[VERIFIED]** The Part-8b closure verdict transfers to a penalized cavity DNS
  over synthetic *and* real BEDMAP1 beds: K-theory kills the wake/backscatter
  structure that controls basal heat flux
  ([`REPORT_SUBGLACIAL.md`](REPORT_SUBGLACIAL.md),
  [`REPORT_SUBGLACIAL_REAL.md`](REPORT_SUBGLACIAL_REAL.md), Figs 31–38), and the
  3-D a-posteriori LES makes the basal **melt rate closure-dependent**
  (`run_subglacial3d.py`).
- **[VERIFIED, RESULT 11]** Counter-gradient heat flux measured: `C_G > −1`
  grows with stratification — flux carries the global pressure field's memory,
  which down-gradient K-theory cannot represent
  ([`REPORT_CG_BUOYANCY.md`](REPORT_CG_BUOYANCY.md), Fig 52, GPU).
- **[VERIFIED + mechanism]** §G.1 thermal-wall ceiling: scalloped walls give
  `Nu/Nu_flat < 1` (conduction-limited, boundary-condition-robust — Robin ice
  wall and Navier slip change nothing); mechanism earned via the exact
  area-partition identity (`scallop_g1_populations.py`); the `(1+CV²)` truncation
  is **FALSIFIED**.

**Mainstream-model correction (drop-in)**
- **[DERIVED → code]** `subglacial/glads_memory_correction.py` turns the RESULT 21
  Mori–Zwanzig projection into a retrofit for operational GlaDS-type closures.
  Large-scale models slave basal sliding to an *instantaneous* effective-pressure
  law, dropping the eliminated channel's memory; the exact reduced dynamics is a
  generalized Langevin equation with kernel `K(τ) = −a·b·e^{−τ/τ₂}`, whose
  `τ₂ → 0` limit *is* the local closure — so the post-drainage **surge lag is
  lost** in the mainstream model. `apply_memory_kernel(...)` convolves it back in.
  Verified deterministically: corrected closure matches the resolved cavity↔channel
  truth to <1e-4, the memoryless closure misses the interior peak
  (`tests/test_glads_memory_correction.py`). The real ISSM/GlaDS run remains
  pending.

**Real-data validation (§H)**
- **[VERIFIED directional]** RTN > 1 concentrates at the grounding line on
  Bedmap2 (median 6 km vs 221 km) and survives an independent BedMachine v4
  cross-check at native 500 m ([`REPORT_RTN_MISI_BAND.md`](REPORT_RTN_MISI_BAND.md),
  `validation/REAL_DATA_RESULTS.md`, Fig 57).
- **[FALSIFIED as written]** the §G.4 literal thermal sliding kernel: the
  `H²/κ ≈ 1.5×10⁵ yr` lag is ~8×10⁴× too slow on 131 real lakes — the lag is
  **hydromechanical**; the peaked kernel *shape* and order-of-magnitude *value*
  are **[DERIVED]** from cavity↔channel physics, and the projection is an exact
  Mori–Zwanzig GLE
  ([`REPORT_HYDRAULIC_MZ_PROJECTION.md`](REPORT_HYDRAULIC_MZ_PROJECTION.md),
  RESULT 21).
- **[VERIFIED — synthetic]** estimator calibrations: GL-migration level-set law
  (RESULT 16, [`REPORT_GLMIG_ESTIMATOR.md`](REPORT_GLMIG_ESTIMATOR.md)),
  kernel-shape-generic lag estimator (RESULT 17,
  [`REPORT_SLIDING_KERNEL_SHAPE.md`](REPORT_SLIDING_KERNEL_SHAPE.md)),
  φ-area inversion (RESULT 18, [`REPORT_RTN_PHI_INVERSION.md`](REPORT_RTN_PHI_INVERSION.md)),
  hydrology-corrected MISI band (RESULT 19), intrusion-clock driver
  (RESULT 20, [`REPORT_RTN_INTRUSION_CLOCK.md`](REPORT_RTN_INTRUSION_CLOCK.md)).
- **[VERIFIED + DERIVED — relocated from K1]** the persistence family NR33–NR35
  (moved here from the theory cluster, since their data applications read this
  repo's validation code): repeat-radar persistence of distributed water is a
  **pressure gauge** (`N ≤ 3.5 bar` at 4 yr; the 7 persistent-specular ICECAP
  cells satisfy `φ ≥ 0.98` — [`REPORT_NEW_RELATIONSHIPS10.md`](REPORT_NEW_RELATIONSHIPS10.md));
  the ice-side interface kernel **is** an exact tempered half-order fractional
  derivative ([`REPORT_NEW_RELATIONSHIPS11.md`](REPORT_NEW_RELATIONSHIPS11.md));
  and the bracket is two-sided with a dated melt correction
  ([`REPORT_NEW_RELATIONSHIPS12.md`](REPORT_NEW_RELATIONSHIPS12.md)).
- Also in this cluster: tidal-admittance and temporal-CSD field analyses
  ([`REPORT_TIDAL_ADMITTANCE_FIELD.md`](REPORT_TIDAL_ADMITTANCE_FIELD.md),
  [`REPORT_TEMPORAL_CSD_FIELD.md`](REPORT_TEMPORAL_CSD_FIELD.md)), the
  spatial-EWS field ([`REPORT_SPATIAL_EWS_FIELD.md`](REPORT_SPATIAL_EWS_FIELD.md)),
  the ATL15 lake-drainage response
  ([`REPORT_LAKE_DRAINAGE_RESPONSE.md`](REPORT_LAKE_DRAINAGE_RESPONSE.md)), radar
  roughness ([`REPORT_RADAR_ROUGHNESS.md`](REPORT_RADAR_ROUGHNESS.md)), the
  sliding-kernel shape ([`REPORT_SLIDING_KERNEL_SHAPE.md`](REPORT_SLIDING_KERNEL_SHAPE.md)),
  the SN master curve ([`REPORT_SN_MASTER_CURVE.md`](REPORT_SN_MASTER_CURVE.md)),
  and candidates 1 and 4 ([`REPORT_CANDIDATE1.md`](REPORT_CANDIDATE1.md),
  [`REPORT_CANDIDATE4.md`](REPORT_CANDIDATE4.md)).

## What remains a HYP

- **§G.3** RTN as the *threshold* for ocean-intrusion regime change ([HYP / LIT];
  only the directional concentration is verified).
- **§G.4** the hydromechanical lag *mechanism* on real glaciers ([HYP mechanism];
  shape/value derived, not data-fit — drainage dates are USAP-DC-gated).
- **§H.1.2/§H.1.3** intrusion-clock *hydraulic pacing* and `u_*` pacing
  ([HYP → disfavored at continental scale]; **[HYP supported]** in marine West
  Antarctica, §H.1.4 — regime-dependent).
- **§G.6** unified melt-rate phenomenology (OK only with *local* flux).

## What is pending

- Gated data: USAP-DC lake drainage-date series (§V.2 full lag fit), BedMachine
  v3 via Earthdata, CATS2008 tides
  (`validation/external/tide_loader.py`).
- §H.3 CMN correction inside a *real* ice-sheet model (ISSM/GlaDS) — the
  synthetic-solver half is done.
- GPU re-runs of the full CuPy family on a CUDA device. The GPU backend
  verification harness `gpu_family_sweep.py` spans this cluster, K3 and K5 and
  is preserved in the monorepo archive
  ([`glaciers/gpu_family_sweep.py`](https://github.com/abdh0saifelden2-debug/K/blob/main/glaciers/gpu_family_sweep.py)).

## Contents

- `subglacial/` — cavity DNS/LES library: `flow.py`, `flow3d.py`, candidates
  1/3/4 probes (the double-diffusion candidate 2 solver lives here too, but its
  *runs* are in `K5-ocean-probes`), Stefan/moving-boundary, slip/wall-flux gates,
  `glads_memory_correction.py`, bundled BEDMAP1 transect (`data/`).
- `validation/` — §V pipeline: `synthetic/` harnesses, `validators/`,
  `external/` real-data loaders + runners, `reports/`, `REAL_DATA_RESULTS.md`.
- `closure/`, `compressible/` — vendored leaf solver dependencies from the theory
  cluster, so this repo imports cleanly on its own (see `AUDIT.md`).
- NR33–NR35 chains (relocated from the theory cluster): `new_relationships10.py`,
  `new_relationships11.py`, `new_relationships12.py`, reports
  `REPORT_NEW_RELATIONSHIPS10.md`, `REPORT_NEW_RELATIONSHIPS11.md`,
  `REPORT_NEW_RELATIONSHIPS12.md`, figures `figures/nr33_*`, `figures/nr34_*`,
  `figures/nr35_*`.
- `GETTING_STARTED.md` — 15-minute tutorial: plug the closure into a
  GlaDS/Röthlisberger model and watch the post-drainage surge lag appear.
- Runners: `run_subglacial.py`, `run_subglacial3d.py`, `run_candidate1.py`,
  `run_candidate4.py`, `run_stefan_sweep.py`.
- `figures/` — Figs 31–38, 49–52, 56–59 + candidate JSONs.
- `tests/` — 39 test modules.

## Quick start

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python run_subglacial.py --bed real --out-dir figures
python validation/external/run_rtn_bedmap2.py --stride 3 --phi 0.9
python -m pytest            # 414 passed, 16 skipped
```

## Provenance

Split out of the **K** monorepo, partitioned by claim cluster:

| repository | claim cluster |
|---|---|
| `K1-two-clocks-theory` | observation, two-clocks theory, closure benchmarks |
| `K2-subglacial-cavity` *(this repo)* | cavity DNS, real-bed validation, field-analysis validation |
| `K3-scallop-migration` | scallop instability family, channelisation |
| `K4-swirl-vortex` | atmospheric vortex application |
| `K5-ocean-probes` | ice–ocean double diffusion |

The pristine monorepo was snapshotted **before** any edit:
`K-monorepo-archive.tar.gz`, SHA-256
`ef637ff55f912a5d1404f677429f9429eccc8102a8cab23cee79cf055bbf1220`
(`K-monorepo-archive.sha256`). The cross-repo claim ledger (`FUTURE_WORK.md`)
and paper outline are deliberately **not** copied here — they live only in that
archive. [`AUDIT.md`](AUDIT.md) records the full split audit: every vendored
file, every edit, and the AST verification result (reproduce it with
[`K-audit` v1.0](https://github.com/abdh0saifelden2-debug/K-audit/tree/v1.0)).

## TODO (future)
- (6) A-posteriori closed-loop LES benchmark (projected-FDT vs Smagorinsky vs filtered DNS)
