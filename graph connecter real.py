# -*- coding: utf-8 -*-
import numpy as np
from fractions import Fraction
def graph_con():
    
       
    
        #Getting the ab coordinate 
    xcoor1 = input("put the x of the 1st order pair ")
    ycoor1 = input("put the y of the 1st order pair ")
        
    
        #Putting them into a list
    coor1 = []
    coor1.append(xcoor1)
    coor1.append(ycoor1)
        
    
        #Python assigned x and y as str, turning them into floats
    k = 0
    for ele in coor1:
        coor1[k] = float(ele)
        k = k+1
        
        #Print out some fun messages
    print("The starting xy coordinate is " + str(coor1))
    
        #Converting some varibles to smaller names to make life easier
    x1 = coor1[0]
    y1 = coor1[1]
    
    
    
    
    
    #Now we get our 2nd point
    
    
    
    
    
    
        #Getting the cd coordinate 
    xcoor2 = input("put the x of the 2st order pair ")
    ycoor2 = input("put the y of the 2st order pair ")
    

        #Putting them into a list
    coor2 = []
    coor2.append(xcoor2)
    coor2.append(ycoor2)
    

        #Python assigned x and y as str, turning them into floats
    j = 0
    for ele in coor2:
        coor2[j] = float(ele)
        j = j+1
    
        #Print out some fun messages
    print("The ending xy coordinate is " + str(coor2))

        #Converting some varibles to smaller names to make life easier
    x2 = coor2[0]
    y2 = coor2[1]
    
    
        #Check if x1<x2, otherwise code wont work
    if x2<x1:
        print("Error, the end coordinate is behind the begining coordinate")
        print(y1)
        print(y2)
        exit()
            
    

    
    
    
    
        #Now we math, we will need x1-x2 and y1-y2 alot while never needing the indivisual values, so we will refer to the difrrence between x1-x2 as x and same goes for y1-y2, which will go as y
    x = x1 - x2
    y = y1 - y2
    
    
        #We need to set up a system of eq to solve based off the proof, so we will fill in the matrix for a and b
    a = [[(x**3),(x**2)],[3*(x**2),2*x]]
    b = [y,0]
    
        
        #now time to solve the eq
    coef = np.linalg.solve(a,b)
    q = coef[0]
    r = coef[1]
    qq = str(Fraction(q).limit_denominator())
    rr = str(Fraction(r).limit_denominator())
    
        #printing the equation
    
    print("The equation of the graph containing the points ( " +str(x1) + " , " + str(y1) + " ), and, ( " +str(x2) + " , " + str(y2) + " ), is...  " + str(qq) + "(x-" +str(x2) + ")^3 + " + str(rr) + "(x-" + str(x2) + ")^2 + " + str(y2)) 
    
    
    
        #make an eq out of the solution
    import matplotlib.pyplot as plt
    def f(x,Q,R,X2,Y2):
        return Q*(x-X2)**3 + R*(x-X2)**2 + Y2
    
    
        #graphing 
    xlist =np.arange(x1,x2+0.2,0.1 )
    ylist = f(xlist,q,r,x2,y2)

    plt.figure(num=0,dpi=120)
    plt.plot(xlist,ylist)
    
        #adding more points to the graph
    add_points = 0
    while add_points != 1:
        con = input("Do you wanna add more points to the graph? type 1 to end program, type any other number to continue?")
        print(type(con))
        print(con)
        if con == "1":
            add_points = 1
        #Else stament below
            
        
        
        #Set x1=x2 and define a new x2 over and over agian until otherwise, we want the old endpoints to be the new start points
            
        else:
            x1 = x2
            y1 = y2
            
        
        
        #copy-paste
        #Getting the cd coordinate 
            xcoor2 = input("put the x of the next order pair ")
            ycoor2 = input("put the y of the next order pair ")
            
        
                #Putting them into a list
            coor2 = []
            coor2.append(xcoor2)
            coor2.append(ycoor2)
            
        
                #Python assigned x and y as str, turning them into floats
            j = 0
            for ele in coor2:
                coor2[j] = float(ele)
                j = j+1
            
                #Print out some fun messages
            print("The ending xy coordinate is " + str(coor2))
        
                #Converting some varibles to smaller names to make life easier
            x2 = coor2[0]
            y2 = coor2[1]
            
            
                #Check if x1<x2, otherwise code wont work
            if x2<x1:
                print("Error, the end coordinate is behind the begining coordinate")
                print(y1)
                print(y2)
                exit()    
            
        
            
            
            
            
                #Now we do math, we will need x1-x2 and y1-y2 alot while never needing the indivisual values, so we will refer to the difrrence between x1-x2 as x and same goes for y1-y2, which will go as y
            x = x1 - x2
            y = y1 - y2
            
            
                #We need to set up a system of eq to solve based off the proof, so we will fill in the matrix for a and b
            a = [[(x**3),(x**2)],[3*(x**2),2*x]]
            b = [y,0]
            
                
                #now time to solve the eq
            coef = np.linalg.solve(a,b)
            q = coef[0]
            r = coef[1]
            qq = str(Fraction(q).limit_denominator())
            rr = str(Fraction(r).limit_denominator())
            
                #printing
                
            print("The equation of the graph containing the points ( " +str(x1) + " , " + str(y1) + " ), and, ( " +str(x2) + " , " + str(y2) + " ), is...  " + str(qq) + "(x-" +str(x2) + ")^3 + " + str(rr) + "(x-" + str(x2) + ")^2 + " + str(y2))
            
            
                #make an eq out of the solution
            import matplotlib.pyplot as plt
            def f(x,Q,R,X2,Y2):
                return Q*(x-X2)**3 + R*(x-X2)**2 + Y2
            
            #Graphing our new eq based off of our new points
            xlist =np.arange(x1,x2+0.2,0.1 )
            ylist = f(xlist,q,r,x2,y2)

            plt.figure(num=0,dpi=120)
            plt.plot(xlist,ylist)
            
            #convert fraction into decimals, print eq
            
        


    
    
    
    
    
       
        
        
    
    
    
    
    
    
    
    
    
    
    
    
        
        
        
        
        
        
        
