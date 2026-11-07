# 投注建议 · 2026-11-07

覆盖 11-07 至 11-08 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 139 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Paderborn vs Ein Frankfurt | 德甲 | 11-07 15:30 | 小于 2.5 球 | 2.25 | **2.32** | 2.67* | €1.00 |
| 2 | Cagliari vs Frosinone | 意甲 | 11-07 15:00 | 客胜 Frosinone | 2.11 | **2.17** | 2.41* | €1.00 |
| 3 | Arsenal vs Hull | 英超 | 11-07 16:00 | 小于 2.5 球 | 2.20 | **2.26** | 2.50* | €1.00 |
| 4 | Antwerp vs Lommel SK | 比甲 | 11-07 20:45 | 小于 2.5 球 | 2.17 | **2.24** | 2.41* | €1.00 |
| 5 | Pau FC vs Nantes | 法乙 | 11-07 20:00 | 主胜 Pau FC | 2.66 | **2.74** | 2.89* | €1.00 |
| 6 | Hoffenheim vs Schalke 04 | 德甲 | 11-08 19:30 | 小于 2.5 球 | 2.09 | **2.15** | 2.59* | €1.00 |
| 7 | Iraklis vs Panathinaikos | 希超 | 11-08 16:30 | 平局 | 4.29 | **4.42** | 4.63* | €1.00 |
| 8 | Monza vs Atalanta | 意甲 | 11-08 15:00 | 客胜 Atalanta | 1.92 | **1.98** | 2.06* | €1.00 |
| 9 | Corum vs Fenerbahce | 土超 | 11-08 14:00 | 主胜 Corum | 3.84 | **3.95** | 4.08* | €1.00 |
| 10 | Besiktas vs Genclerbirligi | 土超 | 11-08 19:00 | 小于 2.5 球 | 2.75 | **2.83** | 2.89* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Paderborn vs Ein Frankfurt — 小于 2.5 球**

```
20261107-D1-Paderborn-EinFrankfurt-U25
```

**2. Cagliari vs Frosinone — 客胜 Frosinone**

```
20261107-I1-Cagliari-Frosinone-A
```

**3. Arsenal vs Hull — 小于 2.5 球**

```
20261107-E0-Arsenal-Hull-U25
```

**4. Antwerp vs Lommel SK — 小于 2.5 球**

```
20261107-B1-Antwerp-LommelSK-U25
```

**5. Pau FC vs Nantes — 主胜 Pau FC**

```
20261107-F2-PauFC-Nantes-H
```

**6. Hoffenheim vs Schalke 04 — 小于 2.5 球**

```
20261108-D1-Hoffenheim-Schalke04-U25
```

**7. Iraklis vs Panathinaikos — 平局**

```
20261108-G1-Iraklis-Panathinaikos-D
```

**8. Monza vs Atalanta — 客胜 Atalanta**

```
20261108-I1-Monza-Atalanta-A
```

**9. Corum vs Fenerbahce — 主胜 Corum**

```
20261108-T1-Corum-Fenerbahce-H
```

**10. Besiktas vs Genclerbirligi — 小于 2.5 球**

