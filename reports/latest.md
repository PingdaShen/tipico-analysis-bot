# 投注建议 · 2026-11-05

覆盖 11-05 至 11-06 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 20 场比赛

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Celtic vs Besiktas | 欧联 | 11-05 21:00 | 主胜 Celtic | 2.34 | **2.41** | 2.94* | €1.00 |
| 2 | St Truiden vs Brann | 欧协联 | 11-05 21:00 | 客胜 Brann | 3.88 | **4.00** | 4.80* | €1.00 |
| 3 | KuPS vs Gent | 欧协联 | 11-05 18:45 | 主胜 KuPS | 4.52 | **4.66** | 5.25* | €1.00 |
| 4 | Atalanta vs FK Kairat | 欧协联 | 11-05 18:45 | 小于 2.5 球 | 3.13 | **3.23** | 3.59* | €1.00 |
| 5 | Sociedad vs Lyon | 欧联 | 11-05 18:45 | 客胜 Lyon | 4.41 | **4.55** | 4.88* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Celtic vs Besiktas — 主胜 Celtic**

```
20261105-EL-Celtic-Besiktas-H
```

**2. St Truiden vs Brann — 客胜 Brann**

```
20261105-UECL-StTruiden-Brann-A
```

**3. KuPS vs Gent — 主胜 KuPS**

```
20261105-UECL-KuPS-Gent-H
```

**4. Atalanta vs FK Kairat — 小于 2.5 球**

```
20261105-UECL-Atalanta-FKKairat-U25
```

**5. Sociedad vs Lyon — 客胜 Lyon**

```
20261105-EL-Sociedad-Lyon-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261105-EL-Celtic-Besiktas-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261105-UECL-StTruiden-Brann-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261105-UECL-KuPS-Gent-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261105-UECL-Atalanta-FKKairat-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261105-EL-Sociedad-Lyon-A --odds <Tipico赔率> --stake 1.00
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
| Sociedad vs Lyon | 客胜 Lyon + 大于 2.5 球 | 6.54 | **6.74** | 7.31 |
| Sociedad vs Lyon | 平局 + 小于 2.5 球 | 6.63 | **6.83** | 11.19 |
| Sociedad vs Lyon | 客胜 Lyon + 小于 2.5 球 | 13.55 | **13.96** | 11.15 |
| Celtic vs Besiktas | 主胜 Celtic + 大于 2.5 球 | 3.24 | **3.34** | 3.91 |
| Celtic vs Besiktas | 主胜 Celtic + 小于 2.5 球 | 8.38 | **8.64** | 5.80 |
| Atalanta vs FK Kairat | 主胜 Atalanta + 小于 2.5 球 | 4.66 | **4.80** | 3.79 |
| Atalanta vs FK Kairat | 平局 + 小于 2.5 球 | 12.11 | **12.47** | 27.15 |
| Atalanta vs FK Kairat | 客胜 FK Kairat + 大于 2.5 球 | 27.93 | **28.76** | 25.50 |
| Atalanta vs FK Kairat | 平局 + 大于 2.5 球 | 30.41 | **31.32** | 12.72 |
| KuPS vs Gent | 平局 + 小于 2.5 球 | 5.11 | **5.26** | 7.70 |
| KuPS vs Gent | 主胜 KuPS + 大于 2.5 球 | 8.24 | **8.49** | 9.48 |
| KuPS vs Gent | 主胜 KuPS + 小于 2.5 球 | 10.02 | **10.33** | 8.65 |
| KuPS vs Gent | 平局 + 大于 2.5 球 | 19.02 | **19.59** | 8.45 |
| St Truiden vs Brann | 客胜 Brann + 大于 2.5 球 | 5.21 | **5.36** | 5.81 |
| St Truiden vs Brann | 平局 + 小于 2.5 球 | 7.60 | **7.83** | 13.49 |
| St Truiden vs Brann | 客胜 Brann + 小于 2.5 球 | 15.27 | **15.73** | 11.71 |

## 备注
- 赛程源里没有 11-05 起 2 天内的联赛比赛。fixtures.csv 最新的一场是 2026-11-04（已经是 1 天前），只覆盖 4 个联赛：B1、E1、E2、E3。football-data.co.uk 的赛程是周五下午发布周末场次、周二下午发布周中场次，国际比赛周没有联赛可发就不会更新。等不及可以用 manual_fixtures.csv 手填。
- 从 the-odds-api 取到 35 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 28 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 478 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- 手填赛程里的球队「Ferencváros TC」模型不认识，可能是「Ferencvárosi TC」，这场跳过。
- 手填赛程里的球队「Sparta Prague」模型不认识，可能是「AC Sparta Praha、Spartak Trnava、Slavia Prag」，这场跳过。
- 手填赛程里的球队「PFC Levski Sofia」模型不认识，可能是「Levski Sofia」，这场跳过。
- 手填赛程里的球队「Omonoia FC」模型不认识，可能是「Monza、Concordia、FK Mornar」，这场跳过。
- Sunderland vs Dinamo Zagreb：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「Torreense」模型不认识，可能是「Moreirense、Odense、Horsens」，这场跳过。
- Hapoel Be'er Sheva vs OFI Crete：球队比赛数不够（门槛 min_team_matches），跳过
- Lincoln Red Imps vs Hajduk Split：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「Red Star Belgrade」模型不认识，可能是「Red Star」，这场跳过。
- FC Copenhagen vs FC Iberia 1999：球队比赛数不够（门槛 min_team_matches），跳过
- Lugano vs Kauno Žalgiris：球队比赛数不够（门槛 min_team_matches），跳过
- Twente vs Pafos FC：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「FK Jablonec」模型不认识，可能是「Boulogne」，这场跳过。
- 手填赛程里的球队「KF Egnatia」模型不认识，可能是「KF Tiranë、Fiorentina」，这场跳过。
- 手填赛程里的球队「PFC CSKA Sofia」模型不认识，可能是「CSKA 1948 Sofia、Levski Sofia」，这场跳过。

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。