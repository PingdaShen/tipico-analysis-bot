# 投注建议 · 2026-10-16

覆盖 10-16 至 10-17 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 100 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Burnley vs Wolves | 英冠 | 10-16 21:00 | 主胜 Burnley | 2.76 | **2.84** | 3.10* | €1.00 |
| 2 | Heerenveen vs Excelsior | 荷甲 | 10-16 20:00 | 客胜 Excelsior | 4.68 | **4.82** | 5.14* | €1.00 |
| 3 | Annecy vs Nancy | 法乙 | 10-16 20:00 | 主胜 Annecy | 2.61 | **2.68** | 2.83* | €1.00 |
| 4 | Holstein Kiel vs Hertha | 德乙 | 10-16 18:30 | 小于 2.5 球 | 2.61 | **2.68** | 2.82* | €1.00 |
| 5 | Ayr vs Partick | 苏冠 | 10-16 20:30 | 小于 2.5 球 | 1.93 | **1.99** | 2.00* | €1.00 |
| 6 | Nantes vs Dunkerque | 法乙 | 10-17 14:00 | 客胜 Dunkerque | 3.51 | **3.62** | 4.68* | €1.00 |
| 7 | Stenhousemuir vs Raith Rvs | 苏冠 | 10-17 16:00 | 主胜 Stenhousemuir | 2.59 | **2.67** | 3.11* | €1.00 |
| 8 | Colchester vs Exeter | 英乙 | 10-17 16:00 | 小于 2.5 球 | 1.58 | **1.63** | 1.82* | €1.00 |
| 9 | Grimsby vs Northampton | 英乙 | 10-17 16:00 | 小于 2.5 球 | 1.72 | **1.77** | 1.92* | €1.00 |
| 10 | Metz vs Sochaux | 法乙 | 10-17 14:00 | 小于 2.5 球 | 1.70 | **1.75** | 1.84* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Burnley vs Wolves — 主胜 Burnley**

```
20261016-E1-Burnley-Wolves-H
```

**2. Heerenveen vs Excelsior — 客胜 Excelsior**

```
20261016-N1-Heerenveen-Excelsior-A
```

**3. Annecy vs Nancy — 主胜 Annecy**

```
20261016-F2-Annecy-Nancy-H
```

**4. Holstein Kiel vs Hertha — 小于 2.5 球**

```
20261016-D2-HolsteinKiel-Hertha-U25
```

**5. Ayr vs Partick — 小于 2.5 球**

```
20261016-SC1-Ayr-Partick-U25
```

**6. Nantes vs Dunkerque — 客胜 Dunkerque**

```
20261017-F2-Nantes-Dunkerque-A
```

**7. Stenhousemuir vs Raith Rvs — 主胜 Stenhousemuir**

```
20261017-SC1-Stenhousemuir-RaithRvs-H
```

**8. Colchester vs Exeter — 小于 2.5 球**

```
20261017-E3-Colchester-Exeter-U25
```

**9. Grimsby vs Northampton — 小于 2.5 球**

```
20261017-E3-Grimsby-Northampton-U25
```

**10. Metz vs Sochaux — 小于 2.5 球**

