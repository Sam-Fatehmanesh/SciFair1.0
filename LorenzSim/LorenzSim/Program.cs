using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LorenzSimulator
{
    class Program
    {
        static void Main(string[] args)
        {
            double Radius = 0.01;
            double FrictionCo = 0.42;
            double LengthA = 0.01;
            double LengthB = 0.01;
            double MagneticPer = 0.005;
            double InitialVo = 450;
            double Time = 1000;
            double Ohms = 0.0;
            double Capasitance = 0.096;
            double Mass = 0.008;
            double TimeStep = 0.0000001;

            double parralelCapsitorsResistance(double capsitorsResistance, float numOfCaps)//To find the resistance of multiple identical capacitors in parallel
            {
                double temp = 0;
                for (int i = 0; i < numOfCaps; i++)
                {
                    temp += 1 / capsitorsResistance;
                }
                return 1 / temp;
            }

            double CapVoltage(double Vo, double t, double c, double ohms)
            {
                return Vo * Math.Pow(Math.E, ((-1 * t) / (ohms * c)));
            }

            double Current(double c, double ohms, double Vo, double t1, double t2)
            {
                double V1 = CapVoltage(Vo, t1, c, ohms);
                double V2 = CapVoltage(Vo, t2, c, ohms);
                double dT = t2 - t1;

                return Math.Abs(c * ((V2 - V1) / dT));//this provides imsutatuis voltage
            }

            double Force(double I, double r, double l, double Uo)
            {
                //this equation is made with both the magntic feild 
                //stength at a distance form a wire equation and from
                // the force on a wire in a magnetic feild formula
                return (Math.Pow(I, 2) * l * Uo) / (2 * Math.PI * r);
            }

            double NetForce(double FrictionForce, double force)
            {
                double nF = force - FrictionForce;
                if (force < FrictionForce)
                {
                    nF = 0;
                }
                return nF;
            }

            double Acceleration(double F, double M)
            {
                return F / M;
            }

            double Velocity(double Vo, double T, double c, double ohms, double r, double la, double lb, double Uo, double m, double Fr, double timestep)
            {
                double V = 0.5;
                double I = 0;
                double vF = 0;
                double Ff = 0;
                double nF = 0;
                for (int i = 1; i < T; i++)
                {
                    I = Current(c, ohms, Vo, (i * timestep) - timestep, i * timestep);
                    vF = 2 * Force(I, r, la, Uo);
                    Ff = Fr * 2 * Force(I, r - (lb / 2), lb, Uo);
                    nF = NetForce(Ff, vF);
                    V += timestep * Acceleration(nF, m);
                }
                return V;
            }

            /*double Displacment(double Vo, double T, double c, double ohms, double r, double la, double lb, double Uo, double m, double Fr, double timestep)
            {
                double X = 0;
                double V = 0.5;
                double I = 0;
                double vF = 0;
                double Ff = 0;
                double nF = 0;
                for (int i = 0; i < T; i++)
                {
                    I = Current(c, ohms, Vo, i * timestep - timestep, i * timestep);
                    vF = 2 * Force(I, r, la, Uo);
                    Ff = Fr * 2 * Force(I, r - (lb / 2), lb, Uo);
                    nF = NetForce(Ff, vF);
                    V += timestep * Acceleration(nF, m);
                    X += V * timestep * 0.5;
                }
                return X;
            }*/

            Ohms = parralelCapsitorsResistance(0.08, 4);

            double velocity = Velocity(InitialVo, Time, Capasitance, Ohms, Radius, LengthA, LengthB, MagneticPer, Mass, FrictionCo, TimeStep);
            Console.WriteLine($"Final Velocity --> {velocity}");
            Console.ReadKey();
        }
    }
}