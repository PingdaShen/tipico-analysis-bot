# 投注建议 · 2026-10-22

覆盖 10-22 至 10-23 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 20 场比赛

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Lech Poznan vs Sunderland | 欧联 | 10-22 18:45 | 主胜 Lech Poznan | 3.81 | **3.93** | 4.57* | €1.00 |
| 2 | Besiktas vs Crystal Palace | 欧联 | 10-22 21:00 | 客胜 Crystal Palace | 2.60 | **2.68** | 2.97* | €1.00 |
| 3 | Trabzonspor vs Hearts | 欧协联 | 10-22 18:45 | 小于 2.5 球 | 2.74 | **2.83** | 3.00* | €1.00 |
| 4 | Celtic vs Celta | 欧联 | 10-22 21:00 | 主胜 Celtic | 2.46 | **2.54** | 2.69* | €1.00 |
| 5 | FK Kairat vs Panathinaikos | 欧协联 | 10-22 16:30 | 小于 2.5 球 | 1.84 | **1.90** | 1.99* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Lech Poznan vs Sunderland — 主胜 Lech Poznan**

```
20261022-EL-LechPoznan-Sunderland-H
```

**2. Besiktas vs Crystal Palace — 客胜 Crystal Palace**

```
20261022-EL-Besiktas-CrystalPalace-A
```

**3. Trabzonspor vs Hearts — 小于 2.5 球**

```
20261022-UECL-Trabzonspor-Hearts-U25
```

**4. Celtic vs Celta — 主胜 Celtic**

```
20261022-EL-Celtic-Celta-H
```

**5. FK Kairat vs Panathinaikos — 小于 2.5 球**

```
20261022-UECL-FKKairat-Panathinaikos-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261022-EL-LechPoznan-Sunderland-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261022-EL-Besiktas-CrystalPalace-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261022-UECL-Trabzonspor-Hearts-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261022-EL-Celtic-Celta-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261022-UECL-FKKairat-Panathinaikos-U25 --odds <Tipico赔率> --stake 1.00
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
| Lech Poznan vs Sunderland | 平局 + 小于 2.5 球 | 5.16 | **5.32** | 7.87 |
| Lech Poznan vs Sunderland | 主胜 Lech Poznan + 大于 2.5 球 | 6.35 | **6.54** | 7.59 |
| Lech Poznan vs Sunderland | 主胜 Lech Poznan + 小于 2.5 球 | 9.53 | **9.81** | 7.66 |
| Besiktas vs Crystal Palace | 客胜 Crystal Palace + 大于 2.5 球 | 3.65 | **3.76** | 4.36 |
| Besiktas vs Crystal Palace | 平局 + 小于 2.5 球 | 5.84 | **6.02** | 9.75 |
| Besiktas vs Crystal Palace | 客胜 Crystal Palace + 小于 2.5 球 | 9.04 | **9.32** | 6.44 |
| Celtic vs Celta | 主胜 Celtic + 大于 2.5 球 | 3.71 | **3.82** | 4.48 |
| Celtic vs Celta | 主胜 Celtic + 小于 2.5 球 | 7.33 | **7.55** | 5.47 |
| FK Kairat vs Panathinaikos | 客胜 Panathinaikos + 小于 2.5 球 | 4.31 | **4.44** | 3.47 |
| FK Kairat vs Panathinaikos | 平局 + 小于 2.5 球 | 4.63 | **4.76** | 6.98 |
| FK Kairat vs Panathinaikos | 主胜 FK Kairat + 大于 2.5 球 | 9.01 | **9.28** | 10.61 |
| FK Kairat vs Panathinaikos | 主胜 FK Kairat + 小于 2.5 球 | 10.49 | **10.81** | 8.92 |
| Trabzonspor vs Hearts | 平局 + 小于 2.5 球 | 8.58 | **8.84** | 15.42 |
| Trabzonspor vs Hearts | 客胜 Hearts + 大于 2.5 球 | 8.64 | **8.90** | 9.30 |
| Trabzonspor vs Hearts | 平局 + 大于 2.5 球 | 16.29 | **16.78** | 8.84 |
| Trabzonspor vs Hearts | 客胜 Hearts + 小于 2.5 球 | 18.74 | **19.30** | 16.22 |

## 备注
- 赛程源里没有 10-22 起 2 天内的联赛比赛。fixtures.csv 最新的一场是 2026-10-21（已经是 1 天前），只覆盖 5 个联赛：E1、E2、E3、SC1、SP1。football-data.co.uk 的赛程是周五下午发布周末场次、周二下午发布周中场次，国际比赛周没有联赛可发就不会更新。等不及可以用 manual_fixtures.csv 手填。
- 从 the-odds-api 取到 36 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 31 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 151 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- FC Ararat-Armenia vs AZ Alkmaar：球队比赛数不够（门槛 min_team_matches），跳过
- Dinamo Zagreb vs Nijmegen：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「Ferencváros TC」模型不认识，可能是「Ferencvárosi TC」，这场跳过。
- 手填赛程里的球队「Torreense」模型不认识，可能是「Moreirense、Odense、Horsens」，这场跳过。
- St. Gilloise vs Hapoel Be'er Sheva：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「Omonoia FC」模型不认识，可能是「Monza、Concordia、FK Mornar」，这场跳过。
- 手填赛程里的球队「Sparta Prague」模型不认识，可能是「AC Sparta Praha、Spartak Trnava、Slavia Prag」，这场跳过。
- 手填赛程里的球队「PFC Levski Sofia」模型不认识，可能是「Levski Sofia」，这场跳过。
- 手填赛程里的球队「FK Jablonec」模型不认识，可能是「Boulogne」，这场跳过。
- 手填赛程里的球队「Red Star Belgrade」模型不认识，可能是「Red Star」，这场跳过。
- FC Iberia 1999 vs Mjallby：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「PFC CSKA Sofia」模型不认识，可能是「CSKA 1948 Sofia、Levski Sofia」，这场跳过。
- Kauno Žalgiris vs Brann：球队比赛数不够（门槛 min_team_matches），跳过
- Inter Club d'Escaldes vs Univ. Craiova：球队比赛数不够（门槛 min_team_matches），跳过
- Pafos FC vs Riga FC：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「KF Egnatia」模型不认识，可能是「KF Tiranë、Fiorentina」，这场跳过。
- Thun vs Hajduk Split：球队比赛数不够（门槛 min_team_matches），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。