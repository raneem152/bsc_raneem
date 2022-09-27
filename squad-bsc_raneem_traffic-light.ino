 int green=2;
  int yellow=3;
  int red=4;
  int push_button=6;

void setup() {
  pinMode(green,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(red,OUTPUT);
  
  digitalWrite(green,LOW);
  digitalWrite(yellow,LOW);
  digitalWrite(red,LOW);
  
  pinMode(push_button,INPUT);


}

void loop() {
 if (digitalRead(push_button) == HIGH){
        delay(15); 
        if (digitalRead(push_button) == HIGH) {
            changeLights();
            delay(12000);
        }
    }
 }

void changeLights(){
    digitalWrite(green, HIGH);
    digitalWrite(yellow, LOW);
    digitalWrite(red, LOW);
    delay(2000);
  
    digitalWrite(green, LOW);
    digitalWrite(yellow, HIGH);
    digitalWrite(red, LOW);
    delay(3000);
    
    digitalWrite(green, LOW);
    digitalWrite(yellow, LOW);
    digitalWrite(red, HIGH);
    delay(4000); 

}
