from transformers import AutoConfig, AutoModel, AutoTokenizer


class glm4csc:
    # 载入Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(
        "THUDM/chatglm-6b", trust_remote_code=True)
