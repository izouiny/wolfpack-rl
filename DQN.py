import torch.nn as nn
import torch.nn.functional as F

class DQN(nn.Module):
    def __init__(self, grid_size, n_actions):
        super(DQN, self).__init__()
        # we have 4 channels: free, obstacle, wolf, prey
        self.conv = nn.Sequential(
            nn.Conv2d(4, 32, kernel_size=3, stride=1, padding=1), 
            nn.ReLU(),
            nn.Conv2d(32, 64, kernel_size=3, stride=1, padding=1), 
            nn.ReLU()
        )
        self.fc = nn.Sequential(
            nn.Linear(64 * grid_size * grid_size, 256),
            nn.ReLU(),
            nn.Linear(256, n_actions) 
        )

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x