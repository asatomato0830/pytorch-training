import numpy as np
import torch

data = np.array([
    [[85,78], [67,82], [92,88], [75,70], [60,64]],
    [[70,68], [77,72], [85,90], [60,65], [78,76]],
    [[80,84], [88,87], [66,68], [72,73], [64,60]]  
])

# 1.Numpy配列をTesorに変換
tensor = torch.from_numpy(data)
tensor = torch.tensor(data, dtype=float)
print(tensor.shape)

# 2.2科目、3クラス、各クラス５人に並び替える
per_tensor = torch.permute(tensor, (2,0,1))
print(per_tensor)

# 3.2で作成したデータからクラスごと、個々人の２科目の合計点
total_score = torch.sum(per_tensor, dim = 0)
print(total_score)

# 4.3で作成したデータからクラスごと、2科目合計点の平均
avr_score = torch.mean(total_score, dim = 1)
print(avr_score)

# 5.3で作成したデータからtorch.meanを使わずに4と同じものを導出
tmp_sucorem = total_score.sum(dim = 1)
num_student = total_score.size(dim=1)
manual_avr_score = tmp_sucorem / num_student
print(manual_avr_score)