"""analyze_log.py —— 从训练日志里提取 loss 并做统计

用法：
    python analyze_log.py train.log            # 只做统计
    python analyze_log.py train.log --plot      # 额外画 loss 曲线（需 matplotlib）
"""
import argparse
import re


def parse_loss(log_path):
    """从日志里提取所有 loss 值。

    匹配形如 loss=0.123 或 loss: 0.123 或 "loss": 0.123 的行。
    """
    pattern = re.compile(r"loss[\"'=: ]*([\d.]+)")
    losses = []
    with open(log_path, encoding="utf-8") as f:
        for line in f:
            m = pattern.search(line)
            if m:
                losses.append(float(m.group(1)))
    return losses


def report(losses):
    """打印统计信息。"""
    n = len(losses)
    print(f"共提取 {n} 条 loss 记录")
    print(f"首条: {losses[0]:.4f}    末条: {losses[-1]:.4f}")
    print(f"最小: {min(losses):.4f}    最大: {max(losses):.4f}")
    print(f"平均: {sum(losses) / n:.4f}    下降: {losses[0] - losses[-1]:.4f}")


def plot_loss(losses):
    """画 loss 曲线（可选）。"""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("未安装 matplotlib，跳过绘图（pip install matplotlib）")
        return
    plt.plot(losses)
    plt.xlabel("step")
    plt.ylabel("loss")
    plt.title("training loss")
    plt.grid(True)
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="分析训练日志中的 loss")
    parser.add_argument("log", help="日志文件路径")
    parser.add_argument("--plot", action="store_true", help="画 loss 曲线")
    args = parser.parse_args()

    losses = parse_loss(args.log)
    if not losses:
        print("没找到 loss，检查日志里是否含 loss=xxx / loss: xxx 格式")
        return

    report(losses)
    if args.plot:
        plot_loss(losses)


if __name__ == "__main__":
    main()
