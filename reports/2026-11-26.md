# 投注建议 · 2026-11-26

覆盖 11-26 至 11-27 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 20 场比赛

## 欧战 / 国家队

赛程和赔率来自 the-odds-api，1X2 锚定 Pinnacle。
**开球前再跑一次就能取到收盘价**，所以这些注的 CLV 是算得出来的。
不过跨联赛的实力值本身比联赛模型不确定得多，请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Crystal Palace vs Sociedad | 欧联 | 11-26 21:00 | 小于 2.5 球 | 2.35 | **2.42** | 2.50* | €1.00 |
| 2 | Sp Braga vs KuPS | 欧协联 | 11-26 21:00 | 小于 2.5 球 | 2.45 | **2.52** | 2.59* | €1.00 |
| 3 | Borac Banja Luka vs Atalanta | 欧协联 | 11-26 21:00 | 小于 2.5 球 | 2.49 | **2.56** | 2.62* | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Crystal Palace vs Sociedad — 小于 2.5 球**

```
20261126-EL-CrystalPalace-Sociedad-U25
```

**2. Sp Braga vs KuPS — 小于 2.5 球**

```
20261126-UECL-SpBraga-KuPS-U25
```

**3. Borac Banja Luka vs Atalanta — 小于 2.5 球**

```
20261126-UECL-BoracBanjaLuka-Atalanta-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. 收盘赔率不用管：`record-close-auto` 每半小时跑一次，开球前 45 分钟内会自动抓 Pinnacle 的价格；联赛的收盘价随赛果自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261126-EL-CrystalPalace-Sociedad-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261126-UECL-SpBraga-KuPS-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261126-UECL-BoracBanjaLuka-Atalanta-U25 --odds <Tipico赔率> --stake 1.00
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
| Crystal Palace vs Sociedad | 平局 + 小于 2.5 球 | 5.68 | **5.85** | 9.38 |
| Crystal Palace vs Sociedad | 主胜 Crystal Palace + 小于 2.5 球 | 6.72 | **6.92** | 5.03 |
| Crystal Palace vs Sociedad | 客胜 Sociedad + 小于 2.5 球 | 9.86 | **10.15** | 8.27 |
| Borac Banja Luka vs Atalanta | 客胜 Atalanta + 小于 2.5 球 | 4.90 | **5.05** | 3.70 |
| Borac Banja Luka vs Atalanta | 平局 + 小于 2.5 球 | 7.01 | **7.22** | 12.94 |
| Borac Banja Luka vs Atalanta | 主胜 Borac Banja Luka + 小于 2.5 球 | 18.01 | **18.55** | 18.31 |
| Sp Braga vs KuPS | 平局 + 小于 2.5 球 | 8.97 | **9.23** | 16.91 |
| Sp Braga vs KuPS | 客胜 KuPS + 大于 2.5 球 | 23.55 | **24.25** | 21.92 |
| Sp Braga vs KuPS | 客胜 KuPS + 小于 2.5 球 | 28.85 | **29.71** | 31.73 |
| Sp Braga vs KuPS | 平局 + 大于 2.5 球 | 30.14 | **31.05** | 11.68 |

## 备注
- 从 the-odds-api 取到 36 场带赔率的赛程（1X2 锚定 Pinnacle）。
- 其中 31 场的大小球 2.5 锚定的是软庄——Pinnacle 只挂主盘，欧战常常不是 2.5。
- the-odds-api 免费额度还剩 424 次（每月 500）。
- 欧战：已合并 13 场手录赛果（数据源已经收录的重复行自动忽略）。
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