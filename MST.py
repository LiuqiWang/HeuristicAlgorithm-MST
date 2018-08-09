# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 22:13:58 2018

@author: liuqi
"""

def mst_algo(locs,dist):
    name_or_team = "lwang19"
    mst=[]
    pairs=dist.keys()
    
    cities=[loc[0] for loc in locs]
    start=cities[0]
    linked=[start]
    choices=[[p,dist[p]] for p in pairs if start in p]
    
    n=len(locs)
    while(len(linked)<n):
        choices.sort(key=lambda x:x[1])
        for ch in choices:
            if ch[0][1] not in linked or ch[0][0] not in linked:
                mst.append(ch[0])
                if ch[0][1] not in linked: newcity=ch[0][1]
                else: newcity=ch[0][0]
                linked.append(newcity)
                choices += [[p,dist[p]] for p in pairs if newcity in p]
                break
    return name_or_team, mst
