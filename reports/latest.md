# 投注建议 · 2026-10-15

覆盖 10-15 至 10-16 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 18 场比赛

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | KuPS vs Trabzonspor | 欧协联 | 10-15 18:45 | 主胜 KuPS | 4.67 | **4.81** | 5.67* | €1.00 |
| 2 | Panathinaikos vs Borac Banja Luka | 欧协联 | 10-15 18:45 | 小于 2.5 球 | 2.19 | **2.25** | 2.52* | €1.00 |
| 3 | Bournemouth vs Sturm Graz | 欧联 | 10-15 21:00 | 小于 2.5 球 | 3.01 | **3.10** | 3.33* | €1.00 |
| 4 | Gent vs Aarhus | 欧协联 | 10-15 18:45 | 客胜 Aarhus | 4.52 | **4.65** | 4.99* | €1.00 |
| 5 | St. Gilloise vs Sociedad | 欧联 | 10-15 18:45 | 小于 2.5 球 | 2.19 | **2.25** | 2.38* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. KuPS vs Trabzonspor — 主胜 KuPS**

```
20261015-UECL-KuPS-Trabzonspor-H
```

**2. Panathinaikos vs Borac Banja Luka — 小于 2.5 球**

```
20261015-UECL-Panathinaikos-BoracBanjaLuka-U25
```

**3. Bournemouth vs Sturm Graz — 小于 2.5 球**

```
20261015-EL-Bournemouth-SturmGraz-U25
```

**4. Gent vs Aarhus — 客胜 Aarhus**

```
20261015-UECL-Gent-Aarhus-A
```

**5. St. Gilloise vs Sociedad — 小于 2.5 球**

```
20261015-EL-StGilloise-Sociedad-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261015-UECL-KuPS-Trabzonspor-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261015-UECL-Panathinaikos-BoracBanjaLuka-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261015-EL-Bournemouth-SturmGraz-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261015-UECL-Gent-Aarhus-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261015-EL-StGilloise-Sociedad-U25 --odds <Tipico赔率> --stake 1.00
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
| St. Gilloise vs Sociedad | 平局 + 小于 2.5 球 | 5.19 | **5.35** | 8.30 |
| St. Gilloise vs Sociedad | 主胜 St. Gilloise + 小于 2.5 球 | 7.26 | **7.48** | 5.48 |
| St. Gilloise vs Sociedad | 客胜 Sociedad + 小于 2.5 球 | 7.88 | **8.11** | 6.49 |
| Bournemouth vs Sturm Graz | 主胜 Bournemouth + 小于 2.5 球 | 4.97 | **5.12** | 3.95 |
| Bournemouth vs Sturm Graz | 平局 + 小于 2.5 球 | 10.08 | **10.39** | 20.52 |
| Bournemouth vs Sturm Graz | 客胜 Sturm Graz + 大于 2.5 球 | 16.93 | **17.43** | 16.48 |
| Bournemouth vs Sturm Graz | 平局 + 大于 2.5 球 | 21.06 | **21.69** | 10.21 |
| Gent vs Aarhus | 平局 + 小于 2.5 球 | 5.62 | **5.79** | 8.72 |
| Gent vs Aarhus | 客胜 Aarhus + 大于 2.5 球 | 7.76 | **7.99** | 8.74 |
| Gent vs Aarhus | 客胜 Aarhus + 小于 2.5 球 | 10.81 | **11.13** | 9.34 |
| Gent vs Aarhus | 平局 + 大于 2.5 球 | 16.84 | **17.35** | 8.16 |
| Panathinaikos vs Borac Banja Luka | 主胜 Panathinaikos + 小于 2.5 球 | 3.75 | **3.87** | 3.01 |
| Panathinaikos vs Borac Banja Luka | 平局 + 小于 2.5 球 | 6.91 | **7.12** | 12.41 |
| Panathinaikos vs Borac Banja Luka | 客胜 Borac Banja Luka + 小于 2.5 球 | 21.66 | **22.31** | 22.41 |
| KuPS vs Trabzonspor | 平局 + 小于 2.5 球 | 5.65 | **5.82** | 8.89 |
| KuPS vs Trabzonspor | 主胜 KuPS + 大于 2.5 球 | 7.79 | **8.02** | 8.90 |
| KuPS vs Trabzonspor | 主胜 KuPS + 小于 2.5 球 | 11.66 | **12.01** | 9.82 |

## 备注
- Mansfield vs Oxford：球队数据不足（可能是升班马），跳过
- 从 the-odds-api 取到 36 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 33 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 177 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
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