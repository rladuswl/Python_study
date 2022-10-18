import numpy as np
Score = np.random.randint(100, size=(10, 4)) # 국 영 수 과

# x축은 영어, y축은 국어로 흩뿌리기
import matplotlib데이터가공.pyplot as plt
x = Score[:, 1:2]
y = Score[:, :1]
plt.scatter(x, y)