```
20261108-T1-Besiktas-Genclerbirligi-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261107-D1-Paderborn-EinFrankfurt-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261107-I1-Cagliari-Frosinone-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261107-E0-Arsenal-Hull-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261107-B1-Antwerp-LommelSK-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261107-F2-PauFC-Nantes-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261108-D1-Hoffenheim-Schalke04-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261108-G1-Iraklis-Panathinaikos-D --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261108-I1-Monza-Atalanta-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261108-T1-Corum-Fenerbahce-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261108-T1-Besiktas-Genclerbirligi-U25 --odds <Tipico赔率> --stake 1.00
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
| Antwerp vs Lommel SK | 平局 + 小于 2.5 球 | 5.12 | **5.27** | 8.24 |
| Antwerp vs Lommel SK | 主胜 Antwerp + 小于 2.5 球 | 6.20 | **6.39** | 4.91 |
| Antwerp vs Lommel SK | 客胜 Lommel SK + 小于 2.5 球 | 9.66 | **9.95** | 7.41 |
| Paderborn vs Ein Frankfurt | 平局 + 小于 2.5 球 | 5.11 | **5.27** | 8.43 |
| Paderborn vs Ein Frankfurt | 客胜 Ein Frankfurt + 小于 2.5 球 | 7.13 | **7.35** | 5.35 |
| Paderborn vs Ein Frankfurt | 主胜 Paderborn + 小于 2.5 球 | 9.28 | **9.56** | 7.25 |
| Hoffenheim vs Schalke 04 | 平局 + 小于 2.5 球 | 4.92 | **5.07** | 8.51 |
| Hoffenheim vs Schalke 04 | 主胜 Hoffenheim + 小于 2.5 球 | 5.07 | **5.23** | 3.63 |
| Hoffenheim vs Schalke 04 | 客胜 Schalke 04 + 小于 2.5 球 | 12.78 | **13.16** | 11.64 |
| Arsenal vs Hull | 主胜 Arsenal + 小于 2.5 球 | 3.58 | **3.69** | 2.90 |
| Arsenal vs Hull | 平局 + 小于 2.5 球 | 7.14 | **7.35** | 13.10 |
| Arsenal vs Hull | 客胜 Hull + 大于 2.5 球 | 25.09 | **25.84** | 24.28 |
| Arsenal vs Hull | 客胜 Hull + 小于 2.5 球 | 28.00 | **28.84** | 29.07 |
| Pau FC vs Nantes | 主胜 Pau FC + 大于 2.5 球 | 4.29 | **4.41** | 5.19 |
| Pau FC vs Nantes | 主胜 Pau FC + 小于 2.5 球 | 6.99 | **7.20** | 5.44 |
| Pau FC vs Nantes | 平局 + 大于 2.5 球 | 13.48 | **13.89** | 7.31 |
| Iraklis vs Panathinaikos | 平局 + 小于 2.5 球 | 5.24 | **5.39** | 8.57 |
| Iraklis vs Panathinaikos | 主胜 Iraklis + 大于 2.5 球 | 11.99 | **12.35** | 13.63 |
| Iraklis vs Panathinaikos | 主胜 Iraklis + 小于 2.5 球 | 15.73 | **16.20** | 13.59 |
| Cagliari vs Frosinone | 客胜 Frosinone + 大于 2.5 球 | 2.80 | **2.88** | 3.27 |
| Cagliari vs Frosinone | 客胜 Frosinone + 小于 2.5 球 | 8.61 | **8.87** | 5.96 |
| Monza vs Atalanta | 客胜 Atalanta + 大于 2.5 球 | 2.60 | **2.68** | 3.04 |
| Monza vs Atalanta | 客胜 Atalanta + 小于 2.5 球 | 7.42 | **7.65** | 5.25 |
| Corum vs Fenerbahce | 客胜 Fenerbahce + 大于 2.5 球 | 2.68 | **2.76** | 3.03 |
| Corum vs Fenerbahce | 主胜 Corum + 大于 2.5 球 | 5.28 | **5.44** | 5.90 |
| Corum vs Fenerbahce | 平局 + 大于 2.5 球 | 11.49 | **11.83** | 6.63 |
| Besiktas vs Genclerbirligi | 主胜 Besiktas + 小于 2.5 球 | 4.87 | **5.02** | 3.76 |
| Besiktas vs Genclerbirligi | 平局 + 小于 2.5 球 | 8.16 | **8.40** | 16.25 |
| Besiktas vs Genclerbirligi | 客胜 Genclerbirligi + 大于 2.5 球 | 15.37 | **15.83** | 15.54 |
| Besiktas vs Genclerbirligi | 平局 + 大于 2.5 球 | 21.52 | **22.17** | 9.30 |

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。