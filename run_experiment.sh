python train.py --ename ./experiments/thompson_run_0 --lconfig ./configs/learning_config.json --iter 10000 --reset yes > learning_out/out1.out

python train.py --ename ./experiments/upper_confidence_bound_run_0 --lconfig ./configs/learning_config_ucb.json --iter 2000 --reset yes > learning_out/out2.out

python train.py --ename ./experiments/epsilon_greedy_run_0 --lconfig ./configs/learning_config_ep.json --iter 10000 --reset yes > learning_out/out3.out

python train_compose.py --ename ./experiments/thompson_run_compose_0 --lconfig ./configs/learning_config.json --iter 100000 --reset yes > learning_out/out4.out

python train_compose.py --ename ./experiments/upper_confidence_bound_compose_run_0 --lconfig ./configs/learning_config_ucb.json --iter 100000 --reset yes > learning_out/out5.out

python train_compose.py --ename ./experiments/epsilon_greedy_compose_run_0 --lconfig ./configs/learning_config_ep.json --iter 100000 --reset yes > learning_out/out6.out