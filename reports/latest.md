# 投注建议 · 2026-10-11

覆盖 10-11 至 10-12 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 46 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Mallorca vs Las Palmas | 西乙 | 10-11 18:30 | 小于 2.5 球 | 1.71 | **1.76** | 1.97* | €1.00 |
| 2 | Besiktas vs Kocaelispor | 土超 | 10-11 18:00 | 小于 2.5 球 | 2.00 | **2.06** | 2.25* | €1.00 |
| 3 | St. Gilloise vs Oud-Heverlee Leuven | 比甲 | 10-11 16:00 | 小于 2.5 球 | 2.56 | **2.63** | 2.67* | €1.00 |
| 4 | Como vs Roma | 意甲 | 10-11 12:30 | 小于 2.5 球 | 2.15 | **2.22** | 2.22* | €1.00 |
| 5 | Tenerife vs Girona | 西乙 | 10-12 21:00 | 客胜 Girona | 2.33 | **2.40** | 2.46* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Mallorca vs Las Palmas — 小于 2.5 球**

```
20261011-SP2-Mallorca-LasPalmas-U25
```

**2. Besiktas vs Kocaelispor — 小于 2.5 球**

```
20261011-T1-Besiktas-Kocaelispor-U25
```

**3. St. Gilloise vs Oud-Heverlee Leuven — 小于 2.5 球**

```
20261011-B1-StGilloise-Oud-HeverleeLeuven-U25
```

**4. Como vs Roma — 小于 2.5 球**

```
20261011-I1-Como-Roma-U25
```

**5. Tenerife vs Girona — 客胜 Girona**

```
20261012-SP2-Tenerife-Girona-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261011-SP2-Mallorca-LasPalmas-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261011-T1-Besiktas-Kocaelispor-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261011-B1-StGilloise-Oud-HeverleeLeuven-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261011-I1-Como-Roma-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261012-SP2-Tenerife-Girona-A --odds <Tipico赔率> --stake 1.00
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
| St. Gilloise vs Oud-Heverlee Leuven | 主胜 St. Gilloise + 小于 2.5 球 | 4.50 | **4.63** | 3.34 |
| St. Gilloise vs Oud-Heverlee Leuven | 平局 + 小于 2.5 球 | 7.72 | **7.95** | 16.51 |
| Como vs Roma | 平局 + 小于 2.5 球 | 5.19 | **5.34** | 8.03 |
| Como vs Roma | 客胜 Roma + 小于 2.5 球 | 7.27 | **7.49** | 5.71 |
| Como vs Roma | 主胜 Como + 小于 2.5 球 | 7.42 | **7.65** | 6.06 |
| Mallorca vs Las Palmas | 平局 + 小于 2.5 球 | 4.02 | **4.14** | 6.29 |
| Mallorca vs Las Palmas | 主胜 Mallorca + 小于 2.5 球 | 4.05 | **4.17** | 3.00 |
| Mallorca vs Las Palmas | 客胜 Las Palmas + 小于 2.5 球 | 11.21 | **11.55** | 10.72 |
| Tenerife vs Girona | 客胜 Girona + 大于 2.5 球 | 4.06 | **4.18** | 5.18 |
| Tenerife vs Girona | 客胜 Girona + 小于 2.5 球 | 5.48 | **5.65** | 4.24 |
| Besiktas vs Kocaelispor | 主胜 Besiktas + 小于 2.5 球 | 3.77 | **3.88** | 2.97 |
| Besiktas vs Kocaelispor | 平局 + 小于 2.5 球 | 5.50 | **5.67** | 9.33 |
| Besiktas vs Kocaelispor | 客胜 Kocaelispor + 小于 2.5 球 | 19.36 | **19.94** | 18.34 |

## 备注
- 德甲：已合并 1 场手录赛果（数据源已经收录的重复行自动忽略）。
- Freiburg vs Schalke 04：球队数据不足（可能是升班马），跳过
- 德乙：已合并 1 场手录赛果（数据源已经收录的重复行自动忽略）。
- St Pauli vs Karlsruhe：球队数据不足（可能是升班马），跳过
- Hull vs Everton：球队数据不足（可能是升班马），跳过
- Coventry vs Newcastle：球队数据不足（可能是升班马），跳过
- Troyes vs Marseille：球队数据不足（可能是升班马），跳过
- 法乙：已合并 2 场手录赛果（数据源已经收录的重复行自动忽略）。
- Dijon vs Metz：球队数据不足（可能是升班马），跳过
- Iraklis vs Levadeiakos：球队数据不足（可能是升班马），跳过
- PAOK vs Kalamata：球队数据不足（可能是升班马），跳过
- Modena vs Verona：球队数据不足（可能是升班马），跳过
- Telstar vs Den Haag：球队数据不足（可能是升班马），跳过
- Zwolle vs Cambuur：球队数据不足（可能是升班马），跳过
- 葡超：已合并 1 场手录赛果（数据源已经收录的重复行自动忽略）。
- Sociedad vs La Coruna：球队数据不足（可能是升班马），跳过
- Santander vs Valencia：球队数据不足（可能是升班马），跳过
- Gaziantep vs Corum：球队数据不足（可能是升班马），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。