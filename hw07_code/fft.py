import numpy as np

x_1 = np.array([1,2,1,2])
x_2 = np.array([3,0,-1,-4])
x_1k = np.fft.fft(x_1)
x_2k = np.fft.fft(x_2)
x = x_1 + x_2
x_k = np.fft.fft(x)
x_1k_2k = x_1k + x_2k
print("\nPROBLEM #1")
print("(a) X_1[k] = %s \nX_2[k] = %s\n" %(x_1k, x_2k))
print("(b) x[n] = %s\n" % x)
print("(c) X[k] = %s" % x_k)
print("X_1[k] + X_2[k] = %s\n" % x_1k_2k)

print("\nPROBLEM #2")
x_conv = np.convolve(x_2, x_1)
print("\n(a) %s\n" % x_conv)
i = 0
x_elem_prod = np.zeros(len(x_1k), dtype=complex)
while i < len(x_1k):
     x_elem_prod[i] = x_1k[i] * x_2k[i]
     i+=1
print("(b) %s" % x_elem_prod)
x_ifft = np.fft.ifft(x_elem_prod)
print("(c) %s \n" % x_ifft)
while (len(x_1) < len(x_conv)):
     x_1 = np.append(x_1, [0]); x_2 = np.append(x_2, [0]);
print("\n(d) xz1[n] = %s, xz2[n] = %s\n" %(x_1,x_2))
xz_1k = np.fft.fft(x_1)
xz_2k = np.fft.fft(x_2)
print("\n(e) xz_1k = %s, \nxz_2k = %s\n" %(xz_1k, xz_2k))
xz_elem = np.zeros(len(xz_1k), dtype=complex)
i = 0
while i < len(xz_elem):
     xz_elem[i] = xz_1k[i] * xz_2k[i]
     i+=1
xz_ifft = np.fft.ifft(xz_elem)
print("(f) XZ_k = %s" %xz_elem)
print("(g) IDFT of XZ_k = %s " %xz_ifft)
