# 投注建议 · 2026-11-01

覆盖 11-01 至 11-02 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 65 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Arezzo vs Ascoli | 意乙 | 11-01 15:00 | 客胜 Ascoli | 1.87 | **1.92** | 2.13* | €1.00 |
| 2 | Lommel SK vs Gent | 比甲 | 11-01 18:30 | 主胜 Lommel SK | 3.59 | **3.69** | 4.04* | €1.00 |
| 3 | Frosinone vs Torino | 意甲 | 11-01 15:00 | 主胜 Frosinone | 1.93 | **1.99** | 2.14* | €1.00 |
| 4 | Como vs Venezia | 意甲 | 11-01 12:30 | 小于 2.5 球 | 2.64 | **2.72** | 2.91* | €1.00 |
| 5 | St Pauli vs Nurnberg | 德乙 | 11-01 13:30 | 小于 2.5 球 | 2.06 | **2.12** | 2.21* | €1.00 |
| 6 | Kalamata vs Iraklis | 希超 | 11-02 18:30 | 大于 2.5 球 | 1.93 | **1.99** | 2.10* | €1.00 |
| 7 | Mallorca vs Cadiz | 西乙 | 11-02 21:00 | 小于 2.5 球 | 1.76 | **1.82** | 1.84* | €1.00 |
| 8 | Atalanta vs Parma | 意甲 | 11-02 20:45 | 小于 2.5 球 | 2.15 | **2.22** | 2.23* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Arezzo vs Ascoli — 客胜 Ascoli**

```
20261101-I2-Arezzo-Ascoli-A
```

**2. Lommel SK vs Gent — 主胜 Lommel SK**

```
20261101-B1-LommelSK-Gent-H
```

**3. Frosinone vs Torino — 主胜 Frosinone**

```
20261101-I1-Frosinone-Torino-H
```

**4. Como vs Venezia — 小于 2.5 球**

```
20261101-I1-Como-Venezia-U25
```

**5. St Pauli vs Nurnberg — 小于 2.5 球**

```
20261101-D2-StPauli-Nurnberg-U25
```

**6. Kalamata vs Iraklis — 大于 2.5 球**

```
20261102-G1-Kalamata-Iraklis-O25
```

**7. Mallorca vs Cadiz — 小于 2.5 球**

```
20261102-SP2-Mallorca-Cadiz-U25
```

**8. Atalanta vs Parma — 小于 2.5 球**

```
20261102-I1-Atalanta-Parma-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261101-I2-Arezzo-Ascoli-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261101-B1-LommelSK-Gent-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261101-I1-Frosinone-Torino-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261101-I1-Como-Venezia-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261101-D2-StPauli-Nurnberg-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261102-G1-Kalamata-Iraklis-O25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261102-SP2-Mallorca-Cadiz-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261102-I1-Atalanta-Parma-U25 --odds <Tipico赔率> --stake 1.00
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
| Kalamata vs Iraklis | 主胜 Kalamata + 大于 2.5 球 | 3.76 | **3.88** | 4.56 |
| Kalamata vs Iraklis | 客胜 Iraklis + 大于 2.5 球 | 5.41 | **5.58** | 6.44 |
| Kalamata vs Iraklis | 平局 + 大于 2.5 球 | 14.93 | **15.38** | 7.00 |
| Como vs Venezia | 主胜 Como + 小于 2.5 球 | 4.87 | **5.01** | 3.62 |
| Como vs Venezia | 平局 + 小于 2.5 球 | 7.77 | **8.00** | 15.65 |
| Como vs Venezia | 客胜 Venezia + 小于 2.5 球 | 22.72 | **23.41** | 26.44 |
| Frosinone vs Torino | 主胜 Frosinone + 大于 2.5 球 | 2.37 | **2.44** | 2.68 |
| Atalanta vs Parma | 主胜 Atalanta + 小于 2.5 球 | 4.44 | **4.57** | 3.40 |
| Atalanta vs Parma | 平局 + 小于 2.5 球 | 5.92 | **6.10** | 9.94 |
| Atalanta vs Parma | 客胜 Parma + 小于 2.5 球 | 14.32 | **14.75** | 14.32 |
| Arezzo vs Ascoli | 客胜 Ascoli + 大于 2.5 球 | 2.79 | **2.87** | 3.57 |
| Arezzo vs Ascoli | 客胜 Ascoli + 小于 2.5 球 | 5.67 | **5.84** | 3.92 |
| Mallorca vs Cadiz | 主胜 Mallorca + 小于 2.5 球 | 3.64 | **3.75** | 2.80 |
| Mallorca vs Cadiz | 平局 + 小于 2.5 球 | 4.72 | **4.86** | 7.45 |

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。