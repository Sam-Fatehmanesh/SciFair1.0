int switch1 = 0;
int switch2 = 0;

int t1 = 0.0;
int t2 = 0.0;
int time1 = 0.0;

void setup()
{
    Serial.begin(9600);
    pinmode(switch1,INPUT);
    pinmode(switch2,INPUT);
};

void loop()
{
  if(digitalread(switch1) == HIGH) 
  {
      t1 = micro();
  } 
  if(digitalread(switch2) == HIGH) 
  {
    t2 = micro();
    time1 = t2-t1; 
    time1 = time1/0.000001;
    Serial.println(time1);
  } 
}
