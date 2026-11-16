# 投注建议 · 2026-11-16

覆盖 11-16 至 11-17 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 18 场比赛

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Greece vs Serbia | 国家队 | 11-16 20:45 | 小于 2.5 球 | 2.07 | **2.13** | 2.22* | €1.00 |
| 2 | Lithuania vs Liechtenstein | 国家队 | 11-16 18:00 | 小于 2.5 球 | 1.76 | **1.81** | 1.87* | €1.00 |
| 3 | Estonia vs Bulgaria | 国家队 | 11-16 18:00 | 客胜 Bulgaria | 3.91 | **4.03** | 4.09* | €1.00 |
| 4 | Denmark vs Norway | 国家队 | 11-17 20:45 | 主胜 Denmark | 2.24 | **2.31** | 2.37* | €1.00 |
| 5 | Ukraine vs Georgia | 国家队 | 11-17 20:45 | 主胜 Ukraine | 2.11 | **2.17** | 2.18* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Greece vs Serbia — 小于 2.5 球**

```
20261116-INT-Greece-Serbia-U25
```

**2. Lithuania vs Liechtenstein — 小于 2.5 球**

```
20261116-INT-Lithuania-Liechtenstein-U25
```

**3. Estonia vs Bulgaria — 客胜 Bulgaria**

```
20261116-INT-Estonia-Bulgaria-A
```

**4. Denmark vs Norway — 主胜 Denmark**

```
20261117-INT-Denmark-Norway-H
```

**5. Ukraine vs Georgia — 主胜 Ukraine**

```
20261117-INT-Ukraine-Georgia-H
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261116-INT-Greece-Serbia-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261116-INT-Lithuania-Liechtenstein-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261116-INT-Estonia-Bulgaria-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261117-INT-Denmark-Norway-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261117-INT-Ukraine-Georgia-H --odds <Tipico赔率> --stake 1.00
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
| Estonia vs Bulgaria | 平局 + 小于 2.5 球 | 3.96 | **4.07** | 5.44 |
| Estonia vs Bulgaria | 客胜 Bulgaria + 小于 2.5 球 | 7.47 | **7.69** | 6.30 |
| Estonia vs Bulgaria | 客胜 Bulgaria + 大于 2.5 球 | 8.22 | **8.46** | 10.32 |
| Lithuania vs Liechtenstein | 主胜 Lithuania + 小于 2.5 球 | 2.42 | **2.49** | 2.12 |
| Lithuania vs Liechtenstein | 平局 + 小于 2.5 球 | 7.68 | **7.91** | 12.91 |
| Lithuania vs Liechtenstein | 客胜 Liechtenstein + 小于 2.5 球 | 39.90 | **41.09** | 51.45 |
| Lithuania vs Liechtenstein | 平局 + 大于 2.5 球 | 163.57 | **168.48** | 17.01 |
| Greece vs Serbia | 主胜 Greece + 小于 2.5 球 | 4.24 | **4.37** | 3.41 |
| Greece vs Serbia | 平局 + 小于 2.5 球 | 5.69 | **5.86** | 9.15 |
| Greece vs Serbia | 客胜 Serbia + 大于 2.5 球 | 10.49 | **10.81** | 11.63 |
| Greece vs Serbia | 客胜 Serbia + 小于 2.5 球 | 14.10 | **14.52** | 12.47 |
| Denmark vs Norway | 主胜 Denmark + 大于 2.5 球 | 3.13 | **3.23** | 3.64 |
| Denmark vs Norway | 主胜 Denmark + 小于 2.5 球 | 7.86 | **8.10** | 5.82 |
| Ukraine vs Georgia | 主胜 Ukraine + 大于 2.5 球 | 3.69 | **3.80** | 4.69 |
| Ukraine vs Georgia | 主胜 Ukraine + 小于 2.5 球 | 4.93 | **5.08** | 3.83 |

## 备注
- 从 the-odds-api 取到 18 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 15 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 452 次（每月 500）。
- 国家队：赛果数据最新到 2026-10-06（距今 41 天），这之后的比赛模型还没看到。
- 手填赛程里的球队「Bosnia & Herzegovina」模型不认识，可能是「Bosnia and Herzegovina」，这场跳过。

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。