CHECKPOINT=adgen-chatglm-6b-ft-1e-4
STEP=3000

CUDA_VISIBLE_DEVICES=0 python3 main.py \
    --do_predict \
    --validation_file ../../data/validation.json \
    --test_file ../../data/test.json \
    --overwrite_cache \
    --prompt_column source \
    --response_column target \
    --model_name_or_path ./output/$CHECKPOINT/checkpoint-$STEP  \
    --output_dir ./output/$CHECKPOINT \
    --overwrite_output_dir \
    --max_source_length 256 \
    --max_target_length 256 \
    --per_device_eval_batch_size 1 \
    --predict_with_generate \
    --fp16_full_eval
