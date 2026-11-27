# 投注建议 · 2026-11-27

覆盖 11-27 至 11-28 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 114 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Maritimo vs Nacional | 葡超 | 11-27 21:15 | 客胜 Nacional | 3.07 | **3.17** | 3.44* | €1.00 |
| 2 | Southampton vs Middlesbrough | 英冠 | 11-27 21:00 | 主胜 Southampton | 2.69 | **2.78** | 2.97* | €1.00 |
| 3 | Oud-Heverlee Leuven vs Kortrijk | 比甲 | 11-27 20:45 | 小于 2.5 球 | 2.03 | **2.09** | 2.18* | €1.00 |
| 4 | Venezia vs Bologna | 意甲 | 11-27 20:45 | 客胜 Bologna | 2.24 | **2.31** | 2.40* | €1.00 |
| 5 | Levante vs Santander | 西甲 | 11-27 21:00 | 主胜 Levante | 1.94 | **2.00** | 2.00* | €1.00 |
| 6 | Paderborn vs Schalke 04 | 德甲 | 11-28 15:30 | 小于 2.5 球 | 1.66 | **1.71** | 2.01* | €1.00 |
| 7 | Luton vs Oxford | 英甲 | 11-28 16:00 | 客胜 Oxford | 3.47 | **3.57** | 4.14* | €1.00 |
| 8 | Exeter vs Crawley Town | 英乙 | 11-28 13:30 | 小于 2.5 球 | 1.66 | **1.71** | 1.84* | €1.00 |
| 9 | Walsall vs Northampton | 英乙 | 11-28 16:00 | 小于 2.5 球 | 1.77 | **1.83** | 1.92* | €1.00 |
| 10 | Preston vs Norwich | 英冠 | 11-28 13:30 | 主胜 Preston | 4.19 | **4.31** | 4.48* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Maritimo vs Nacional — 客胜 Nacional**

```
20261127-P1-Maritimo-Nacional-A
```

**2. Southampton vs Middlesbrough — 主胜 Southampton**

```
20261127-E1-Southampton-Middlesbrough-H
```

**3. Oud-Heverlee Leuven vs Kortrijk — 小于 2.5 球**

```
20261127-B1-Oud-HeverleeLeuven-Kortrijk-U25
```

**4. Venezia vs Bologna — 客胜 Bologna**

```
20261127-I1-Venezia-Bologna-A
```

**5. Levante vs Santander — 主胜 Levante**

```
20261127-SP1-Levante-Santander-H
```

**6. Paderborn vs Schalke 04 — 小于 2.5 球**

```
20261128-D1-Paderborn-Schalke04-U25
```

**7. Luton vs Oxford — 客胜 Oxford**

```
20261128-E2-Luton-Oxford-A
```

**8. Exeter vs Crawley Town — 小于 2.5 球**

```
20261128-E3-Exeter-CrawleyTown-U25
```

**9. Walsall vs Northampton — 小于 2.5 球**

```
20261128-E3-Walsall-Northampton-U25
```

**10. Preston vs Norwich — 主胜 Preston**

```
20261128-E1-Preston-Norwich-H
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261127-P1-Maritimo-Nacional-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261127-E1-Southampton-Middlesbrough-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261127-B1-Oud-HeverleeLeuven-Kortrijk-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261127-I1-Venezia-Bologna-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261127-SP1-Levante-Santander-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261128-D1-Paderborn-Schalke04-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261128-E2-Luton-Oxford-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261128-E3-Exeter-CrawleyTown-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261128-E3-Walsall-Northampton-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261128-E1-Preston-Norwich-H --odds <Tipico赔率> --stake 1.00
```

</details>

「可得赔率」带 * 的是市场最高赔率（只说明这个价格在市场上存在，
不一定在 Tipico）；不带 * 的是你自己填进来的 Tipico 赔率。

## 同场组合参考（胜负 + 大小球）

