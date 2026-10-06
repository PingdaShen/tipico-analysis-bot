# 今日投注建议 · 2026-10-06

本金 €10 · 最低赔率 1.50 · 最低优势 3% · 分析了 4 场比赛

## 欧战 / 国家队（手填赔率）

这些赛事没有收盘赔率，**无法计算 CLV**，所以不能用主要指标检验；
欧战的跨联赛实力值本身也比联赛模型不确定得多。请当作次要参考。

| # | 比赛 | 赛事 | 日期 | 选项 | 公平赔率 | **Tipico 最低赔率** | 可得赔率 | 注额 |
|---|---|---|---|---|---|---|---|---|
| 1 | Belarus vs Finland | 国家队 | 10-06 20:45 | 主胜 Belarus | 4.20 | **4.32** | 4.50 | €1.00 |
| 2 | Scotland vs Slovenia | 国家队 | 10-06 20:45 | 客胜 Slovenia | 4.68 | **4.82** | 5.00 | €1.00 |

## 投注 ID

record-bet 和 record-close 表单要填这个（点代码块右上角可直接复制）：

**1. Belarus vs Finland — 主胜 Belarus**

```
20261006-INT-Belarus-Finland-H
```

**2. Scotland vs Slovenia — 客胜 Slovenia**

```
20261006-INT-Scotland-Slovenia-A
```

## 怎么用

1. 在 Tipico App 里找到比赛和对应选项。
2. **只有 Tipico 赔率 ≥ 最低赔率时才下注**，否则跳过这一注。
3. 下注后在 Actions 页面跑 **record-bet**，填 ID、实际赔率、注额。
4. **开球前几分钟**在 Actions 页面跑 **record-close**，填那一刻的市场赔率（有 Pinnacle 用 Pinnacle）。
   欧战和国家队没有收盘赔率源，不记就永远算不出 CLV，这些推荐也就无从检验。联赛不用管，收盘价会自动取。

<details><summary>用终端的话</summary>

```bash
python -m src.ledger add 20261006-INT-Belarus-Finland-H --odds <Tipico赔率> --stake 1.00
python -m src.ledger add 20261006-INT-Scotland-Slovenia-A --odds <Tipico赔率> --stake 1.00
# 开球前：
python -m src.ledger close 20261006-INT-Belarus-Finland-H --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
python -m src.ledger close 20261006-INT-Scotland-Slovenia-A --close-h <收盘主胜> --close-d <收盘平> --close-a <收盘客胜>
```

</details>

「可得赔率」带 * 的是市场最高赔率（只说明这个价格在市场上存在，
不一定在 Tipico）；不带 * 的是你自己填进来的 Tipico 赔率。

## 备注
- 赛程源里没有未来几天的联赛比赛（fixtures.csv 的更新频率不稳定）。
- 国家队：已合并 11 场手录赛果（数据源已经收录的重复行自动忽略）。

---
开球时间来自数据源，可能是英国时间，请以 Tipico 显示为准。本报告是模型输出，不保证盈利；只用亏得起的钱。