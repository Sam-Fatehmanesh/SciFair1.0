import math
  
#!!!!!!!!!!!!
#pls read comments
#!!!!!!!!!

#variables:
#radius
r = 0.0
#friction coeffeint
Fr = 0.0
#length 
l = 0.0
#magnetic perbibility
Uo = 0.0
#inicial voltage
Vo = 0.0
#time
t = 0
#resistance
ohms = 0.0
#capasitance 
c = 0
#mass
m = 0.0

#T is in tenths of a miliscond

#to find resisatance of multiple identical capasitors in parralel
def parralelCapsitorsresistance(capasitorresistance, numofcaps):
    temp = 0.0
    for c in range(numofcaps):
        c = c
        temp += 1/capasitorresistance
    return 1/temp

def CapVoltage(Vo,t,c,ohms):
    #this porvides voltage across a capsitor after a period of time
    return Vo * math.e**( (-1*t) / (ohms*c) )

def Current(c,ohms,Vo,t1,t2):
    V1 = CapVoltage(Vo,t1,c,ohms)
    V2 = CapVoltage(Vo,t2,c,ohms)
    dT = t2-t1
    #this provides instantanius voltage
    I = abs(c * ( (V2-V1)   /    dT  ) )
    return I

def Force(I,r,l,Uo):
    # this equation is made with both the magntic feild 
    # stength at a distance form a wire equation and from
    # the force on a wire in a magnetic feild formula
    F = (I**2 * l * Uo) / (math.pi * r)
    return F

def NetForce(FrictionForce,Force):
    nF = Force - FrictionForce
    if(Force < FrictionForce):
        nF = -1* Force
    nF = Force - FrictionForce
    return nF

#Ts is 'time span' such as a milisecond or nano second for example
def Acceleration(F,m): 
    return F/m 

#adding velosity over and over again for each hundreth of a millisecond
def Velosity(Vo,T,c,ohms,r,l,Uo,m,Fr,timestep):
    V = 1
    I = 0
    vF = 0
    Ff = 0
    nF = 0
    temp = 1
    for n in range(temp,T):
        I = Current(c,ohms,Vo,n*timestep-timestep,n*timestep)
        vF = 2 * Force(I,r,l,Uo)
        Ff = Fr * 2 * Force(I,r-(l/2),l,Uo)
        nF = NetForce(Ff,vF)
        V += timestep*Acceleration(nF,m)
    return V

#T is in hundreth of a miliscond
#displacment is the same as velosity but with the added factors of 1/2 and 1
def Displacment(Vo,T,c,ohms,r,l,Uo,m,Fr,barralL):
    X = 0
    V = 0
    I = 0
    vF = 0
    Ff = 0
    nF = 0
    temp = 1
    for n in range(temp,T):
        if(X > barralL):
            break
        I = Current(c,ohms,Vo,n*0.00001-0.00001,n*0.00001)
        vF = Force(I,r,l,Uo)
        Ff = Fr * 2 * Force(I,r-(l/2),l,Uo)
        nF = NetForce(Ff,vF)
        V += 0.00001 * 0.5 *Acceleration(nF,m)
        X += V * 0.00001
    return X


# almost all of the acceleratrion occurs in 
#the first tenth of a milisecond !!!!

#radius
radius = 0.050
#friction coeffeint
Fr = 0.26
#length 
l = 0.01
#magnetic perbibility
Uo = 0.005
#inicial voltage
Vo = 450
#time
time = 1000
#resistance
ohms = 0.0
#capasitance 
capasitance = 0.0096
#mass
m = 0.05

#T is in unit of timestep

ohms = parralelCapsitorsresistance(0.08,4)

#i = Current(0.0096,ohms,450,0.00009,0.0001)

#v = Velosity(450,10,0.0096,ohms,0.01,0.01,0.001,0.01,0.18)

velosity = Velosity(Vo,time,capasitance,ohms,radius,l,Uo,m,Fr,0.0000001)

print(velosity)
