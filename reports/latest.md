# 投注建议 · 2026-10-20

覆盖 10-20 至 10-21 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 16 场比赛

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Man City vs AEK | 欧冠 | 10-20 21:00 | 小于 2.5 球 | 3.55 | **3.66** | 3.94* | €1.00 |
| 2 | Paris SG vs Barcelona | 欧冠 | 10-20 21:00 | 小于 2.5 球 | 4.20 | **4.33** | 4.57* | €1.00 |
| 3 | Napoli vs Bodo/Glimt | 欧冠 | 10-20 21:00 | 客胜 Bodo/Glimt | 4.19 | **4.31** | 4.34* | €1.00 |
| 4 | Inter vs Shakhtar Donetsk | 欧冠 | 10-21 21:00 | 小于 2.5 球 | 2.98 | **3.07** | 3.80* | €1.00 |
| 5 | Real Madrid vs RB Leipzig | 欧冠 | 10-21 21:00 | 小于 2.5 球 | 3.88 | **4.00** | 4.45* | €1.00 |
| 6 | Como vs Man United | 欧冠 | 10-21 18:45 | 客胜 Man United | 2.63 | **2.71** | 2.92* | €1.00 |
| 7 | Betis vs Feyenoord | 欧冠 | 10-21 21:00 | 客胜 Feyenoord | 4.64 | **4.78** | 5.04* | €1.00 |
| 8 | Bayern Munich vs Arsenal | 欧冠 | 10-21 21:00 | 客胜 Arsenal | 3.16 | **3.25** | 3.36* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Man City vs AEK — 小于 2.5 球**

```
20261020-CL-ManCity-AEK-U25
```

**2. Paris SG vs Barcelona — 小于 2.5 球**

```
20261020-CL-ParisSG-Barcelona-U25
```

**3. Napoli vs Bodo/Glimt — 客胜 Bodo/Glimt**

```
20261020-CL-Napoli-BodoGlimt-A
```

**4. Inter vs Shakhtar Donetsk — 小于 2.5 球**

```
20261021-CL-Inter-ShakhtarDonetsk-U25
```

**5. Real Madrid vs RB Leipzig — 小于 2.5 球**

```
20261021-CL-RealMadrid-RBLeipzig-U25
```

**6. Como vs Man United — 客胜 Man United**

```
20261021-CL-Como-ManUnited-A
```

**7. Betis vs Feyenoord — 客胜 Feyenoord**

```
20261021-CL-Betis-Feyenoord-A
```

**8. Bayern Munich vs Arsenal — 客胜 Arsenal**

