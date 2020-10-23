import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from scipy.optimize import linprog

x = np.linspace(start=0, stop=10, num=101)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure()
plt.plot(x, y_sin, label='sin(x)')
plt.plot(x, y_cos, label='cos(x)')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()

# EXAMPLE

# generate the data
x = np.linspace(0,2*np.pi, 100)
delta = x[1]-x[0] # compute the step for derivative filter
y_sin = np.sin(x)
y_sin_noisy = y_sin + 0.1*np.random.random(y_sin.shape)

# define filters
diff_filter = np.array([1/(2*delta),0,-1/(2*delta)])
moving_avg_filter = np.array([1/5,1/5,1/5,1/5,1/5])

# apply filters
dy_sin_noisy = np.convolve(y_sin_noisy, diff_filter, mode='same')
y_sin_smooth = np.convolve(y_sin_noisy, moving_avg_filter, mode='same')

# plot the data
plt.figure()
plt.plot(x, y_sin_noisy, label='sin(x)+eps')
plt.plot(x, dy_sin_noisy, label='derivative')
plt.plot(x, y_sin_smooth, label='moving avg')
plt.legend()
plt.show()

# UPPGIFT 1

a = np.array(range(1, 6))
# print(a)
# print(a[4])
# print(a.shape)
# print(type(a))

b = np.arange(0, 2*np.pi, 0.1)
# print(b)
# print(b.shape)
# print(type(b))

c = np.arange(1, 7).reshape(3, 2)
# print(c)

d = np.hstack([a, np.array([6, 7])])
# print(d)

e = np.vstack([a, np.array(range(-1, -6, -1))])
# print(e)
# print(e.shape)

f = np.sin(b)
# print(f)


# UPPGIFT 2


def funtion_a(x):
    return x*x


def funtion_b2(x):
    return np.dot(x, x)


def funtion_c1(x):
    return x*x


def function_c2(x):
    return x@x.T


x = np.arange(0, 11, 1.2)
print(funtion_a(x))

y = np.array([1, 2, 3])
print(funtion_b2(y))

z = np.array(range(1, 10)).reshape(3, -1)
print(z)
print(funtion_c1(z))
print(z.shape)

w = np.array(range(1, 17)).reshape(2, -1)
print(w)
print(function_c2(w))


# UPPGIFT 3

def function_envar(x):
    return 1 + x + 4/((x-2)**2)

x = np.arange(-10,10,0.1)
y = np.array([function_envar(xi) for xi in x])
asy1 = x+1
plt.figure()
plt.plot(x,y)
plt.plot([2,2],[999,-999])
plt.plot(x,asy1)
plt.axis([-10,10,-10,20])
plt.show()


# UPPGIFT 4


def funciton_upp4(x):
    return 1+math.sin(x)+0.5*math.cos(4*x)


precision = .6

x = np.arange(-5, 5, 0.1)
tmp = x*0 + np.sin(x)
tmp1 = x*4
tmp2 = x*0 
tmp2 = np.sin(tmp1)
tmp2 = tmp2 * 2
tmp3 = x*0 + np.cos(x)
tmp1 = np.cos(tmp1)
tmp1 = tmp1*0.5 
y = tmp + tmp1 + 1
y1 = tmp3 - tmp2


der_fx = np.array(
    [(funciton_upp4(z+precision)-funciton_upp4(z))/precision for z in x])


plt.figure()
plt.plot(x, der_fx, label="f'(x)_approx")
plt.plot(x, y1, label="f'(x)")
plt.plot(x, y, label='f(x)')
plt.grid()
plt.legend()
plt.show()


# UPPGIFT 5

# def function_x(x):
#     return x/((x**2+4)**(1/3))


def function_x(x):
    return math.sqrt(x)*math.log(x)


low = 1
upp = 4
dx = .01
x = np.arange(low, upp, dx)
y = np.array([function_x(x1) for x1 in x])
index = 0
integral = 0
pos = 0

fig, ax = plt.subplots(1)

plt.plot(x, y)
for xi in x:
    if xi >= low and xi <= upp:
        integral += y[index]*dx
        ax.add_patch(patches.Rectangle((xi, 0), dx, y[index]))
        pos += dx
    index += 1
plt.plot(0, 0, label=str(integral))
plt.legend()
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.show()


# UPPGIFT 6

def function_t(t, a, b):
    return math.exp(-t)*(a*math.cos(t)+b*math.sin(t))+math.cos(t)+2*math.sin(t)


a = np.arange(-5,5,1)
b = np.arange(-5,5,1)
x = np.arange(0, 10, 0.1)
plt.figure()
for a1 in a:
    for b1 in b:
        y = np.array([function_t(t1, a1, b1) for t1 in x])
        plt.plot(x, y)
    
plt.show()


# UPPGIFT 7

