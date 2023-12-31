PRE_SEQ_LEN=128
LR=2e-2

CUDA_VISIBLE_DEVICES=0 python3 main.py \
    --do_train \
    --train_file ../../data/train.json \
    --validation_file ../../data/validation.json \
    --prompt_column source \
    --response_column target \
    --overwrite_cache \
    --model_name_or_path THUDM/chatglm-6b \
    --ptuning_checkpoint ./output/csc-glm-sighan-1514 \
    --output_dir output/csc-chatglm-6b-pt-$PRE_SEQ_LEN-$LR \
    --overwrite_output_dir \
    --max_source_length 256 \
    --max_target_length 256 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 16 \
    --predict_with_generate \
    --max_steps 1000 \
    --logging_steps 10 \
    --save_steps 500 \
    --learning_rate $LR \
    --pre_seq_len $PRE_SEQ_LEN \
    --quantization_bit 4

