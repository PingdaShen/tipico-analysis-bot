# Tipico 足球价值投注模型

每天分析欧洲足球比赛，给出"只有 Tipico 赔率高于某个值才下注"的建议。投注由你在 App 里手动完成。

覆盖三类赛事，数据状况差别很大：

| | 赛程 | 赔率 | 能算 CLV |
|---|---|---|---|
| 国内联赛（22 个，含英冠英甲、苏格兰、德乙意乙西乙法乙、荷比葡土希） | 自动 | 自动 | **能** |
| 欧冠 / 欧联 / 欧协联 | **手填** | **手填** | 手记收盘价后能 |
| 国家队（欧国联、世预赛等） | **手填** | **手填** | 手记收盘价后能 |

football-data.co.uk 完全没有欧战和国家队数据，也没有免费替代源同时提供赛程和赔率，
所以这两类赛事的价格需要你自己填进 `manual_fixtures.csv`（手机上可以用 Actions 的
**add-fixture** 表单）。详见 [CLAUDE.md](CLAUDE.md)。

## 先看这个：模型目前没有优势

22 个联赛、最近 2 个完整赛季的回测（3053 注）：**ROI −8.9%，对 Pinnacle 收盘线的
平均 CLV −0.56%**（t = −2.73，统计显著为负）。

汇总里那个看起来是正的 +0.7% CLV 是度量假象：约 20% 的比赛没有 Pinnacle 收盘赔率，
会退回水位高得多的市场平均收盘线，打赢它很容易但说明不了问题。现在这两个口径分开报告。

**结论：按当前参数，这个模型没有可用的优势。** 只跑模拟投注观察，不要投真钱。

## 上线步骤

1. 在 GitHub 新建一个**私有**仓库，把本项目全部文件推上去。
2. 仓库 Settings → Actions → General → Workflow permissions，选 **Read and write permissions**。
3. Actions 页面先手动运行 **backtest**，看 ROI 和 `sharp_clv`。
4. 再手动运行一次 **daily-report**，之后它每天 06:00 UTC 自动运行。
5. 每天打开 `reports/latest.md` 查看建议。

## 每天怎么用

1. 打开 `reports/latest.md`（也可以直接看 Actions 运行摘要，手机上更方便）。
2. 在 Tipico App 里找到对应比赛，**赔率 ≥ 表格里的"Tipico 最低赔率"才下注**。
3. 下注后在 Actions 页面运行 **record-bet**，填入报告里的 ID、实际赔率和注额。
4. 欧战/国家队的注，**开球前几分钟**再跑一次 **record-close**，把那时的市场赔率
   （有 Pinnacle 用 Pinnacle）填进去。这是这些赛事唯一能算出 CLV 的办法；
   不记就只能看长期盈亏。国内联赛不用管，收盘价会自动取。

赛果源有滞后（国家队落后数周，欧战落后一个赛季），报告备注会写明数据截止到哪天。
缺的比赛可以自己补，**但要按比赛窗口整体补，不要只补你关心的那支球队** ——
只补一半会给出反向的结论：

```bash
python -m src.manual result --comp INT --date 2026-09-29 \
    --home Finland --away Belarus --hg 0 --ag 0 --tournament "UEFA Nations League"
```

想让欧战或国家队比赛进入分析，先用 Actions 的 **add-fixture** 填一场的赔率：
参考市场赔率（Pinnacle 优先）+ Tipico 自己的赔率。不要在参考赔率里填 Tipico 的价格，
否则等于拿 Tipico 和自己比，算不出任何优势。

## 工作流

| | 作用 |
|---|---|
| `daily-report` | 每天 06:00 UTC 结算 + 生成报告 + 提交 |
| `backtest` | 手动滚动回测，结果进运行摘要和构件 |
| `record-bet` | 表单记录一注真实投注 |
| `add-fixture` | 表单填欧战/国家队的赛程和赔率 |
| `record-close` | 表单记收盘赔率（开球前几分钟），算出 CLV |

本项目不保证盈利，只用亏得起的钱。
