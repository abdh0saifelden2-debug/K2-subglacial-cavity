# A-posteriori closed-loop LES benchmark

Synthetic sanity check (no closed-loop time integration performed in this artifact).
Models evaluated instantaneously on filtered DNS field.

## Metrics
- rms_dns, rms_filtered: RMS of initial fields
- smag_rms, pfd_rms: RMS of SGS model output (instantaneous)
- spec_l2_err_pfd_vs_filtered, spec_l2_err_smag_vs_filtered: spectral L2 on initial fields (trivially ~0)

Artifact: `figures/a_posteriori_benchmark_full.json`
Reproduce: `python a_posteriori_benchmark_full.py`

This is a minimal sanity check; true a-posteriori closed-loop validation
(divergence drift, spectrum error over long integration, ensemble over seeds)
remains TODO. The amplitude contrast (PFD ~14% below filtered; Smag ~83% below)
is qualitatively consistent with a-priori expectations.
