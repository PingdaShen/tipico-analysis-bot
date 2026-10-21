# 投注建议 · 2026-10-21

覆盖 10-21 至 10-22 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 31 场比赛

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Inter vs Shakhtar Donetsk | 欧冠 | 10-21 21:00 | 小于 2.5 球 | 2.87 | **2.96** | 3.61* | €1.00 |
| 2 | Real Madrid vs RB Leipzig | 欧冠 | 10-21 21:00 | 小于 2.5 球 | 4.20 | **4.33** | 4.88* | €1.00 |
| 3 | Club Brugge vs Lens | 欧冠 | 10-21 21:00 | 小于 2.5 球 | 2.88 | **2.96** | 3.20* | €1.00 |
| 4 | Como vs Man United | 欧冠 | 10-21 18:45 | 客胜 Man United | 2.58 | **2.66** | 2.87* | €1.00 |
| 5 | Betis vs Feyenoord | 欧冠 | 10-21 21:00 | 客胜 Feyenoord | 4.24 | **4.37** | 4.56* | €1.00 |
| 6 | Lech Poznan vs Sunderland | 欧联 | 10-22 18:45 | 主胜 Lech Poznan | 3.83 | **3.94** | 4.80* | €1.00 |
| 7 | Besiktas vs Crystal Palace | 欧联 | 10-22 21:00 | 客胜 Crystal Palace | 2.70 | **2.78** | 3.17* | €1.00 |
| 8 | NK Celje vs Salzburg | 欧联 | 10-22 21:00 | 主胜 NK Celje | 4.66 | **4.80** | 5.18* | €1.00 |
| 9 | Celtic vs Celta | 欧联 | 10-22 21:00 | 主胜 Celtic | 2.45 | **2.53** | 2.66* | €1.00 |
| 10 | Hoffenheim vs Lyon | 欧联 | 10-22 21:00 | 客胜 Lyon | 3.05 | **3.14** | 3.28* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Inter vs Shakhtar Donetsk — 小于 2.5 球**

```
20261021-CL-Inter-ShakhtarDonetsk-U25
```

**2. Real Madrid vs RB Leipzig — 小于 2.5 球**

```
20261021-CL-RealMadrid-RBLeipzig-U25
```

**3. Club Brugge vs Lens — 小于 2.5 球**

```
20261021-CL-ClubBrugge-Lens-U25
```

**4. Como vs Man United — 客胜 Man United**

```
20261021-CL-Como-ManUnited-A
```

**5. Betis vs Feyenoord — 客胜 Feyenoord**

```
20261021-CL-Betis-Feyenoord-A
```

**6. Lech Poznan vs Sunderland — 主胜 Lech Poznan**

```
20261022-EL-LechPoznan-Sunderland-H
```

**7. Besiktas vs Crystal Palace — 客胜 Crystal Palace**

```
20261022-EL-Besiktas-CrystalPalace-A
```

**8. NK Celje vs Salzburg — 主胜 NK Celje**

```
20261022-EL-NKCelje-Salzburg-H
```

**9. Celtic vs Celta — 主胜 Celtic**

```
20261022-EL-Celtic-Celta-H
```

**10. Hoffenheim vs Lyon — 客胜 Lyon**

