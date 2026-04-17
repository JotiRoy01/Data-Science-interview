import flappy_bird_gymnasium
import gymnasium as gym
import torch
from dqn import DQN
from experience_replay import ReplayMemory
import itertools
import yaml
import torch.nn as nn
import torch.optimizer as optim

if torch.backends.mps.is_available() :
    device = "mps"
elif torch.cuda.is_available() :
    device = "cuda"
else :
    device = "cpu"

class Agent :
    def __init__(self, param_set) :
        self.param_set = param_set

        with open("parameter.yaml", "r") as f :
            all_param_set = yaml.safe_load(f)
            params = all_param_set[param_set]
        
        #self.env_id = params["env_id"]
        self.epsilon_init = params["epsilon_init"]
        self.epsilon_min = params["epsilon_min"]
        self.epsilon_decay = params["epsilon_decay"]

        self.gamma = params["gamma"]
        self.alpha = params["alpha"]

        self.replay_memory_size = params["replay_memory_size"]
        self.mini_batch_size = params["mini_batch_size"]
        self.network_sync_rate = params["network_sync_rate"]
        self.reward_threshold = params["reward_threshold"]

        self.loss_fn = nn.MSELoss()
        self.optimizer = None

    def run(self, is_traning = True, render = False) :
        env = gym.make("FlappyBird-v0", render_mode="human" if render else None)

        num_states = env.observation_space.shape[0] #input dim
        num_actions = env.action_space.n # output dim

        policy_dqn = DQN(num_states, num_actions).to(device)

        state, _ = env.reset()

        if is_traning :
            memory = ReplayMemory(self.replay_memory_size)
            epsilon = self.epsilon_init

            target_dqn = DQN(num_states, num_actions).to(device)
            # copy the wt & bias vals from policy -> target
            target_dqn.load_state_dict(policy_dqn.state_dict())

            steps = 0

            self.optimizer = optim.Adam(policy_dqn.parameters(), lr=self.alpha)

        for episode in itertools.count() :
            state, _ = env.reset()
            state = torch.tensor(state, dtype=torch.float, device = device)


            while not terminated:
                # Next action:
                # (feed the observation to your agent here)
                if is_traning and random.random() < epsilon :
                    action = env.action_space.sample() # explore
                    action = torch.tensor(action, dtype=torch.long, device = device)
                else :
                    with torch.no_grad() :
                        action = policy_dqp(state.unsqueeze(dim=0)).squeeze().argmax() # exploit

                # Processing:
                next_state, reward, terminated, _, _ = env.step(action.item())

                next_state = torch.tensor(next_state, dtype=torch.long, device = device)
                reward = torch.tensor(reward, dtype=torch.long, device = device)

                if is_traning :
                    memory.append((state, action, new_state, reward, terminated))
                    steps += 1

                state = new_state
                episode_rewards += reward
            
            print(f"for episode = {episode+1} total reward = {episode_rewards}")

            if is_training :
                # epsilon decay
                epsilon = max(epsilon * self.epsilon_decay, self.epsilon_min)
            
            if is_traning and len(memory) > self.mini_batch_size :
                # get sample
                mini_batch = memory.sample(self.mini_batch_size)
                optimizer(mini_batch, policy_dqn, target_dqn)

            # sync the network
            if steps > self.network_sync_rate :
                target_dqn.load_state_dict(policy_dqn.state_dict())
                steps = 0
        #env.close() -> commented beacuse we want to manually stop
    
    def optimize(self, mini_batch, policy_dqn, target_dqn) :
        # get experience
        for state, action, next_state, reward, terminated in mini_batch :
            if terminated :
                target = reward
            else :
                with torch.no_grad() :
                    target_q = reward + self.gamma * target_dqn(next_state).max()

            current_q = policy_dqn(state)

            # loss
            loss = self.loss_fn(current_q, target_q)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
            