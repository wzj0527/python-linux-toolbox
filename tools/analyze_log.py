import re
import argparse
parser = argparse.ArgumentParser()# 造一个解析器
parser.add_argument("log")# 声明我要接受一个参数名字叫log
args = parser.parse_args()# 真正去解析命令行，结果存进 args
pattern = re.compile(r'loss=([\d.]+)')# 预编译，生成一个重复可用的匹配规则
# 这里的匹配规则是找到loos=，[\d.]匹配数字字符或者. # +匹配前一个规则的字符出现1至无数次
losses = []
with open(args.log,encoding="utf-8") as f:
    for line in f:
        m = pattern.search(line)#  在这一行里找模板，找到返回"匹配对象"，找不到返回 None
        if m:
            losses.append(float(m.group(1)))
             # group(1) = 第一个括号抓到的东西
print(losses)
print("共",len(losses),"条")
print("首条：",losses[0],"末条：",losses[-1])
print("最小：",min(losses),"最大:",max(losses))
print("平均：",sum(losses)/len(losses))