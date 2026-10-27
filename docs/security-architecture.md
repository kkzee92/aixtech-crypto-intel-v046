# Security architecture notes v0.46

Research controls for a paper-only crypto information system. Not a certified product.

## Zero-trust principles

- Paper-only execution guard: any non-PAPER mode raises PermissionError.
- Trade/withdrawal credential names refused at boundary.
- Isolation check stub: research/audit contexts must not share operator secrets.
- No live network by default; fixtures are synthetic and attested.

## Data security

- Expanded redaction: API keys, seeds, BIP39 fragments, PEM private key headers, ETH-style 0x[64 hex] keys, session tokens, high-entropy long tokens via Shannon entropy proxy (>4.2).
- Hash-chained audit log with enhanced Merkle-style multi-hash (prev + current + timestamp + optional extra context).
- Source attestation via SHA-256 of label + body.
- Anomaly scoring: volume spike + price jump + kurtosis proxy feeds risk gates and adaptive sizing.
- PDPA-style tripwire recommended over fixtures and docs.
- gitleaks / secret scanning recommended in CI.

## Lineage and integrity

Sealed hash chain for every research decision and fixture load. Data residency stamp: synthetic research only.

## Honesty

These are research stubs. Do not treat as production security controls. No live trading secrets in this tree.
