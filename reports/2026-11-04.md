# 投注建议 · 2026-11-04

覆盖 11-04 至 11-05 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 32 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Wrexham vs Middlesbrough | 英冠 | 11-04 20:45 | 主胜 Wrexham | 3.84 | **3.95** | 4.07* | €1.00 |

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 2 | Lens vs Como | 欧冠 | 11-04 21:00 | 主胜 Lens | 2.95 | **3.04** | 3.67* | €1.00 |
| 3 | AEK vs Real Madrid | 欧冠 | 11-04 18:45 | 小于 2.5 球 | 3.18 | **3.28** | 3.64* | €1.00 |
| 4 | RB Leipzig vs Man City | 欧冠 | 11-04 21:00 | 小于 2.5 球 | 3.46 | **3.57** | 3.60* | €1.00 |
| 5 | Celtic vs Besiktas | 欧联 | 11-05 21:00 | 主胜 Celtic | 2.36 | **2.43** | 3.05* | €1.00 |
| 6 | St Truiden vs Brann | 欧协联 | 11-05 21:00 | 客胜 Brann | 3.81 | **3.92** | 4.39* | €1.00 |
| 7 | KuPS vs Gent | 欧协联 | 11-05 18:45 | 主胜 KuPS | 4.48 | **4.61** | 5.03* | €1.00 |
| 8 | Benfica vs Lech Poznan | 欧联 | 11-05 21:00 | 小于 2.5 球 | 3.31 | **3.41** | 3.54* | €1.00 |
| 9 | Atalanta vs FK Kairat | 欧协联 | 11-05 18:45 | 小于 2.5 球 | 2.75 | **2.84** | 2.93* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Lens vs Como — 主胜 Lens**

```
20261104-CL-Lens-Como-H
```

**2. AEK vs Real Madrid — 小于 2.5 球**

```
20261104-CL-AEK-RealMadrid-U25
```

**3. Wrexham vs Middlesbrough — 主胜 Wrexham**

```
20261104-E1-Wrexham-Middlesbrough-H
```

**4. RB Leipzig vs Man City — 小于 2.5 球**

```
20261104-CL-RBLeipzig-ManCity-U25
```

**5. Celtic vs Besiktas — 主胜 Celtic**

```
20261105-EL-Celtic-Besiktas-H
```

**6. St Truiden vs Brann — 客胜 Brann**

```
20261105-UECL-StTruiden-Brann-A
```

**7. KuPS vs Gent — 主胜 KuPS**

```
20261105-UECL-KuPS-Gent-H
```

**8. Benfica vs Lech Poznan — 小于 2.5 球**

```
20261105-EL-Benfica-LechPoznan-U25
```

**9. Atalanta vs FK Kairat — 小于 2.5 球**

```
20261105-UECL-Atalanta-FKKairat-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261104-CL-Lens-Como-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261104-CL-AEK-RealMadrid-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261104-E1-Wrexham-Middlesbrough-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261104-CL-RBLeipzig-ManCity-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261105-EL-Celtic-Besiktas-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261105-UECL-StTruiden-Brann-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261105-UECL-KuPS-Gent-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261105-EL-Benfica-LechPoznan-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261105-UECL-Atalanta-FKKairat-U25 --odds <Tipico赔率> --stake 1.00
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
| Wrexham vs Middlesbrough | 主胜 Wrexham + 大于 2.5 球 | 5.85 | **6.03** | 6.61 |
| Wrexham vs Middlesbrough | 平局 + 小于 2.5 球 | 6.04 | **6.23** | 9.79 |
| Wrexham vs Middlesbrough | 主胜 Wrexham + 小于 2.5 球 | 11.15 | **11.48** | 9.15 |
| Wrexham vs Middlesbrough | 平局 + 大于 2.5 球 | 12.78 | **13.16** | 7.07 |
| AEK vs Real Madrid | 客胜 Real Madrid + 小于 2.5 球 | 5.55 | **5.72** | 4.34 |
| AEK vs Real Madrid | 平局 + 小于 2.5 球 | 9.90 | **10.20** | 20.05 |
| AEK vs Real Madrid | 主胜 AEK + 大于 2.5 球 | 13.39 | **13.79** | 13.49 |
| AEK vs Real Madrid | 平局 + 大于 2.5 球 | 17.36 | **17.88** | 9.20 |
| Lens vs Como | 主胜 Lens + 大于 2.5 球 | 4.30 | **4.43** | 5.21 |
| Lens vs Como | 平局 + 小于 2.5 球 | 5.69 | **5.86** | 9.26 |
| Lens vs Como | 主胜 Lens + 小于 2.5 球 | 9.42 | **9.70** | 6.82 |
| RB Leipzig vs Man City | 客胜 Man City + 小于 2.5 球 | 7.70 | **7.93** | 5.58 |
| RB Leipzig vs Man City | 平局 + 小于 2.5 球 | 8.93 | **9.20** | 17.43 |
| RB Leipzig vs Man City | 主胜 RB Leipzig + 小于 2.5 球 | 21.35 | **21.99** | 19.21 |
| Benfica vs Lech Poznan | 主胜 Benfica + 小于 2.5 球 | 5.62 | **5.79** | 4.34 |
| Benfica vs Lech Poznan | 平局 + 小于 2.5 球 | 10.46 | **10.78** | 22.26 |
| Benfica vs Lech Poznan | 客胜 Lech Poznan + 大于 2.5 球 | 16.68 | **17.18** | 16.17 |
| Benfica vs Lech Poznan | 平局 + 大于 2.5 球 | 18.85 | **19.42** | 9.64 |
| Celtic vs Besiktas | 主胜 Celtic + 大于 2.5 球 | 3.26 | **3.36** | 3.95 |
| Celtic vs Besiktas | 主胜 Celtic + 小于 2.5 球 | 8.54 | **8.80** | 5.87 |
| Atalanta vs FK Kairat | 主胜 Atalanta + 小于 2.5 球 | 4.39 | **4.52** | 3.51 |
| Atalanta vs FK Kairat | 平局 + 小于 2.5 球 | 9.51 | **9.79** | 19.45 |
| Atalanta vs FK Kairat | 客胜 FK Kairat + 大于 2.5 球 | 23.08 | **23.77** | 21.32 |
| Atalanta vs FK Kairat | 平局 + 大于 2.5 球 | 27.50 | **28.33** | 11.09 |
| KuPS vs Gent | 平局 + 小于 2.5 球 | 5.14 | **5.29** | 7.71 |
| KuPS vs Gent | 主胜 KuPS + 大于 2.5 球 | 8.26 | **8.50** | 9.50 |
| KuPS vs Gent | 主胜 KuPS + 小于 2.5 球 | 9.78 | **10.07** | 8.47 |
| KuPS vs Gent | 平局 + 大于 2.5 球 | 19.67 | **20.26** | 8.64 |
| St Truiden vs Brann | 客胜 Brann + 大于 2.5 球 | 5.55 | **5.72** | 6.34 |
| St Truiden vs Brann | 平局 + 小于 2.5 球 | 6.31 | **6.50** | 10.39 |
| St Truiden vs Brann | 客胜 Brann + 小于 2.5 球 | 12.11 | **12.47** | 9.53 |

## 备注
- Kortrijk vs KV Mechelen：球队数据不足（可能是升班马），跳过
- Oxford Utd vs Reading：球队数据不足（可能是升班马），跳过
- 从 the-odds-api 取到 45 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 38 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 484 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- Slavia Praha vs Arsenal：球队比赛数不够（门槛 min_team_matches），跳过
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