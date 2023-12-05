import json
import matplotlib.pyplot as plt
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument("--state_log_path")
# parser.add_argument("--pic_save_path")
# args = parser.parse_args()


def get_state_logs() -> list:
    logs = [
        {"loss": 1.2237, "learning_rate": 0.019933333333333334, "epoch": 1},
        {"loss": 0.591, "learning_rate": 0.019866666666666668, "epoch": 2},
        {"loss": 0.5326, "learning_rate": 0.0198, "epoch": 3},
        {"loss": 0.5149, "learning_rate": 0.019733333333333335, "epoch": 4},
        {"loss": 0.456, "learning_rate": 0.019666666666666666, "epoch": 5},
        {"loss": 0.4644, "learning_rate": 0.0196, "epoch": 6},
        {"loss": 0.3777, "learning_rate": 0.019533333333333333, "epoch": 7},
        {"loss": 0.4416, "learning_rate": 0.019466666666666667, "epoch": 8},
        {"loss": 0.3815, "learning_rate": 0.0194, "epoch": 9},
        {"loss": 0.4626, "learning_rate": 0.019333333333333334, "epoch": 10},
    ]
    loss = []
    lr = []
    epoch = []
    for l in logs:
        loss.append(l["loss"])
        lr.append(l["learning_rate"])
        epoch.append(l["epoch"])

    return loss, lr, epoch


def draw_glm_states(
    log_path: list = None, save_path: str = "pic/", pic_name: str = "logs"
):
    # TODO read log file and release argparser,
    loss, lr, epoch = get_state_logs()

    plt.title(pic_name)
    plt.plot(epoch, loss)
    plt.plot(epoch, lr)
    plt.legend(["loss", "learning_rate"], loc="upper right")
    plt.savefig(save_path + pic_name)


def main():
    draw_glm_states()


if __name__ == "__main__":
    main()
