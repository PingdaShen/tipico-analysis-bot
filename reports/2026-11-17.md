# 投注建议 · 2026-11-17

覆盖 11-17 至 11-18 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 7 场比赛

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Wales vs Portugal | 国家队 | 11-17 20:45 | 小于 2.5 球 | 2.38 | **2.46** | 2.62* | €1.00 |
| 2 | Denmark vs Norway | 国家队 | 11-17 20:45 | 主胜 Denmark | 2.35 | **2.42** | 2.53* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Wales vs Portugal — 小于 2.5 球**

```
20261117-INT-Wales-Portugal-U25
```

**2. Denmark vs Norway — 主胜 Denmark**

```
20261117-INT-Denmark-Norway-H
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261117-INT-Wales-Portugal-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261117-INT-Denmark-Norway-H --odds <Tipico赔率> --stake 1.00
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
| Denmark vs Norway | 主胜 Denmark + 大于 2.5 球 | 3.18 | **3.28** | 3.66 |
| Denmark vs Norway | 平局 + 小于 2.5 球 | 7.01 | **7.22** | 12.15 |
| Denmark vs Norway | 主胜 Denmark + 小于 2.5 球 | 9.02 | **9.29** | 6.57 |
| Wales vs Portugal | 客胜 Portugal + 小于 2.5 球 | 4.66 | **4.80** | 3.64 |
| Wales vs Portugal | 平局 + 小于 2.5 球 | 6.90 | **7.11** | 12.15 |
| Wales vs Portugal | 主胜 Wales + 小于 2.5 球 | 16.74 | **17.25** | 16.00 |

## 备注
- 赛程源里没有 11-17 起 2 天内的联赛比赛。fixtures.csv 最新的一场是 2026-11-16（已经是 1 天前），只覆盖 7 个联赛：E2、E3、EC、SC1、SC2、SC3、SP2。football-data.co.uk 的赛程是周五下午发布周末场次、周二下午发布周中场次，国际比赛周没有联赛可发就不会更新。等不及可以用 manual_fixtures.csv 手填。
- 从 the-odds-api 取到 8 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 8 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 450 次（每月 500）。
- 国家队：赛果数据最新到 2026-10-06（距今 42 天），这之后的比赛模型还没看到。
- 手填赛程里的球队「Bosnia & Herzegovina」模型不认识，可能是「Bosnia and Herzegovina」，这场跳过。

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。