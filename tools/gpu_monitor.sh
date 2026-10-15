#!/bin/bash
# gpu_monitor.sh —— 定时记录 GPU 状态到日志
# 用法：
#   ./gpu_monitor.sh 5      每 5 秒记录一次
#   ./gpu_monitor.sh        默认 5 秒
# 停止：Ctrl+C

INTERVAL=${1:-5}   # 第一个参数是间隔秒数，没传就用默认 5

echo "开始监控 GPU，每 ${INTERVAL} 秒记录一次，Ctrl+C 停止..."

while true; do
    # 取当前时间
    TS=$(date '+%Y-%m-%d %H:%M:%S')

    # 取 GPU 利用率/显存，输出机器可读的 csv 格式（去表头、去单位）
    GPU=$(nvidia-smi --query-gpu=utilization.gpu,memory.used,memory.total \
                     --format=csv,noheader,nounits)

    # tee -a：既打印到屏幕，又追加写入 gpu.log
    echo "${TS}, ${GPU}" | tee -a gpu.log

    sleep "${INTERVAL}"
done
