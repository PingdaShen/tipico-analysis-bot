# 投注建议 · 2026-11-03

覆盖 11-03 至 11-04 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 31 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Northampton vs Oldham | 英乙 | 11-03 20:45 | 小于 2.5 球 | 1.55 | **1.60** | 1.67* | €1.00 |
| 2 | QPR vs Burnley | 英冠 | 11-03 20:45 | 客胜 Burnley | 3.26 | **3.36** | 3.48* | €1.00 |
| 3 | Derby vs Norwich | 英冠 | 11-03 20:45 | 主胜 Derby | 3.25 | **3.34** | 3.38* | €1.00 |
| 4 | Wrexham vs Middlesbrough | 英冠 | 11-04 20:45 | 主胜 Wrexham | 3.84 | **3.95** | 4.07* | €1.00 |

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 5 | Barcelona vs Aston Villa | 欧冠 | 11-03 21:00 | 小于 2.5 球 | 4.40 | **4.54** | 4.89* | €1.00 |
| 6 | Shakhtar Donetsk vs Sp Lisbon | 欧冠 | 11-03 18:45 | 小于 2.5 球 | 2.08 | **2.14** | 2.17* | €1.00 |
| 7 | Lens vs Como | 欧冠 | 11-04 21:00 | 主胜 Lens | 2.66 | **2.74** | 3.04* | €1.00 |
| 8 | AEK vs Real Madrid | 欧冠 | 11-04 18:45 | 小于 2.5 球 | 3.08 | **3.17** | 3.44* | €1.00 |
| 9 | Porto vs Napoli | 欧冠 | 11-04 21:00 | 小于 2.5 球 | 2.02 | **2.08** | 2.11* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Barcelona vs Aston Villa — 小于 2.5 球**

```
20261103-CL-Barcelona-AstonVilla-U25
```

**2. Northampton vs Oldham — 小于 2.5 球**

```
20261103-E3-Northampton-Oldham-U25
```

**3. QPR vs Burnley — 客胜 Burnley**

```
20261103-E1-QPR-Burnley-A
```

**4. Shakhtar Donetsk vs Sp Lisbon — 小于 2.5 球**

```
20261103-CL-ShakhtarDonetsk-SpLisbon-U25
```

**5. Derby vs Norwich — 主胜 Derby**

```
20261103-E1-Derby-Norwich-H
```

**6. Lens vs Como — 主胜 Lens**

```
20261104-CL-Lens-Como-H
```

**7. AEK vs Real Madrid — 小于 2.5 球**

```
20261104-CL-AEK-RealMadrid-U25
```

**8. Wrexham vs Middlesbrough — 主胜 Wrexham**

```
20261104-E1-Wrexham-Middlesbrough-H
```

**9. Porto vs Napoli — 小于 2.5 球**

