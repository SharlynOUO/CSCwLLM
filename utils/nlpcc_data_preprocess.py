import pandas as pd
import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--raw_path")
parser.add_argument("--dataset_output_dir_path")
parser.add_argument("--encoding_type")
args = parser.parse_args()

PROMPT = "请纠正此句的错别字:"


def get_dataset(ds_path: str):
    dataset = pd.read_csv(
        ds_path,
        sep="\t",
        names=["source", "target"],
        encoding=args.encoding_type,
    )
    dataset["source"] = dataset["source"].str.strip()
    dataset["target"] = dataset["target"].str.strip()
    return dataset


def to_test_set(dataset_df: pd.DataFrame):
    json_dict = zip(dataset_df["source"], dataset_df["target"])
    ret = []

    for jd in json_dict:
        ret.append(json.dumps({"source": PROMPT + jd[0], "target": jd[1]}) + "\n")
    return ret


def main():
    with open(
        args.dataset_output_dir_path,
        "w",
        encoding=args.encoding_type,
    ) as w:
        w.writelines(to_test_set(get_dataset(args.raw_path)))


if __name__ == "__main__":
    main()
