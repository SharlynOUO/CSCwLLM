import argparse
import json

parser = argparse.ArgumentParser()

parser.add_argument("--correct_set_path")
parser.add_argument("--error_set_path")
parser.add_argument("--dataset_output_dir_path")
parser.add_argument("--encoding_type")

args = parser.parse_args()

CORRECT_PATH = args.correct_set_path
ERROR_PATH = args.error_set_path
OUT_DIR = args.dataset_output_dir_path
ENCODING_TYPE = args.encoding_type


def package_query(correct: str, error: str) -> str:
    if len(correct)-len(error) != 0:
        return None
    return json.dumps({"source": "请纠正此句的错别字:"+correct, "target": error})+"\n"


def main():

    srcf = open(CORRECT_PATH, mode="r", encoding=ENCODING_TYPE)
    errf = open(ERROR_PATH, mode="r", encoding=ENCODING_TYPE)
    outf = open(OUT_DIR, mode="w", encoding=ENCODING_TYPE)

    src = srcf.readline()
    tar = errf.readline()

    batch = []
    batch_count = 0
    while src and tar:

        q = package_query(src.strip(), tar.strip())
        if q == None:
            continue
        batch.append(q)
        batch_count += 1

        if batch_count >= 20:
            outf.writelines(batch)
            batch_count = 0
            batch = []

        src = srcf.readline()
        tar = errf.readline()

    if batch_count != 0:
        outf.writelines(batch)

    srcf.close()
    errf.close()
    outf.close()


if __name__ == '__main__':
    main()
