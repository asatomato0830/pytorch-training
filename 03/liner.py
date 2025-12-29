import torch
from torch import nn

if __name__ == "__main__":
    #　入力用テンソル
    _in = torch.ones((32, 1024))
    print(f"_in : {_in.shape}")

    fc = nn.Linear(in_features=1024, out_features=256, bias=True)
    out = fc(_in)
    print(f"out : {out.shape}")

    fc2 = nn.Linear(in_features=256, out_features=2048, bias=False)
    out2 = fc2(out)
    print(f"out2 : {out2.shape}")

    out3 = out.view(32, 16, 16)
    print(f"out3 : {out3.shape}")