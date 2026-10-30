# 投注建议 · 2026-10-30

覆盖 10-30 至 10-31 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 128 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Nantes vs Clermont | 法乙 | 10-30 20:00 | 客胜 Clermont | 4.77 | **4.91** | 6.31* | €1.00 |
| 2 | Stenhousemuir vs Livingston | 苏冠 | 10-30 20:30 | 主胜 Stenhousemuir | 3.95 | **4.06** | 4.36* | €1.00 |
| 3 | Cottbus vs Bochum | 德乙 | 10-30 18:30 | 主胜 Cottbus | 2.55 | **2.63** | 2.72* | €1.00 |
| 4 | Le Havre vs Paris SG | 法甲 | 10-30 19:00 | 小于 2.5 球 | 2.89 | **2.98** | 2.99* | €1.00 |
| 5 | Salford vs Exeter | 英乙 | 10-31 16:00 | 小于 2.5 球 | 1.71 | **1.76** | 2.02* | €1.00 |
| 6 | Troyes vs Le Mans | 法甲 | 10-31 20:45 | 客胜 Le Mans | 2.54 | **2.61** | 2.89* | €1.00 |
| 7 | Hull vs Ipswich | 英超 | 10-31 16:00 | 主胜 Hull | 2.29 | **2.36** | 2.58* | €1.00 |
| 8 | East Fife vs Queen of Sth | 苏甲 | 10-31 16:00 | 客胜 Queen of Sth | 3.16 | **3.25** | 3.50* | €1.00 |
| 9 | Middlesbrough vs Charlton | 英冠 | 10-31 16:00 | 小于 2.5 球 | 2.59 | **2.66** | 2.82* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Nantes vs Clermont — 客胜 Clermont**

```
20261030-F2-Nantes-Clermont-A
```

**2. Stenhousemuir vs Livingston — 主胜 Stenhousemuir**

```
20261030-SC1-Stenhousemuir-Livingston-H
```

**3. Cottbus vs Bochum — 主胜 Cottbus**

```
20261030-D2-Cottbus-Bochum-H
```

**4. Le Havre vs Paris SG — 小于 2.5 球**

```
20261030-F1-LeHavre-ParisSG-U25
```

**5. Salford vs Exeter — 小于 2.5 球**

```
20261031-E3-Salford-Exeter-U25
```

**6. Troyes vs Le Mans — 客胜 Le Mans**

```
20261031-F1-Troyes-LeMans-A
```

**7. Hull vs Ipswich — 主胜 Hull**

```
20261031-E0-Hull-Ipswich-H
```

**8. East Fife vs Queen of Sth — 客胜 Queen of Sth**

```
20261031-SC2-EastFife-QueenofSth-A
```

**9. Middlesbrough vs Charlton — 小于 2.5 球**

```
20261031-E1-Middlesbrough-Charlton-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261030-F2-Nantes-Clermont-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261030-SC1-Stenhousemuir-Livingston-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261030-D2-Cottbus-Bochum-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261030-F1-LeHavre-ParisSG-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261031-E3-Salford-Exeter-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261031-F1-Troyes-LeMans-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261031-E0-Hull-Ipswich-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261031-SC2-EastFife-QueenofSth-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261031-E1-Middlesbrough-Charlton-U25 --odds <Tipico赔率> --stake 1.00
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
| Cottbus vs Bochum | 主胜 Cottbus + 大于 2.5 球 | 3.50 | **3.60** | 4.08 |
| Cottbus vs Bochum | 平局 + 小于 2.5 球 | 6.31 | **6.50** | 10.74 |
| Cottbus vs Bochum | 主胜 Cottbus + 小于 2.5 球 | 9.48 | **9.76** | 6.84 |
| Hull vs Ipswich | 主胜 Hull + 大于 2.5 球 | 3.54 | **3.65** | 4.49 |
| Hull vs Ipswich | 主胜 Hull + 小于 2.5 球 | 6.47 | **6.66** | 4.67 |
| Middlesbrough vs Charlton | 主胜 Middlesbrough + 小于 2.5 球 | 4.67 | **4.81** | 3.63 |
| Middlesbrough vs Charlton | 平局 + 小于 2.5 球 | 7.70 | **7.93** | 14.55 |
| Middlesbrough vs Charlton | 客胜 Charlton + 大于 2.5 球 | 15.07 | **15.53** | 15.00 |
| Middlesbrough vs Charlton | 客胜 Charlton + 小于 2.5 球 | 23.60 | **24.31** | 23.79 |
| Salford vs Exeter | 平局 + 小于 2.5 球 | 3.85 | **3.97** | 5.87 |
| Salford vs Exeter | 主胜 Salford + 小于 2.5 球 | 4.45 | **4.58** | 3.46 |
| Salford vs Exeter | 客胜 Exeter + 小于 2.5 球 | 10.07 | **10.37** | 8.06 |
| Le Havre vs Paris SG | 客胜 Paris SG + 小于 2.5 球 | 5.38 | **5.54** | 4.03 |
| Le Havre vs Paris SG | 平局 + 小于 2.5 球 | 8.36 | **8.62** | 16.97 |
| Le Havre vs Paris SG | 主胜 Le Havre + 小于 2.5 球 | 24.68 | **25.42** | 25.83 |
| Troyes vs Le Mans | 客胜 Le Mans + 大于 2.5 球 | 3.94 | **4.06** | 4.88 |
| Troyes vs Le Mans | 客胜 Le Mans + 小于 2.5 球 | 7.13 | **7.34** | 5.28 |
| Nantes vs Clermont | 平局 + 小于 2.5 球 | 5.49 | **5.65** | 8.29 |
| Nantes vs Clermont | 客胜 Clermont + 大于 2.5 球 | 8.30 | **8.55** | 9.66 |
| Nantes vs Clermont | 客胜 Clermont + 小于 2.5 球 | 11.22 | **11.56** | 9.43 |
| Nantes vs Clermont | 平局 + 大于 2.5 球 | 17.84 | **18.37** | 8.50 |
| Stenhousemuir vs Livingston | 平局 + 小于 2.5 球 | 4.02 | **4.14** | 6.11 |
| Stenhousemuir vs Livingston | 主胜 Stenhousemuir + 小于 2.5 球 | 9.03 | **9.30** | 6.96 |
| East Fife vs Queen of Sth | 客胜 Queen of Sth + 大于 2.5 球 | 4.92 | **5.07** | 5.97 |
| East Fife vs Queen of Sth | 平局 + 小于 2.5 球 | 5.09 | **5.25** | 8.08 |
| East Fife vs Queen of Sth | 客胜 Queen of Sth + 小于 2.5 球 | 8.79 | **9.05** | 6.70 |

## 备注
- Elversberg vs Mainz：球队数据不足（可能是升班马），跳过
- M'gladbach vs Paderborn：球队数据不足（可能是升班马），跳过
- Schalke 04 vs RB Leipzig：球队数据不足（可能是升班马），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。