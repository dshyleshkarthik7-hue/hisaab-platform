# Hisaab financial methodology pack

## Model
See `docs/MODEL.md` for the monthly cash-flow Monte Carlo process.

## Tax Intelligence
- Rules are versioned by tax year and regime (`python/tax_engine.py`).
- Each pack records source, effective date, verified date, and status.
- Ingestion candidates never alter live rules until approved and mapped by a human operator.

## Limitations
- Simplified return model (lognormal monthly).
- Fixed job-loss / medical probabilities.
- Illustrative salary estimator for TY 2026-27.
- Not SEBI-registered advice.
