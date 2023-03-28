
import py5
import random 


def setup():
    
    py5.size(1000, 1000)
    py5.background(0)
    
    global a
    a = 3
    
    global b 
    b = 1
    
    global d
    d = 0.1
    
    #py5.no_loop()
    
    py5.frame_rate(30)
    

    
    


def draw():
    global a
    global b
    global d
    
   
    
    a = a + 5
    if a > 300:
        a = 5
        
    b = b + 3
    
    d = d + 0.002
    
   
    
    py5.stroke(0)
    py5.stroke_weight(1)
       
    for i in range(100):
        for s in range(100):
            rand_s = random.randint(5, 100)
        py5.line(100, 100 + i, 100 + i * 8, 780 + rand_s) 
        
       
        
        
        py5.fill (4, 4, 4)
        py5.stroke(20, 20, 20)
        py5.stroke_weight(0)
        py5.translate(200, 600)
        py5.rotate(py5.radians(30 + b))
        py5.circle(30, 30, 0.01 + d)
    
        
         
        
py5.run_sketch()
       
        
        
        
        
    

