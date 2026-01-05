import math
import pandas as pd


STAB_RAND = 1.275
BENCH = 2763

STAT_BONUS = 94 ## 31 IVs + 252 EVs

def calc_stat(hp,spd):
    true_hp = math.floor(((2*hp)+STAT_BONUS)/2)+60
    true_spd = math.floor((math.floor(((2*spd)+STAT_BONUS)/2)+5)*1.1)

    return true_hp,true_spd

dex = pd.read_excel('/Users/jbrobst/Downloads/pokedex.xlsx')

fes = dex[dex['fully_evolved'] == True].copy().reset_index(drop=True)

gust_list = []

for mon in dex:
    hp,spd = calc_stat(mon['hp'],mon['spd'])

    te = 1
    for t in ['1','2']:
    ## type effectivness
        if mon[f'type_{t}'].str.lower() in ['rock','electric','steel']:
            te *= 0.5
        elif mon[f'type_{t}'].str.lower() in ['fighting','bug','grass']:
            te *= 2
    
    bulk = spd * ((hp/(STAB_RAND * te))-2)

    if bulk <= BENCH:
        gust_list.append(mon['name'])

