import argparse
from collect_human_experiences import collect_and_store

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('experiment', type=int, help='experiment to run')

    args = parser.parse_args()

    if args.experiment == 1:
        print("Running experiment 1")
        collect_and_store("MountainCar-v0", "experiences.pkl", 10)
    elif args.experiment == 2:
        print("Running experiment 2")
        collect_and_store("Acrobot-v1", "experiences.pkl", 10)