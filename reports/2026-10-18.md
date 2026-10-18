# 投注建议 · 2026-10-18

覆盖 10-18 至 10-19 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 47 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Panetolikos vs Olympiakos | 希超 | 10-18 16:00 | 小于 2.5 球 | 1.81 | **1.86** | 1.96* | €1.00 |
| 2 | Milan vs Atalanta | 意甲 | 10-18 18:00 | 客胜 Atalanta | 3.84 | **3.95** | 4.12* | €1.00 |
| 3 | Groningen vs Ajax | 荷甲 | 10-18 16:45 | 小于 2.5 球 | 2.89 | **2.97** | 3.06* | €1.00 |
| 4 | Malaga vs Sociedad | 西甲 | 10-18 18:30 | 小于 2.5 球 | 1.89 | **1.95** | 1.99* | €1.00 |
| 5 | Osasuna vs Santander | 西甲 | 10-18 14:00 | 大于 2.5 球 | 1.56 | **1.60** | 1.63* | €1.00 |
| 6 | Monza vs Cagliari | 意甲 | 10-19 18:30 | 客胜 Cagliari | 2.71 | **2.79** | 3.04* | €1.00 |
| 7 | Celta B vs Tenerife | 西乙 | 10-19 20:30 | 主胜 Celta B | 2.39 | **2.46** | 2.51* | €1.00 |
| 8 | Rodez vs Montpellier | 法乙 | 10-19 20:45 | 小于 2.5 球 | 2.05 | **2.11** | 2.15* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Panetolikos vs Olympiakos — 小于 2.5 球**

```
20261018-G1-Panetolikos-Olympiakos-U25
```

**2. Milan vs Atalanta — 客胜 Atalanta**

```
20261018-I1-Milan-Atalanta-A
```

**3. Groningen vs Ajax — 小于 2.5 球**

```
20261018-N1-Groningen-Ajax-U25
```

**4. Malaga vs Sociedad — 小于 2.5 球**

```
20261018-SP1-Malaga-Sociedad-U25
```

**5. Osasuna vs Santander — 大于 2.5 球**

```
20261018-SP1-Osasuna-Santander-O25
```

**6. Monza vs Cagliari — 客胜 Cagliari**

```
20261019-I1-Monza-Cagliari-A
```

**7. Celta B vs Tenerife — 主胜 Celta B**

```
20261019-SP2-CeltaB-Tenerife-H
```

**8. Rodez vs Montpellier — 小于 2.5 球**

```
20261019-F2-Rodez-Montpellier-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261018-G1-Panetolikos-Olympiakos-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261018-I1-Milan-Atalanta-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261018-N1-Groningen-Ajax-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261018-SP1-Malaga-Sociedad-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261018-SP1-Osasuna-Santander-O25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261019-I1-Monza-Cagliari-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261019-SP2-CeltaB-Tenerife-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261019-F2-Rodez-Montpellier-U25 --odds <Tipico赔率> --stake 1.00
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
| Rodez vs Montpellier | 平局 + 小于 2.5 球 | 4.71 | **4.85** | 7.24 |
| Rodez vs Montpellier | 客胜 Montpellier + 小于 2.5 球 | 6.86 | **7.07** | 5.29 |
| Rodez vs Montpellier | 主胜 Rodez + 小于 2.5 球 | 7.71 | **7.94** | 6.23 |
| Panetolikos vs Olympiakos | 客胜 Olympiakos + 小于 2.5 球 | 3.42 | **3.52** | 2.69 |
| Panetolikos vs Olympiakos | 平局 + 小于 2.5 球 | 4.87 | **5.02** | 8.01 |
| Panetolikos vs Olympiakos | 主胜 Panetolikos + 小于 2.5 球 | 18.16 | **18.70** | 18.00 |
| Milan vs Atalanta | 平局 + 小于 2.5 球 | 5.11 | **5.26** | 7.82 |
| Milan vs Atalanta | 客胜 Atalanta + 大于 2.5 球 | 6.41 | **6.60** | 7.50 |
| Milan vs Atalanta | 客胜 Atalanta + 小于 2.5 球 | 9.57 | **9.86** | 7.86 |
| Monza vs Cagliari | 客胜 Cagliari + 大于 2.5 球 | 4.60 | **4.74** | 5.76 |
| Monza vs Cagliari | 客胜 Cagliari + 小于 2.5 球 | 6.61 | **6.81** | 5.12 |
| Groningen vs Ajax | 平局 + 小于 2.5 球 | 6.65 | **6.85** | 12.07 |
| Groningen vs Ajax | 客胜 Ajax + 小于 2.5 球 | 8.19 | **8.44** | 5.93 |
| Groningen vs Ajax | 主胜 Groningen + 小于 2.5 球 | 13.51 | **13.92** | 10.53 |
| Osasuna vs Santander | 主胜 Osasuna + 大于 2.5 球 | 2.62 | **2.70** | 3.02 |
| Osasuna vs Santander | 客胜 Santander + 大于 2.5 球 | 5.85 | **6.03** | 6.18 |
| Osasuna vs Santander | 平局 + 大于 2.5 球 | 10.96 | **11.29** | 6.65 |
| Malaga vs Sociedad | 平局 + 小于 2.5 球 | 4.50 | **4.63** | 6.90 |
| Malaga vs Sociedad | 客胜 Sociedad + 小于 2.5 球 | 5.49 | **5.65** | 4.11 |
| Malaga vs Sociedad | 主胜 Malaga + 小于 2.5 球 | 8.07 | **8.31** | 7.14 |
| Celta B vs Tenerife | 主胜 Celta B + 大于 2.5 球 | 3.94 | **4.06** | 4.86 |
| Celta B vs Tenerife | 主胜 Celta B + 小于 2.5 球 | 6.05 | **6.23** | 4.69 |

## 备注
- Bielefeld vs Osnabruck：球队数据不足（可能是升班马），跳过
- Tottenham vs Coventry：球队数据不足（可能是升班马），跳过
- Kalamata vs OFI Crete：球队数据不足（可能是升班马），跳过
- PAOK vs Iraklis：球队数据不足（可能是升班马），跳过
- Sampdoria vs Arezzo：球队数据不足（可能是升班马），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。