# 投注建议 · 2026-11-02

覆盖 11-02 至 11-03 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 23 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Kalamata vs Iraklis | 希超 | 11-02 18:30 | 大于 2.5 球 | 1.93 | **1.99** | 2.10* | €1.00 |
| 2 | Mallorca vs Cadiz | 西乙 | 11-02 21:00 | 小于 2.5 球 | 1.77 | **1.82** | 1.84* | €1.00 |
| 3 | Atalanta vs Parma | 意甲 | 11-02 20:45 | 小于 2.5 球 | 2.15 | **2.22** | 2.23* | €1.00 |

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 4 | Barcelona vs Aston Villa | 欧冠 | 11-03 21:00 | 小于 2.5 球 | 4.16 | **4.28** | 4.52* | €1.00 |
| 5 | Shakhtar Donetsk vs Sp Lisbon | 欧冠 | 11-03 18:45 | 小于 2.5 球 | 2.08 | **2.14** | 2.17* | €1.00 |
| 6 | Villarreal vs Paris SG | 欧冠 | 11-03 21:00 | 主胜 Villarreal | 4.72 | **4.86** | 4.91* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Kalamata vs Iraklis — 大于 2.5 球**

```
20261102-G1-Kalamata-Iraklis-O25
```

**2. Mallorca vs Cadiz — 小于 2.5 球**

```
20261102-SP2-Mallorca-Cadiz-U25
```

**3. Atalanta vs Parma — 小于 2.5 球**

```
20261102-I1-Atalanta-Parma-U25
```

**4. Barcelona vs Aston Villa — 小于 2.5 球**

```
20261103-CL-Barcelona-AstonVilla-U25
```

**5. Shakhtar Donetsk vs Sp Lisbon — 小于 2.5 球**

```
20261103-CL-ShakhtarDonetsk-SpLisbon-U25
```

**6. Villarreal vs Paris SG — 主胜 Villarreal**

```
20261103-CL-Villarreal-ParisSG-H
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261102-G1-Kalamata-Iraklis-O25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261102-SP2-Mallorca-Cadiz-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261102-I1-Atalanta-Parma-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261103-CL-Barcelona-AstonVilla-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261103-CL-ShakhtarDonetsk-SpLisbon-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261103-CL-Villarreal-ParisSG-H --odds <Tipico赔率> --stake 1.00
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
| Kalamata vs Iraklis | 主胜 Kalamata + 大于 2.5 球 | 3.75 | **3.86** | 4.55 |
| Kalamata vs Iraklis | 客胜 Iraklis + 大于 2.5 球 | 5.45 | **5.61** | 6.48 |
| Kalamata vs Iraklis | 平局 + 大于 2.5 球 | 14.97 | **15.42** | 7.00 |
| Atalanta vs Parma | 主胜 Atalanta + 小于 2.5 球 | 4.43 | **4.56** | 3.40 |
| Atalanta vs Parma | 平局 + 小于 2.5 球 | 5.94 | **6.11** | 9.97 |
| Atalanta vs Parma | 客胜 Parma + 小于 2.5 球 | 14.27 | **14.70** | 14.35 |
| Mallorca vs Cadiz | 主胜 Mallorca + 小于 2.5 球 | 3.64 | **3.75** | 2.81 |
| Mallorca vs Cadiz | 平局 + 小于 2.5 球 | 4.72 | **4.86** | 7.44 |
| Shakhtar Donetsk vs Sp Lisbon | 平局 + 小于 2.5 球 | 5.11 | **5.26** | 7.95 |
| Shakhtar Donetsk vs Sp Lisbon | 客胜 Sp Lisbon + 小于 2.5 球 | 5.76 | **5.93** | 4.58 |
| Shakhtar Donetsk vs Sp Lisbon | 主胜 Shakhtar Donetsk + 小于 2.5 球 | 8.93 | **9.20** | 7.30 |
| Barcelona vs Aston Villa | 主胜 Barcelona + 小于 2.5 球 | 7.66 | **7.89** | 5.89 |
| Barcelona vs Aston Villa | 客胜 Aston Villa + 大于 2.5 球 | 9.24 | **9.52** | 9.47 |
| Barcelona vs Aston Villa | 平局 + 小于 2.5 球 | 12.66 | **13.04** | 26.79 |
| Barcelona vs Aston Villa | 平局 + 大于 2.5 球 | 13.11 | **13.51** | 8.48 |
| Villarreal vs Paris SG | 主胜 Villarreal + 大于 2.5 球 | 6.35 | **6.54** | 6.74 |
| Villarreal vs Paris SG | 客胜 Paris SG + 小于 2.5 球 | 7.71 | **7.94** | 5.73 |
| Villarreal vs Paris SG | 平局 + 小于 2.5 球 | 8.63 | **8.89** | 16.13 |
| Villarreal vs Paris SG | 主胜 Villarreal + 小于 2.5 球 | 18.37 | **18.93** | 15.74 |

## 备注
- 从 the-odds-api 取到 9 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 9 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 496 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- LASK vs ŠK Slovan Bratislava：球队比赛数不够（门槛 min_team_matches），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。