没有数据源报组合赔率，所以这些**不是推荐**，只是阈值：
在 Tipico 的组合投注里找到对应选项，**赔率 ≥ 最低赔率才值得下**。
注意组合的公平赔率不等于两个盘口相乘——平局和大球强烈负相关。

| 比赛 | 组合 | 公平赔率 | **最低赔率** | 相乘会误算成 |
|---|---|---|---|---|
| Oud-Heverlee Leuven vs Kortrijk | 平局 + 小于 2.5 球 | 4.84 | **4.98** | 7.75 |
| Oud-Heverlee Leuven vs Kortrijk | 主胜 Oud-Heverlee Leuven + 小于 2.5 球 | 5.54 | **5.71** | 4.04 |
| Oud-Heverlee Leuven vs Kortrijk | 客胜 Kortrijk + 小于 2.5 球 | 9.41 | **9.70** | 8.56 |
| Paderborn vs Schalke 04 | 平局 + 小于 2.5 球 | 3.25 | **3.35** | 4.95 |
| Paderborn vs Schalke 04 | 主胜 Paderborn + 小于 2.5 球 | 6.55 | **6.74** | 4.65 |
| Paderborn vs Schalke 04 | 客胜 Schalke 04 + 小于 2.5 球 | 7.00 | **7.21** | 5.38 |
| Southampton vs Middlesbrough | 主胜 Southampton + 大于 2.5 球 | 3.87 | **3.99** | 4.56 |
| Southampton vs Middlesbrough | 平局 + 小于 2.5 球 | 5.96 | **6.14** | 9.71 |
| Southampton vs Middlesbrough | 主胜 Southampton + 小于 2.5 球 | 8.88 | **9.14** | 6.60 |
| Preston vs Norwich | 平局 + 小于 2.5 球 | 6.20 | **6.38** | 10.13 |
| Preston vs Norwich | 主胜 Preston + 大于 2.5 球 | 6.39 | **6.58** | 7.14 |
| Preston vs Norwich | 主胜 Preston + 小于 2.5 球 | 12.15 | **12.52** | 10.14 |
| Luton vs Oxford | 客胜 Oxford + 大于 2.5 球 | 5.11 | **5.26** | 5.90 |
| Luton vs Oxford | 平局 + 小于 2.5 球 | 6.26 | **6.45** | 10.08 |
| Luton vs Oxford | 客胜 Oxford + 小于 2.5 球 | 10.79 | **11.12** | 8.41 |
| Exeter vs Crawley Town | 平局 + 小于 2.5 球 | 3.77 | **3.88** | 5.66 |
| Exeter vs Crawley Town | 主胜 Exeter + 小于 2.5 球 | 4.47 | **4.60** | 3.33 |
| Exeter vs Crawley Town | 客胜 Crawley Town + 小于 2.5 球 | 8.87 | **9.13** | 8.01 |
| Walsall vs Northampton | 平局 + 小于 2.5 球 | 4.03 | **4.15** | 6.03 |
| Walsall vs Northampton | 主胜 Walsall + 小于 2.5 球 | 5.75 | **5.93** | 4.35 |
| Walsall vs Northampton | 客胜 Northampton + 小于 2.5 球 | 7.05 | **7.27** | 5.96 |
| Venezia vs Bologna | 客胜 Bologna + 大于 2.5 球 | 3.89 | **4.01** | 5.04 |
| Venezia vs Bologna | 客胜 Bologna + 小于 2.5 球 | 5.28 | **5.44** | 4.04 |
| Maritimo vs Nacional | 客胜 Nacional + 大于 2.5 球 | 5.73 | **5.91** | 6.97 |
| Maritimo vs Nacional | 客胜 Nacional + 小于 2.5 球 | 6.62 | **6.82** | 5.50 |
| Maritimo vs Nacional | 平局 + 大于 2.5 球 | 15.08 | **15.53** | 8.17 |
| Levante vs Santander | 主胜 Levante + 大于 2.5 球 | 2.43 | **2.50** | 2.73 |

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。