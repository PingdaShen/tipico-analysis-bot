# 投注建议 · 2026-11-06

覆盖 11-06 至 11-07 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 101 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Ascoli vs Palermo | 意乙 | 11-06 20:30 | 主胜 Ascoli | 2.70 | **2.78** | 3.01* | €1.00 |
| 2 | Venezia vs Udinese | 意甲 | 11-06 20:45 | 客胜 Udinese | 2.86 | **2.94** | 3.08* | €1.00 |
| 3 | Braunschweig vs Cottbus | 德乙 | 11-06 18:30 | 客胜 Cottbus | 3.22 | **3.32** | 3.35* | €1.00 |
| 4 | Paderborn vs Ein Frankfurt | 德甲 | 11-07 15:30 | 小于 2.5 球 | 2.25 | **2.32** | 2.67* | €1.00 |
| 5 | Cagliari vs Frosinone | 意甲 | 11-07 15:00 | 客胜 Frosinone | 2.11 | **2.17** | 2.41* | €1.00 |
| 6 | Arsenal vs Hull | 英超 | 11-07 16:00 | 小于 2.5 球 | 2.20 | **2.26** | 2.50* | €1.00 |
| 7 | Antwerp vs Lommel SK | 比甲 | 11-07 20:45 | 小于 2.5 球 | 2.17 | **2.24** | 2.41* | €1.00 |
| 8 | Pau FC vs Nantes | 法乙 | 11-07 20:00 | 主胜 Pau FC | 2.66 | **2.74** | 2.89* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Ascoli vs Palermo — 主胜 Ascoli**

```
20261106-I2-Ascoli-Palermo-H
```

**2. Venezia vs Udinese — 客胜 Udinese**

```
20261106-I1-Venezia-Udinese-A
```

**3. Braunschweig vs Cottbus — 客胜 Cottbus**

```
20261106-D2-Braunschweig-Cottbus-A
```

**4. Paderborn vs Ein Frankfurt — 小于 2.5 球**

```
20261107-D1-Paderborn-EinFrankfurt-U25
```

**5. Cagliari vs Frosinone — 客胜 Frosinone**

```
20261107-I1-Cagliari-Frosinone-A
```

**6. Arsenal vs Hull — 小于 2.5 球**

```
20261107-E0-Arsenal-Hull-U25
```

**7. Antwerp vs Lommel SK — 小于 2.5 球**

```
20261107-B1-Antwerp-LommelSK-U25
```

**8. Pau FC vs Nantes — 主胜 Pau FC**

```
20261107-F2-PauFC-Nantes-H
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261106-I2-Ascoli-Palermo-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261106-I1-Venezia-Udinese-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261106-D2-Braunschweig-Cottbus-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261107-D1-Paderborn-EinFrankfurt-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261107-I1-Cagliari-Frosinone-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261107-E0-Arsenal-Hull-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261107-B1-Antwerp-LommelSK-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261107-F2-PauFC-Nantes-H --odds <Tipico赔率> --stake 1.00
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
| Braunschweig vs Cottbus | 客胜 Cottbus + 大于 2.5 球 | 4.39 | **4.53** | 4.93 |
| Braunschweig vs Cottbus | 平局 + 大于 2.5 球 | 10.33 | **10.64** | 6.40 |
| Braunschweig vs Cottbus | 客胜 Cottbus + 小于 2.5 球 | 12.04 | **12.40** | 9.28 |
| Arsenal vs Hull | 主胜 Arsenal + 小于 2.5 球 | 3.58 | **3.69** | 2.90 |
| Arsenal vs Hull | 平局 + 小于 2.5 球 | 7.14 | **7.35** | 13.10 |
| Arsenal vs Hull | 客胜 Hull + 大于 2.5 球 | 25.09 | **25.84** | 24.28 |
| Arsenal vs Hull | 客胜 Hull + 小于 2.5 球 | 28.00 | **28.84** | 29.07 |
| Pau FC vs Nantes | 主胜 Pau FC + 大于 2.5 球 | 4.29 | **4.41** | 5.19 |
| Pau FC vs Nantes | 主胜 Pau FC + 小于 2.5 球 | 6.99 | **7.20** | 5.44 |
| Pau FC vs Nantes | 平局 + 大于 2.5 球 | 13.48 | **13.89** | 7.31 |
| Venezia vs Udinese | 平局 + 小于 2.5 球 | 4.62 | **4.76** | 6.88 |
| Venezia vs Udinese | 客胜 Udinese + 大于 2.5 球 | 4.76 | **4.91** | 5.93 |
| Venezia vs Udinese | 客胜 Udinese + 小于 2.5 球 | 7.14 | **7.35** | 5.51 |
| Cagliari vs Frosinone | 客胜 Frosinone + 大于 2.5 球 | 2.80 | **2.88** | 3.27 |
| Cagliari vs Frosinone | 客胜 Frosinone + 小于 2.5 球 | 8.61 | **8.87** | 5.96 |
| Ascoli vs Palermo | 主胜 Ascoli + 大于 2.5 球 | 4.13 | **4.26** | 5.28 |
| Ascoli vs Palermo | 平局 + 小于 2.5 球 | 4.53 | **4.67** | 7.33 |
| Ascoli vs Palermo | 主胜 Ascoli + 小于 2.5 球 | 7.81 | **8.05** | 5.54 |

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。