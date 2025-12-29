import torch
from torch import nn

class Mymodel(nn.Module):
    def __init__(self, num_cluss=64):
        super().__init__()

        self.conv = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=5, stride=8, padding=2)
        self.bn = nn.BatchNorm2d(num_features=256)
        self.relu = nn.ReLU()

        self.linear = nn.Linear(in_features=256*16*16, out_features=num_cluss)

    def forward(self, x):
        x = self.conv(x)
        x = self.bn(x)
        x = self.relu(x)
        x = torch.flatten(x, 1)
        x = self.linear(x)
        return x
    
if __name__ == "__main__":

    in_tensor = torch.ones((32, 3, 128, 128))

    model = Mymodel()

    out = model(in_tensor)
    print(f"out : {repr(in_tensor.shape)}")
    print(f"out : {repr(out.shape)}")