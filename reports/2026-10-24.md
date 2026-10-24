# 投注建议 · 2026-10-24

覆盖 10-24 至 10-25 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 151 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Partick vs Stenhousemuir | 苏冠 | 10-24 16:00 | 客胜 Stenhousemuir | 4.76 | **4.91** | 6.59* | €1.00 |
| 2 | Bristol Rvs vs Swindon | 英乙 | 10-24 13:30 | 客胜 Swindon | 4.12 | **4.25** | 5.09* | €1.00 |
| 3 | Oud-Heverlee Leuven vs Lommel SK | 比甲 | 10-24 18:15 | 小于 2.5 球 | 1.99 | **2.05** | 2.27* | €1.00 |
| 4 | Eyupspor vs Kasimpasa | 土超 | 10-24 12:30 | 主胜 Eyupspor | 4.81 | **4.95** | 5.40* | €1.00 |
| 5 | Exeter vs Fleetwood Town | 英乙 | 10-24 16:00 | 小于 2.5 球 | 1.56 | **1.61** | 1.75* | €1.00 |
| 6 | Barcelona vs Real Madrid | 西甲 | 10-25 21:00 | 小于 2.5 球 | 4.46 | **4.60** | 4.78* | €1.00 |
| 7 | Ath Bilbao vs Getafe | 西甲 | 10-25 14:00 | 平局 | 3.61 | **3.72** | 3.81* | €1.00 |
| 8 | Braunschweig vs Hannover | 德乙 | 10-25 13:30 | 小于 2.5 球 | 2.49 | **2.57** | 2.63* | €1.00 |
| 9 | Genk vs Standard | 比甲 | 10-25 13:30 | 小于 2.5 球 | 2.19 | **2.26** | 2.29* | €1.00 |
| 10 | Rennes vs Strasbourg | 法甲 | 10-25 17:15 | 客胜 Strasbourg | 3.79 | **3.91** | 3.92* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Partick vs Stenhousemuir — 客胜 Stenhousemuir**

```
20261024-SC1-Partick-Stenhousemuir-A
```

**2. Bristol Rvs vs Swindon — 客胜 Swindon**

```
20261024-E3-BristolRvs-Swindon-A
```

**3. Oud-Heverlee Leuven vs Lommel SK — 小于 2.5 球**

```
20261024-B1-Oud-HeverleeLeuven-LommelSK-U25
```

**4. Eyupspor vs Kasimpasa — 主胜 Eyupspor**

```
20261024-T1-Eyupspor-Kasimpasa-H
```

**5. Exeter vs Fleetwood Town — 小于 2.5 球**

```
20261024-E3-Exeter-FleetwoodTown-U25
```

**6. Barcelona vs Real Madrid — 小于 2.5 球**

```
20261025-SP1-Barcelona-RealMadrid-U25
```

**7. Ath Bilbao vs Getafe — 平局**

```
20261025-SP1-AthBilbao-Getafe-D
```

**8. Braunschweig vs Hannover — 小于 2.5 球**

```
20261025-D2-Braunschweig-Hannover-U25
```

**9. Genk vs Standard — 小于 2.5 球**

```
20261025-B1-Genk-Standard-U25
```

**10. Rennes vs Strasbourg — 客胜 Strasbourg**