```
20261022-EL-Hoffenheim-Lyon-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261021-CL-Inter-ShakhtarDonetsk-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261021-CL-RealMadrid-RBLeipzig-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261021-CL-ClubBrugge-Lens-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261021-CL-Como-ManUnited-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261021-CL-Betis-Feyenoord-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261022-EL-LechPoznan-Sunderland-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261022-EL-Besiktas-CrystalPalace-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261022-EL-NKCelje-Salzburg-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261022-EL-Celtic-Celta-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261022-EL-Hoffenheim-Lyon-A --odds <Tipico赔率> --stake 1.00
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
| Como vs Man United | 客胜 Man United + 大于 2.5 球 | 3.68 | **3.79** | 4.36 |
| Como vs Man United | 平局 + 小于 2.5 球 | 5.88 | **6.06** | 9.71 |
| Como vs Man United | 客胜 Man United + 小于 2.5 球 | 8.68 | **8.94** | 6.35 |
| Club Brugge vs Lens | 客胜 Lens + 大于 2.5 球 | 4.73 | **4.88** | 5.29 |
| Club Brugge vs Lens | 平局 + 小于 2.5 球 | 6.99 | **7.20** | 12.18 |
| Club Brugge vs Lens | 主胜 Club Brugge + 小于 2.5 球 | 7.95 | **8.18** | 6.07 |
| Club Brugge vs Lens | 客胜 Lens + 小于 2.5 球 | 12.73 | **13.11** | 9.93 |
| Betis vs Feyenoord | 客胜 Feyenoord + 大于 2.5 球 | 5.87 | **6.04** | 6.37 |
| Betis vs Feyenoord | 主胜 Betis + 小于 2.5 球 | 7.24 | **7.46** | 5.49 |
| Betis vs Feyenoord | 平局 + 小于 2.5 球 | 7.65 | **7.88** | 13.64 |
| Betis vs Feyenoord | 客胜 Feyenoord + 小于 2.5 球 | 15.30 | **15.75** | 12.69 |
| Inter vs Shakhtar Donetsk | 主胜 Inter + 小于 2.5 球 | 5.09 | **5.24** | 3.96 |
| Inter vs Shakhtar Donetsk | 平局 + 小于 2.5 球 | 8.77 | **9.03** | 17.38 |
| Inter vs Shakhtar Donetsk | 客胜 Shakhtar Donetsk + 大于 2.5 球 | 13.97 | **14.39** | 14.04 |
| Inter vs Shakhtar Donetsk | 客胜 Shakhtar Donetsk + 小于 2.5 球 | 26.52 | **27.32** | 26.26 |
| Real Madrid vs RB Leipzig | 主胜 Real Madrid + 小于 2.5 球 | 7.54 | **7.76** | 5.66 |
| Real Madrid vs RB Leipzig | 客胜 RB Leipzig + 大于 2.5 球 | 11.99 | **12.35** | 11.96 |
| Real Madrid vs RB Leipzig | 平局 + 小于 2.5 球 | 12.65 | **13.03** | 28.38 |
| Real Madrid vs RB Leipzig | 平局 + 大于 2.5 球 | 14.51 | **14.95** | 8.87 |
| Lech Poznan vs Sunderland | 平局 + 小于 2.5 球 | 5.34 | **5.50** | 8.16 |
| Lech Poznan vs Sunderland | 主胜 Lech Poznan + 大于 2.5 球 | 6.42 | **6.61** | 7.61 |
| Lech Poznan vs Sunderland | 主胜 Lech Poznan + 小于 2.5 球 | 9.47 | **9.75** | 7.69 |
| Besiktas vs Crystal Palace | 客胜 Crystal Palace + 大于 2.5 球 | 3.91 | **4.03** | 4.71 |
| Besiktas vs Crystal Palace | 平局 + 小于 2.5 球 | 5.82 | **6.00** | 9.53 |
| Besiktas vs Crystal Palace | 客胜 Crystal Palace + 小于 2.5 球 | 8.68 | **8.94** | 6.31 |
| Celtic vs Celta | 主胜 Celtic + 大于 2.5 球 | 3.78 | **3.89** | 4.59 |
| Celtic vs Celta | 主胜 Celtic + 小于 2.5 球 | 7.01 | **7.22** | 5.27 |
| Hoffenheim vs Lyon | 客胜 Lyon + 大于 2.5 球 | 4.19 | **4.31** | 4.73 |
| Hoffenheim vs Lyon | 平局 + 大于 2.5 球 | 10.61 | **10.93** | 6.54 |
| Hoffenheim vs Lyon | 客胜 Lyon + 小于 2.5 球 | 11.17 | **11.50** | 8.57 |
| NK Celje vs Salzburg | 主胜 NK Celje + 大于 2.5 球 | 7.01 | **7.22** | 7.66 |
| NK Celje vs Salzburg | 平局 + 大于 2.5 球 | 13.26 | **13.66** | 7.49 |
| NK Celje vs Salzburg | 主胜 NK Celje + 小于 2.5 球 | 13.87 | **14.29** | 11.87 |

## 备注
- 从 the-odds-api 取到 45 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 39 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 157 次（每月 500）。
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