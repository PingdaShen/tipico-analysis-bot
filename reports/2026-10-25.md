# 投注建议 · 2026-10-25

覆盖 10-25 至 10-26 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 56 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Barcelona vs Real Madrid | 西甲 | 10-25 21:00 | 小于 2.5 球 | 4.46 | **4.60** | 4.78* | €1.00 |
| 2 | Ath Bilbao vs Getafe | 西甲 | 10-25 14:00 | 平局 | 3.61 | **3.72** | 3.81* | €1.00 |
| 3 | Braunschweig vs Hannover | 德乙 | 10-25 13:30 | 小于 2.5 球 | 2.49 | **2.57** | 2.63* | €1.00 |
| 4 | Genk vs Standard | 比甲 | 10-25 13:30 | 小于 2.5 球 | 2.19 | **2.26** | 2.29* | €1.00 |
| 5 | Rennes vs Strasbourg | 法甲 | 10-25 17:15 | 客胜 Strasbourg | 3.79 | **3.91** | 3.92* | €1.00 |
| 6 | Montpellier vs Red Star | 法乙 | 10-26 20:45 | 小于 2.5 球 | 1.82 | **1.87** | 1.90* | €1.00 |
| 7 | Walsall vs Salford | 英乙 | 10-26 21:00 | 主胜 Walsall | 3.10 | **3.19** | 3.20* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Barcelona vs Real Madrid — 小于 2.5 球**

```
20261025-SP1-Barcelona-RealMadrid-U25
```

**2. Ath Bilbao vs Getafe — 平局**

```
20261025-SP1-AthBilbao-Getafe-D
```

**3. Braunschweig vs Hannover — 小于 2.5 球**

```
20261025-D2-Braunschweig-Hannover-U25
```

**4. Genk vs Standard — 小于 2.5 球**

```
20261025-B1-Genk-Standard-U25
```

**5. Rennes vs Strasbourg — 客胜 Strasbourg**

```
20261025-F1-Rennes-Strasbourg-A
```

**6. Montpellier vs Red Star — 小于 2.5 球**

```
20261026-F2-Montpellier-RedStar-U25
```

**7. Walsall vs Salford — 主胜 Walsall**

```
20261026-E3-Walsall-Salford-H
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261025-SP1-Barcelona-RealMadrid-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261025-SP1-AthBilbao-Getafe-D --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261025-D2-Braunschweig-Hannover-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261025-B1-Genk-Standard-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261025-F1-Rennes-Strasbourg-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261026-F2-Montpellier-RedStar-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261026-E3-Walsall-Salford-H --odds <Tipico赔率> --stake 1.00
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
| Genk vs Standard | 平局 + 小于 2.5 球 | 5.30 | **5.46** | 8.71 |
| Genk vs Standard | 主胜 Genk + 小于 2.5 球 | 5.51 | **5.67** | 4.13 |
| Genk vs Standard | 客胜 Standard + 小于 2.5 球 | 11.60 | **11.95** | 10.04 |
| Braunschweig vs Hannover | 平局 + 小于 2.5 球 | 5.85 | **6.03** | 9.81 |
| Braunschweig vs Hannover | 客胜 Hannover + 小于 2.5 球 | 7.92 | **8.15** | 5.90 |
| Braunschweig vs Hannover | 主胜 Braunschweig + 小于 2.5 球 | 9.65 | **9.94** | 7.73 |
| Walsall vs Salford | 平局 + 小于 2.5 球 | 5.00 | **5.15** | 7.62 |
| Walsall vs Salford | 主胜 Walsall + 大于 2.5 球 | 5.07 | **5.22** | 6.09 |
| Walsall vs Salford | 主胜 Walsall + 小于 2.5 球 | 7.98 | **8.22** | 6.32 |
| Rennes vs Strasbourg | 客胜 Strasbourg + 大于 2.5 球 | 5.15 | **5.30** | 5.60 |
| Rennes vs Strasbourg | 平局 + 大于 2.5 球 | 10.47 | **10.79** | 6.65 |
| Rennes vs Strasbourg | 客胜 Strasbourg + 小于 2.5 球 | 14.39 | **14.83** | 11.75 |
| Montpellier vs Red Star | 平局 + 小于 2.5 球 | 4.32 | **4.45** | 6.45 |
| Montpellier vs Red Star | 主胜 Montpellier + 小于 2.5 球 | 5.79 | **5.96** | 4.40 |
| Ath Bilbao vs Getafe | 主胜 Ath Bilbao + 小于 2.5 球 | 3.40 | **3.50** | 2.80 |
| Ath Bilbao vs Getafe | 平局 + 小于 2.5 球 | 4.01 | **4.13** | 5.62 |
| Ath Bilbao vs Getafe | 客胜 Getafe + 小于 2.5 球 | 10.12 | **10.42** | 9.24 |
| Barcelona vs Real Madrid | 主胜 Barcelona + 小于 2.5 球 | 10.77 | **11.10** | 7.59 |
| Barcelona vs Real Madrid | 平局 + 小于 2.5 球 | 11.55 | **11.90** | 24.11 |
| Barcelona vs Real Madrid | 客胜 Real Madrid + 小于 2.5 球 | 22.41 | **23.08** | 19.68 |

## 备注
- Hull vs Brentford：球队数据不足（可能是升班马），跳过
- Auxerre vs Le Mans：球队数据不足（可能是升班马），跳过
- Toulouse vs Troyes：球队数据不足（可能是升班马），跳过
- Olympiakos vs Kalamata：球队数据不足（可能是升班马），跳过
- Atalanta vs Frosinone：球队数据不足（可能是升班马），跳过
- Verona vs Pisa：球队数据不足（可能是升班马），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。