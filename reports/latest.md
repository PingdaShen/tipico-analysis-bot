# 投注建议 · 2026-10-10

覆盖 10-10 至 10-11 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 135 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Inverness C vs Stenhousemuir | 苏冠 | 10-10 16:00 | 客胜 Stenhousemuir | 2.88 | **2.97** | 3.80 | €1.00 |
| 2 | Barcelona vs Getafe | 西甲 | 10-10 18:30 | 小于 2.5 球 | 3.19 | **3.29** | 3.80 | €1.00 |
| 3 | Shrewsbury vs Exeter | 英乙 | 10-10 16:00 | 小于 2.5 球 | 1.51 | **1.55** | 1.67 | €1.00 |
| 4 | Hearts vs St Mirren | 苏超 | 10-10 16:00 | 小于 2.5 球 | 2.36 | **2.43** | 2.60 | €1.00 |
| 5 | Doncaster vs Burton | 英甲 | 10-10 16:00 | 客胜 Burton | 4.15 | **4.27** | 4.40 | €1.00 |
| 6 | Mallorca vs Las Palmas | 西乙 | 10-11 18:30 | 小于 2.5 球 | 1.71 | **1.76** | 1.97* | €1.00 |
| 7 | Besiktas vs Kocaelispor | 土超 | 10-11 18:00 | 小于 2.5 球 | 2.00 | **2.06** | 2.25* | €1.00 |
| 8 | St. Gilloise vs Oud-Heverlee Leuven | 比甲 | 10-11 16:00 | 小于 2.5 球 | 2.56 | **2.63** | 2.67* | €1.00 |
| 9 | Como vs Roma | 意甲 | 10-11 12:30 | 小于 2.5 球 | 2.15 | **2.22** | 2.22* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Inverness C vs Stenhousemuir — 客胜 Stenhousemuir**

```
20261010-SC1-InvernessC-Stenhousemuir-A
```

**2. Barcelona vs Getafe — 小于 2.5 球**

```
20261010-SP1-Barcelona-Getafe-U25
```

**3. Shrewsbury vs Exeter — 小于 2.5 球**

```
20261010-E3-Shrewsbury-Exeter-U25
```

**4. Hearts vs St Mirren — 小于 2.5 球**

```
20261010-SC0-Hearts-StMirren-U25
```

**5. Doncaster vs Burton — 客胜 Burton**

```
20261010-E2-Doncaster-Burton-A
```

**6. Mallorca vs Las Palmas — 小于 2.5 球**

```
20261011-SP2-Mallorca-LasPalmas-U25
```

**7. Besiktas vs Kocaelispor — 小于 2.5 球**

```
20261011-T1-Besiktas-Kocaelispor-U25
```

**8. St. Gilloise vs Oud-Heverlee Leuven — 小于 2.5 球**

```
20261011-B1-StGilloise-Oud-HeverleeLeuven-U25
```

**9. Como vs Roma — 小于 2.5 球**

