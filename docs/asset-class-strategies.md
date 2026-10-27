# Asset-class strategy notes v0.46

Research heuristics only. Not forecasts.

Regime from regime.py: trend / range / stress.
Anomaly score from security.py feeds adaptive sizing.

## Major
EMA trend + ADX>25 + Ichimoku above cloud + Bollinger mid + MACD >0 + StochRSI 20-80 + vol clustering <1.5 + low anomaly. Range reversion with RSI washout + divergence + BB lower + MACD not strongly negative. Adaptive size. Cap ~8%.

## Large-cap alt
Volume breakout + ADX + Ichimoku + BB upper + MACD >0. Adaptive size. Cap 4%.

## Stablecoin
Peg watch/depeg alert only. Size 0.

## DeFi
Calm trend + ADX + Ichimoku + vol-profile concentration + MACD >0 + low anomaly. Adaptive size. Cap 2%.

## Meme
Qualified burst + ADX + vol concentration + StochRSI <85. Adaptive size. Cap 0.5%, 3-bar horizon.

## L2
Relative strength vs non-stress benchmark + ADX + BB mid + MACD >0. Adaptive size. Cap 3%.

## RWA
Slow trend + ADX + MACD, gap halt, low anomaly. Adaptive size. Cap 2%.

## Perpetual
Negative funding carry if drift contained + ADX ok + low anomaly. Adaptive size. Cap 2%.

Still out of scope: live orders, trade keys, return claims.