```
20261025-F1-Rennes-Strasbourg-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261024-SC1-Partick-Stenhousemuir-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261024-E3-BristolRvs-Swindon-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261024-B1-Oud-HeverleeLeuven-LommelSK-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261024-T1-Eyupspor-Kasimpasa-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261024-E3-Exeter-FleetwoodTown-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261025-SP1-Barcelona-RealMadrid-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261025-SP1-AthBilbao-Getafe-D --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261025-D2-Braunschweig-Hannover-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261025-B1-Genk-Standard-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261025-F1-Rennes-Strasbourg-A --odds <Tipico赔率> --stake 1.00
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
| Oud-Heverlee Leuven vs Lommel SK | 平局 + 小于 2.5 球 | 4.58 | **4.71** | 7.24 |
| Oud-Heverlee Leuven vs Lommel SK | 主胜 Oud-Heverlee Leuven + 小于 2.5 球 | 5.91 | **6.08** | 4.74 |
| Oud-Heverlee Leuven vs Lommel SK | 客胜 Lommel SK + 小于 2.5 球 | 8.77 | **9.03** | 6.55 |
| Genk vs Standard | 平局 + 小于 2.5 球 | 5.30 | **5.46** | 8.71 |
| Genk vs Standard | 主胜 Genk + 小于 2.5 球 | 5.51 | **5.67** | 4.13 |
| Genk vs Standard | 客胜 Standard + 小于 2.5 球 | 11.60 | **11.95** | 10.04 |
| Braunschweig vs Hannover | 平局 + 小于 2.5 球 | 5.85 | **6.03** | 9.81 |
| Braunschweig vs Hannover | 客胜 Hannover + 小于 2.5 球 | 7.92 | **8.15** | 5.90 |
| Braunschweig vs Hannover | 主胜 Braunschweig + 小于 2.5 球 | 9.65 | **9.94** | 7.73 |
| Bristol Rvs vs Swindon | 客胜 Swindon + 大于 2.5 球 | 6.30 | **6.49** | 7.15 |
| Bristol Rvs vs Swindon | 平局 + 小于 2.5 球 | 6.36 | **6.55** | 10.18 |
| Bristol Rvs vs Swindon | 客胜 Swindon + 小于 2.5 球 | 11.96 | **12.31** | 9.75 |
| Bristol Rvs vs Swindon | 平局 + 大于 2.5 球 | 13.35 | **13.75** | 7.47 |
| Exeter vs Fleetwood Town | 平局 + 小于 2.5 球 | 3.26 | **3.36** | 4.70 |
| Exeter vs Fleetwood Town | 主胜 Exeter + 小于 2.5 球 | 5.58 | **5.75** | 4.14 |
| Exeter vs Fleetwood Town | 客胜 Fleetwood Town + 小于 2.5 球 | 6.42 | **6.61** | 5.35 |
| Rennes vs Strasbourg | 客胜 Strasbourg + 大于 2.5 球 | 5.15 | **5.30** | 5.60 |
| Rennes vs Strasbourg | 平局 + 大于 2.5 球 | 10.47 | **10.79** | 6.65 |
| Rennes vs Strasbourg | 客胜 Strasbourg + 小于 2.5 球 | 14.39 | **14.83** | 11.75 |
| Partick vs Stenhousemuir | 平局 + 小于 2.5 球 | 4.05 | **4.18** | 6.16 |
| Partick vs Stenhousemuir | 客胜 Stenhousemuir + 大于 2.5 球 | 8.59 | **8.85** | 11.52 |
| Partick vs Stenhousemuir | 客胜 Stenhousemuir + 小于 2.5 球 | 10.69 | **11.01** | 8.12 |
| Ath Bilbao vs Getafe | 主胜 Ath Bilbao + 小于 2.5 球 | 3.40 | **3.50** | 2.80 |
| Ath Bilbao vs Getafe | 平局 + 小于 2.5 球 | 4.01 | **4.13** | 5.62 |
| Ath Bilbao vs Getafe | 客胜 Getafe + 小于 2.5 球 | 10.12 | **10.42** | 9.24 |
| Barcelona vs Real Madrid | 主胜 Barcelona + 小于 2.5 球 | 10.77 | **11.10** | 7.59 |
| Barcelona vs Real Madrid | 平局 + 小于 2.5 球 | 11.55 | **11.90** | 24.11 |
| Barcelona vs Real Madrid | 客胜 Real Madrid + 小于 2.5 球 | 22.41 | **23.08** | 19.68 |
| Eyupspor vs Kasimpasa | 平局 + 小于 2.5 球 | 4.82 | **4.97** | 7.32 |
| Eyupspor vs Kasimpasa | 主胜 Eyupspor + 大于 2.5 球 | 8.64 | **8.89** | 10.17 |
| Eyupspor vs Kasimpasa | 主胜 Eyupspor + 小于 2.5 球 | 10.84 | **11.16** | 9.11 |
| Eyupspor vs Kasimpasa | 平局 + 大于 2.5 球 | 19.30 | **19.88** | 8.17 |

## 备注
- FC Koln vs Schalke 04：球队数据不足（可能是升班马），跳过
- Paderborn vs Hamburg：球队数据不足（可能是升班马），跳过
- RB Leipzig vs Elversberg：球队数据不足（可能是升班马），跳过
- Coventry vs Fulham：球队数据不足（可能是升班马），跳过
- Hull vs Brentford：球队数据不足（可能是升班马），跳过
- Auxerre vs Le Mans：球队数据不足（可能是升班马），跳过
- Toulouse vs Troyes：球队数据不足（可能是升班马），跳过
- Iraklis vs Kifisia：球队数据不足（可能是升班马），跳过
- Olympiakos vs Kalamata：球队数据不足（可能是升班马），跳过
- Atalanta vs Frosinone：球队数据不足（可能是升班马），跳过
- Catanzaro vs Ascoli：球队数据不足（可能是升班马），跳过
- Arezzo vs Benevento：球队数据不足（可能是升班马），跳过
- Verona vs Pisa：球队数据不足（可能是升班马），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。