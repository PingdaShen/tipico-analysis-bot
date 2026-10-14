# 投注建议 · 2026-10-14

覆盖 10-14 至 10-15 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 30 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | QPR vs Derby | 英冠 | 10-14 20:45 | 客胜 Derby | 4.19 | **4.31** | 4.57* | €1.00 |

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 2 | Feyenoord vs Como | 欧冠 | 10-14 18:45 | 主胜 Feyenoord | 2.65 | **2.73** | 3.18* | €1.00 |
| 3 | Roma vs Real Madrid | 欧冠 | 10-14 21:00 | 小于 2.5 球 | 2.61 | **2.68** | 2.80* | €1.00 |
| 4 | Shakhtar Donetsk vs AEK | 欧冠 | 10-14 21:00 | 小于 2.5 球 | 1.83 | **1.88** | 1.93* | €1.00 |
| 5 | Betis vs Porto | 欧冠 | 10-14 21:00 | 客胜 Porto | 3.30 | **3.40** | 3.43* | €1.00 |
| 6 | Panathinaikos vs Borac Banja Luka | 欧协联 | 10-15 18:45 | 小于 2.5 球 | 2.26 | **2.33** | 2.60* | €1.00 |
| 7 | Gent vs Aarhus | 欧协联 | 10-15 18:45 | 客胜 Aarhus | 4.52 | **4.66** | 5.17* | €1.00 |
| 8 | Bournemouth vs Sturm Graz | 欧联 | 10-15 21:00 | 小于 2.5 球 | 2.91 | **3.00** | 3.18* | €1.00 |
| 9 | Hearts vs Nordsjaelland | 欧协联 | 10-15 21:00 | 主胜 Hearts | 2.83 | **2.91** | 3.04* | €1.00 |
| 10 | Benfica vs Celtic | 欧联 | 10-15 21:00 | 小于 2.5 球 | 2.72 | **2.80** | 2.83* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Feyenoord vs Como — 主胜 Feyenoord**

```
20261014-CL-Feyenoord-Como-H
```

**2. QPR vs Derby — 客胜 Derby**

```
20261014-E1-QPR-Derby-A
```

**3. Roma vs Real Madrid — 小于 2.5 球**

```
20261014-CL-Roma-RealMadrid-U25
```

**4. Shakhtar Donetsk vs AEK — 小于 2.5 球**

```
20261014-CL-ShakhtarDonetsk-AEK-U25
```

**5. Betis vs Porto — 客胜 Porto**

```
20261014-CL-Betis-Porto-A
```

**6. Panathinaikos vs Borac Banja Luka — 小于 2.5 球**

```
20261015-UECL-Panathinaikos-BoracBanjaLuka-U25
```

**7. Gent vs Aarhus — 客胜 Aarhus**

```
20261015-UECL-Gent-Aarhus-A
```

**8. Bournemouth vs Sturm Graz — 小于 2.5 球**

```
20261015-EL-Bournemouth-SturmGraz-U25
```

**9. Hearts vs Nordsjaelland — 主胜 Hearts**

```
20261015-UECL-Hearts-Nordsjaelland-H
```

**10. Benfica vs Celtic — 小于 2.5 球**