def taylor_sin(x, n):
    sum = 0
    for n1 in range(n+1):
        sum += (math.pow(-1,n1)*math.pow(x,1+2*n1))/(math.factorial(1+2*n1))
    return sum

x = np.arange(-10, 10, 0.1)
y = np.array([math.sin(x1) for x1 in x])

plt.figure()
plt.ylim(-2,2)
plt.plot(x, y)
for k in range(14):
    sin_taylor = np.array([taylor_sin(x1,k) for x1 in x])
    plt.plot(x, sin_taylor, label="P_"+str(k))
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.legend()
plt.show()


# UPPGIFT 8

x = np.arange(-10, 10, 0.1)
y = np.array([math.cos(x1) for x1 in x])
z = x - y

plt.figure()
plt.ylim(-5, 5)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.plot(x, x, label='x')
plt.plot(x, y, label='cos(x)')
plt.plot(x, z, label='x-cos(x)')
plt.legend()
plt.show()

count = 0
a = -2
b = 3
c = 0
while abs(a-b) > math.pow(10, -12):
    count += 1
    c = (a+b)/2
    if c-math.cos(c) < 0:
        a = c
    else:
        b = c
print(str(c) + " f(c)= " + str(c-math.cos(c)))
print("iterations bisection: " + str(count))

count = 0
x0 = -2
x1 = 0
while abs(x0-x1) > math.pow(10, -12):
    count += 1
    x1 = x0
    x0 = x0 - (x0+math.cos(x0))/(1-math.sin(x0))

print(str(x0) + " f(c)= " + str(x0-math.cos(x0)))
print("iterations newton: " + str(count))


# UPPGIFT 9

a = 1
b = 1


def f(x, y):
    return math.sqrt(a**2*x**2 + b**2*y**2)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# cone
theta = np.arange(0, 2*np.pi+np.pi/50, 0.1)
r1 = np.arange(0, 1, 0.1)
t1, R1 = np.meshgrid(theta, r1)

X1 = R1 * np.cos(t1)
Y1 = R1 * np.sin(t1)
Z1 = -R1 +1
ax.plot_surface(X1, Y1, Z1, cmap='jet')


x = np.arange(-10, 10, 0.1)
y = np.arange(-10, 10, 0.1)
xx, yy = np.meshgrid(x, y)
z = -np.sqrt(xx**2 + yy**2) + 10
z[z < 0] = 0
# ax.set_zlim(0,10)
#z = np.array([math.sqrt(a**2*x1**2 + b**2*y1**2) for x1,y1 in zip(x,y)])
ax.plot_surface(xx, yy, z, cmap='jet')

# pyramid
n_theta = 2
n_phi = 5 
r = 2       

theta, phi = np.mgrid[0.0:0.5*np.pi:n_theta*1j, 0.0:2.0*np.pi:n_phi*1j]

x = r*np.sin(theta)*np.cos(phi)
y = r*np.sin(theta)*np.sin(phi)
z = r*np.cos(theta)
ax.plot_surface(x,y,z, cmap='inferno')
v = np.array([[-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1], [0, 0, 1]])
ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

verts = [[v[0], v[1], v[4]], [v[0], v[3], v[4]],
         [v[2], v[1], v[4]], [v[2], v[3], v[4]], [v[0], v[1], v[2], v[3]]]

ax.add_collection3d(Poly3DCollection(verts, facecolors='b', edgecolors='r'))


# sphere
n_theta = 100
n_phi = 200
r = 2

theta, phi = np.mgrid[0.0:0.5*np.pi:n_theta*1j, 0.0:2.0*np.pi:n_phi*1j]

x = r*np.sin(theta)*np.cos(phi)
y = r*np.sin(theta)*np.sin(phi)
z = r*np.cos(theta)
ax.plot_surface(x, y, z, cmap='inferno')

# spirals
u = np.linspace(0, 4*np.pi, 400)
x = u/np.pi 
y = np.sin(u)
z = np.cos(u)
ax.plot(x, y, z, 'r')
ax.plot(x, -y, -z, 'b')
plt.show()


# UPPGIFT 10

a = np.array([[4, -1, -9, -4, -6], [1, 1, -1, 4, -5],
              [0, -3, 4, 7, 0], [3, -5, -5, -3, 7], [9, -1, 4, -8, -9]])
b = np.array([-59,-21,20,16,-11])
x = np.linalg.solve(a,b)
print(x)
print(np.allclose(np.dot(a,x),b)) #check solution correct 

x = np.array([1325.9, 1167.3, 1069.1, 992.5, 821.2, 676.3, 548,
              515.4, 476.3, 342, 25.5, 31.3, 150.4, 226, 395.5, 454, 255.1])
y = np.array([28820, 25460, 21810, 20640, 18000, 16300, 14160,
              13620, 13080, 10360, 1360, 1620, 5390, 7680, 12210, 13600, 8430])
