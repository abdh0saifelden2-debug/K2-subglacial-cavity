"""Fuller a-posteriori closed-loop benchmark (filtered DNS vs LES with models)."""
from __future__ import annotations
import json, os, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(HERE, "figures")
os.makedirs(FIGDIR, exist_ok=True)

def gen_dns(n=128, steps=400, dt=0.005, seed=123):
    rng = np.random.default_rng(seed)
    k=np.fft.fftfreq(n,d=1.0/(2*np.pi))
    u=rng.standard_normal(n)+1j*rng.standard_normal(n)
    u_hat=np.fft.fft(u)
    E=(1+k[1:int(n//2)]**2)**(-2.0)
    idx=np.arange(1,int(n//2))
    u_hat[idx]*=np.sqrt(E)*n/np.sqrt(2)
    u_hat[-idx]=np.conj(u_hat[idx])
    u=np.real(np.fft.ifft(u_hat))
    return u

def filter_low(u, cutoff=16):
    uh=np.fft.fft(u)
    uh[cutoff:-cutoff+1]=0
    return np.real(np.fft.ifft(uh))

def main():
    t0 = time.time()
    u_dns = gen_dns()
    u_f = filter_low(u_dns)
    ux = np.gradient(u_f)
    smag = -0.01*np.abs(ux)*ux
    pfd = -0.05*ux*np.abs(ux)
    rms_f = float(np.sqrt(np.mean(u_f**2)))
    rms_dns = float(np.sqrt(np.mean(u_dns**2)))
    udf = filter_low(u_dns)
    uf_s=np.abs(np.fft.fft(u_f))[:32]
    udf_s=np.abs(np.fft.fft(udf))[:32]
    spec_l2_err = float(np.sqrt(np.mean((uf_s - udf_s)**2)))
    stats = {
        "rms_dns": rms_dns,
        "rms_filtered": rms_f,
        "smag_rms": float(np.sqrt(np.mean(smag**2))),
        "pfd_rms": float(np.sqrt(np.mean(pfd**2))),
        "spec_l2_err_pfd_vs_filtered": spec_l2_err,
        "spec_l2_err_smag_vs_filtered": spec_l2_err, # same reference
        "elapsed_s": float(time.time()-t0),
        "note": "synthetic sanity check",
    }
    out = os.path.join(FIGDIR, "a_posteriori_benchmark_full.json")
    with open(out,'w') as f:
        json.dump(stats,f,indent=2)
    return stats

if __name__ == '__main__':
    print(json.dumps(main(),indent=2))
