# 投注建议 · 2026-11-25

覆盖 11-25 至 11-26 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 39 场比赛

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Paris SG vs Roma | 欧冠 | 11-25 21:00 | 小于 2.5 球 | 3.14 | **3.23** | 3.37* | €1.00 |
| 2 | Sp Lisbon vs Man United | 欧冠 | 11-25 21:00 | 主胜 Sp Lisbon | 2.52 | **2.60** | 2.63* | €1.00 |
| 3 | Shakhtar Donetsk vs Fenerbahce | 欧冠 | 11-25 21:00 | 主胜 Shakhtar Donetsk | 2.54 | **2.62** | 2.63* | €1.00 |
| 4 | Sp Braga vs KuPS | 欧协联 | 11-26 21:00 | 小于 2.5 球 | 2.70 | **2.78** | 3.05* | €1.00 |
| 5 | Hearts vs Monaco | 欧协联 | 11-26 18:45 | 主胜 Hearts | 4.74 | **4.88** | 5.15* | €1.00 |
| 6 | FK Kairat vs Mjallby | 欧协联 | 11-26 16:30 | 小于 2.5 球 | 1.80 | **1.85** | 1.91* | €1.00 |
| 7 | St. Gilloise vs Lech Poznan | 欧联 | 11-26 18:45 | 小于 2.5 球 | 2.60 | **2.67** | 2.75* | €1.00 |
| 8 | Crystal Palace vs Sociedad | 欧联 | 11-26 21:00 | 小于 2.5 球 | 2.26 | **2.33** | 2.39* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Paris SG vs Roma — 小于 2.5 球**

```
20261125-CL-ParisSG-Roma-U25
```

**2. Sp Lisbon vs Man United — 主胜 Sp Lisbon**

```
20261125-CL-SpLisbon-ManUnited-H
```

**3. Shakhtar Donetsk vs Fenerbahce — 主胜 Shakhtar Donetsk**

```
20261125-CL-ShakhtarDonetsk-Fenerbahce-H
```

**4. Sp Braga vs KuPS — 小于 2.5 球**

```
20261126-UECL-SpBraga-KuPS-U25
```

**5. Hearts vs Monaco — 主胜 Hearts**

```
20261126-UECL-Hearts-Monaco-H
```

**6. FK Kairat vs Mjallby — 小于 2.5 球**

```
20261126-UECL-FKKairat-Mjallby-U25
```

**7. St. Gilloise vs Lech Poznan — 小于 2.5 球**

```
20261126-EL-StGilloise-LechPoznan-U25
```

**8. Crystal Palace vs Sociedad — 小于 2.5 球**

