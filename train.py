from learn.learner import Learner
from tools.runner import run
from tools.updater import update
import pandas as pd
from tools.state_generator import get_state_transition
import yaml
import json
from learn.utils import FileHandler, get_file_suffix_map
import os
import shutil
from tools.env_generator import generate_env, generate_init_env

total_iter = 200

# Initial configuration is should be in /runs/intersection
runner_config = './configs/config.yaml'
learning_config = './configs/learning_config'

with open(runner_config, "r") as f:
    runner_config = yaml.safe_load(f)

with open(learning_config, "r") as f:
    learning_config = json.load(f)

runner_config['configs']['sumo_loc'] = 'runs/intersection'
# Project name won't change
learning_config['state'], learning_config['transition'] = get_state_transition()

filehandler1 = FileHandler('intersection_0', get_file_suffix_map(learning_config['exploration']))
filehandler2 = FileHandler('intersection_1', get_file_suffix_map(learning_config['exploration']))
filehandler3 = FileHandler('intersection_2', get_file_suffix_map(learning_config['exploration']))
# run(runner_config) # Initial run

for i in range(total_iter):
    print(f'---------------------------Learning start round {i}-----------------------------------------')
    runner_config['configs']['sumo_loc'] += '_' + str(i)

    run(runner_config)

    if i != 0:
        env = generate_env(f'runs/intersection_{i}',filehandler.get_local_path('action_hist'))
    else:
        env = generate_init_env()

    for j in range(3):
        learning_config['task_name'] = f'intersection_{j}'
        learner = Learner(learning_config)
        learner.run_learning(env)

    param = [{'duration': '33', 'state': 'GGGrrrGGGrrrrrr'},
        {'duration': '6', 'state': 'yyyrrryyyrrrrrr'},
        {'duration': '33', 'state': 'rrrGGGrrrrrrrrr'},
        {'duration': '6', 'state': 'rrryyyrrrrrrrrr'},
        {'duration': '33', 'state': 'rrrrrrrrrGGGGGG'},
        {'duration': '6', 'state': 'rrrrrrrrryyyyyy'}]

    param[0]['duration'] = pd.read_csv(filehandler1.get_local_path('update_content').iloc[-1]['g'])
    param[2]['duration'] = pd.read_csv(filehandler2.get_local_path('update_content').iloc[-1]['g'])
    param[4]['duration'] = pd.read_csv(filehandler3.get_local_path('update_content').iloc[-1]['g'])

    os.mkdir(f'./runs/intersection_{i+1}')
    shutil.copytree(src=f'intersection_{i}', dst=f'intersection_{i+1}')

    update(param_out=param, path=f'intersection_{i+1}')

    # Revert back
    runner_config['configs']['sumo_loc'] = runner_config['configs']['sumo_loc'][:-2]

