#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import os, time
import numpy as np

import main
import main_cy

n = int(1e+5)

t0 = time.time()

main.test(n)

t1 = time.time()

main_cy.test(n)

t2 = time.time()



t3 = time.time()



t4 = time.time()

print("費時:", (t2-t1)-(t1-t0), t1-t0, t2-t1)