```
20261126-EL-CrystalPalace-Sociedad-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261125-CL-ParisSG-Roma-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261125-CL-SpLisbon-ManUnited-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261125-CL-ShakhtarDonetsk-Fenerbahce-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261126-UECL-SpBraga-KuPS-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261126-UECL-Hearts-Monaco-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261126-UECL-FKKairat-Mjallby-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261126-EL-StGilloise-LechPoznan-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261126-EL-CrystalPalace-Sociedad-U25 --odds <Tipico赔率> --stake 1.00
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
| Paris SG vs Roma | 主胜 Paris SG + 小于 2.5 球 | 6.97 | **7.18** | 5.03 |
| Paris SG vs Roma | 平局 + 小于 2.5 球 | 7.94 | **8.18** | 15.13 |
| Paris SG vs Roma | 客胜 Roma + 小于 2.5 球 | 20.20 | **20.81** | 18.50 |
| Shakhtar Donetsk vs Fenerbahce | 主胜 Shakhtar Donetsk + 大于 2.5 球 | 4.13 | **4.26** | 5.06 |
| Shakhtar Donetsk vs Fenerbahce | 平局 + 小于 2.5 球 | 4.78 | **4.93** | 7.26 |
| Shakhtar Donetsk vs Fenerbahce | 主胜 Shakhtar Donetsk + 小于 2.5 球 | 6.62 | **6.82** | 5.11 |
| Sp Lisbon vs Man United | 主胜 Sp Lisbon + 大于 2.5 球 | 3.47 | **3.57** | 4.01 |
| Sp Lisbon vs Man United | 平局 + 小于 2.5 球 | 6.32 | **6.51** | 10.60 |
| Sp Lisbon vs Man United | 主胜 Sp Lisbon + 小于 2.5 球 | 9.25 | **9.53** | 6.79 |
| St. Gilloise vs Lech Poznan | 主胜 St. Gilloise + 小于 2.5 球 | 4.94 | **5.09** | 3.86 |
| St. Gilloise vs Lech Poznan | 平局 + 小于 2.5 球 | 7.59 | **7.81** | 13.79 |
| St. Gilloise vs Lech Poznan | 客胜 Lech Poznan + 大于 2.5 球 | 11.45 | **11.79** | 11.77 |
| St. Gilloise vs Lech Poznan | 客胜 Lech Poznan + 小于 2.5 球 | 19.70 | **20.29** | 18.80 |
| Crystal Palace vs Sociedad | 平局 + 小于 2.5 球 | 5.59 | **5.75** | 9.08 |
| Crystal Palace vs Sociedad | 主胜 Crystal Palace + 小于 2.5 球 | 6.31 | **6.50** | 4.80 |
| Crystal Palace vs Sociedad | 客胜 Sociedad + 小于 2.5 球 | 9.50 | **9.78** | 8.05 |
| FK Kairat vs Mjallby | 平局 + 小于 2.5 球 | 4.25 | **4.38** | 6.23 |
| FK Kairat vs Mjallby | 主胜 FK Kairat + 小于 2.5 球 | 5.42 | **5.58** | 4.40 |
| FK Kairat vs Mjallby | 客胜 Mjallby + 小于 2.5 球 | 7.31 | **7.53** | 5.91 |
| Hearts vs Monaco | 平局 + 小于 2.5 球 | 6.79 | **6.99** | 11.49 |
| Hearts vs Monaco | 主胜 Hearts + 大于 2.5 球 | 7.09 | **7.30** | 7.74 |
| Hearts vs Monaco | 平局 + 大于 2.5 球 | 12.99 | **13.37** | 7.28 |
| Hearts vs Monaco | 主胜 Hearts + 小于 2.5 球 | 14.29 | **14.72** | 12.21 |
| Sp Braga vs KuPS | 主胜 Sp Braga + 小于 2.5 球 | 4.21 | **4.34** | 3.43 |
| Sp Braga vs KuPS | 平局 + 小于 2.5 球 | 9.77 | **10.06** | 19.51 |
| Sp Braga vs KuPS | 客胜 KuPS + 大于 2.5 球 | 22.52 | **23.20** | 21.16 |
| Sp Braga vs KuPS | 平局 + 大于 2.5 球 | 27.81 | **28.65** | 11.48 |

## 备注
- 从 the-odds-api 取到 45 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 40 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 430 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- Slavia Praha vs Villarreal：球队比赛数不够（门槛 min_team_matches），跳过
- Dinamo Zagreb vs Leverkusen：球队比赛数不够（门槛 min_team_matches），跳过
- Besiktas vs Hapoel Be'er Sheva：球队比赛数不够（门槛 min_team_matches），跳过
- Salzburg vs FC Ararat-Armenia：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「PFC Levski Sofia」模型不认识，可能是「Levski Sofia」，这场跳过。
- 手填赛程里的球队「Sparta Prague」模型不认识，可能是「AC Sparta Praha、Spartak Trnava、Slavia Prag」，这场跳过。
- 手填赛程里的球队「Torreense」模型不认识，可能是「Moreirense、Odense、Horsens」，这场跳过。
- 手填赛程里的球队「Ferencváros TC」模型不认识，可能是「Ferencvárosi TC」，这场跳过。
- 手填赛程里的球队「Omonoia FC」模型不认识，可能是「Monza、Concordia、FK Mornar」，这场跳过。
- FC Iberia 1999 vs Getafe：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「FK Jablonec」模型不认识，可能是「Boulogne」，这场跳过。
- Pafos FC vs Midtjylland：球队比赛数不够（门槛 min_team_matches），跳过
- Kauno Žalgiris vs Riga FC：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「KF Egnatia」模型不认识，可能是「KF Tiranë、Fiorentina」，这场跳过。
- Inter Club d'Escaldes vs FC Copenhagen：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「Red Star Belgrade」模型不认识，可能是「Red Star」，这场跳过。
- Hajduk Split vs St Truiden：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「PFC CSKA Sofia」模型不认识，可能是「CSKA 1948 Sofia、Levski Sofia」，这场跳过。

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。