A = np.vstack([x, np.ones(len(x))]).T
print(A)
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
print(m, c)
plt.plot(x, y, 'o', label='Origina data', markersize=10)
plt.plot(x, m*x + c, 'r', label='Fitted line')
plt.legend()
plt.show()
print("Price to Senda:" + str(325.4*m + c))
print("Price to Goteborg(yen):" + str(455*m + c))
print("Price to Goteborg(kr):" + str((455*m + c)*0.084))



#double check 
# # price
# c = np.array([1.95, 0.49, 0.99, 1.20, 31.96, 6.50, 6.95, 0.95, 0.49, 2.99, 2.69, 5.99, 1.09,
#               1.99, 2.99, 12.90, 6.90, 0.99, 17.90, 2.99, 6.99, 7.99, 19.90, 8.99, 7.99, 1000])
# print(len(c))
# # food:    protein carbohydrate fat A      B1    B2    B3    B12  C    D     K
# A_ub = np.array([[930, 2000, 1100, 13700, 40440, 36490, 14950, 260, 1280, 900, 2820, 2000, 0, 1090, 2900, 0, 3090, 3220,
#                   24900, 12600, 19900, 19190, 20000, 21500, 19400, 0],

#                  [9600, 17000, 9340, 72500, 41220, 30160, 16700, 13810, 5800, 3900, 6640,
#                   8530, 97330, 22840, 3600, 0, 3260, 5260, 1300, 1120, 0, 0, 0, 0, 700, 0],

#                  [240, 90, 100, 1870, 7610, 19940, 60750, 170, 100, 200, 370, 14660, 0, 330,
#                   400, 100000, 340, 3250, 3310, 10600, 8670, 12440, 16000, 6900, 3800, 0],

#                  [0.835, 0.0006, 0, 0, 0, 0.001, 0.001, 0.003, 0, 0.042, 0.031, 0.007, 0,
#                   0, 0.469, 0, 0, 0.046, 0.602, 0.149, 0.009, 0.012, 0.026, 0.024, 9.5, 0],

#                  [0.066, 0.08, 0.046, 0.447, 10.99, 0.874, 0.643, 0.017, 0.061, 0.037, 0.071, 0.067,
#                   0.008, 0.031, 0.078, 0, 0.081, 0.044, 0.03, 0.066, 0.79, 0.23, 0.120, 0.190, 0.48, 0],

#                  [0.058, 0.03, 0.027, 0.215, 4.0, 0.87, 0.113, 0.026, 0.040, 0, 0.117, 0.13, 0.007,
#                   0.073, 0.189, 0, 0.402, 0.183, 0.320, 0.5, 0.280, 0.2, 0.11, 0.15, 2.4, 0],

#                  [0.983, 1.05, 0.116, 6.365, 40.3, 1.623, 1.8, 0.091, 0.234, 0.594, 0.639, 1.738,
#                   0.082, 0.665, 0.724, 0, 3.607, 0, 0.05, 0.064, 6.68, 4.16, 7.3, 12.0, 12.0, 0],

#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.00004, 0.0005,
#                   0.0016, 0.001, 0.007, 0.002, 0.004, 0.0003, 0.032, 2],

#                  [5.9, 19.7, 7.4, 0, 0.3, 6.0, 6.3, 4.6, 36.6, 14.0, 89.2,
#                   10.0, 0, 8.7, 28.0, 0, 2.1, 0, 0, 0, 0, 0, 0, 0, 33.8, 0],

#                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
#                   0, 0.002, 0.080, 0.180, 0.001, 0.006, 0, 0.01, 0.002, 0.0004, 10],

#                  [0.0132, 0.0019, 0, 0, 0, 0.047, 0.014, 0.002, 0.076,
#                   0.008, 0.101, 0.021, 0, 0, 0.483, 0.06, 0, 0, 0.003, 0.03, 0, 0, 0, 0, 0, 0]])
# """ print(len(A_ub), len(A_ub[5])) """
# print('c' + str(c.shape))
# print('aub' + str(A_ub.shape))
# # need
# b_ub = np.array([60000, 275000, 70000, 0.7, 1.1,
#                  1.2, 15, 0.002, 75, 0.01, 0.065])
# print( 'bub' + str(b_ub.shape))
# # energy
# A_eq = np.matrix(
#     '173;322;166;1418;1361;1866;2629;218;103;74;141;670;1576;371;97;3699;93;252;1682;647;647;787;964;621;482;0')

# A_eq = [[173], [322], [166], [1418], [1361], [1866], [2629], [218], [103], [74], [141], [670], [
#     1576], [371], [97], [3699], [93], [252], [1682], [647], [647], [787], [964], [621], [482], [0]]
# """ print(A_eq) """
# # energy need
# b_eq = 8710

# res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq,
#               b_eq=b_eq, options={"tol": 1e-10})
# print(res)
