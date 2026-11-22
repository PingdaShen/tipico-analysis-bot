# 投注建议 · 2026-11-22

覆盖 11-22 至 11-23 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 52 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Milan vs Frosinone | 意甲 | 11-22 18:00 | 客胜 Frosinone | 4.23 | **4.36** | 5.21* | €1.00 |
| 2 | Lommel SK vs Standard | 比甲 | 11-22 19:15 | 小于 2.5 球 | 2.10 | **2.17** | 2.35* | €1.00 |
| 3 | Olympiakos vs Iraklis | 希超 | 11-22 18:00 | 小于 2.5 球 | 2.24 | **2.31** | 2.50* | €1.00 |
| 4 | Cottbus vs Hertha | 德乙 | 11-22 13:30 | 主胜 Cottbus | 4.01 | **4.13** | 4.44* | €1.00 |
| 5 | Hull vs Brighton | 英超 | 11-22 15:00 | 小于 2.5 球 | 2.06 | **2.12** | 2.19* | €1.00 |
| 6 | Sochaux vs Dunkerque | 法乙 | 11-23 20:45 | 客胜 Dunkerque | 2.69 | **2.77** | 2.87* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Milan vs Frosinone — 客胜 Frosinone**

```
20261122-I1-Milan-Frosinone-A
```

**2. Lommel SK vs Standard — 小于 2.5 球**

```
20261122-B1-LommelSK-Standard-U25
```

**3. Olympiakos vs Iraklis — 小于 2.5 球**

```
20261122-G1-Olympiakos-Iraklis-U25
```

**4. Cottbus vs Hertha — 主胜 Cottbus**

```
20261122-D2-Cottbus-Hertha-H
```

**5. Hull vs Brighton — 小于 2.5 球**

```
20261122-E0-Hull-Brighton-U25
```

**6. Sochaux vs Dunkerque — 客胜 Dunkerque**

```
20261123-F2-Sochaux-Dunkerque-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261122-I1-Milan-Frosinone-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261122-B1-LommelSK-Standard-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261122-G1-Olympiakos-Iraklis-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261122-D2-Cottbus-Hertha-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261122-E0-Hull-Brighton-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261123-F2-Sochaux-Dunkerque-A --odds <Tipico赔率> --stake 1.00
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
| Lommel SK vs Standard | 主胜 Lommel SK + 大于 2.5 球 | 4.29 | **4.42** | 5.37 |
| Lommel SK vs Standard | 平局 + 小于 2.5 球 | 4.90 | **5.05** | 7.88 |
| Lommel SK vs Standard | 主胜 Lommel SK + 小于 2.5 球 | 8.23 | **8.48** | 5.93 |
| Cottbus vs Hertha | 主胜 Cottbus + 大于 2.5 球 | 5.53 | **5.69** | 6.13 |
| Cottbus vs Hertha | 平局 + 小于 2.5 球 | 7.34 | **7.56** | 12.92 |
| Cottbus vs Hertha | 主胜 Cottbus + 小于 2.5 球 | 14.62 | **15.06** | 11.60 |
| Hull vs Brighton | 平局 + 小于 2.5 球 | 5.34 | **5.50** | 8.55 |
| Hull vs Brighton | 主胜 Hull + 大于 2.5 球 | 8.90 | **9.17** | 10.22 |
| Hull vs Brighton | 主胜 Hull + 小于 2.5 球 | 12.86 | **13.25** | 10.84 |
| Sochaux vs Dunkerque | 平局 + 小于 2.5 球 | 4.37 | **4.50** | 6.48 |
| Sochaux vs Dunkerque | 客胜 Dunkerque + 大于 2.5 球 | 4.54 | **4.68** | 5.89 |
| Sochaux vs Dunkerque | 客胜 Dunkerque + 小于 2.5 球 | 6.60 | **6.80** | 4.95 |
| Olympiakos vs Iraklis | 主胜 Olympiakos + 小于 2.5 球 | 3.71 | **3.82** | 2.92 |
| Olympiakos vs Iraklis | 平局 + 小于 2.5 球 | 6.98 | **7.19** | 13.61 |
| Olympiakos vs Iraklis | 客胜 Iraklis + 小于 2.5 球 | 30.20 | **31.11** | 32.59 |
| Milan vs Frosinone | 客胜 Frosinone + 大于 2.5 球 | 5.63 | **5.80** | 6.08 |
| Milan vs Frosinone | 平局 + 小于 2.5 球 | 9.03 | **9.30** | 15.84 |
| Milan vs Frosinone | 平局 + 大于 2.5 球 | 10.31 | **10.62** | 6.92 |
| Milan vs Frosinone | 客胜 Frosinone + 小于 2.5 球 | 17.04 | **17.56** | 13.92 |

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。