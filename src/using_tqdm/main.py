from tqdm import tqdm
import time


def main():
    p_bar = tqdm(total=100)
    def increment():
        p_bar.update(1)
    for i in range(100):
        increment()
        time.sleep(0.01)


if __name__ == "__main__":
    main()
