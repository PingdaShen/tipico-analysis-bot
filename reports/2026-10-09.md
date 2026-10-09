# 今日投注建议 · 2026-10-09

本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 112 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Inverness C vs Stenhousemuir | 苏冠 | 10-10 15:00 | 客胜 Stenhousemuir | 2.88 | **2.97** | 4.20* | €1.00 |
| 2 | Barcelona vs Getafe | 西甲 | 10-10 17:30 | 小于 2.5 球 | 3.19 | **3.29** | 4.00* | €1.00 |
| 3 | Doncaster vs Burton | 英甲 | 10-10 15:00 | 客胜 Burton | 4.15 | **4.27** | 5.00* | €1.00 |
| 4 | Shrewsbury vs Exeter | 英乙 | 10-10 15:00 | 平局 | 2.97 | **3.06** | 3.40* | €1.00 |
| 5 | Chelsea vs Bournemouth | 英超 | 10-10 15:00 | 客胜 Bournemouth | 4.17 | **4.30** | 4.75* | €1.00 |

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

**3. Doncaster vs Burton — 客胜 Burton**

```
20261010-E2-Doncaster-Burton-A
```

**4. Shrewsbury vs Exeter — 平局**

```
20261010-E3-Shrewsbury-Exeter-D
```

**5. Chelsea vs Bournemouth — 客胜 Bournemouth**

```
20261010-E0-Chelsea-Bournemouth-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261010-SC1-InvernessC-Stenhousemuir-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261010-SP1-Barcelona-Getafe-U25 --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261010-E2-Doncaster-Burton-A --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261010-E3-Shrewsbury-Exeter-D --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261010-E0-Chelsea-Bournemouth-A --odds <Tipico赔率> --stake 1.00
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
| Chelsea vs Bournemouth | 客胜 Bournemouth + 大于 2.5 球 | 5.93 | **6.10** | 6.69 |
| Chelsea vs Bournemouth | 平局 + 小于 2.5 球 | 6.40 | **6.59** | 11.27 |
| Chelsea vs Bournemouth | 平局 + 大于 2.5 球 | 12.63 | **13.01** | 6.81 |
| Chelsea vs Bournemouth | 客胜 Bournemouth + 小于 2.5 球 | 14.09 | **14.51** | 11.07 |
| Doncaster vs Burton | 平局 + 小于 2.5 球 | 5.29 | **5.45** | 8.03 |
| Doncaster vs Burton | 客胜 Burton + 大于 2.5 球 | 7.11 | **7.32** | 8.24 |
| Doncaster vs Burton | 客胜 Burton + 小于 2.5 球 | 9.97 | **10.27** | 8.37 |
| Shrewsbury vs Exeter | 平局 + 小于 2.5 球 | 3.19 | **3.29** | 4.47 |
| Shrewsbury vs Exeter | 主胜 Shrewsbury + 小于 2.5 球 | 5.15 | **5.30** | 4.13 |
| Shrewsbury vs Exeter | 客胜 Exeter + 小于 2.5 球 | 6.41 | **6.61** | 5.06 |
| Inverness C vs Stenhousemuir | 平局 + 小于 2.5 球 | 3.78 | **3.89** | 5.68 |
| Inverness C vs Stenhousemuir | 客胜 Stenhousemuir + 大于 2.5 球 | 4.96 | **5.11** | 7.56 |
| Inverness C vs Stenhousemuir | 客胜 Stenhousemuir + 小于 2.5 球 | 6.87 | **7.07** | 4.65 |
| Barcelona vs Getafe | 主胜 Barcelona + 小于 2.5 球 | 4.66 | **4.80** | 3.76 |
| Barcelona vs Getafe | 平局 + 小于 2.5 球 | 12.82 | **13.21** | 30.96 |
| Barcelona vs Getafe | 客胜 Getafe + 大于 2.5 球 | 37.35 | **38.47** | 30.84 |
| Barcelona vs Getafe | 客胜 Getafe + 小于 2.5 球 | 48.91 | **50.38** | 67.62 |

## 备注
- Beveren vs Lommel SK：球队数据不足（可能是升班马），跳过
- Paderborn vs Stuttgart：球队数据不足（可能是升班马），跳过
- Union Berlin vs Elversberg：球队数据不足（可能是升班马），跳过
- Heidenheim vs Kaiserslautern：球队数据不足（可能是升班马），跳过
- Darmstadt vs Cottbus：球队数据不足（可能是升班马），跳过
- Osnabruck vs Dresden：球队数据不足（可能是升班马），跳过
- Nurnberg vs Wolfsburg：球队数据不足（可能是升班马），跳过
- Middlesbrough vs Wolves：球队数据不足（可能是升班马），跳过
- Notts County vs Oxford：球队数据不足（可能是升班马），跳过
- Huddersfield vs Sheffield Weds：球队数据不足（可能是升班马），跳过
- Leicester vs Peterboro：球队数据不足（可能是升班马），跳过
- Mansfield vs Bromley：球队数据不足（可能是升班马），跳过
- Milton Keynes Dons vs Reading：球队数据不足（可能是升班马），跳过
- York vs Northampton：球队数据不足（可能是升班马），跳过
- Paris SG vs Le Mans：球队数据不足（可能是升班马），跳过
- Sochaux vs Boulogne：球队数据不足（可能是升班马），跳过
- Nantes vs Reims：球队数据不足（可能是升班马），跳过
- Napoli vs Frosinone：球队数据不足（可能是升班马），跳过
- Benevento vs Cesena：球队数据不足（可能是升班马），跳过
- Sudtirol vs Ascoli：球队数据不足（可能是升班马），跳过
- Vicenza vs Pisa：球队数据不足（可能是升班马），跳过
- Arezzo vs Cremonese：球队数据不足（可能是升班马），跳过
- Maritimo vs Porto：球队数据不足（可能是升班马），跳过
- Academico Viseu vs Estoril：球队数据不足（可能是升班马），跳过
- Malaga vs Espanol：球队数据不足（可能是升班马），跳过
- Genclerbirligi vs Amedspor：球队数据不足（可能是升班马），跳过
- Alanyaspor vs Erzurumspor：球队数据不足（可能是升班马），跳过

---
开球时间来自数据源，可能是英国时间，请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。