```
20261104-CL-Porto-Napoli-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261103-CL-Barcelona-AstonVilla-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261103-E3-Northampton-Oldham-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261103-E1-QPR-Burnley-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261103-CL-ShakhtarDonetsk-SpLisbon-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261103-E1-Derby-Norwich-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261104-CL-Lens-Como-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261104-CL-AEK-RealMadrid-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261104-E1-Wrexham-Middlesbrough-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261104-CL-Porto-Napoli-U25 --odds <Tipico赔率> --stake 1.00
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
| Derby vs Norwich | 主胜 Derby + 大于 2.5 球 | 5.00 | **5.15** | 5.81 |
| Derby vs Norwich | 平局 + 小于 2.5 球 | 5.59 | **5.76** | 8.83 |
| Derby vs Norwich | 主胜 Derby + 小于 2.5 球 | 9.25 | **9.53** | 7.37 |
| QPR vs Burnley | 客胜 Burnley + 大于 2.5 球 | 5.09 | **5.24** | 5.99 |
| QPR vs Burnley | 平局 + 小于 2.5 球 | 5.36 | **5.52** | 8.40 |
| QPR vs Burnley | 客胜 Burnley + 小于 2.5 球 | 9.08 | **9.35** | 7.16 |
| Wrexham vs Middlesbrough | 主胜 Wrexham + 大于 2.5 球 | 5.85 | **6.03** | 6.61 |
| Wrexham vs Middlesbrough | 平局 + 小于 2.5 球 | 6.04 | **6.23** | 9.79 |
| Wrexham vs Middlesbrough | 主胜 Wrexham + 小于 2.5 球 | 11.15 | **11.48** | 9.15 |
| Wrexham vs Middlesbrough | 平局 + 大于 2.5 球 | 12.78 | **13.16** | 7.07 |
| Northampton vs Oldham | 平局 + 小于 2.5 球 | 3.45 | **3.55** | 4.83 |
| Northampton vs Oldham | 主胜 Northampton + 小于 2.5 球 | 5.14 | **5.29** | 4.17 |
| Northampton vs Oldham | 客胜 Oldham + 小于 2.5 球 | 6.23 | **6.42** | 5.05 |
| Shakhtar Donetsk vs Sp Lisbon | 平局 + 小于 2.5 球 | 5.04 | **5.19** | 7.83 |
| Shakhtar Donetsk vs Sp Lisbon | 客胜 Sp Lisbon + 小于 2.5 球 | 5.89 | **6.07** | 4.66 |
| Shakhtar Donetsk vs Sp Lisbon | 主胜 Shakhtar Donetsk + 小于 2.5 球 | 8.85 | **9.11** | 7.20 |
| Barcelona vs Aston Villa | 主胜 Barcelona + 小于 2.5 球 | 8.35 | **8.60** | 6.33 |
| Barcelona vs Aston Villa | 客胜 Aston Villa + 大于 2.5 球 | 8.60 | **8.85** | 8.82 |
| Barcelona vs Aston Villa | 平局 + 大于 2.5 球 | 12.34 | **12.71** | 8.19 |
| Barcelona vs Aston Villa | 平局 + 小于 2.5 球 | 13.00 | **13.39** | 27.89 |
| AEK vs Real Madrid | 客胜 Real Madrid + 小于 2.5 球 | 5.45 | **5.62** | 4.26 |
| AEK vs Real Madrid | 平局 + 小于 2.5 球 | 9.57 | **9.86** | 19.09 |
| AEK vs Real Madrid | 主胜 AEK + 大于 2.5 球 | 12.66 | **13.04** | 12.76 |
| AEK vs Real Madrid | 平局 + 大于 2.5 球 | 17.63 | **18.16** | 9.19 |
| Lens vs Como | 主胜 Lens + 大于 2.5 球 | 3.83 | **3.94** | 4.58 |
| Lens vs Como | 平局 + 小于 2.5 球 | 5.86 | **6.03** | 9.70 |
| Lens vs Como | 主胜 Lens + 小于 2.5 球 | 8.74 | **9.00** | 6.35 |
| Porto vs Napoli | 平局 + 小于 2.5 球 | 5.01 | **5.17** | 7.77 |
| Porto vs Napoli | 主胜 Porto + 小于 2.5 球 | 5.30 | **5.46** | 4.16 |
| Porto vs Napoli | 客胜 Napoli + 小于 2.5 球 | 9.33 | **9.61** | 7.92 |

## 备注
- Kortrijk vs KV Mechelen：球队数据不足（可能是升班马），跳过
- Preston vs Sheffield Utd：球队数据不足（可能是升班马），跳过
- Oxford Utd vs Reading：球队数据不足（可能是升班马），跳过
- 从 the-odds-api 取到 19 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 19 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 490 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- LASK vs ŠK Slovan Bratislava：球队比赛数不够（门槛 min_team_matches），跳过
- Slavia Praha vs Arsenal：球队比赛数不够（门槛 min_team_matches），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。