```
20261015-EL-Benfica-Celtic-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. **开球前几分钟**在 Actions 页面跑 **record-close**，填那一刻的市场赔率（有 Pinnacle 用 Pinnacle）。
   欧战和国家队没有收盘赔率源，不记就永远算不出 CLV，这些推荐也就无从检验。联赛不用管，收盘价会自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261014-CL-Feyenoord-Como-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-E1-QPR-Derby-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-Roma-RealMadrid-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-ShakhtarDonetsk-AEK-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-CL-Betis-Porto-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261015-UECL-Panathinaikos-BoracBanjaLuka-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261015-UECL-Gent-Aarhus-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261015-EL-Bournemouth-SturmGraz-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261015-UECL-Hearts-Nordsjaelland-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261015-EL-Benfica-Celtic-U25 --odds <Tipico赔率> --stake 1.00
# 开球前：
python -m src.ledger close 20261014-CL-Feyenoord-Como-H --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-Roma-RealMadrid-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-ShakhtarDonetsk-AEK-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261014-CL-Betis-Porto-A --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261015-UECL-Panathinaikos-BoracBanjaLuka-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261015-UECL-Gent-Aarhus-A --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261015-EL-Bournemouth-SturmGraz-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261015-UECL-Hearts-Nordsjaelland-H --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261015-EL-Benfica-Celtic-U25 --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
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
| QPR vs Derby | 平局 + 小于 2.5 球 | 5.20 | **5.35** | 8.07 |
| QPR vs Derby | 客胜 Derby + 大于 2.5 球 | 7.00 | **7.21** | 8.13 |
| QPR vs Derby | 客胜 Derby + 小于 2.5 球 | 10.43 | **10.74** | 8.65 |
| QPR vs Derby | 平局 + 大于 2.5 球 | 15.78 | **16.25** | 7.59 |
| Feyenoord vs Como | 主胜 Feyenoord + 大于 2.5 球 | 3.64 | **3.75** | 4.30 |
| Feyenoord vs Como | 平局 + 小于 2.5 球 | 6.31 | **6.50** | 10.63 |
| Feyenoord vs Como | 主胜 Feyenoord + 小于 2.5 球 | 9.68 | **9.97** | 6.89 |
| Shakhtar Donetsk vs AEK | 平局 + 小于 2.5 球 | 4.18 | **4.30** | 6.19 |
| Shakhtar Donetsk vs AEK | 主胜 Shakhtar Donetsk + 小于 2.5 球 | 6.38 | **6.57** | 4.97 |
| Shakhtar Donetsk vs AEK | 客胜 AEK + 小于 2.5 球 | 6.60 | **6.80** | 5.41 |
| Roma vs Real Madrid | 平局 + 小于 2.5 球 | 6.13 | **6.32** | 10.45 |
| Roma vs Real Madrid | 客胜 Real Madrid + 小于 2.5 球 | 7.21 | **7.43** | 5.32 |
| Roma vs Real Madrid | 主胜 Roma + 小于 2.5 球 | 12.18 | **12.55** | 10.01 |
| Betis vs Porto | 平局 + 小于 2.5 球 | 5.09 | **5.24** | 7.93 |
| Betis vs Porto | 客胜 Porto + 大于 2.5 球 | 5.25 | **5.41** | 6.25 |
| Betis vs Porto | 主胜 Betis + 小于 2.5 球 | 6.14 | **6.33** | 4.93 |
| Betis vs Porto | 客胜 Porto + 小于 2.5 球 | 8.86 | **9.13** | 6.99 |
| Benfica vs Celtic | 平局 + 小于 2.5 球 | 8.69 | **8.95** | 15.81 |
| Benfica vs Celtic | 客胜 Celtic + 大于 2.5 球 | 11.42 | **11.76** | 11.86 |
| Benfica vs Celtic | 平局 + 大于 2.5 球 | 17.49 | **18.02** | 9.18 |
| Benfica vs Celtic | 客胜 Celtic + 小于 2.5 球 | 21.89 | **22.54** | 20.43 |
| Bournemouth vs Sturm Graz | 主胜 Bournemouth + 小于 2.5 球 | 4.84 | **4.99** | 3.86 |
| Bournemouth vs Sturm Graz | 平局 + 小于 2.5 球 | 9.73 | **10.03** | 19.39 |
| Bournemouth vs Sturm Graz | 客胜 Sturm Graz + 大于 2.5 球 | 16.47 | **16.96** | 16.11 |
| Bournemouth vs Sturm Graz | 平局 + 大于 2.5 球 | 21.04 | **21.67** | 10.13 |
| Gent vs Aarhus | 平局 + 小于 2.5 球 | 5.68 | **5.85** | 8.79 |
| Gent vs Aarhus | 客胜 Aarhus + 大于 2.5 球 | 7.83 | **8.06** | 8.81 |
| Gent vs Aarhus | 客胜 Aarhus + 小于 2.5 球 | 10.69 | **11.01** | 9.28 |
| Gent vs Aarhus | 平局 + 大于 2.5 球 | 17.37 | **17.90** | 8.34 |
| Panathinaikos vs Borac Banja Luka | 主胜 Panathinaikos + 小于 2.5 球 | 3.99 | **4.11** | 3.15 |
| Panathinaikos vs Borac Banja Luka | 平局 + 小于 2.5 球 | 6.90 | **7.11** | 12.63 |
| Panathinaikos vs Borac Banja Luka | 客胜 Borac Banja Luka + 小于 2.5 球 | 21.41 | **22.06** | 22.06 |
| Hearts vs Nordsjaelland | 主胜 Hearts + 大于 2.5 球 | 4.17 | **4.30** | 4.91 |
| Hearts vs Nordsjaelland | 平局 + 小于 2.5 球 | 5.75 | **5.92** | 9.30 |
| Hearts vs Nordsjaelland | 主胜 Hearts + 小于 2.5 球 | 8.76 | **9.03** | 6.66 |

## 备注
- Mansfield vs Oxford：球队数据不足（可能是升班马），跳过
- 从 the-odds-api 取到 45 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 42 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 191 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
- ŠK Slovan Bratislava vs Stuttgart：球队比赛数不够（门槛 min_team_matches），跳过
- AZ Alkmaar vs Hapoel Be'er Sheva：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「Sparta Prague」模型不认识，可能是「AC Sparta Praha、Spartak Trnava、Slavia Prag」，这场跳过。
- 手填赛程里的球队「Omonoia FC」模型不认识，可能是「Monza、Concordia、FK Mornar」，这场跳过。
- 手填赛程里的球队「Torreense」模型不认识，可能是「Moreirense、Odense、Horsens」，这场跳过。
- Dinamo Zagreb vs Anderlecht：球队比赛数不够（门槛 min_team_matches），跳过
- Jagiellonia vs FC Ararat-Armenia：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「Ferencváros TC」模型不认识，可能是「Ferencvárosi TC」，这场跳过。
- 手填赛程里的球队「PFC Levski Sofia」模型不认识，可能是「Levski Sofia」，这场跳过。
- 手填赛程里的球队「PFC CSKA Sofia」模型不认识，可能是「CSKA 1948 Sofia、Levski Sofia」，这场跳过。
- Hajduk Split vs Ajax：球队比赛数不够（门槛 min_team_matches），跳过
- Riga FC vs FK Kairat：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「Red Star Belgrade」模型不认识，可能是「Red Star」，这场跳过。
- 手填赛程里的球队「KF Egnatia」模型不认识，可能是「KF Tiranë、Fiorentina」，这场跳过。
- Mjallby vs Inter Club d'Escaldes：球队比赛数不够（门槛 min_team_matches），跳过
- Atalanta vs Pafos FC：球队比赛数不够（门槛 min_team_matches），跳过
- Brighton vs Kauno Žalgiris：球队比赛数不够（门槛 min_team_matches），跳过
- St Truiden vs FC Iberia 1999：球队比赛数不够（门槛 min_team_matches），跳过
- 手填赛程里的球队「FK Jablonec」模型不认识，可能是「Boulogne」，这场跳过。

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。