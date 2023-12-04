
# for train set
python3 utils/preprocess.py \
    --correct_set_path data/simplified/train15_correct.txt \
    --error_set_path data/simplified/train15_error.txt \
    --dataset_output_dir_path data/train.json \
    --encoding_type utf-8

# for validation set
python3 utils/preprocess.py \
    --correct_set_path data/simplified/test15_correct.txt \
    --error_set_path data/simplified/test15_error.txt \
    --dataset_output_dir_path data/validation.json \
    --encoding_type utf-8

# for test set
python3 utils/preprocess.py \
    --correct_set_path data/simplified/test14_correct.txt \
    --error_set_path data/simplified/test14_error.txt \
    --dataset_output_dir_path data/test.json \
    --encoding_type utf-8


