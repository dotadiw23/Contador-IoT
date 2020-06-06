//ENTRADAS
int trigIN = 10;
int echoIN = 9;
int duracionIN;
int distanciaIN;

//SALIDAS
int trigOUT = 2;
int echoOUT = 3;
int duracionOUT;
int distanciaOUT;
  
void setup(){
  Serial.begin(9600);
  //Sensores de entrada
  pinMode(trigIN, OUTPUT);
  pinMode(echoIN, INPUT);
  //Sensores de salida
  pinMode(trigOUT, OUTPUT);
  pinMode(echoOUT, INPUT);
}

void loop(){
  //Contador de Entradas
  digitalWrite(trigIN, LOW);
  delayMicroseconds(4);
  digitalWrite(trigIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigIN, LOW);
  
  duracionIN = pulseIn(echoIN, HIGH);
  duracionIN = duracionIN / 2;
  distanciaIN = duracionIN /29; 
  
  //Contador de Salidas  
  digitalWrite(trigOUT, LOW);
  delayMicroseconds(4);
  digitalWrite(trigOUT, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigOUT, LOW);
  
  duracionOUT = pulseIn(echoOUT, HIGH);
  duracionOUT = duracionOUT / 2;
  distanciaOUT = duracionOUT /29;
  
  if(distanciaIN >= 1 && distanciaIN <= 10){
    Serial.println('1');
    delay(1000);
  }else if(distanciaOUT >= 0 && distanciaOUT <= 10){
    Serial.println('0');
    delay(1000);
  } 
}
