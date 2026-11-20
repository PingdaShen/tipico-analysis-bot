# 投注建议 · 2026-11-20

覆盖 11-20 至 11-21 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 138 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Nancy vs Dijon | 法乙 | 11-20 20:00 | 客胜 Dijon | 3.54 | **3.65** | 3.97* | €1.00 |
| 2 | Darmstadt vs Heidenheim | 德乙 | 11-20 18:30 | 主胜 Darmstadt | 2.94 | **3.03** | 3.20* | €1.00 |
| 3 | Ath Bilbao vs Espanol | 西甲 | 11-20 21:00 | 小于 2.5 球 | 2.03 | **2.09** | 2.11* | €1.00 |
| 4 | Troyes vs Le Havre | 法甲 | 11-20 20:45 | 小于 2.5 球 | 1.81 | **1.87** | 1.88* | €1.00 |
| 5 | Schalke 04 vs Stuttgart | 德甲 | 11-21 18:30 | 小于 2.5 球 | 2.13 | **2.19** | 2.63* | €1.00 |
| 6 | Leverkusen vs Paderborn | 德甲 | 11-21 15:30 | 小于 2.5 球 | 2.68 | **2.76** | 3.16* | €1.00 |
| 7 | Elversberg vs Freiburg | 德甲 | 11-21 15:30 | 主胜 Elversberg | 2.94 | **3.03** | 3.41* | €1.00 |
| 8 | Newport County vs Swindon | 英乙 | 11-21 13:30 | 客胜 Swindon | 3.43 | **3.53** | 3.83* | €1.00 |
| 9 | Oldham vs Exeter | 英乙 | 11-21 16:00 | 小于 2.5 球 | 1.57 | **1.62** | 1.74* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Nancy vs Dijon — 客胜 Dijon**

```
20261120-F2-Nancy-Dijon-A
```

**2. Darmstadt vs Heidenheim — 主胜 Darmstadt**

```
20261120-D2-Darmstadt-Heidenheim-H
```

**3. Ath Bilbao vs Espanol — 小于 2.5 球**

```
20261120-SP1-AthBilbao-Espanol-U25
```

**4. Troyes vs Le Havre — 小于 2.5 球**

```
20261120-F1-Troyes-LeHavre-U25
```

**5. Schalke 04 vs Stuttgart — 小于 2.5 球**

```
20261121-D1-Schalke04-Stuttgart-U25
```

**6. Leverkusen vs Paderborn — 小于 2.5 球**

```
20261121-D1-Leverkusen-Paderborn-U25
```

**7. Elversberg vs Freiburg — 主胜 Elversberg**

```
20261121-D1-Elversberg-Freiburg-H
```

**8. Newport County vs Swindon — 客胜 Swindon**

```
20261121-E3-NewportCounty-Swindon-A
```

**9. Oldham vs Exeter — 小于 2.5 球**

```
20261121-E3-Oldham-Exeter-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261120-F2-Nancy-Dijon-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261120-D2-Darmstadt-Heidenheim-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261120-SP1-AthBilbao-Espanol-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261120-F1-Troyes-LeHavre-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261121-D1-Schalke04-Stuttgart-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261121-D1-Leverkusen-Paderborn-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261121-D1-Elversberg-Freiburg-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261121-E3-NewportCounty-Swindon-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261121-E3-Oldham-Exeter-U25 --odds <Tipico赔率> --stake 1.00
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
| Elversberg vs Freiburg | 主胜 Elversberg + 大于 2.5 球 | 3.96 | **4.08** | 4.51 |
| Elversberg vs Freiburg | 平局 + 大于 2.5 球 | 10.34 | **10.65** | 6.45 |
| Elversberg vs Freiburg | 主胜 Elversberg + 小于 2.5 球 | 11.39 | **11.73** | 8.45 |
| Leverkusen vs Paderborn | 主胜 Leverkusen + 小于 2.5 球 | 4.99 | **5.14** | 3.81 |
| Leverkusen vs Paderborn | 平局 + 小于 2.5 球 | 7.74 | **7.98** | 14.99 |
| Leverkusen vs Paderborn | 客胜 Paderborn + 小于 2.5 球 | 22.67 | **23.35** | 22.56 |
| Schalke 04 vs Stuttgart | 平局 + 小于 2.5 球 | 4.82 | **4.97** | 8.19 |
| Schalke 04 vs Stuttgart | 客胜 Stuttgart + 小于 2.5 球 | 5.77 | **5.94** | 4.09 |
| Schalke 04 vs Stuttgart | 主胜 Schalke 04 + 小于 2.5 球 | 11.23 | **11.56** | 9.67 |
| Darmstadt vs Heidenheim | 主胜 Darmstadt + 大于 2.5 球 | 4.05 | **4.17** | 4.64 |
| Darmstadt vs Heidenheim | 主胜 Darmstadt + 小于 2.5 球 | 10.75 | **11.08** | 8.02 |
| Newport County vs Swindon | 客胜 Swindon + 大于 2.5 球 | 5.54 | **5.70** | 6.50 |
| Newport County vs Swindon | 客胜 Swindon + 小于 2.5 球 | 9.00 | **9.27** | 7.25 |
| Newport County vs Swindon | 平局 + 大于 2.5 球 | 13.84 | **14.26** | 7.41 |
| Oldham vs Exeter | 平局 + 小于 2.5 球 | 3.47 | **3.57** | 4.94 |
| Oldham vs Exeter | 主胜 Oldham + 小于 2.5 球 | 4.78 | **4.92** | 3.82 |
| Oldham vs Exeter | 客胜 Exeter + 小于 2.5 球 | 7.21 | **7.43** | 5.80 |
| Troyes vs Le Havre | 平局 + 小于 2.5 球 | 4.24 | **4.36** | 6.25 |
| Troyes vs Le Havre | 主胜 Troyes + 小于 2.5 球 | 5.61 | **5.78** | 4.54 |
| Troyes vs Le Havre | 客胜 Le Havre + 小于 2.5 球 | 7.31 | **7.53** | 5.86 |
| Nancy vs Dijon | 客胜 Dijon + 大于 2.5 球 | 5.42 | **5.59** | 6.18 |
| Nancy vs Dijon | 客胜 Dijon + 小于 2.5 球 | 10.19 | **10.49** | 8.28 |
| Nancy vs Dijon | 平局 + 大于 2.5 球 | 12.00 | **12.36** | 7.11 |
| Ath Bilbao vs Espanol | 主胜 Ath Bilbao + 小于 2.5 球 | 4.29 | **4.42** | 3.40 |
| Ath Bilbao vs Espanol | 平局 + 小于 2.5 球 | 5.39 | **5.55** | 8.62 |
| Ath Bilbao vs Espanol | 客胜 Espanol + 大于 2.5 球 | 10.68 | **11.00** | 11.69 |
| Ath Bilbao vs Espanol | 客胜 Espanol + 小于 2.5 球 | 13.28 | **13.68** | 11.99 |

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。