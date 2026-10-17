# 投注建议 · 2026-10-17

覆盖 10-17 至 10-18 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 128 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Nantes vs Dunkerque | 法乙 | 10-17 14:00 | 客胜 Dunkerque | 3.51 | **3.62** | 4.68* | €1.00 |
| 2 | Stenhousemuir vs Raith Rvs | 苏冠 | 10-17 16:00 | 主胜 Stenhousemuir | 2.59 | **2.67** | 3.11* | €1.00 |
| 3 | Colchester vs Exeter | 英乙 | 10-17 16:00 | 小于 2.5 球 | 1.58 | **1.63** | 1.82* | €1.00 |
| 4 | Grimsby vs Northampton | 英乙 | 10-17 16:00 | 小于 2.5 球 | 1.72 | **1.77** | 1.92* | €1.00 |
| 5 | Metz vs Sochaux | 法乙 | 10-17 14:00 | 小于 2.5 球 | 1.70 | **1.75** | 1.84* | €1.00 |
| 6 | Panetolikos vs Olympiakos | 希超 | 10-18 16:00 | 小于 2.5 球 | 1.81 | **1.86** | 1.96* | €1.00 |
| 7 | Milan vs Atalanta | 意甲 | 10-18 18:00 | 客胜 Atalanta | 3.84 | **3.95** | 4.12* | €1.00 |
| 8 | Groningen vs Ajax | 荷甲 | 10-18 16:45 | 小于 2.5 球 | 2.89 | **2.97** | 3.06* | €1.00 |
| 9 | Malaga vs Sociedad | 西甲 | 10-18 18:30 | 小于 2.5 球 | 1.89 | **1.95** | 1.99* | €1.00 |
| 10 | Osasuna vs Santander | 西甲 | 10-18 14:00 | 大于 2.5 球 | 1.56 | **1.60** | 1.63* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Nantes vs Dunkerque — 客胜 Dunkerque**

```
20261017-F2-Nantes-Dunkerque-A
```

**2. Stenhousemuir vs Raith Rvs — 主胜 Stenhousemuir**

```
20261017-SC1-Stenhousemuir-RaithRvs-H
```

**3. Colchester vs Exeter — 小于 2.5 球**

```
20261017-E3-Colchester-Exeter-U25
```

**4. Grimsby vs Northampton — 小于 2.5 球**

```
20261017-E3-Grimsby-Northampton-U25
```

**5. Metz vs Sochaux — 小于 2.5 球**

```
20261017-F2-Metz-Sochaux-U25
```

**6. Panetolikos vs Olympiakos — 小于 2.5 球**

```
20261018-G1-Panetolikos-Olympiakos-U25
```

**7. Milan vs Atalanta — 客胜 Atalanta**

```
20261018-I1-Milan-Atalanta-A
```

**8. Groningen vs Ajax — 小于 2.5 球**

```
20261018-N1-Groningen-Ajax-U25
```

**9. Malaga vs Sociedad — 小于 2.5 球**

```
20261018-SP1-Malaga-Sociedad-U25
```

**10. Osasuna vs Santander — 大于 2.5 球**