```
20261011-I1-Como-Roma-U25
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261010-SC1-InvernessC-Stenhousemuir-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261010-SP1-Barcelona-Getafe-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261010-E3-Shrewsbury-Exeter-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261010-SC0-Hearts-StMirren-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261010-E2-Doncaster-Burton-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261011-SP2-Mallorca-LasPalmas-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261011-T1-Besiktas-Kocaelispor-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261011-B1-StGilloise-Oud-HeverleeLeuven-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261011-I1-Como-Roma-U25 --odds <Tipico赔率> --stake 1.00
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
| Doncaster vs Burton | 平局 + 小于 2.5 球 | 5.29 | **5.45** | 8.03 |
| Doncaster vs Burton | 客胜 Burton + 大于 2.5 球 | 7.11 | **7.32** | 8.24 |
| Doncaster vs Burton | 客胜 Burton + 小于 2.5 球 | 9.97 | **10.27** | 8.37 |
| Shrewsbury vs Exeter | 平局 + 小于 2.5 球 | 3.19 | **3.29** | 4.47 |
| Shrewsbury vs Exeter | 主胜 Shrewsbury + 小于 2.5 球 | 5.15 | **5.30** | 4.13 |
| Shrewsbury vs Exeter | 客胜 Exeter + 小于 2.5 球 | 6.41 | **6.61** | 5.06 |
| Como vs Roma | 平局 + 小于 2.5 球 | 5.19 | **5.34** | 8.03 |
| Como vs Roma | 客胜 Roma + 小于 2.5 球 | 7.27 | **7.49** | 5.71 |
| Como vs Roma | 主胜 Como + 小于 2.5 球 | 7.42 | **7.65** | 6.06 |
| Hearts vs St Mirren | 主胜 Hearts + 小于 2.5 球 | 4.86 | **5.01** | 3.64 |
| Hearts vs St Mirren | 平局 + 小于 2.5 球 | 6.50 | **6.69** | 11.62 |
| Hearts vs St Mirren | 客胜 St Mirren + 小于 2.5 球 | 15.54 | **16.01** | 15.92 |
| Inverness C vs Stenhousemuir | 平局 + 小于 2.5 球 | 3.78 | **3.89** | 5.68 |
| Inverness C vs Stenhousemuir | 客胜 Stenhousemuir + 大于 2.5 球 | 4.96 | **5.11** | 7.56 |
| Inverness C vs Stenhousemuir | 客胜 Stenhousemuir + 小于 2.5 球 | 6.87 | **7.07** | 4.65 |
| Barcelona vs Getafe | 主胜 Barcelona + 小于 2.5 球 | 4.66 | **4.80** | 3.76 |
| Barcelona vs Getafe | 平局 + 小于 2.5 球 | 12.82 | **13.21** | 30.96 |
| Barcelona vs Getafe | 客胜 Getafe + 大于 2.5 球 | 37.35 | **38.47** | 30.84 |
| Barcelona vs Getafe | 客胜 Getafe + 小于 2.5 球 | 48.91 | **50.38** | 67.62 |
| Mallorca vs Las Palmas | 平局 + 小于 2.5 球 | 4.02 | **4.14** | 6.29 |
| Mallorca vs Las Palmas | 主胜 Mallorca + 小于 2.5 球 | 4.05 | **4.17** | 3.00 |
| Mallorca vs Las Palmas | 客胜 Las Palmas + 小于 2.5 球 | 11.21 | **11.55** | 10.72 |
| Besiktas vs Kocaelispor | 主胜 Besiktas + 小于 2.5 球 | 3.77 | **3.88** | 2.97 |
| Besiktas vs Kocaelispor | 平局 + 小于 2.5 球 | 5.50 | **5.67** | 9.33 |
| Besiktas vs Kocaelispor | 客胜 Kocaelispor + 小于 2.5 球 | 19.36 | **19.94** | 18.34 |

## 备注
- 德甲：已合并 1 场手录赛果（数据源已经收录的重复行自动忽略）。
- Paderborn vs Stuttgart：球队数据不足（可能是升班马），跳过
- Union Berlin vs Elversberg：球队数据不足（可能是升班马），跳过
- Freiburg vs Schalke 04：球队数据不足（可能是升班马），跳过
- 德乙：已合并 1 场手录赛果（数据源已经收录的重复行自动忽略）。
- Darmstadt vs Cottbus：球队数据不足（可能是升班马），跳过
- Osnabruck vs Dresden：球队数据不足（可能是升班马），跳过
- Nurnberg vs Wolfsburg：球队数据不足（可能是升班马），跳过
- St Pauli vs Karlsruhe：球队数据不足（可能是升班马），跳过
- Hull vs Everton：球队数据不足（可能是升班马），跳过
- Middlesbrough vs Wolves：球队数据不足（可能是升班马），跳过
- Notts County vs Oxford：球队数据不足（可能是升班马），跳过
- Huddersfield vs Sheffield Weds：球队数据不足（可能是升班马），跳过
- Leicester vs Peterboro：球队数据不足（可能是升班马），跳过
- Mansfield vs Bromley：球队数据不足（可能是升班马），跳过
- Milton Keynes Dons vs Reading：球队数据不足（可能是升班马），跳过
- York vs Northampton：球队数据不足（可能是升班马），跳过
- Paris SG vs Le Mans：球队数据不足（可能是升班马），跳过
- Troyes vs Marseille：球队数据不足（可能是升班马），跳过
- 法乙：已合并 2 场手录赛果（数据源已经收录的重复行自动忽略）。
- Nantes vs Reims：球队数据不足（可能是升班马），跳过
- Iraklis vs Levadeiakos：球队数据不足（可能是升班马），跳过
- Napoli vs Frosinone：球队数据不足（可能是升班马），跳过
- Benevento vs Cesena：球队数据不足（可能是升班马），跳过
- Sudtirol vs Ascoli：球队数据不足（可能是升班马），跳过
- Vicenza vs Pisa：球队数据不足（可能是升班马），跳过
- Arezzo vs Cremonese：球队数据不足（可能是升班马），跳过
- Modena vs Verona：球队数据不足（可能是升班马），跳过
- Telstar vs Den Haag：球队数据不足（可能是升班马），跳过
- Zwolle vs Cambuur：球队数据不足（可能是升班马），跳过
- 葡超：已合并 1 场手录赛果（数据源已经收录的重复行自动忽略）。
- Maritimo vs Porto：球队数据不足（可能是升班马），跳过
- Academico Viseu vs Estoril：球队数据不足（可能是升班马），跳过
- Sociedad vs La Coruna：球队数据不足（可能是升班马），跳过
- Santander vs Valencia：球队数据不足（可能是升班马），跳过
- Genclerbirligi vs Amedspor：球队数据不足（可能是升班马），跳过
- Alanyaspor vs Erzurumspor：球队数据不足（可能是升班马），跳过
- Gaziantep vs Corum：球队数据不足（可能是升班马），跳过

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。