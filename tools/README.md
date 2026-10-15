# tools/ —— 阶段一小工具

## gpu_monitor.sh

定时记录 GPU 利用率 / 显存到日志，训练时监控显卡状态。

```bash
./gpu_monitor.sh 5        # 每 5 秒记录一次
./gpu_monitor.sh          # 默认 5 秒
```

输出示例（追加写入 gpu.log）：

```
2026-10-15 16:00:00, 85, 12345, 24576
```

用到的技术点：`nvidia-smi --query-gpu`、`while` 循环、`tee -a`、带默认值的传参 `${1:-5}`。

## analyze_log.py

从训练日志里提取 loss 并统计 / 画曲线。

```bash
python analyze_log.py sample_train.log          # 只做统计
python analyze_log.py sample_train.log --plot   # 额外画曲线（需 matplotlib）
```

输出示例：

```
共提取 9 条 loss 记录
首条: 2.3026    末条: 1.0880
最小: 1.0880    最大: 2.3026
平均: 1.6474    下降: 1.2146
```

用到的技术点：正则提取、`argparse`、文件读取、`matplotlib`（可选）。
