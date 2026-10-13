# 投注建议 · 2026-10-13

覆盖 10-13 至 10-14 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 29 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Cardiff vs Watford | 英冠 | 10-13 20:45 | 客胜 Watford | 4.11 | **4.23** | 4.51* | €1.00 |
| 2 | QPR vs Derby | 英冠 | 10-14 20:45 | 客胜 Derby | 4.19 | **4.31** | 4.57* | €1.00 |

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 3 | RB Leipzig vs PSV Eindhoven | 欧冠 | 10-13 20:00 | 客胜 PSV Eindhoven | 4.26 | **4.39** | 4.67* | €1.00 |
| 4 | Galatasaray vs Barcelona | 欧冠 | 10-13 20:00 | 小于 2.5 球 | 4.21 | **4.34** | 4.61* | €1.00 |
| 5 | Arsenal vs Lille | 欧冠 | 10-13 20:00 | 小于 2.5 球 | 2.47 | **2.54** | 2.58* | €1.00 |
| 6 | Feyenoord vs Como | 欧冠 | 10-14 17:45 | 主胜 Feyenoord | 2.79 | **2.87** | 3.52* | €1.00 |
| 7 | Roma vs Real Madrid | 欧冠 | 10-14 20:00 | 小于 2.5 球 | 2.60 | **2.68** | 2.84* | €1.00 |
| 8 | Shakhtar Donetsk vs AEK | 欧冠 | 10-14 20:00 | 小于 2.5 球 | 1.84 | **1.89** | 1.95* | €1.00 |
| 9 | Betis vs Porto | 欧冠 | 10-14 20:00 | 客胜 Porto | 3.25 | **3.35** | 3.42* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Cardiff vs Watford — 客胜 Watford**

```
20261013-E1-Cardiff-Watford-A
```

**2. RB Leipzig vs PSV Eindhoven — 客胜 PSV Eindhoven**

```
20261013-CL-RBLeipzig-PSVEindhoven-A
```

**3. Galatasaray vs Barcelona — 小于 2.5 球**

```
20261013-CL-Galatasaray-Barcelona-U25
```

**4. Arsenal vs Lille — 小于 2.5 球**

```
20261013-CL-Arsenal-Lille-U25
```

**5. Feyenoord vs Como — 主胜 Feyenoord**

```
20261014-CL-Feyenoord-Como-H
```

**6. Roma vs Real Madrid — 小于 2.5 球**

```
20261014-CL-Roma-RealMadrid-U25
```

**7. QPR vs Derby — 客胜 Derby**

```
20261014-E1-QPR-Derby-A
```

**8. Shakhtar Donetsk vs AEK — 小于 2.5 球**

```
20261014-CL-ShakhtarDonetsk-AEK-U25
```

**9. Betis vs Porto — 客胜 Porto**

