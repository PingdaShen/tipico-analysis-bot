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
| 3 | Lens vs Sp Lisbon | 欧冠 | 10-13 18:45 | 主胜 Lens | 3.87 | **3.99** | 4.76* | €1.00 |
| 4 | RB Leipzig vs PSV Eindhoven | 欧冠 | 10-13 21:00 | 客胜 PSV Eindhoven | 4.48 | **4.61** | 5.04* | €1.00 |
| 5 | Galatasaray vs Barcelona | 欧冠 | 10-13 21:00 | 小于 2.5 球 | 4.15 | **4.27** | 4.48* | €1.00 |
| 6 | Arsenal vs Lille | 欧冠 | 10-13 21:00 | 小于 2.5 球 | 2.53 | **2.60** | 2.69* | €1.00 |
| 7 | Feyenoord vs Como | 欧冠 | 10-14 18:45 | 主胜 Feyenoord | 2.82 | **2.90** | 3.54* | €1.00 |
| 8 | Roma vs Real Madrid | 欧冠 | 10-14 21:00 | 小于 2.5 球 | 2.60 | **2.68** | 2.84* | €1.00 |
| 9 | Betis vs Porto | 欧冠 | 10-14 21:00 | 客胜 Porto | 3.25 | **3.35** | 3.44* | €1.00 |
| 10 | Shakhtar Donetsk vs AEK | 欧冠 | 10-14 21:00 | 小于 2.5 球 | 1.84 | **1.89** | 1.93* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Lens vs Sp Lisbon — 主胜 Lens**

```
20261013-CL-Lens-SpLisbon-H
```

**2. RB Leipzig vs PSV Eindhoven — 客胜 PSV Eindhoven**

```
20261013-CL-RBLeipzig-PSVEindhoven-A
```

**3. Cardiff vs Watford — 客胜 Watford**

```
20261013-E1-Cardiff-Watford-A
```

**4. Galatasaray vs Barcelona — 小于 2.5 球**

```
20261013-CL-Galatasaray-Barcelona-U25
```

**5. Arsenal vs Lille — 小于 2.5 球**

```
20261013-CL-Arsenal-Lille-U25
```

**6. Feyenoord vs Como — 主胜 Feyenoord**

```
20261014-CL-Feyenoord-Como-H
```

**7. Roma vs Real Madrid — 小于 2.5 球**

```
20261014-CL-Roma-RealMadrid-U25
```

**8. QPR vs Derby — 客胜 Derby**

```
20261014-E1-QPR-Derby-A
```

**9. Betis vs Porto — 客胜 Porto**

```
20261014-CL-Betis-Porto-A
```

**10. Shakhtar Donetsk vs AEK — 小于 2.5 球**

