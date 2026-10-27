"""Security helpers: redaction, attestation, paper-only guards, Merkle lineage, entropy proxy.

Research controls only. Not a certified security product. Zero-trust isolation stubs.
"""

from __future__ import annotations

import hashlib
import math
import re
from datetime import datetime, timezone

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|private[_-]?key|seed|mnemonic|bip39|wallet[_-]?key)\s*[:=]\s*[\w+/=]{8,}"),
    re.compile(r"(?i)(sk-|pk_|ghp_|github_pat_|solana[_-]?key|ed25519)"),
    re.compile(r"\b(?:[a-z]+\\s+){11,23}[a-z]+\\b"),  # rough BIP39 fragment
    re.compile(r"(?i)(session[_-]?token|cookie|bearer)\s*[:=]\s*[\w+/=.-]{10,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),  # PEM headers
    re.compile(r"0x[a-fA-F0-9]{64}"),  # ETH private key style
    re.compile(r"(?i)(hardware[_-]?wallet|ledger|trezor).*export"),
]


def _entropy(s: str) -> float:
    """Shannon entropy proxy for high-entropy secret detection."""
    if not s:
        return 0.0
    prob = [float(s.count(c)) / len(s) for c in set(s)]
    return -sum(p * math.log2(p) for p in prob if p > 0)


def redact(text: str) -> str:
    """Redact secret-like strings. Expanded for PEM, ETH keys, high-entropy blobs."""
    for pat in SECRET_PATTERNS:
        text = pat.sub("[REDACTED]", text)
    # High-entropy long tokens
    tokens = re.findall(r"\b[\w+/=.-]{32,}\b", text)
    for tok in tokens:
        if _entropy(tok) > 4.2:
            text = text.replace(tok, "[REDACTED-ENTROPY]")
    return text


def assert_paper_only(mode: str) -> None:
    if mode.upper() != "PAPER":
        raise PermissionError("live mode refused; paper-only research system")


def refuse_trade_secret(name: str) -> None:
    lowered = name.lower()
    if any(k in lowered for k in ("trade", "withdraw", "transfer", "order", "exchange_key", "live_api")):
        raise PermissionError(f"trade/withdrawal credential refused: {name}")


def attest_source(label: str, body: str) -> str:
    """Hash label + body for fixture integrity."""
    return hashlib.sha256(f"{label}:{body}".encode()).hexdigest()


def merkle_lineage(prev_hash: str, current: str, ts: str | None = None, extra: str = "") -> str:
    """Enhanced Merkle-style sealed multi-hash: prev + current + ts + optional extra context."""
    ts = ts or datetime.now(timezone.utc).isoformat()
    payload = f"{prev_hash}:{current}:{ts}:{extra}"
    return hashlib.sha256(payload.encode()).hexdigest()


def anomaly_score(volume: float, avg_volume: float, price_jump: float, kurtosis_proxy: float = 0.0) -> float:
    """Enhanced anomaly: volume spike, price jump, and kurtosis proxy for fat tails."""
    vol_ratio = volume / (avg_volume or 1)
    jump_score = abs(price_jump) * 10
    kurt_score = max(kurtosis_proxy - 3, 0) * 0.1  # excess kurtosis
    return min(1.0, max(vol_ratio - 1, 0) * 0.25 + jump_score + kurt_score)


def isolation_check(context: str) -> bool:
    """Zero-trust isolation stub: research context must not share operator secrets."""
    return context.lower() in ("research", "audit", "paper")
