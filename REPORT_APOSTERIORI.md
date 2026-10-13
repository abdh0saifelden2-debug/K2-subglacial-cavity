# A-posteriori closed-loop LES benchmark

Minimal 1D synthetic benchmark comparing Smagorinsky and projected-FDT (PFD)
against filtered DNS.

## Metrics
- dns_rms, filtered_rms: RMS of fields
- smag_rms_sgs, pfd_rms_sgs: RMS of SGS model output
- corr_smag_filtered: correlation between Smagorinsky SGS and filtered gradient (placeholder)

Artifact: `figures/a_posteriori_closed_loop_benchmark.json`
Reproduce: `python a_posteriori_closed_loop_benchmark.py`

This is a minimal sanity check; full a-posteriori validation (divergence drift,
spectrum error, stability over long integration) remains TODO per README.
