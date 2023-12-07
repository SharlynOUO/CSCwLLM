
bash preprocess.sh

cd competitors/glm
bash train.sh
bash evaluate.sh # just to generate prediction

cd ../..
bash visulize.sh
bash csc_evaluate.sh
