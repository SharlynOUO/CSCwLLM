PRE_SEQ_LEN=128
CHECKPOINT=csc-chatglm-6b-pt-128-2e-2
STEP=500

CUDA_VISIBLE_DEVICES=0 python3 main.py \
    --do_predict \
    --validation_file ../../data/test.json \
    --test_file ../../data/test.json \
    --overwrite_cache \
    --prompt_column source \
    --response_column target \
    --model_name_or_path THUDM/chatglm-6b \
    --ptuning_checkpoint ./output/csc-glm-sighan-15-only \
    --output_dir ./output/$CHECKPOINT \
    --overwrite_output_dir \
    --max_source_length 256 \
    --max_target_length 256 \
    --per_device_eval_batch_size 1 \
    --predict_with_generate \
    --pre_seq_len $PRE_SEQ_LEN \
    --quantization_bit 4
