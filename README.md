# AIxTech crypto intel v0.46: paper-only trading information system

Research harness for automated cryptocurrency **information** and paper strategy evaluation. It does not place live orders, does not store exchange secrets, and is not financial advice.

Builds on [zeekiankok92/aixtech-crypto-intel](https://github.com/zeekiankok92/aixtech-crypto-intel) and successive enhancements under kkzee92 (latest prior: v0.45).

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![version](https://img.shields.io/badge/version-0.46.0-blue)
![mode](https://img.shields.io/badge/execution-paper%20only-orange)
![Licence](https://img.shields.io/badge/licence-MIT-green)

## Enhancements in v0.46

- MACD proxy (EMA12-EMA26) and StochRSI momentum confirmation across asset classes.
- Adaptive position sizing reduced under high anomaly score or volatility clustering.
- Expanded multi-factor filters: MACD positive for trend entries, StochRSI not extreme for memes.
- Strengthened security: additional redaction for PEM private keys, ETH-style 0x64 hex keys, high-entropy tokens via Shannon entropy proxy; enhanced Merkle lineage with optional extra context; kurtosis in anomaly scoring; isolation check stub.
- Updated docs for strategies and security architecture.

See [docs/asset-class-strategies.md](docs/asset-class-strategies.md) and [docs/security-architecture.md](docs/security-architecture.md).

## What it does

- Eight asset classes with advanced multi-factor research rules incorporating MACD, StochRSI, adaptive anomaly sizing, prior Bollinger/vol-profile/Ichimoku/ADX.
- Multi-scale regime + volatility tier + anomaly scoring (incl. kurtosis).
- Signals with EMA, MACD, Bollinger, ADX, VWAP proxies, StochRSI, then multi-gate risk with adaptive size.
- Paper-only backtests with class costs; enhanced hash-chained audit with sealed Merkle multi-hash.
- Synthetic candles only. No network by default.

| Asset class | Enhanced research rule (v0.46) | Risk cap (base) | Cost |
|---|---|---|---|
| Major | Multi-EMA + MACD + StochRSI + Bollinger + ADX + Ichimoku + controlled anomaly/vol; stand aside stress/high-anomaly | 8% (adaptive) | 8 bps |
| Large-cap alt | Volume breakout + multi-momentum + MACD + Bollinger + ADX | 4% (adaptive) | 14 bps |
| Stablecoin | Adaptive peg + multi-stat alerts only | 0% | n/a |
| DeFi | Calm multi-scale + channel + MACD + cloud + vol-profile + low anomaly | 2% (adaptive) | 22 bps |
| Meme | Qualified burst with volume profile, StochRSI not extreme, consistency filters | 0.5% (adaptive) | 45 bps |
| L2 | Multi-period RS + MACD + BB + relative volume vs benchmark | 3% (adaptive) | 16 bps |
| RWA | Slow multi-scale low-vol trend with MACD, adaptive gap, anomaly | 2% (adaptive) | 12 bps |
| Perpetual | Funding carry with adaptive drift, stability, low anomaly | 2% (adaptive) | 10 bps |

## Run

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
PYTHONPATH=src python -c "from crypto_intel.strategies import signal_for; print('ready')"
PYTHONPATH=src pytest tests/ -q
```

## Controls

Paper-only. No live credentials. Class caps with adaptive confidence and sizing under anomaly/vol, kill switch stub, drawdown, statistical anomaly (incl. kurtosis) + correlation + MACD/StochRSI gates, hash-chained audit with enhanced Merkle, expanded redaction (PEM/ETH/entropy), PDPA tripwire, gitleaks recommended. Zero-trust research design with isolation stubs.

## Honesty

No live exchange connector. Scores describe synthetic fixtures. Not investment, legal, or compliance advice. Research only.
