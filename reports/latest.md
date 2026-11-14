# 投注建议 · 2026-11-14

覆盖 11-14 至 11-15 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 65 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Salford vs Northampton | 英乙 | 11-14 16:00 | 小于 2.5 球 | 1.68 | **1.73** | 1.84* | €1.00 |
| 2 | Mallorca vs Cordoba | 西乙 | 11-14 18:30 | 小于 2.5 球 | 2.17 | **2.24** | 2.32* | €1.00 |
| 3 | Kidderminster vs Halifax | 英格兰国家联赛 | 11-14 16:00 | 小于 2.5 球 | 1.82 | **1.87** | 1.94* | €1.00 |
| 4 | Exeter vs Cheltenham | 英乙 | 11-14 13:30 | 小于 2.5 球 | 1.69 | **1.74** | 1.80* | €1.00 |

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 5 | Romania vs Poland | 国家队 | 11-14 20:45 | 主胜 Romania | 4.14 | **4.26** | 4.58* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Romania vs Poland — 主胜 Romania**

```
20261114-INT-Romania-Poland-H
```

**2. Salford vs Northampton — 小于 2.5 球**

```
20261114-E3-Salford-Northampton-U25
```

**3. Mallorca vs Cordoba — 小于 2.5 球**

```
20261114-SP2-Mallorca-Cordoba-U25
```

**4. Kidderminster vs Halifax — 小于 2.5 球**

```
20261114-EC-Kidderminster-Halifax-U25
```

**5. Exeter vs Cheltenham — 小于 2.5 球**

```
20261114-E3-Exeter-Cheltenham-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261114-INT-Romania-Poland-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261114-E3-Salford-Northampton-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261114-SP2-Mallorca-Cordoba-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261114-EC-Kidderminster-Halifax-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261114-E3-Exeter-Cheltenham-U25 --odds <Tipico赔率> --stake 1.00
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
| Exeter vs Cheltenham | 平局 + 小于 2.5 球 | 4.03 | **4.15** | 5.93 |
| Exeter vs Cheltenham | 主胜 Exeter + 小于 2.5 球 | 4.48 | **4.62** | 3.47 |
| Exeter vs Cheltenham | 客胜 Cheltenham + 小于 2.5 球 | 8.35 | **8.60** | 7.44 |
| Salford vs Northampton | 主胜 Salford + 小于 2.5 球 | 3.93 | **4.04** | 3.06 |
| Salford vs Northampton | 平局 + 小于 2.5 球 | 4.06 | **4.19** | 6.09 |
| Salford vs Northampton | 客胜 Northampton + 小于 2.5 球 | 10.51 | **10.83** | 9.55 |
| Kidderminster vs Halifax | 平局 + 小于 2.5 球 | 4.26 | **4.38** | 6.28 |
| Kidderminster vs Halifax | 主胜 Kidderminster + 小于 2.5 球 | 6.24 | **6.43** | 4.95 |
| Kidderminster vs Halifax | 客胜 Halifax + 小于 2.5 球 | 6.47 | **6.66** | 5.30 |
| Mallorca vs Cordoba | 平局 + 小于 2.5 球 | 5.33 | **5.49** | 8.94 |
| Mallorca vs Cordoba | 主胜 Mallorca + 小于 2.5 球 | 5.80 | **5.97** | 4.08 |
| Romania vs Poland | 平局 + 小于 2.5 球 | 5.77 | **5.94** | 9.08 |
| Romania vs Poland | 主胜 Romania + 大于 2.5 球 | 6.70 | **6.90** | 7.67 |
| Romania vs Poland | 主胜 Romania + 小于 2.5 球 | 10.83 | **11.15** | 8.99 |
| Romania vs Poland | 平局 + 大于 2.5 球 | 15.17 | **15.62** | 7.75 |

## 备注
- 从 the-odds-api 取到 17 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 14 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 458 次（每月 500）。
- 国家队：赛果数据最新到 2026-10-06（距今 39 天），这之后的比赛模型还没看到。
- 手填赛程里的球队「Bosnia & Herzegovina」模型不认识，可能是「Bosnia and Herzegovina」，这场跳过。

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。