# 投注建议 · 2026-11-13

覆盖 11-13 至 11-14 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 18 场比赛

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Netherlands vs Greece | 国家队 | 11-13 20:45 | 小于 2.5 球 | 2.32 | **2.39** | 2.41* | €1.00 |
| 2 | Liechtenstein vs Azerbaijan | 国家队 | 11-13 20:45 | 小于 2.5 球 | 1.61 | **1.66** | 1.66* | €1.00 |
| 3 | Moldova vs Kazakhstan | 国家队 | 11-13 18:00 | 客胜 Kazakhstan | 2.86 | **2.94** | 2.95* | €1.00 |
| 4 | Romania vs Poland | 国家队 | 11-14 20:45 | 主胜 Romania | 3.67 | **3.78** | 3.88* | €1.00 |
| 5 | Norway vs Wales | 国家队 | 11-14 18:00 | 小于 2.5 球 | 2.75 | **2.83** | 2.90* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Netherlands vs Greece — 小于 2.5 球**

```
20261113-INT-Netherlands-Greece-U25
```

**2. Liechtenstein vs Azerbaijan — 小于 2.5 球**

```
20261113-INT-Liechtenstein-Azerbaijan-U25
```

**3. Moldova vs Kazakhstan — 客胜 Kazakhstan**

```
20261113-INT-Moldova-Kazakhstan-A
```

**4. Romania vs Poland — 主胜 Romania**

```
20261114-INT-Romania-Poland-H
```

**5. Norway vs Wales — 小于 2.5 球**

```
20261114-INT-Norway-Wales-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261113-INT-Netherlands-Greece-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261113-INT-Liechtenstein-Azerbaijan-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261113-INT-Moldova-Kazakhstan-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261114-INT-Romania-Poland-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261114-INT-Norway-Wales-U25 --odds <Tipico赔率> --stake 1.00
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
| Moldova vs Kazakhstan | 客胜 Kazakhstan + 大于 2.5 球 | 5.67 | **5.84** | 7.31 |
| Moldova vs Kazakhstan | 客胜 Kazakhstan + 小于 2.5 球 | 5.76 | **5.93** | 4.69 |
| Liechtenstein vs Azerbaijan | 客胜 Azerbaijan + 小于 2.5 球 | 2.51 | **2.59** | 2.14 |
| Liechtenstein vs Azerbaijan | 平局 + 小于 2.5 球 | 5.46 | **5.62** | 8.37 |
| Liechtenstein vs Azerbaijan | 主胜 Liechtenstein + 小于 2.5 球 | 24.92 | **25.66** | 28.54 |
| Netherlands vs Greece | 主胜 Netherlands + 小于 2.5 球 | 5.04 | **5.19** | 3.85 |
| Netherlands vs Greece | 平局 + 小于 2.5 球 | 6.31 | **6.50** | 10.77 |
| Netherlands vs Greece | 客胜 Greece + 小于 2.5 球 | 13.54 | **13.94** | 12.80 |
| Norway vs Wales | 平局 + 小于 2.5 球 | 9.06 | **9.33** | 16.83 |
| Norway vs Wales | 客胜 Wales + 大于 2.5 球 | 12.68 | **13.06** | 13.01 |
| Norway vs Wales | 平局 + 大于 2.5 球 | 18.83 | **19.40** | 9.61 |
| Norway vs Wales | 客胜 Wales + 小于 2.5 球 | 23.89 | **24.61** | 22.80 |
| Romania vs Poland | 平局 + 小于 2.5 球 | 5.40 | **5.56** | 8.39 |
| Romania vs Poland | 主胜 Romania + 大于 2.5 球 | 5.96 | **6.14** | 6.90 |
| Romania vs Poland | 主胜 Romania + 小于 2.5 球 | 9.57 | **9.85** | 7.85 |

## 备注
- 赛程源里没有 11-13 起 2 天内的联赛比赛。fixtures.csv 最新的一场是 2026-11-09（已经是 4 天前），只覆盖 19 个联赛：B1、D1、D2、E0、E1、F1、F2、G1、I1、I2、N1、P1、SC0、SC1、SC2、SC3、SP1、SP2、T1。football-data.co.uk 的赛程是周五下午发布周末场次、周二下午发布周中场次，国际比赛周没有联赛可发就不会更新。等不及可以用 manual_fixtures.csv 手填。
- 从 the-odds-api 取到 19 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 15 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 460 次（每月 500）。
- 国家队：赛果数据最新到 2026-10-06（距今 38 天），这之后的比赛模型还没看到。
- 手填赛程里的球队「Bosnia & Herzegovina」模型不认识，可能是「Bosnia and Herzegovina」，这场跳过。

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。