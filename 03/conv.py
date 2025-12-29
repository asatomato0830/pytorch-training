import torch
from torch import nn

if __name__ == "__main__":

    my_tensor = torch.ones((32, 3, 128, 128))
    print(f"original : {my_tensor.shape}")

    conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3)
    out = conv(my_tensor)
    print(f"out1: {out.shape}")

    conv2 = nn.Conv2d(in_channels=3, out_channels=256, kernel_size=3, stride=2, padding=1)
    out2 = conv2(my_tensor)
    print(f"out2: {out2.shape}")

    conv3= nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5, stride=1, padding=1)
    out3 = conv3(my_tensor)
    print(f"out3: {out3.shape}")