```
20261021-CL-BayernMunich-Arsenal-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261020-CL-ManCity-AEK-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261020-CL-ParisSG-Barcelona-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261020-CL-Napoli-BodoGlimt-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261021-CL-Inter-ShakhtarDonetsk-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261021-CL-RealMadrid-RBLeipzig-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261021-CL-Como-ManUnited-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261021-CL-Betis-Feyenoord-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261021-CL-BayernMunich-Arsenal-A --odds <Tipico赔率> --stake 1.00
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
| Man City vs AEK | 主胜 Man City + 小于 2.5 球 | 5.36 | **5.53** | 4.24 |
| Man City vs AEK | 平局 + 小于 2.5 球 | 13.15 | **13.55** | 32.38 |
| Man City vs AEK | 平局 + 大于 2.5 球 | 29.76 | **30.65** | 12.70 |
| Man City vs AEK | 客胜 AEK + 大于 2.5 球 | 30.27 | **31.18** | 26.65 |
| Paris SG vs Barcelona | 主胜 Paris SG + 大于 2.5 球 | 2.89 | **2.98** | 3.16 |
| Paris SG vs Barcelona | 平局 + 小于 2.5 球 | 10.11 | **10.41** | 19.53 |
| Paris SG vs Barcelona | 主胜 Paris SG + 小于 2.5 球 | 14.25 | **14.68** | 10.11 |
| Paris SG vs Barcelona | 客胜 Barcelona + 小于 2.5 球 | 14.53 | **14.96** | 11.39 |
| Napoli vs Bodo/Glimt | 平局 + 小于 2.5 球 | 6.09 | **6.28** | 10.02 |
| Napoli vs Bodo/Glimt | 客胜 Bodo/Glimt + 大于 2.5 球 | 6.43 | **6.62** | 7.15 |
| Napoli vs Bodo/Glimt | 客胜 Bodo/Glimt + 小于 2.5 球 | 12.02 | **12.38** | 10.11 |
| Como vs Man United | 客胜 Man United + 大于 2.5 球 | 3.89 | **4.01** | 4.65 |
| Como vs Man United | 平局 + 小于 2.5 球 | 5.69 | **5.86** | 9.15 |
| Como vs Man United | 客胜 Man United + 小于 2.5 球 | 8.13 | **8.37** | 6.07 |
| Bayern Munich vs Arsenal | 客胜 Arsenal + 大于 2.5 球 | 4.71 | **4.85** | 5.40 |
| Bayern Munich vs Arsenal | 平局 + 小于 2.5 球 | 6.07 | **6.26** | 9.82 |
| Bayern Munich vs Arsenal | 客胜 Arsenal + 小于 2.5 球 | 9.59 | **9.88** | 7.60 |
| Bayern Munich vs Arsenal | 平局 + 大于 2.5 球 | 12.44 | **12.81** | 6.98 |
| Betis vs Feyenoord | 客胜 Feyenoord + 大于 2.5 球 | 6.45 | **6.64** | 6.97 |
| Betis vs Feyenoord | 平局 + 小于 2.5 球 | 7.88 | **8.12** | 14.16 |
| Betis vs Feyenoord | 客胜 Feyenoord + 小于 2.5 球 | 16.52 | **17.02** | 13.89 |
| Inter vs Shakhtar Donetsk | 主胜 Inter + 小于 2.5 球 | 5.18 | **5.33** | 4.04 |
| Inter vs Shakhtar Donetsk | 平局 + 小于 2.5 球 | 9.30 | **9.58** | 18.83 |
| Inter vs Shakhtar Donetsk | 客胜 Shakhtar Donetsk + 大于 2.5 球 | 14.41 | **14.85** | 14.47 |
| Inter vs Shakhtar Donetsk | 客胜 Shakhtar Donetsk + 小于 2.5 球 | 28.94 | **29.81** | 28.70 |
| Real Madrid vs RB Leipzig | 主胜 Real Madrid + 小于 2.5 球 | 7.00 | **7.21** | 5.30 |
| Real Madrid vs RB Leipzig | 客胜 RB Leipzig + 大于 2.5 球 | 11.60 | **11.95** | 11.56 |
| Real Madrid vs RB Leipzig | 平局 + 小于 2.5 球 | 11.87 | **12.22** | 25.85 |
| Real Madrid vs RB Leipzig | 平局 + 大于 2.5 球 | 15.15 | **15.60** | 8.96 |

## 备注
- 赛程源里没有 10-20 起 2 天内的联赛比赛。fixtures.csv 最新的一场是 2026-10-19（已经是 1 天前），只覆盖 20 个联赛：D1、D2、E0、E1、E2、E3、F1、F2、G1、I1、I2、N1、P1、SC0、SC1、SC2、SC3、SP1、SP2、T1。football-data.co.uk 的赛程是周五下午发布周末场次、周二下午发布周中场次，国际比赛周没有联赛可发就不会更新。等不及可以用 manual_fixtures.csv 手填。
- 从 the-odds-api 取到 18 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 18 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 163 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- Fenerbahce vs Slavia Praha：球队比赛数不够（门槛 min_team_matches），跳过
- Roma vs ŠK Slovan Bratislava：球队比赛数不够（门槛 min_team_matches），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。