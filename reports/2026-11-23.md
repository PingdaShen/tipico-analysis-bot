# 投注建议 · 2026-11-23

覆盖 11-23 至 11-24 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 16 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Sochaux vs Dunkerque | 法乙 | 11-23 20:45 | 客胜 Dunkerque | 2.68 | **2.77** | 2.87* | €1.00 |

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 2 | Como vs AEK | 欧冠 | 11-24 21:00 | 小于 2.5 球 | 2.76 | **2.84** | 3.37* | €1.00 |
| 3 | RB Leipzig vs Lens | 欧冠 | 11-24 21:00 | 小于 2.5 球 | 3.22 | **3.31** | 3.54* | €1.00 |
| 4 | Galatasaray vs Aston Villa | 欧冠 | 11-24 18:45 | 小于 2.5 球 | 2.91 | **2.99** | 3.13* | €1.00 |
| 5 | Man City vs Napoli | 欧冠 | 11-24 21:00 | 小于 2.5 球 | 3.17 | **3.27** | 3.41* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Sochaux vs Dunkerque — 客胜 Dunkerque**

```
20261123-F2-Sochaux-Dunkerque-A
```

**2. Como vs AEK — 小于 2.5 球**

```
20261124-CL-Como-AEK-U25
```

**3. RB Leipzig vs Lens — 小于 2.5 球**

```
20261124-CL-RBLeipzig-Lens-U25
```

**4. Galatasaray vs Aston Villa — 小于 2.5 球**

```
20261124-CL-Galatasaray-AstonVilla-U25
```

**5. Man City vs Napoli — 小于 2.5 球**

```
20261124-CL-ManCity-Napoli-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261123-F2-Sochaux-Dunkerque-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261124-CL-Como-AEK-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261124-CL-RBLeipzig-Lens-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261124-CL-Galatasaray-AstonVilla-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261124-CL-ManCity-Napoli-U25 --odds <Tipico赔率> --stake 1.00
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
| Sochaux vs Dunkerque | 平局 + 小于 2.5 球 | 4.40 | **4.54** | 6.51 |
| Sochaux vs Dunkerque | 客胜 Dunkerque + 大于 2.5 球 | 4.54 | **4.68** | 5.88 |
| Sochaux vs Dunkerque | 客胜 Dunkerque + 小于 2.5 球 | 6.57 | **6.77** | 4.94 |
| Galatasaray vs Aston Villa | 平局 + 小于 2.5 球 | 6.74 | **6.95** | 11.69 |
| Galatasaray vs Aston Villa | 客胜 Aston Villa + 小于 2.5 球 | 9.09 | **9.36** | 6.64 |
| Galatasaray vs Aston Villa | 主胜 Galatasaray + 小于 2.5 球 | 11.64 | **11.99** | 9.25 |
| Como vs AEK | 主胜 Como + 小于 2.5 球 | 5.24 | **5.39** | 4.18 |
| Como vs AEK | 平局 + 小于 2.5 球 | 8.08 | **8.32** | 14.77 |
| Como vs AEK | 客胜 AEK + 大于 2.5 球 | 9.56 | **9.84** | 10.31 |
| Como vs AEK | 客胜 AEK + 小于 2.5 球 | 21.06 | **21.70** | 18.15 |
| Man City vs Napoli | 主胜 Man City + 小于 2.5 球 | 5.78 | **5.95** | 4.37 |
| Man City vs Napoli | 平局 + 小于 2.5 球 | 9.50 | **9.79** | 19.61 |
| Man City vs Napoli | 客胜 Napoli + 大于 2.5 球 | 13.29 | **13.69** | 13.01 |
| Man City vs Napoli | 客胜 Napoli + 小于 2.5 球 | 27.02 | **27.83** | 28.24 |
| RB Leipzig vs Lens | 主胜 RB Leipzig + 小于 2.5 球 | 6.58 | **6.78** | 5.07 |
| RB Leipzig vs Lens | 客胜 Lens + 大于 2.5 球 | 7.63 | **7.86** | 8.04 |
| RB Leipzig vs Lens | 平局 + 小于 2.5 球 | 9.15 | **9.43** | 17.41 |
| RB Leipzig vs Lens | 平局 + 大于 2.5 球 | 13.23 | **13.63** | 7.85 |

## 备注
- 从 the-odds-api 取到 9 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 9 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 442 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- ŠK Slovan Bratislava vs Betis：球队比赛数不够（门槛 min_team_matches），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。