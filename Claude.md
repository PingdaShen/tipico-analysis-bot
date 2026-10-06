# CLAUDE.md · Tipico 足球价值投注模型
 
本文件是给 Claude Code 的项目说明。开始任何修改前请完整阅读，尤其是"硬性规则"。
 
## 项目目标
 
为欧洲足球（包括但不仅限于五大联赛，欧冠，欧联杯，欧协联，欧国联等）每天生成投注建议，用户在 Tipico App 里**手动**下注。
如果当天有值得下单的其他足球比赛，也给用户进行推荐。
本金很小（10 欧 - 30 欧），目标不是赚大钱，而是：在严格的纪律下，尽量做出正期望的选择，并用数据诚实地评估模型是否真的有优势。
除了基本的胜负推荐外，还可进行下注组合，例如：胜负+大小球
 
## 硬性规则（不可违反）
 
1. **不自动下单。** 不写任何登录 Tipico、模拟点击、调用 Tipico 接口或抓取 Tipico 网站的代码。所有投注由用户本人在 App 里完成。
2. **不处理账户凭证。** 不索要、不存储、不在代码、配置、日志、Secrets 或提交记录里写入任何 Tipico 账号密码。
3. **不绕过监管。** 不涉及 LUGAS / OASIS 规避、VPN、海外无牌照平台或 Polymarket。
4. **不承诺盈利。** 报告和文档里不出现"稳赚""保证盈利"之类的表述。
5. **不做加注追损。** 不实现马丁格尔、斐波那契等亏损后加倍的注码方法。
6. **无前视偏差。** 任何拟合和回测只能使用预测时点之前的数据（`DixonColes.fit` 只用 `date < ref_date` 的比赛）。

## 用户背景与偏好
 
- 熟悉欧洲足球，了解绝大部分欧洲俱乐部以及国家队（英超、西甲、德甲、意甲、法甲、欧冠、欧联、欧协联、欧国联等）。
- 联赛不仅限于甲级，国家队不仅限于欧洲传统强队。
- 本金 10 欧至30 欧；可能会使用 Tipico 首存奖金，奖金流水要求最低赔率 1.50（配置里的 `value.min_odds`）。
- 模型的推理预测数据除了关注赔率等信息之外，还应和比赛信息、球员状态、球队战术等专业信息相结合，从而作出预测。
- 偏好：少而精的推荐，宁可不下注也不要勉强的注。
- 报告用中文，表格要能在手机上的 GitHub 页面阅读。

## 架构
 
```
config.yaml              所有可调参数（不要在代码里写死数值）
src/data.py              从 football-data.co.uk 下载历史赛果/赔率和未来赛程，带本地缓存
src/model.py             Dixon-Coles 模型（时间衰减 + 低比分修正 + 解析梯度）
src/market.py            赔率列映射、去水、收盘赔率、赛果判定
src/value.py             概率融合、最低可接受赔率、候选筛选、注额
src/daily.py             每日入口：拟合 → 评估 → 写报告 → 记录模拟投注
src/ledger.py            真实/模拟投注记录：添加、自动结算、汇总（ROI、CLV）
src/backtest.py          逐周滚动回测（用 Bet365 赔率代替 Tipico）
tests/                   离线测试（合成联赛数据，不依赖网络）
.github/workflows/       daily.yml 每天运行；backtest.yml 手动回测；record-bet.yml 网页表单记录投注
reports/                 每日报告 latest.md、YYYY-MM-DD.md 及 CSV
bets/                    ledger.csv（真实）、paper_ledger.csv（模拟）
```
 
## 模型与选注逻辑
 
1. **模型概率**：每个联赛单独拟合 Dixon-Coles，训练窗口为最近 `history_seasons` 个赛季，按 `xi` 做时间衰减。球队训练场次少于 `min_team_matches`（如升班马）时不出推荐。
2. **市场概率**：Pinnacle 赔率（`PSH/PSD/PSA`、`P>2.5/P<2.5`）按比例去水；没有时退回市场平均赔率。
3. **最终概率**：`p_final = w * p_model + (1 - w) * p_market`，`w = blend.model_weight`。市场是锚，模型只负责发现偏差。
4. **最低可接受赔率**：`min_odds = max((1 + min_edge) / p_final, value.min_odds)`。用户只在 Tipico 赔率 ≥ 这个值时下注。
5. **候选条件**（全部满足）：模型概率高于市场概率；`min_odds ≤ max_odds`；市场最高赔率 `Max*` ≥ `min_odds`（说明这个价格在市场上真实存在）。
6. **排序与数量**：按市场最高赔率下的优势排序，每场比赛最多一注，最多 `max_picks` 注。
7. **注额**：本金小时用 `flat`（固定 1 欧）；本金变大后可改 `kelly`（1/4 凯利，单注上限为本金的 `max_stake_pct`）。注额按 `stake_step` 取整。

## 评估标准
 
- **主要指标是 CLV**（实际赔率 / 收盘赔率 − 1），不是短期盈亏。至少几百注后再判断模型是否有效。
- 模拟投注按 `min_odds` 记账（假设刚好拿到最低可接受价格），这是偏保守的估计。
- 如果回测和模拟投注的平均 CLV 长期 ≤ 0，应如实报告"模型没有优势"，而不是继续调参直到回测好看（避免过拟合）。

## 常用命令
 
```bash
pip install -r requirements.txt
python -m pytest -q                       # 离线测试
python -m src.daily                        # 生成今天的报告
python -m src.daily --date 2026-10-10      # 指定日期
python -m src.backtest --seasons 2         # 回测最近 2 个完整赛季
python -m src.ledger add <ID> --odds 2.10 --stake 1
python -m src.ledger settle                # 自动结算已结束的比赛
python -m src.ledger summary               # 真实/模拟投注汇总
```
 
## 开发规范
 
- 新功能必须有离线测试；测试不访问网络（用 `tests/synthetic.py` 和注入的 loader）。
- 数值参数一律放进 `config.yaml`。
- 修改模型或选注逻辑后，先跑回测，在提交说明里写出回测前后 ROI 和 CLV 的变化。
- 报告措辞保持中性，不夸大。

## 已知限制

- `fixtures.csv` 的更新频率我们没有核实；如果当天没有赛程数据，报告会显示没有推荐。
- 开球时间可能是英国时间。
- Tipico 的最低注额、奖金条款需要用户在 App 里确认后写进 `config.yaml`。
