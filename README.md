# Collect Human Experiences

## Installation
Assuming both python and git installed:
```bash
git clone https://github.com/BAMANEE/CollectHumanExperiences 
cd CollectHumanExperiences
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
  
## Run the experiments 

### MountainCar
Experiment 1 consists of the Mountain Car gym environment.

![](https://www.gymlibrary.dev/_images/mountain_car.gif)

The car is controlled using the left and right arrow of the keyboard. The goal is to reach the yellow flag in the top right with the car as fast as possible. An episode ends if the flag is reached or when the time limit has been exceeded. New episodes start automatically after the previous one finished.

First practice a bit by running:
```bash
python experiment.py 1
```

This will run the environment for 10 episodes and is just for getting to know the environment a bit. 
  
After practice, play for another 10 episodes for real by again running:
```bash
python experiment.py 1
```
Try to play to the best of your ability this time.

### Acrobot
Experiment 2 consists of the Acrobot environment

![](https://www.gymlibrary.dev/_images/acrobot.gif)

The lowest joint is controlled with the left and right arrows on the keyboard. The goal is to get the free end of the chain above the line as fast a possible. An episode one again ends if the goal is reached or if the time limit has been exceeded.
 
First play 10 time episodes as practice by running
```bash
python experiment.py 2
```
  
Then play 10 episodes for real by again running

```bash
python experiment.py 2
```
Where you again try to play to the best of your ability.

## Sent the results
 
When done with the experiments, zip the results folder and send them to me by email at bas.neeleman@ru.nl
