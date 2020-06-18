#Hello, below is the description of this python script
#This python program's purpose is to simulate the motion of a projectile that
#is propelled by a railgun. A railgun accelerates projectiles by 
#using perpendicular magnetic fields, thus the Lorentz Force to push the projectile.
#I do not know Calculous and in my attempts to find an alternative 
#I landed on Summation and Sigma. Summation allows for me to use 
#normal algebra and arithmetic and add them up until I have 
#reached my desired value. However, each calculation must be for a 
#very slice amount of time in order for the final results to be accurate.
#Thus, the program uses a "for" loop to find the final values.
#To run this program, first, download the python IDE from python.org if not already installed.
#Next, copy the program into a new file. From there you can run the program.

#importing nessesary libraries
import math

#Resistance of multiple capacitors in parallel
def ParallelCapacitorsresistance(capOhms, numcap):
    num = 0
    for c in range(numcap):
        c=c
        num += 1/capOhms 
    return 1/num

#Current of capacitor during discharge relative to time
def Current(c,ohms,Vo,t):
    return Vo * math.e**(-1* t / ohms * c) / ohms

#Function for force with current and magnetic permeability derived 
#from both force on wire formula and magnetic field from wire formula.
def LorForce(I,Uo):
    F = (I**2) * Uo / math.pi
    return F

#net force 
def NetForce(FrictionForce,Force):
    nF = Force - FrictionForce
    return nF

#Uses resistivity, length, and cross section to find resistance
def Resistancefromresistivity(resistivity,L,CrossSection):
    return (resistivity/100)**3 * L *CrossSection
    
#Force by multiplying the pressure by the affected area
def Forcefrompresure(pressure,area):
    return area * pressure

#Uses summation to find desired values
def thoreticals(timestep,T,Vo,c,ohmsi,Uo,m,Fr,pressureF,resistivity,railCross):

    #initializing nessesary variables
    X = 0
    V = 0
    I = 0
    vF = 0
    Ff = 0
    nF = 0
    tT = int(T/timestep)
    ohms = 0

    #The main loop where the Final values are calculated.
    #The timestep variable is the size of time that is calculated for
    #each time the loop runs each calculation. Each time, the previous values 
    #are added to the new ones. The smaller timestep is the more accurate the 
    #results are, however, it takes the computer proportionally more time to run it.
    for n in range(1, tT):
        #Finding resistance on rails relative to projectile displacement on them
        ohms = Resistancefromresistivity(resistivity,X,railCross) + ohmsi

        #Current provided by the capacitors and resistance
        I = timestep * Current(c,ohms,Vo,n*timestep)

        #The Lorentz force from current and permiability
        vF = 2 * LorForce(I,Uo)

        #The friction force product from friction coefficient and pressure
        Ff = Fr * 2 * pressureF

        #Netforce on projectile with subtraction
        nF = NetForce(Ff,vF)

        #Velosity being added over and over using acceration and time
        V = V + (timestep * nF/m )

        #Displacment with velosity and time
        X += V * timestep * 0.5

        #Condition that if acceration ends, to provide all the data and values
        if vF <= 0:
            break

    #prints all desired values
    print("************************************")
    print("************************************")
    print("Displacment (m): ", X)
    print("************************************")
    print("Time (s): ",n*timestep)
    print("************************************")
    print("Magnetic Force (N): ",vF)
    print("************************************")
    print("Final Velosity (m/s): ",V)
    print("************************************")
    print("Eletrical Energy (inicial J): ",Vo**2 * c * 0.5)
    print("************************************")
    print("Kenetic Energy (final J): ",V**2 * m * 0.5)
    print("************************************")
    print("Eletrical->Kenetic efficiency: ",(V**2 * m * 0.5)/(Vo**2 * c * 0.5))
    print("************************************")

########################
#Change variables for different tests and simulation runs
#######################

#Friction Coeffeint of rails
Fr = 0.4

#Magnetic Perbibility in Henry per meters of projectile
Uo = 0.005

#Inicial Voltage in volts of capacitor bank
Vo = 4500

#Capacitor bank Resistance in ohms 
ohmsi = ParallelCapacitorsresistance(0.00008,1)

#Capacitance in farads of Capacitor bank
capasitance = .0000001

#mass in kilograms of projectile
m = 0.01

#Ts is in unit of timestep in seconds increace for more accuracy or decreace for faster run time
Ts = 0.001 

#Time simulation can last, in seconds
Time = 5

#Force from presure, in newtons, of rails on to projectile
pressureF = Forcefrompresure(0.5,0.05**2)

#Resistivity of rails in ohms per m^3
reistivity = 7.2 * 10**(-5)

#cross section of rails in m^2
railCross = 0.01

thoreticals(Ts,Time,Vo,capasitance,ohmsi,Uo,m,Fr,pressureF,reistivity,railCross)
