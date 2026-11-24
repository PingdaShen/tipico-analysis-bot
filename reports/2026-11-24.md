# 投注建议 · 2026-11-24

覆盖 11-24 至 11-25 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 58 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Bradford vs Barnsley | 英甲 | 11-24 20:45 | 小于 2.5 球 | 2.37 | **2.44** | 2.58* | €1.00 |

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 2 | Como vs AEK | 欧冠 | 11-24 21:00 | 小于 2.5 球 | 2.79 | **2.87** | 3.41* | €1.00 |
| 3 | RB Leipzig vs Lens | 欧冠 | 11-24 21:00 | 小于 2.5 球 | 3.35 | **3.45** | 3.79* | €1.00 |
| 4 | Man City vs Napoli | 欧冠 | 11-24 21:00 | 小于 2.5 球 | 3.39 | **3.49** | 3.71* | €1.00 |
| 5 | Bodo/Glimt vs LASK | 欧冠 | 11-24 18:45 | 小于 2.5 球 | 3.96 | **4.08** | 4.26* | €1.00 |
| 6 | Inter vs Stuttgart | 欧冠 | 11-25 21:00 | 小于 2.5 球 | 3.75 | **3.87** | 4.08* | €1.00 |
| 7 | Paris SG vs Roma | 欧冠 | 11-25 21:00 | 小于 2.5 球 | 3.11 | **3.20** | 3.34* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Como vs AEK — 小于 2.5 球**

```
20261124-CL-Como-AEK-U25
```

**2. RB Leipzig vs Lens — 小于 2.5 球**

```
20261124-CL-RBLeipzig-Lens-U25
```

**3. Man City vs Napoli — 小于 2.5 球**

```
20261124-CL-ManCity-Napoli-U25
```

**4. Bradford vs Barnsley — 小于 2.5 球**

```
20261124-E2-Bradford-Barnsley-U25
```

**5. Bodo/Glimt vs LASK — 小于 2.5 球**

```
20261124-CL-BodoGlimt-LASK-U25
```

**6. Inter vs Stuttgart — 小于 2.5 球**

```
20261125-CL-Inter-Stuttgart-U25
```

**7. Paris SG vs Roma — 小于 2.5 球**

```
20261125-CL-ParisSG-Roma-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261124-CL-Como-AEK-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261124-CL-RBLeipzig-Lens-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261124-CL-ManCity-Napoli-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261124-E2-Bradford-Barnsley-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261124-CL-BodoGlimt-LASK-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261125-CL-Inter-Stuttgart-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261125-CL-ParisSG-Roma-U25 --odds <Tipico赔率> --stake 1.00
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
| Bradford vs Barnsley | 主胜 Bradford + 小于 2.5 球 | 5.41 | **5.57** | 4.13 |
| Bradford vs Barnsley | 平局 + 小于 2.5 球 | 6.14 | **6.32** | 10.39 |
| Bradford vs Barnsley | 客胜 Barnsley + 小于 2.5 球 | 13.37 | **13.77** | 11.91 |
| Bodo/Glimt vs LASK | 主胜 Bodo/Glimt + 小于 2.5 球 | 7.71 | **7.94** | 5.56 |
| Bodo/Glimt vs LASK | 平局 + 小于 2.5 球 | 11.11 | **11.44** | 24.50 |
| Bodo/Glimt vs LASK | 客胜 LASK + 小于 2.5 球 | 30.50 | **31.41** | 31.37 |
| Como vs AEK | 主胜 Como + 小于 2.5 球 | 5.32 | **5.48** | 4.24 |
| Como vs AEK | 平局 + 小于 2.5 球 | 8.19 | **8.44** | 15.05 |
| Como vs AEK | 客胜 AEK + 大于 2.5 球 | 9.14 | **9.41** | 9.84 |
| Como vs AEK | 客胜 AEK + 小于 2.5 球 | 20.39 | **21.00** | 17.57 |
| Man City vs Napoli | 主胜 Man City + 小于 2.5 球 | 6.16 | **6.34** | 4.61 |
| Man City vs Napoli | 平局 + 小于 2.5 球 | 10.04 | **10.34** | 21.38 |
| Man City vs Napoli | 客胜 Napoli + 大于 2.5 球 | 13.52 | **13.93** | 13.26 |
| Man City vs Napoli | 客胜 Napoli + 小于 2.5 球 | 30.30 | **31.21** | 31.69 |
| RB Leipzig vs Lens | 主胜 RB Leipzig + 小于 2.5 球 | 6.63 | **6.83** | 5.10 |
| RB Leipzig vs Lens | 客胜 Lens + 大于 2.5 球 | 8.46 | **8.71** | 8.88 |
| RB Leipzig vs Lens | 平局 + 小于 2.5 球 | 9.48 | **9.77** | 18.35 |
| RB Leipzig vs Lens | 平局 + 大于 2.5 球 | 12.96 | **13.35** | 7.81 |
| Paris SG vs Roma | 主胜 Paris SG + 小于 2.5 球 | 6.40 | **6.59** | 4.73 |
| Paris SG vs Roma | 平局 + 小于 2.5 球 | 8.28 | **8.53** | 15.94 |
| Paris SG vs Roma | 客胜 Roma + 大于 2.5 球 | 9.69 | **9.99** | 9.97 |
| Paris SG vs Roma | 客胜 Roma + 小于 2.5 球 | 22.34 | **23.01** | 21.01 |
| Inter vs Stuttgart | 主胜 Inter + 小于 2.5 球 | 7.73 | **7.97** | 5.56 |
| Inter vs Stuttgart | 平局 + 小于 2.5 球 | 10.23 | **10.54** | 21.58 |
| Inter vs Stuttgart | 客胜 Stuttgart + 小于 2.5 球 | 25.35 | **26.11** | 24.80 |

## 备注
- 从 the-odds-api 取到 18 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 18 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 436 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- ŠK Slovan Bratislava vs Betis：球队比赛数不够（门槛 min_team_matches），跳过
- Slavia Praha vs Villarreal：球队比赛数不够（门槛 min_team_matches），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。