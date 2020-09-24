#!/usr/bin/env python
# coding: utf-8

# In[4]:


import sys
import math
import matplotlib.pyplot as plt
class projectile() : 
    def __init__(self,angle,veloc) :
        self.angle = angle
        self.veloc = veloc
        self.t = 0.0
        self.x = 0.0
        self.y = 0.0
    def time(self) :
        self.t = 2*( math.sin( self.angle * math.pi / 180  ) ) * self.veloc / 9.8
    def vertical(self,sec) :
        self.y = ( ( math.sin( self.angle * math.pi / 180 ) ) * self.veloc * sec - (4.9 * sec * sec) )
    def horizon(self,sec) :
         if( sec <= self.t ) :
            self.x = ( math.cos( self.angle * math.pi / 180 ) )  * self.veloc * sec
angle = input("請輸入角度")
veloc = input("請輸入速度")
angle = int(angle)
veloc = int(veloc)
ans = projectile(angle,veloc)
ans.time()
i=0
while i < ans.t :
    ans.vertical(i)
    ans.horizon(i)
    #print( ans.x , ans.y , sep=',' )
    plt.plot(ans.x,ans.y,"o")
    i+=0.1
plt.show()


# In[35]:





# In[ ]:





# In[ ]:




