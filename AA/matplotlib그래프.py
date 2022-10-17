import numpy as np
import matplotlib데이터가공.pyplot as plt

# 스타일 ggplot
# x=0~100까지 100 나누기
# y=3x+7을 plot그래프 짧은 점선 초록색
plt.style.use('ggplot')
x = np.linspace(0, 100, 100)
y = 3*x + 7
plt.plot(x, y, linestyle='--', color='green')