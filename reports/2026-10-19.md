# 投注建议 · 2026-10-19

覆盖 10-19 至 10-20 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 14 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Monza vs Cagliari | 意甲 | 10-19 18:30 | 客胜 Cagliari | 2.71 | **2.79** | 3.04* | €1.00 |
| 2 | Celta B vs Tenerife | 西乙 | 10-19 20:30 | 主胜 Celta B | 2.39 | **2.46** | 2.51* | €1.00 |
| 3 | Rodez vs Montpellier | 法乙 | 10-19 20:45 | 小于 2.5 球 | 2.05 | **2.11** | 2.15* | €1.00 |

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 4 | Man City vs AEK | 欧冠 | 10-20 21:00 | 小于 2.5 球 | 3.52 | **3.62** | 3.94* | €1.00 |
| 5 | Paris SG vs Barcelona | 欧冠 | 10-20 21:00 | 小于 2.5 球 | 4.38 | **4.51** | 4.87* | €1.00 |
| 6 | Napoli vs Bodo/Glimt | 欧冠 | 10-20 21:00 | 客胜 Bodo/Glimt | 4.63 | **4.77** | 4.95* | €1.00 |
| 7 | Porto vs PSV Eindhoven | 欧冠 | 10-20 21:00 | 客胜 PSV Eindhoven | 4.73 | **4.88** | 5.02* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Monza vs Cagliari — 客胜 Cagliari**

```
20261019-I1-Monza-Cagliari-A
```

**2. Celta B vs Tenerife — 主胜 Celta B**

```
20261019-SP2-CeltaB-Tenerife-H
```

**3. Rodez vs Montpellier — 小于 2.5 球**

```
20261019-F2-Rodez-Montpellier-U25
```

**4. Man City vs AEK — 小于 2.5 球**

```
20261020-CL-ManCity-AEK-U25
```

**5. Paris SG vs Barcelona — 小于 2.5 球**

```
20261020-CL-ParisSG-Barcelona-U25
```

**6. Napoli vs Bodo/Glimt — 客胜 Bodo/Glimt**

```
20261020-CL-Napoli-BodoGlimt-A
```

**7. Porto vs PSV Eindhoven — 客胜 PSV Eindhoven**

```
20261020-CL-Porto-PSVEindhoven-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261019-I1-Monza-Cagliari-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261019-SP2-CeltaB-Tenerife-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261019-F2-Rodez-Montpellier-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261020-CL-ManCity-AEK-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261020-CL-ParisSG-Barcelona-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261020-CL-Napoli-BodoGlimt-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261020-CL-Porto-PSVEindhoven-A --odds <Tipico赔率> --stake 1.00
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
| Rodez vs Montpellier | 平局 + 小于 2.5 球 | 4.71 | **4.85** | 7.24 |
| Rodez vs Montpellier | 客胜 Montpellier + 小于 2.5 球 | 6.86 | **7.07** | 5.29 |
| Rodez vs Montpellier | 主胜 Rodez + 小于 2.5 球 | 7.71 | **7.94** | 6.23 |
| Monza vs Cagliari | 客胜 Cagliari + 大于 2.5 球 | 4.60 | **4.74** | 5.76 |
| Monza vs Cagliari | 客胜 Cagliari + 小于 2.5 球 | 6.61 | **6.81** | 5.12 |
| Celta B vs Tenerife | 主胜 Celta B + 大于 2.5 球 | 3.94 | **4.06** | 4.86 |
| Celta B vs Tenerife | 主胜 Celta B + 小于 2.5 球 | 6.05 | **6.23** | 4.69 |
| Man City vs AEK | 主胜 Man City + 小于 2.5 球 | 5.06 | **5.21** | 4.12 |
| Man City vs AEK | 平局 + 小于 2.5 球 | 14.63 | **15.07** | 36.02 |
| Man City vs AEK | 客胜 AEK + 大于 2.5 球 | 32.91 | **33.89** | 28.71 |
| Man City vs AEK | 平局 + 大于 2.5 球 | 34.12 | **35.14** | 14.31 |
| Paris SG vs Barcelona | 主胜 Paris SG + 大于 2.5 球 | 2.83 | **2.91** | 3.08 |
| Paris SG vs Barcelona | 平局 + 小于 2.5 球 | 10.17 | **10.48** | 19.69 |
| Paris SG vs Barcelona | 主胜 Paris SG + 小于 2.5 球 | 14.92 | **15.36** | 10.41 |
| Paris SG vs Barcelona | 客胜 Barcelona + 小于 2.5 球 | 15.86 | **16.33** | 12.26 |
| Napoli vs Bodo/Glimt | 客胜 Bodo/Glimt + 大于 2.5 球 | 6.83 | **7.04** | 7.46 |
| Napoli vs Bodo/Glimt | 平局 + 小于 2.5 球 | 6.91 | **7.12** | 11.86 |
| Napoli vs Bodo/Glimt | 客胜 Bodo/Glimt + 小于 2.5 球 | 14.32 | **14.75** | 12.17 |
| Porto vs PSV Eindhoven | 平局 + 小于 2.5 球 | 6.93 | **7.13** | 11.85 |
| Porto vs PSV Eindhoven | 客胜 PSV Eindhoven + 大于 2.5 球 | 7.06 | **7.27** | 7.64 |
| Porto vs PSV Eindhoven | 平局 + 大于 2.5 球 | 12.95 | **13.34** | 7.29 |
| Porto vs PSV Eindhoven | 客胜 PSV Eindhoven + 小于 2.5 球 | 14.37 | **14.80** | 12.43 |

## 备注
- Tottenham vs Coventry：球队数据不足（可能是升班马），跳过
- 从 the-odds-api 取到 9 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 9 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 169 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- Fenerbahce vs Slavia Praha：球队比赛数不够（门槛 min_team_matches），跳过
- Roma vs ŠK Slovan Bratislava：球队比赛数不够（门槛 min_team_matches），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。