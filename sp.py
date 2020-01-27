#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 07:46:28 2018

@author: Mengxi Shen
"""
import pandas as pd
import matplotlib.pyplot as plt
products=pd.read_csv("products.csv")
df=(products[products["discontinued"] != True]).sort_values("price",ascending=False)
df["decile"]=pd.qcut(df["price"],10,labels=range(10))
mean_df=df.groupby("decile").mean()
plt.scatter(mean_df.price,mean_df.reviews)
plt.grid()
plt.xlabel("Price")
plt.ylabel("Review")
plt.savefig("price_review.png",dpi=150)
