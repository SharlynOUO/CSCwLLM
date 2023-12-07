
# for train set
python3 utils/preprocess.py \
    --correct_set_path data/simplified/train13_correct.txt \
    --error_set_path data/simplified/train13_error.txt \
    --dataset_output_dir_path data/train.json \
    --encoding_type utf-8

# for validation set
python3 utils/preprocess.py \
    --correct_set_path data/simplified/test13_correct.txt \
    --error_set_path data/simplified/test13_error.txt \
    --dataset_output_dir_path data/validation.json \
    --encoding_type utf-8

# for test set
python3 utils/nlpcc_data_preprocess.py \
    --raw_path data/nlpcc_data.txt \
    --dataset_output_dir_path data/test.json \
    --encoding_type utf-8


