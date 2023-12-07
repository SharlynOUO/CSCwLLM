# encoding=utf-8
import argparse
import json
import re

parser = argparse.ArgumentParser(
    description="GEC OpenNMT Service",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)
parser.add_argument("--gold_file", default="test1.txt", help="input file path")
parser.add_argument("--modelout_file", default="test2.txt", help="input file path")
opt = parser.parse_args()

PROMPT = "请纠正此句的错别字:"
PROMPTLEN = len(PROMPT)


def change_punctuation(sentence: str):
    punctuation = r"[、＂\\…,，\.。\[【】\]、\":：;；\?？!！\|\'‘’“”——\^……（）\(\)\b%％]+"
    sentence = re.sub(punctuation, "", sentence)
    return sentence


def main():
    sents = {}

    with open(opt.gold_file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            lines = json.loads(line)
            src = change_punctuation(lines.get("source")[PROMPTLEN:])
            tar = change_punctuation(lines.get("target"))
            sents[tar] = [
                src,
                tar,
            ]
    with open(opt.modelout_file, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            lines = json.loads(line)
            # output中的labels相当于goldfile中的target
            # print(line)
            sents[change_punctuation(lines.get("labels"))].append(
                change_punctuation(lines.get("predict"))
            )

    # 顺序按照：source，target，output排列
    TP = 0
    FP = 0
    FN = 0

    for value in sents.values():
        minlen = min(len(value[0]), len(value[1]), len(value[2]))
        src = value[0][:minlen]
        tar = value[1][:minlen]
        pred = value[2][:minlen]
        if src != tar and tar == pred:  # 正确识别错误的句子数
            TP += 1
        if src == tar and src != pred:  # 非错别字被误报为错别字
            FP += 1
        if src != tar and tar != pred:  # 未能正确识别错别字
            FN += 1
    al_wro = TP + FP
    wro = TP + FN
    cor = TP
    try:
        precision = round((cor / al_wro) * 100, 2)
    except:
        precision = "-"
    try:
        recall = round((cor / wro) * 100, 2)
    except:
        recall = "-"
    try:
        f1 = round(precision * recall * 2 / (precision + recall), 2)
    except:
        f1 = "-"
    print(f"precision：{precision}({cor}/{al_wro})")
    print(f"recall：{recall}({cor}/{wro})")
    print(f"F1：{f1}")


if __name__ == "__main__":
    main()
