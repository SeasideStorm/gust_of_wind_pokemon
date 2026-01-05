# gust_of_wind_pokemon
When talking about how good something is, something that is echoed to emphasis the frailty of a Pokémon is that it ‘goes down to a gust of wind’. However, this made me wonder. Which Pokemon literally go down to a gust of wind. Gust is a move after all, so this is something that can be theoretically quantified. To do this, I used Gust’s BP of 40 and a base special attack of 91, the average for all fully-evolved flying types. This special attack with then fully invested (31 IVs, 252 EVs, SpA boosting nature), and STAB was included. 

I wrote a simple python code that ran through every fully-evolved Pokemon 3 times, each with a different stat investment. The three were negative (0 EVs and 0 IVs in HP and SpDef, negative SpDef nature), none (0 EVs and 31 IVs in HP and SpDef, neutral nature), and high (252 EVs and 31 IVs in HP and SpDef, SpDef boosting nature). For each investment type, there were 16 damage calculations done to account for the 0.85-1.0 random variable, and the damage was also stored as both a standard and critical hit. From there, the percentage of normal and critical hits that were not survivable were averaged separately, before being combined with the critical hit chance as a weight (so (23/24 * normal average) + (1/24 * critical average)). 

Unsurprisingly, even with negative investment the only Pokémon that actually goes down to a gust of wind 100% of the time is Shedninja. However, linked I have a spreadsheet that lists the % chance that a Pokemon that can​ go down to a gust of wind will. In total, there are: 

159 that have a chance with negative investment
45 that have a chance with no investment
7 that have a chance with high investment

Outside of Shedinja, the highest chance of going down to a gust of wind is 12.5% for both Negative and Low investments (held by several Pokemon) and 6.51% for High Investment (held by Pheromosa). 