```
20261014-CL-Betis-Porto-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. **开球前几分钟**在 Actions 页面跑 **record-close**，填那一刻的市场赔率（有 Pinnacle 用 Pinnacle）。
   欧战和国家队没有收盘赔率源，不记就永远算不出 CLV，这些推荐也就无从检验。联赛不用管，收盘价会自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261013-E1-Cardiff-Watford-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261013-CL-RBLeipzig-PSVEindhoven-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261013-CL-Galatasaray-Barcelona-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261013-CL-Arsenal-Lille-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-Feyenoord-Como-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-Roma-RealMadrid-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-E1-QPR-Derby-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-ShakhtarDonetsk-AEK-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-Betis-Porto-A --odds <Tipico赔率> --stake 1.00
# 开球前：
python -m src.ledger close 20261013-CL-RBLeipzig-PSVEindhoven-A --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261013-CL-Galatasaray-Barcelona-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261013-CL-Arsenal-Lille-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-Feyenoord-Como-H --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-Roma-RealMadrid-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-ShakhtarDonetsk-AEK-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-Betis-Porto-A --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
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
| Cardiff vs Watford | 平局 + 小于 2.5 球 | 5.89 | **6.07** | 9.84 |
| Cardiff vs Watford | 主胜 Cardiff + 小于 2.5 球 | 5.90 | **6.08** | 4.60 |
| Cardiff vs Watford | 客胜 Watford + 大于 2.5 球 | 6.22 | **6.40** | 7.11 |
| Cardiff vs Watford | 客胜 Watford + 小于 2.5 球 | 12.14 | **12.50** | 9.75 |
| QPR vs Derby | 平局 + 小于 2.5 球 | 5.20 | **5.35** | 8.07 |
| QPR vs Derby | 客胜 Derby + 大于 2.5 球 | 7.00 | **7.21** | 8.13 |
| QPR vs Derby | 客胜 Derby + 小于 2.5 球 | 10.43 | **10.74** | 8.65 |
| QPR vs Derby | 平局 + 大于 2.5 球 | 15.78 | **16.25** | 7.59 |
| Arsenal vs Lille | 主胜 Arsenal + 小于 2.5 球 | 4.00 | **4.12** | 3.21 |
| Arsenal vs Lille | 平局 + 小于 2.5 球 | 8.24 | **8.49** | 15.86 |
| Arsenal vs Lille | 客胜 Lille + 大于 2.5 球 | 24.44 | **25.18** | 22.51 |
| Arsenal vs Lille | 客胜 Lille + 小于 2.5 球 | 29.67 | **30.56** | 33.11 |
| Galatasaray vs Barcelona | 客胜 Barcelona + 小于 2.5 球 | 8.19 | **8.43** | 6.11 |
| Galatasaray vs Barcelona | 主胜 Galatasaray + 大于 2.5 球 | 8.91 | **9.18** | 9.15 |
| Galatasaray vs Barcelona | 平局 + 小于 2.5 球 | 11.88 | **12.24** | 25.11 |
| Galatasaray vs Barcelona | 平局 + 大于 2.5 球 | 11.96 | **12.32** | 7.82 |
| RB Leipzig vs PSV Eindhoven | 客胜 PSV Eindhoven + 大于 2.5 球 | 5.33 | **5.49** | 5.67 |
| RB Leipzig vs PSV Eindhoven | 平局 + 大于 2.5 球 | 9.59 | **9.88** | 6.61 |
| RB Leipzig vs PSV Eindhoven | 平局 + 小于 2.5 球 | 10.31 | **10.62** | 20.04 |
| RB Leipzig vs PSV Eindhoven | 客胜 PSV Eindhoven + 小于 2.5 球 | 21.37 | **22.01** | 17.19 |
| Feyenoord vs Como | 主胜 Feyenoord + 大于 2.5 球 | 3.74 | **3.85** | 4.34 |
| Feyenoord vs Como | 平局 + 小于 2.5 球 | 7.07 | **7.28** | 12.33 |
| Feyenoord vs Como | 主胜 Feyenoord + 小于 2.5 球 | 11.03 | **11.36** | 7.82 |
| Shakhtar Donetsk vs AEK | 平局 + 小于 2.5 球 | 4.21 | **4.33** | 6.26 |
| Shakhtar Donetsk vs AEK | 主胜 Shakhtar Donetsk + 小于 2.5 球 | 6.45 | **6.64** | 5.02 |
| Shakhtar Donetsk vs AEK | 客胜 AEK + 小于 2.5 球 | 6.61 | **6.81** | 5.41 |
| Roma vs Real Madrid | 平局 + 小于 2.5 球 | 6.22 | **6.41** | 10.61 |
| Roma vs Real Madrid | 客胜 Real Madrid + 小于 2.5 球 | 7.16 | **7.38** | 5.33 |
| Roma vs Real Madrid | 主胜 Roma + 小于 2.5 球 | 11.91 | **12.27** | 9.79 |
| Betis vs Porto | 平局 + 小于 2.5 球 | 5.11 | **5.26** | 7.88 |
| Betis vs Porto | 客胜 Porto + 大于 2.5 球 | 5.31 | **5.47** | 6.32 |
| Betis vs Porto | 客胜 Porto + 小于 2.5 球 | 8.39 | **8.64** | 6.71 |

## 欧冠赛程（还没有赔率）

赛程来自 openligadb，但它没有赔率——没有市场锚就算不出最低赔率，
所以这些**还不是推荐**。下面是模型自己的概率（未与市场融合），
用来判断哪几场值得去查赔率。要让某场进入推荐，把赔率填进去：

```bash
python -m src.manual add --comp CL --date <YYYY-MM-DD> \
    --home <主队> --away <客队> \
    --ref-h <参考主胜> --ref-d <参考平> --ref-a <参考客胜> \
    --tip-h <Tipico主胜> --tip-d <Tipico平> --tip-a <Tipico客胜>
```

| 日期 | 时间 | 比赛 | 模型主胜 | 平 | 客胜 | 模型小于 2.5 |
|---|---|---|---|---|---|---|
| 10-14 | 20:00 | Slovan Bratislava vs Stuttgart | 28% | 23% | 49% | 35% |

## 备注
- 从 the-odds-api 取到 18 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 17 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- Sabah FK vs Slavia Praha：球队比赛数不够（门槛 min_team_matches），跳过
- ŠK Slovan Bratislava vs Stuttgart：球队比赛数不够（门槛 min_team_matches），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。