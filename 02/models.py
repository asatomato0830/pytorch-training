import torch
from torch import nn

class Mymodel(nn.Module):
    def __init__(self, mytensor: torch.Tensor, elem_add: int, elem_multiply: int):
        super().__init__()
        self.mytensor = mytensor
        self.elem_add = elem_add
        self.elem_multiply =  elem_multiply

    def forward(self, x: torch.Tensor):
        assert x.size() == self.mytensor.size(), "Input tensor size must match mytensor size"
            
        problem2 = x + self.mytensor
        problem3 = problem2 + self.elem_add
        problem4 = problem3 * self.elem_multiply
            
        return problem2, problem3, problem4
            

        
if __name__ == "__main__":

    mymodel = Mymodel(torch.ones(3,3), 4, 6)

    output2, output3, output4 = mymodel(torch.full((3,3), 2))

    print("Output of Problem 2:\n", output2)
    print("Output of Problem 3:\n", output3)    
    print("Output of Problem 4:\n", output4)
