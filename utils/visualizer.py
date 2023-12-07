import json
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--state_log_path")
parser.add_argument("--pic_save_path")
parser.add_argument("--pic_name")
args = parser.parse_args()


def get_state_logs(states) -> list:
    logs = states["log_history"]
    loss = []
    lr = []
    epoch = []
    for l in logs:
        loss.append(l.get("loss"))
        lr.append(l.get("learning_rate"))
        epoch.append(l.get("epoch"))

    return loss, lr, epoch


def draw_glm_states(log_path: list, save_path: str, pic_name: str):
    with open(log_path) as f:
        states = json.load(f)

    loss, lr, epoch = get_state_logs(states)

    plt.title(pic_name)
    plt.plot(epoch, loss)
    plt.plot(epoch, lr)
    plt.legend(["loss", "learning_rate"], loc="upper right")
    plt.savefig(save_path + pic_name)


def main():
    draw_glm_states(args.state_log_path, args.pic_save_path, args.pic_name)


if __name__ == "__main__":
    main()
