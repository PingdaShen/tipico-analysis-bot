# 投注建议 · 2026-10-31

覆盖 10-31 至 11-01 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 160 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Salford vs Exeter | 英乙 | 10-31 16:00 | 小于 2.5 球 | 1.71 | **1.76** | 2.02* | €1.00 |
| 2 | Troyes vs Le Mans | 法甲 | 10-31 20:45 | 客胜 Le Mans | 2.54 | **2.61** | 2.89* | €1.00 |
| 3 | Hull vs Ipswich | 英超 | 10-31 16:00 | 主胜 Hull | 2.29 | **2.36** | 2.58* | €1.00 |
| 4 | East Fife vs Queen of Sth | 苏甲 | 10-31 16:00 | 客胜 Queen of Sth | 3.16 | **3.25** | 3.50* | €1.00 |
| 5 | Middlesbrough vs Charlton | 英冠 | 10-31 16:00 | 小于 2.5 球 | 2.59 | **2.66** | 2.82* | €1.00 |
| 6 | Arezzo vs Ascoli | 意乙 | 11-01 15:00 | 客胜 Ascoli | 1.87 | **1.92** | 2.13* | €1.00 |
| 7 | Lommel SK vs Gent | 比甲 | 11-01 18:30 | 主胜 Lommel SK | 3.59 | **3.69** | 4.04* | €1.00 |
| 8 | Frosinone vs Torino | 意甲 | 11-01 15:00 | 主胜 Frosinone | 1.93 | **1.99** | 2.14* | €1.00 |
| 9 | Como vs Venezia | 意甲 | 11-01 12:30 | 小于 2.5 球 | 2.64 | **2.72** | 2.91* | €1.00 |
| 10 | St Pauli vs Nurnberg | 德乙 | 11-01 13:30 | 小于 2.5 球 | 2.06 | **2.12** | 2.21* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Salford vs Exeter — 小于 2.5 球**

```
20261031-E3-Salford-Exeter-U25
```

**2. Troyes vs Le Mans — 客胜 Le Mans**

```
20261031-F1-Troyes-LeMans-A
```

**3. Hull vs Ipswich — 主胜 Hull**

```
20261031-E0-Hull-Ipswich-H
```

**4. East Fife vs Queen of Sth — 客胜 Queen of Sth**

```
20261031-SC2-EastFife-QueenofSth-A
```

**5. Middlesbrough vs Charlton — 小于 2.5 球**

```
20261031-E1-Middlesbrough-Charlton-U25
```

**6. Arezzo vs Ascoli — 客胜 Ascoli**

```
20261101-I2-Arezzo-Ascoli-A
```

**7. Lommel SK vs Gent — 主胜 Lommel SK**

```
20261101-B1-LommelSK-Gent-H
```

**8. Frosinone vs Torino — 主胜 Frosinone**

```
20261101-I1-Frosinone-Torino-H
```

**9. Como vs Venezia — 小于 2.5 球**

```
20261101-I1-Como-Venezia-U25
```

**10. St Pauli vs Nurnberg — 小于 2.5 球**

```
20261101-D2-StPauli-Nurnberg-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261031-E3-Salford-Exeter-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261031-F1-Troyes-LeMans-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261031-E0-Hull-Ipswich-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261031-SC2-EastFife-QueenofSth-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261031-E1-Middlesbrough-Charlton-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261101-I2-Arezzo-Ascoli-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261101-B1-LommelSK-Gent-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261101-I1-Frosinone-Torino-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261101-I1-Como-Venezia-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261101-D2-StPauli-Nurnberg-U25 --odds <Tipico赔率> --stake 1.00
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
| Lommel SK vs Gent | 平局 + 小于 2.5 球 | 4.73 | **4.87** | 7.17 |
| Lommel SK vs Gent | 主胜 Lommel SK + 大于 2.5 球 | 6.07 | **6.25** | 7.44 |
| Lommel SK vs Gent | 主胜 Lommel SK + 小于 2.5 球 | 8.76 | **9.02** | 6.92 |
| St Pauli vs Nurnberg | 平局 + 小于 2.5 球 | 4.77 | **4.91** | 7.54 |
| St Pauli vs Nurnberg | 主胜 St Pauli + 小于 2.5 球 | 6.20 | **6.38** | 4.67 |
| St Pauli vs Nurnberg | 客胜 Nurnberg + 小于 2.5 球 | 8.67 | **8.93** | 7.16 |
| Hull vs Ipswich | 主胜 Hull + 大于 2.5 球 | 3.54 | **3.65** | 4.49 |
| Hull vs Ipswich | 主胜 Hull + 小于 2.5 球 | 6.47 | **6.66** | 4.67 |
| Middlesbrough vs Charlton | 主胜 Middlesbrough + 小于 2.5 球 | 4.67 | **4.81** | 3.63 |
| Middlesbrough vs Charlton | 平局 + 小于 2.5 球 | 7.70 | **7.93** | 14.55 |
| Middlesbrough vs Charlton | 客胜 Charlton + 大于 2.5 球 | 15.07 | **15.53** | 15.00 |
| Middlesbrough vs Charlton | 客胜 Charlton + 小于 2.5 球 | 23.60 | **24.31** | 23.79 |
| Salford vs Exeter | 平局 + 小于 2.5 球 | 3.85 | **3.97** | 5.87 |
| Salford vs Exeter | 主胜 Salford + 小于 2.5 球 | 4.45 | **4.58** | 3.46 |
| Salford vs Exeter | 客胜 Exeter + 小于 2.5 球 | 10.07 | **10.37** | 8.06 |
| Troyes vs Le Mans | 客胜 Le Mans + 大于 2.5 球 | 3.94 | **4.06** | 4.88 |
| Troyes vs Le Mans | 客胜 Le Mans + 小于 2.5 球 | 7.13 | **7.34** | 5.28 |
| Como vs Venezia | 主胜 Como + 小于 2.5 球 | 4.87 | **5.01** | 3.62 |
| Como vs Venezia | 平局 + 小于 2.5 球 | 7.77 | **8.00** | 15.65 |
| Como vs Venezia | 客胜 Venezia + 小于 2.5 球 | 22.72 | **23.41** | 26.44 |
| Frosinone vs Torino | 主胜 Frosinone + 大于 2.5 球 | 2.37 | **2.44** | 2.68 |
| Arezzo vs Ascoli | 客胜 Ascoli + 大于 2.5 球 | 2.79 | **2.87** | 3.57 |
| Arezzo vs Ascoli | 客胜 Ascoli + 小于 2.5 球 | 5.67 | **5.84** | 3.92 |
| East Fife vs Queen of Sth | 客胜 Queen of Sth + 大于 2.5 球 | 4.92 | **5.07** | 5.97 |
| East Fife vs Queen of Sth | 平局 + 小于 2.5 球 | 5.09 | **5.25** | 8.08 |
| East Fife vs Queen of Sth | 客胜 Queen of Sth + 小于 2.5 球 | 8.79 | **9.05** | 6.70 |

## 备注
- M'gladbach vs Paderborn：球队数据不足（可能是升班马），跳过
- Schalke 04 vs RB Leipzig：球队数据不足（可能是升班马），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。