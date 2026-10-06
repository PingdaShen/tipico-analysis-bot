# Tipico 足球价值投注模型

每天自动分析五大联赛未来两天的比赛，给出"只有 Tipico 赔率高于某个值才下注"的建议。投注由你在 App 里手动完成。

## 上线步骤

1. 在 GitHub 新建一个**私有**仓库，把本项目全部文件推上去。
2. 仓库 Settings → Actions → General → Workflow permissions，选 **Read and write permissions**。
3. Actions 页面先手动运行 **backtest**，看回测结果（ROI 和平均 CLV）。
4. 再手动运行一次 **daily-report**，之后它每天 06:00 UTC 自动运行。
5. 每天打开 `reports/latest.md` 查看建议。

## 每天怎么用

1. 打开 `reports/latest.md`。
2. 在 Tipico App 里找到对应比赛，**赔率 ≥ 表格里的"Tipico 最低赔率"才下注**。
3. 下注后在 GitHub 的 Actions 页面运行 **record-bet**，填入报告里的 ID、实际赔率和注额，手机上也能操作。

建议先只看模拟投注（`bets/paper_ledger.csv`）跑几周，平均 CLV 为正再考虑真钱。

详细设计见 [CLAUDE.md](CLAUDE.md)。本项目不保证盈利，只用亏得起的钱。
