import pyamg
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

N = 10

A = pyamg.gallery.poisson((N,N), format='csr')
ml = pyamg.ruge_stuben_solver(A)

print(ml)

b = np.ones(A.shape[0])
u = ml.solve(b, tol=1e-10)

print("residual:", np.linalg.norm(b-A*u))
print("solution:", u.shape)
# print("shapes:", (A*x))
# print("shapes:", (A@x))
# print("reshapes:", u.reshape((N,N)))


x = np.linspace(0,1,N)
y = np.linspace(0,1,N)
xx, yy = np.meshgrid(x,y)
# print(xx.shape, u.reshape((N,N)).shape)


fig = plt.figure()
ax=fig.add_subplot(1,1,1, projection='3d')
surf = ax.plot_trisurf(xx.flatten(), yy.flatten(), u, linewidth=0.2, antialiased=True, cmap=plt.cm.CMRmap)
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()