```
20261017-F2-Metz-Sochaux-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261016-E1-Burnley-Wolves-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261016-N1-Heerenveen-Excelsior-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261016-F2-Annecy-Nancy-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261016-D2-HolsteinKiel-Hertha-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261016-SC1-Ayr-Partick-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261017-F2-Nantes-Dunkerque-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261017-SC1-Stenhousemuir-RaithRvs-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261017-E3-Colchester-Exeter-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261017-E3-Grimsby-Northampton-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261017-F2-Metz-Sochaux-U25 --odds <Tipico赔率> --stake 1.00
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
| Holstein Kiel vs Hertha | 平局 + 小于 2.5 球 | 6.18 | **6.37** | 10.41 |
| Holstein Kiel vs Hertha | 客胜 Hertha + 小于 2.5 球 | 8.02 | **8.26** | 6.11 |
| Holstein Kiel vs Hertha | 主胜 Holstein Kiel + 小于 2.5 球 | 10.28 | **10.59** | 8.07 |
| Burnley vs Wolves | 主胜 Burnley + 大于 2.5 球 | 4.25 | **4.38** | 5.13 |
| Burnley vs Wolves | 主胜 Burnley + 小于 2.5 球 | 7.83 | **8.06** | 5.95 |
| Colchester vs Exeter | 平局 + 小于 2.5 球 | 3.30 | **3.40** | 4.83 |
| Colchester vs Exeter | 主胜 Colchester + 小于 2.5 球 | 5.16 | **5.31** | 3.89 |
| Colchester vs Exeter | 客胜 Exeter + 小于 2.5 球 | 7.37 | **7.59** | 5.95 |
| Grimsby vs Northampton | 平局 + 小于 2.5 球 | 4.08 | **4.20** | 6.33 |
| Grimsby vs Northampton | 主胜 Grimsby + 小于 2.5 球 | 4.27 | **4.40** | 3.15 |
| Grimsby vs Northampton | 客胜 Northampton + 小于 2.5 球 | 9.88 | **10.17** | 9.46 |
| Annecy vs Nancy | 主胜 Annecy + 大于 2.5 球 | 4.40 | **4.54** | 5.58 |
| Annecy vs Nancy | 主胜 Annecy + 小于 2.5 球 | 6.39 | **6.58** | 4.89 |
| Metz vs Sochaux | 平局 + 小于 2.5 球 | 4.00 | **4.12** | 6.01 |
| Metz vs Sochaux | 主胜 Metz + 小于 2.5 球 | 4.31 | **4.44** | 3.28 |
| Metz vs Sochaux | 客胜 Sochaux + 小于 2.5 球 | 9.34 | **9.62** | 8.52 |
| Nantes vs Dunkerque | 客胜 Dunkerque + 大于 2.5 球 | 5.34 | **5.50** | 6.30 |
| Nantes vs Dunkerque | 客胜 Dunkerque + 小于 2.5 球 | 10.25 | **10.56** | 7.93 |
| Nantes vs Dunkerque | 平局 + 大于 2.5 球 | 13.38 | **13.78** | 7.47 |
| Heerenveen vs Excelsior | 客胜 Excelsior + 大于 2.5 球 | 6.54 | **6.74** | 7.25 |
| Heerenveen vs Excelsior | 平局 + 小于 2.5 球 | 6.99 | **7.20** | 12.70 |
| Heerenveen vs Excelsior | 客胜 Excelsior + 小于 2.5 球 | 16.45 | **16.95** | 13.19 |
| Ayr vs Partick | 平局 + 小于 2.5 球 | 4.51 | **4.64** | 7.08 |
| Ayr vs Partick | 客胜 Partick + 小于 2.5 球 | 5.02 | **5.17** | 3.90 |
| Ayr vs Partick | 主胜 Ayr + 小于 2.5 球 | 10.35 | **10.66** | 8.35 |
| Stenhousemuir vs Raith Rvs | 平局 + 小于 2.5 球 | 3.73 | **3.84** | 5.44 |
| Stenhousemuir vs Raith Rvs | 主胜 Stenhousemuir + 大于 2.5 球 | 4.75 | **4.89** | 6.94 |
| Stenhousemuir vs Raith Rvs | 主胜 Stenhousemuir + 小于 2.5 球 | 5.68 | **5.86** | 4.13 |

## 备注
- Elversberg vs Augsburg：球队数据不足（可能是升班马），跳过
- Schalke 04 vs Mainz：球队数据不足（可能是升班马），跳过
- Werder Bremen vs Paderborn：球队数据不足（可能是升班马），跳过
- Cottbus vs Nurnberg：球队数据不足（可能是升班马），跳过
- Wolfsburg vs Heidenheim：球队数据不足（可能是升班马），跳过
- Hannover vs St Pauli：球队数据不足（可能是升班马），跳过
- Fulham vs Hull：球队数据不足（可能是升班马），跳过
- Le Mans vs Toulouse：球队数据不足（可能是升班马），跳过
- Troyes vs Lens：球队数据不足（可能是升班马），跳过
- Frosinone vs Sassuolo：球队数据不足（可能是升班马），跳过
- Verona vs Catanzaro：球队数据不足（可能是升班马），跳过
- Ascoli vs Empoli：球队数据不足（可能是升班马），跳过
- Benevento vs Vicenza：球队数据不足（可能是升班马），跳过
- Corum vs Rizespor：球队数据不足（可能是升班马），跳过
- Erzurumspor vs Eyupspor：球队数据不足（可能是升班马），跳过
- Amedspor vs Konyaspor：球队数据不足（可能是升班马），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。