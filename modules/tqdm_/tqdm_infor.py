# -*- coding: utf-8 -*-
from tqdm import tqdm
pbar = tqdm(["a", "b", "c", "d"])
for char in pbar:
    pbar.set_description("Processing %s" % char)
