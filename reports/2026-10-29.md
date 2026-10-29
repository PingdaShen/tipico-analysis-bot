# 投注建议 · 2026-10-29

覆盖 10-29 至 10-30 开赛的比赛 · 本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 2 场比赛

## 联赛

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Fiorentina vs Atalanta | 意甲 | 10-29 20:45 | 客胜 Atalanta | 2.73 | **2.81** | 3.01* | €1.00 |

## 投注 ID

record-bet 表单要填这个（点代码块右上角可直接复制）：

**1. Fiorentina vs Atalanta — 客胜 Atalanta**

```
20261029-I1-Fiorentina-Atalanta-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261029-I1-Fiorentina-Atalanta-A --odds <Tipico赔率> --stake 1.00
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
| Fiorentina vs Atalanta | 客胜 Atalanta + 大于 2.5 球 | 4.05 | **4.17** | 4.81 |
| Fiorentina vs Atalanta | 平局 + 小于 2.5 球 | 5.75 | **5.92** | 9.08 |
| Fiorentina vs Atalanta | 客胜 Atalanta + 小于 2.5 球 | 8.39 | **8.64** | 6.33 |

---
开球时间已换算成德国时间（report.kickoff_offset_hours），仍请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。