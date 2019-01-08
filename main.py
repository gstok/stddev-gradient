#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np;

a = np.array([3.0, 3.0, 2.0, 4.9, 100.2, -8.9]);

# 数值微分求标准差梯度
def gradient ():
    d = 1e-5;
    grad = np.zeros(a.size);
    func = lambda : np.sqrt(np.sum((a - np.mean(a)) ** 2) / a.size);
    # func = lambda : np.std(a, ddof = 1);
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

def func2 (index):
    # x
    x = a[index];
    # 平均数
    avg = np.mean(a);
    # 平方和
    sqsum = np.sum((a - avg) ** 2);
    # N
    n = a.size;
    return (np.power(sqsum / n, -0.5) * (x - avg)) / n;

print(grad);
n1 = func2(0);
n2 = func2(1);
n3 = func2(2);
n4 = func2(3);
n5 = func2(4);
n6 = func2(5);
b = [n1, n2, n3, n4, n5, n6];
print(b);





