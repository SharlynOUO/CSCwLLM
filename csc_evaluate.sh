CHECKPOINT=csc-chatglm-6b-pt-128-2e-2
STEP=1500

# test glm output
python3 utils/evaluate.py \
    --gold_file data/test.json\
    --modelout_file competitors/glm/output/$CHECKPOINT/generated_predictions.txt
