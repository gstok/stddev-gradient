#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np;

a = np.array([3.0, 3.0, 2.0, 4.9, 100.2, -8.9]);

# 数值微分求标准差梯度
def gradient ():
    d = 1e-5;
    grad = np.zeros(a.size);
    func = lambda : np.std(a, ddof = 1);
    # func = lambda : np.mean(a);
    for index, value in enumerate(a):
        bak = value;
        a[index] -= d;
        leftv = func();
        a[index] = bak;
        a[index] += d;
        rightv = func();
        a[index] = bak;
        grad[index] = (rightv - leftv) / (d * 2);
    return grad;

grad = gradient();

print(grad);

# std = np.std(a, ddof = 1);
# avg = np.mean(a);
# k = std ** 2;
# t = 0.5 * np.power(k, -0.5);
# print(a.size);
# print(t * (a - avg) / a.size);

d = 1e-5;
a = 10;
leftv = np.sqrt(a - d);
rightv = np.sqrt(a + d);
rst = (rightv - leftv) / (d * 2);
print(rst);
rst2 = 0.5 * np.power(a, -0.5);
print(rst2);





