# 投注建议 · 2026-11-28

覆盖 11-28 至 11-29 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 150 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Paderborn vs Schalke 04 | 德甲 | 11-28 15:30 | 小于 2.5 球 | 1.66 | **1.71** | 2.01* | €1.00 |
| 2 | Luton vs Oxford | 英甲 | 11-28 16:00 | 客胜 Oxford | 3.47 | **3.57** | 4.14* | €1.00 |
| 3 | Exeter vs Crawley Town | 英乙 | 11-28 13:30 | 小于 2.5 球 | 1.66 | **1.71** | 1.84* | €1.00 |
| 4 | Walsall vs Northampton | 英乙 | 11-28 16:00 | 小于 2.5 球 | 1.77 | **1.83** | 1.92* | €1.00 |
| 5 | Preston vs Norwich | 英冠 | 11-28 13:30 | 主胜 Preston | 4.19 | **4.31** | 4.48* | €1.00 |
| 6 | Crystal Palace vs Hull | 英超 | 11-29 15:05 | 客胜 Hull | 3.36 | **3.46** | 3.85* | €1.00 |
| 7 | Standard vs Club Brugge | 比甲 | 11-29 18:30 | 小于 2.5 球 | 2.68 | **2.76** | 2.85* | €1.00 |
| 8 | Sunderland vs Tottenham | 英超 | 11-29 15:05 | 主胜 Sunderland | 3.42 | **3.52** | 3.62* | €1.00 |
| 9 | Atromitos vs Panathinaikos | 希超 | 11-29 16:00 | 平局 | 4.17 | **4.29** | 4.33* | €1.00 |
| 10 | Mallorca vs Castellon | 西乙 | 11-29 16:15 | 小于 2.5 球 | 1.87 | **1.93** | 1.94* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Paderborn vs Schalke 04 — 小于 2.5 球**

```
20261128-D1-Paderborn-Schalke04-U25
```

**2. Luton vs Oxford — 客胜 Oxford**

```
20261128-E2-Luton-Oxford-A
```

**3. Exeter vs Crawley Town — 小于 2.5 球**

```
20261128-E3-Exeter-CrawleyTown-U25
```

**4. Walsall vs Northampton — 小于 2.5 球**

```
20261128-E3-Walsall-Northampton-U25
```

**5. Preston vs Norwich — 主胜 Preston**

```
20261128-E1-Preston-Norwich-H
```

**6. Crystal Palace vs Hull — 客胜 Hull**

```
20261129-E0-CrystalPalace-Hull-A
```

**7. Standard vs Club Brugge — 小于 2.5 球**

```
20261129-B1-Standard-ClubBrugge-U25
```

**8. Sunderland vs Tottenham — 主胜 Sunderland**

```
20261129-E0-Sunderland-Tottenham-H
```

**9. Atromitos vs Panathinaikos — 平局**

```
20261129-G1-Atromitos-Panathinaikos-D
```

**10. Mallorca vs Castellon — 小于 2.5 球**

```
20261129-SP2-Mallorca-Castellon-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261128-D1-Paderborn-Schalke04-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261128-E2-Luton-Oxford-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261128-E3-Exeter-CrawleyTown-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261128-E3-Walsall-Northampton-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261128-E1-Preston-Norwich-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261129-E0-CrystalPalace-Hull-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261129-B1-Standard-ClubBrugge-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261129-E0-Sunderland-Tottenham-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261129-G1-Atromitos-Panathinaikos-D --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261129-SP2-Mallorca-Castellon-U25 --odds <Tipico赔率> --stake 1.00
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
| Standard vs Club Brugge | 客胜 Club Brugge + 小于 2.5 球 | 6.03 | **6.21** | 4.48 |
| Standard vs Club Brugge | 平局 + 小于 2.5 球 | 7.06 | **7.27** | 12.59 |
| Standard vs Club Brugge | 主胜 Standard + 小于 2.5 球 | 15.35 | **15.81** | 14.26 |
| Paderborn vs Schalke 04 | 平局 + 小于 2.5 球 | 3.25 | **3.35** | 4.95 |
| Paderborn vs Schalke 04 | 主胜 Paderborn + 小于 2.5 球 | 6.55 | **6.74** | 4.65 |
| Paderborn vs Schalke 04 | 客胜 Schalke 04 + 小于 2.5 球 | 7.00 | **7.21** | 5.38 |
| Crystal Palace vs Hull | 平局 + 小于 2.5 球 | 4.63 | **4.77** | 7.16 |
| Crystal Palace vs Hull | 客胜 Hull + 大于 2.5 球 | 5.52 | **5.69** | 6.89 |
| Crystal Palace vs Hull | 客胜 Hull + 小于 2.5 球 | 8.59 | **8.84** | 6.56 |
| Sunderland vs Tottenham | 平局 + 小于 2.5 球 | 4.31 | **4.44** | 6.36 |
| Sunderland vs Tottenham | 主胜 Sunderland + 大于 2.5 球 | 6.05 | **6.23** | 7.51 |
| Sunderland vs Tottenham | 主胜 Sunderland + 小于 2.5 球 | 7.86 | **8.09** | 6.27 |
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
| Atromitos vs Panathinaikos | 平局 + 小于 2.5 球 | 5.07 | **5.23** | 8.12 |
| Atromitos vs Panathinaikos | 主胜 Atromitos + 大于 2.5 球 | 11.30 | **11.64** | 12.92 |
| Atromitos vs Panathinaikos | 主胜 Atromitos + 小于 2.5 球 | 14.16 | **14.59** | 12.24 |
| Atromitos vs Panathinaikos | 平局 + 大于 2.5 球 | 23.39 | **24.09** | 8.57 |
| Mallorca vs Castellon | 平局 + 小于 2.5 球 | 4.41 | **4.54** | 6.54 |
| Mallorca vs Castellon | 主胜 Mallorca + 小于 2.5 球 | 5.76 | **5.93** | 4.47 |
| Mallorca vs Castellon | 客胜 Castellon + 小于 2.5 球 | 7.49 | **7.72** | 6.36 |

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。