```
20261018-SP1-Osasuna-Santander-O25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261017-F2-Nantes-Dunkerque-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261017-SC1-Stenhousemuir-RaithRvs-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261017-E3-Colchester-Exeter-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261017-E3-Grimsby-Northampton-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261017-F2-Metz-Sochaux-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261018-G1-Panetolikos-Olympiakos-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261018-I1-Milan-Atalanta-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261018-N1-Groningen-Ajax-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261018-SP1-Malaga-Sociedad-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261018-SP1-Osasuna-Santander-O25 --odds <Tipico赔率> --stake 1.00
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
| Colchester vs Exeter | 平局 + 小于 2.5 球 | 3.30 | **3.40** | 4.83 |
| Colchester vs Exeter | 主胜 Colchester + 小于 2.5 球 | 5.16 | **5.31** | 3.89 |
| Colchester vs Exeter | 客胜 Exeter + 小于 2.5 球 | 7.37 | **7.59** | 5.95 |
| Grimsby vs Northampton | 平局 + 小于 2.5 球 | 4.08 | **4.20** | 6.33 |
| Grimsby vs Northampton | 主胜 Grimsby + 小于 2.5 球 | 4.27 | **4.40** | 3.15 |
| Grimsby vs Northampton | 客胜 Northampton + 小于 2.5 球 | 9.88 | **10.17** | 9.46 |
| Metz vs Sochaux | 平局 + 小于 2.5 球 | 4.00 | **4.12** | 6.01 |
| Metz vs Sochaux | 主胜 Metz + 小于 2.5 球 | 4.31 | **4.44** | 3.28 |
| Metz vs Sochaux | 客胜 Sochaux + 小于 2.5 球 | 9.34 | **9.62** | 8.52 |
| Nantes vs Dunkerque | 客胜 Dunkerque + 大于 2.5 球 | 5.34 | **5.50** | 6.30 |
| Nantes vs Dunkerque | 客胜 Dunkerque + 小于 2.5 球 | 10.25 | **10.56** | 7.93 |
| Nantes vs Dunkerque | 平局 + 大于 2.5 球 | 13.38 | **13.78** | 7.47 |
| Panetolikos vs Olympiakos | 客胜 Olympiakos + 小于 2.5 球 | 3.42 | **3.52** | 2.69 |
| Panetolikos vs Olympiakos | 平局 + 小于 2.5 球 | 4.87 | **5.02** | 8.01 |
| Panetolikos vs Olympiakos | 主胜 Panetolikos + 小于 2.5 球 | 18.16 | **18.70** | 18.00 |
| Milan vs Atalanta | 平局 + 小于 2.5 球 | 5.11 | **5.26** | 7.82 |
| Milan vs Atalanta | 客胜 Atalanta + 大于 2.5 球 | 6.41 | **6.60** | 7.50 |
| Milan vs Atalanta | 客胜 Atalanta + 小于 2.5 球 | 9.57 | **9.86** | 7.86 |
| Groningen vs Ajax | 平局 + 小于 2.5 球 | 6.65 | **6.85** | 12.07 |
| Groningen vs Ajax | 客胜 Ajax + 小于 2.5 球 | 8.19 | **8.44** | 5.93 |
| Groningen vs Ajax | 主胜 Groningen + 小于 2.5 球 | 13.51 | **13.92** | 10.53 |
| Stenhousemuir vs Raith Rvs | 平局 + 小于 2.5 球 | 3.73 | **3.84** | 5.44 |
| Stenhousemuir vs Raith Rvs | 主胜 Stenhousemuir + 大于 2.5 球 | 4.75 | **4.89** | 6.94 |
| Stenhousemuir vs Raith Rvs | 主胜 Stenhousemuir + 小于 2.5 球 | 5.68 | **5.86** | 4.13 |
| Osasuna vs Santander | 主胜 Osasuna + 大于 2.5 球 | 2.62 | **2.70** | 3.02 |
| Osasuna vs Santander | 客胜 Santander + 大于 2.5 球 | 5.85 | **6.03** | 6.18 |
| Osasuna vs Santander | 平局 + 大于 2.5 球 | 10.96 | **11.29** | 6.65 |
| Malaga vs Sociedad | 平局 + 小于 2.5 球 | 4.50 | **4.63** | 6.90 |
| Malaga vs Sociedad | 客胜 Sociedad + 小于 2.5 球 | 5.49 | **5.65** | 4.11 |
| Malaga vs Sociedad | 主胜 Malaga + 小于 2.5 球 | 8.07 | **8.31** | 7.14 |

## 备注
- Elversberg vs Augsburg：球队数据不足（可能是升班马），跳过
- Schalke 04 vs Mainz：球队数据不足（可能是升班马），跳过
- Werder Bremen vs Paderborn：球队数据不足（可能是升班马），跳过
- Wolfsburg vs Heidenheim：球队数据不足（可能是升班马），跳过
- Hannover vs St Pauli：球队数据不足（可能是升班马），跳过
- Bielefeld vs Osnabruck：球队数据不足（可能是升班马），跳过
- Fulham vs Hull：球队数据不足（可能是升班马），跳过
- Troyes vs Lens：球队数据不足（可能是升班马），跳过
- Kalamata vs OFI Crete：球队数据不足（可能是升班马），跳过
- PAOK vs Iraklis：球队数据不足（可能是升班马），跳过
- Ascoli vs Empoli：球队数据不足（可能是升班马），跳过
- Benevento vs Vicenza：球队数据不足（可能是升班马），跳过
- Sampdoria vs Arezzo：球队数据不足（可能是升班马），跳过
- Erzurumspor vs Eyupspor：球队数据不足（可能是升班马），跳过
- Amedspor vs Konyaspor：球队数据不足（可能是升班马），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。