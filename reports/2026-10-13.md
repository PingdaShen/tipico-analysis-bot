# 投注建议 · 2026-10-13

覆盖 10-13 至 10-14 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 13 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Cardiff vs Watford | 英冠 | 10-13 20:45 | 客胜 Watford | 4.11 | **4.23** | 4.51* | €1.00 |
| 2 | QPR vs Derby | 英冠 | 10-14 20:45 | 客胜 Derby | 4.19 | **4.31** | 4.57* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Cardiff vs Watford — 客胜 Watford**

```
20261013-E1-Cardiff-Watford-A
```

**2. QPR vs Derby — 客胜 Derby**

```
20261014-E1-QPR-Derby-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261013-E1-Cardiff-Watford-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261014-E1-QPR-Derby-A --odds <Tipico赔率> --stake 1.00
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
| Cardiff vs Watford | 平局 + 小于 2.5 球 | 5.89 | **6.07** | 9.84 |
| Cardiff vs Watford | 主胜 Cardiff + 小于 2.5 球 | 5.90 | **6.08** | 4.60 |
| Cardiff vs Watford | 客胜 Watford + 大于 2.5 球 | 6.22 | **6.40** | 7.11 |
| Cardiff vs Watford | 客胜 Watford + 小于 2.5 球 | 12.14 | **12.50** | 9.75 |
| QPR vs Derby | 平局 + 小于 2.5 球 | 5.20 | **5.35** | 8.07 |
| QPR vs Derby | 客胜 Derby + 大于 2.5 球 | 7.00 | **7.21** | 8.13 |
| QPR vs Derby | 客胜 Derby + 小于 2.5 球 | 10.43 | **10.74** | 8.65 |
| QPR vs Derby | 平局 + 大于 2.5 球 | 15.78 | **16.25** | 7.59 |

## 欧冠赛程（还没有赔率）

赛程来自 openligadb，但它没有赔率——没有市场锚就算不出最低赔率，
所以这些**还不是推荐**。下面是模型自己的概率（未与市场融合），
用来判断哪几场值得去查赔率。要让某场进入推荐，把赔率填进去：

```bash
python -m src.manual add --comp CL --date <YYYY-MM-DD> \
    --home <主队> --away <客队> \
    --ref-h <参考主胜> --ref-d <参考平> --ref-a <参考客胜> \
    --tip-h <Tipico主胜> --tip-d <Tipico平> --tip-a <Tipico客胜>
```

| 日期 | 时间 | 比赛 | 模型主胜 | 平 | 客胜 | 模型小于 2.5 |
|---|---|---|---|---|---|---|
| 10-13 | 17:45 | Lens vs Sp Lisbon | 37% | 26% | 37% | 47% |
| 10-13 | 20:00 | Inter vs Club Brugge | 66% | 19% | 15% | 36% |
| 10-13 | 20:00 | Galatasaray vs Barcelona | 21% | 21% | 58% | 31% |
| 10-13 | 20:00 | Ath Madrid vs Man United | 47% | 25% | 28% | 43% |
| 10-13 | 20:00 | Arsenal vs Lille | 70% | 20% | 10% | 50% |
| 10-13 | 20:00 | Viking vs Bayern Munich | 12% | 14% | 74% | 20% |
| 10-13 | 20:00 | RB Leipzig vs PSV Eindhoven | 47% | 22% | 32% | 27% |
| 10-13 | 20:00 | Villarreal vs Napoli | 40% | 26% | 34% | 46% |
| 10-14 | 17:45 | LASK vs Liverpool | 8% | 14% | 78% | 32% |
| 10-14 | 17:45 | Feyenoord vs Como | 56% | 23% | 21% | 41% |
| 10-14 | 20:00 | Aston Villa vs Fenerbahce | 63% | 20% | 17% | 34% |
| 10-14 | 20:00 | Slovan Bratislava vs Stuttgart | 28% | 23% | 49% | 35% |
| 10-14 | 20:00 | Shakhtar Donetsk vs AEK | 40% | 32% | 28% | 69% |
| 10-14 | 20:00 | Bodo/Glimt vs Dortmund | 37% | 23% | 40% | 33% |
| 10-14 | 20:00 | Betis vs Porto | 34% | 29% | 38% | 57% |
| 10-14 | 20:00 | Roma vs Real Madrid | 27% | 26% | 47% | 49% |
| 10-14 | 20:00 | Man City vs Paris SG | 55% | 22% | 23% | 37% |

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。