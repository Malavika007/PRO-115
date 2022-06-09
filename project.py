import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('escape_velocity.csv')
Velocity_list = df['Velocity'].tolist()
Escaped_list = df['Escaped'].tolist()

fig = px.scatter(x=Velocity_list, y=Escaped_list)
fig.show()

velocity_array = np.array(Velocity_list)
escaped_array = np.array(Escaped_list)

m, c = np.polyfit(velocity_array, escaped_array, 1)
y = []

for x in velocity_array:
    y_value = m * x + c
    y.append(y_value)

fig = px.scatter(x = velocity_array, y= escaped_array)
fig.update_layout(shapes = [
    dict(
        type = 'line',
        y0 = min(y), y1 = max(y),
        x0 = min(velocity_array), x1 = max(velocity_array)
    )
])
fig.show()

X = np.reshape(Velocity_list, (len(Velocity_list), 1))
Y = np.reshape(Escaped_list, (len(Escaped_list), 1))

lr =LogisticRegression()
lr.fit(X, Y)

plt.figure()
plt.scatter(X.ravel(), y, color='black', zorder = 20)

def model(x):
  return 1 / (1 + np.exp(-x))

X_test = np.linspace(0, 5000, 10000)
escape_chances = model(X_test * lr.coef_ + lr.intercept_).ravel()


plt.plot(X_test, escape_chances, color='red', linewidth=3)
plt.axhline(y=0, color='k', linestyle='-')
plt.axhline(y=1, color='k', linestyle='-')
plt.axhline(y=0.5, color='b', linestyle='--')

plt.axvline(x=X_test[6843], color='b', linestyle='--')

plt.ylabel('y')
plt.xlabel('X')
plt.xlim(3400, 3450)
plt.show()
print(X_test[6843])
