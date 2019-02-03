import math

#!!!!!!!!!!!!
#pls read comments
#!!!!!!!!!

#to find resisatance of multiple identical capasitors in parralel
def parralelCapsitorsresistance(capasitorresistance, numofcaps):
    temp = 0.0
    for c in range(numofcaps):
        temp += 1/capasitorresistance
    return 1/temp

def CapVoltage(Vo,t,c,ohms):
    #this porvides voltage across a capsitor after a period of time
    return Vo * math.e**( (-1*t) / (ohms*c) )

def Current(c,ohms,Vo,t1,t2):
    V1 = CapVoltage(Vo,t1,c,ohms)
    V2 = CapVoltage(Vo,t2,c,ohms)
    dT = t2-t1
    #this provides peudo-instantanius voltage
    I = abs(c * ( (V2-V1)   /    dT  ) )
    return I

def Force(I,r,l,Uo):
    # this equation is made with both the magntic feild
    # stength at a distance form a wire equation and from
    # the force on a wire in a magnetic feild formula
    F = ((I**2) * l * Uo) / (2 * math.pi * r)
    return F

def NetForce(FrictionForce,Force):
    nF = Force - FrictionForce
    if(Force < FrictionForce):
        nF = 0
    return nF

#Ts is 'time span' such as a milisecond or nano second for example
def Acceleration(F,m):
    return F/m
#T is in hundreth of a miliscond
#displacment is the same as velosity but with the added factors of 1/2 and 1
def thoreticals(timestep,T,Vo,c,ohms,r,la,lb,Uo,m,Fr):
    X = 0
    V = 0
    I = 0
    vF = 0
    Ff = 0
    nF = 0
    #this for loop substitutes for calculus
    for n in range(1,T):
        if(X >= 0.14):
            print(n*timestep)
            print(vF)
            print(V)
            break
        I = Current(c,ohms,Vo,(n*timestep)-timestep,n*timestep)
        vF = 2* Force(I,r,la,Uo)
        Ff = Fr * 2 * Force(I,r-(lb/2),lb,Uo)
        nF = NetForce(Ff,vF)
        #nF = 0
        V += timestep * Acceleration(nF,m)
        X += V * timestep * 0.5


# almost all of the acceleratrion occurs in
#the first tenth of a milisecond !!!!

#radius
radius = 0.01
#friction coeffeint
Fr = 0.42
#lengtha
la = 0.01
#lengthb
lb = 0.01
#magnetic perbibility
Uo = 0.005
#inicial voltage
Vo = 440
#time
time = 1000000000
#resistance
ohms = 1.4
#capasitance
capasitance = 0.0096
#mass
m = 0.0069
#Ts is in unit of timestep
Ts = 0.00000001

ohms += parralelCapsitorsresistance(0.08,4)

thoreticals(Ts,time,Vo,capasitance,ohms,radius,la,lb,Uo,m,Fr)
