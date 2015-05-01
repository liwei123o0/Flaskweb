# -*- coding: utf-8 -*-
#! /usr/bin/env python
a =[1,2,3]
b =[1,2,3]
c = [a[i] + b[i] for i in range(min(len(a),len(b)))]
print c