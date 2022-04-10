from env import board
from deep_learning import DQNAgent
import pandas as pd

COLUMNS = ['quizzes','solutions']
PATH = "./sudoku.csv"
df_train = pd.read_csv(PATH,
                       skipinitialspace=True,
                       names = COLUMNS,
                       index_col=False)

quizzescount = df_train['quizzes'].count()

def run_maze():
    step = 0
    episodes = 10
    for episode in range(episodes):
        currentstate = env.reset()
        while True:
            action = neuralbrain.choose_action(currentstate)
            futurestate_, reward, done = env.step(action)
            neuralbrain.store_transition(currentstate, action, reward, futurestate_)
            if (step%20  == 0):
                neuralbrain.learn()
            currentstate = futurestate_
            if done:
                break
            step += 1

    print('game over')

if __name__ == "__main__":
    env = board()
    neuralbrain = DQNAgent(env.n_actions, env.n_features,
                      learning_rate=0.1,
                      reward_decay=0.9,
                      e_greedy=0.9,
                      replace_target_iter=50,
                      memory_size=200)
    for i in range(1,101):
        run_maze()
        env._build_maze()