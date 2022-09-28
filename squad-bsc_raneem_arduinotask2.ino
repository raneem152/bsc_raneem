//4 buttons (forward, backward, rotate right, and rotate left), represented motion signals on a real motor driver and real motor controlling 2 motors, robot control is done by push buttons 
 
//for motors connected to h-bridge
const int leftForward = 3;   
const int leftBackward = 2;  
const int rightForward = 4;  
const int rightBackward = 5; 

//buttons
int Button1 = 6;     
int Button2 = 7;     
int Button3 = 8;     
int Button4 = 9;     

int ButtonState1 = 0;     
int ButtonState2 = 0;     
int ButtonState3 = 0;     
int ButtonState4 = 0;     

void setup() 
{
 Serial.begin(9600);
 
 pinMode(leftForward, OUTPUT); 
 pinMode(leftBackward, OUTPUT);
 pinMode(rightForward, OUTPUT); 
 pinMode(rightBackward, OUTPUT);

  //pushbutton as input
 pinMode(Button1, INPUT);    
 pinMode(Button2, INPUT);    
 pinMode(Button3, INPUT);    
 pinMode(Button4, INPUT);    
 
}

void loop(){
  ButtonState1 = digitalRead(Button1);  
  ButtonState2 = digitalRead(Button2);  
  ButtonState3 = digitalRead(Button3);  
  ButtonState4 = digitalRead(Button4);  

 // button1-->forward  button2-->backword    button3-->left    button4-->right
 
  if (ButtonState1 == HIGH)
  { 
    forward();
  }
 
  else if (ButtonState2 == HIGH)
  {
    backward();
  }
  
  else if (ButtonState3 == HIGH)
  {
    left();
  }
   
    else if (ButtonState4 == HIGH)
  {
    right();
  }
  else 
  {
    Stop();
  }
 }

void forward(){
  digitalWrite(leftForward, HIGH);
  digitalWrite(leftBackward, LOW);
  digitalWrite(rightForward, HIGH);
  digitalWrite(rightBackward, LOW);
}

void left(){
  digitalWrite(leftForward, LOW);
  digitalWrite(leftBackward, HIGH);
  digitalWrite(rightForward, HIGH);
  digitalWrite(rightBackward, LOW);
}


void right(){
  digitalWrite(leftForward, HIGH);
  digitalWrite(leftBackward, LOW);
  digitalWrite(rightForward, LOW);
  digitalWrite(rightBackward, HIGH);
}


void backward(){
  digitalWrite(leftForward, LOW);
  digitalWrite(leftBackward, HIGH);
  digitalWrite(rightForward, LOW);
  digitalWrite(rightBackward, HIGH);
}


void Stop(){
  digitalWrite(leftForward, LOW);
  digitalWrite(leftBackward, LOW);
  digitalWrite(rightForward, LOW);
  digitalWrite(rightBackward, LOW);
}