```
20261014-CL-ShakhtarDonetsk-AEK-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. **开球前几分钟**在 Actions 页面跑 **record-close**，填那一刻的市场赔率（有 Pinnacle 用 Pinnacle）。
   欧战和国家队没有收盘赔率源，不记就永远算不出 CLV，这些推荐也就无从检验。联赛不用管，收盘价会自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261013-CL-Lens-SpLisbon-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261013-CL-RBLeipzig-PSVEindhoven-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261013-E1-Cardiff-Watford-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261013-CL-Galatasaray-Barcelona-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261013-CL-Arsenal-Lille-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-Feyenoord-Como-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-Roma-RealMadrid-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-E1-QPR-Derby-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-Betis-Porto-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-ShakhtarDonetsk-AEK-U25 --odds <Tipico赔率> --stake 1.00
# 开球前：
python -m src.ledger close 20261013-CL-Lens-SpLisbon-H --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261013-CL-RBLeipzig-PSVEindhoven-A --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261013-CL-Galatasaray-Barcelona-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261013-CL-Arsenal-Lille-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-Feyenoord-Como-H --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-Roma-RealMadrid-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-Betis-Porto-A --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-ShakhtarDonetsk-AEK-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
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
| Lens vs Sp Lisbon | 平局 + 小于 2.5 球 | 5.30 | **5.46** | 8.24 |
| Lens vs Sp Lisbon | 主胜 Lens + 大于 2.5 球 | 6.09 | **6.27** | 7.12 |
| Lens vs Sp Lisbon | 主胜 Lens + 小于 2.5 球 | 10.66 | **10.98** | 8.50 |
| Arsenal vs Lille | 主胜 Arsenal + 小于 2.5 球 | 4.10 | **4.22** | 3.27 |
| Arsenal vs Lille | 平局 + 小于 2.5 球 | 8.31 | **8.55** | 16.21 |
| Arsenal vs Lille | 客胜 Lille + 大于 2.5 球 | 25.38 | **26.14** | 23.45 |
| Arsenal vs Lille | 客胜 Lille + 小于 2.5 球 | 32.11 | **33.07** | 35.84 |
| Galatasaray vs Barcelona | 客胜 Barcelona + 小于 2.5 球 | 7.81 | **8.04** | 5.90 |
| Galatasaray vs Barcelona | 主胜 Galatasaray + 大于 2.5 球 | 9.51 | **9.80** | 9.74 |
| Galatasaray vs Barcelona | 平局 + 小于 2.5 球 | 12.07 | **12.43** | 25.53 |
| Galatasaray vs Barcelona | 平局 + 大于 2.5 球 | 12.57 | **12.95** | 8.11 |
| RB Leipzig vs PSV Eindhoven | 客胜 PSV Eindhoven + 大于 2.5 球 | 5.57 | **5.74** | 5.92 |
| RB Leipzig vs PSV Eindhoven | 平局 + 大于 2.5 球 | 9.81 | **10.10** | 6.77 |
| RB Leipzig vs PSV Eindhoven | 平局 + 小于 2.5 球 | 10.74 | **11.06** | 21.09 |
| RB Leipzig vs PSV Eindhoven | 客胜 PSV Eindhoven + 小于 2.5 球 | 22.76 | **23.44** | 18.43 |
| Feyenoord vs Como | 主胜 Feyenoord + 大于 2.5 球 | 3.76 | **3.87** | 4.36 |
| Feyenoord vs Como | 平局 + 小于 2.5 球 | 7.19 | **7.40** | 12.59 |
| Feyenoord vs Como | 主胜 Feyenoord + 小于 2.5 球 | 11.24 | **11.57** | 7.97 |
| Shakhtar Donetsk vs AEK | 平局 + 小于 2.5 球 | 4.21 | **4.33** | 6.26 |
| Shakhtar Donetsk vs AEK | 主胜 Shakhtar Donetsk + 小于 2.5 球 | 6.45 | **6.64** | 5.02 |
| Shakhtar Donetsk vs AEK | 客胜 AEK + 小于 2.5 球 | 6.61 | **6.81** | 5.41 |
| Roma vs Real Madrid | 平局 + 小于 2.5 球 | 6.23 | **6.41** | 10.61 |
| Roma vs Real Madrid | 客胜 Real Madrid + 小于 2.5 球 | 7.14 | **7.36** | 5.31 |
| Roma vs Real Madrid | 主胜 Roma + 小于 2.5 球 | 11.96 | **12.32** | 9.83 |
| Betis vs Porto | 平局 + 小于 2.5 球 | 5.11 | **5.26** | 7.88 |
| Betis vs Porto | 客胜 Porto + 大于 2.5 球 | 5.31 | **5.47** | 6.31 |
| Betis vs Porto | 客胜 Porto + 小于 2.5 球 | 8.38 | **8.63** | 6.70 |

## 备注
- 从 the-odds-api 取到 18 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 16 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 211 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- Sabah FK vs Slavia Praha：球队比赛数不够（门槛 min_team_matches），跳过
- ŠK Slovan Bratislava vs Stuttgart：球队比赛数不够（门槛 min_team_matches），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。