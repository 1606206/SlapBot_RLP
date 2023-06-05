const int pinPWMA = 6;
const int pinAIN2 = 7;
const int pinAIN1 = 8;
const int pinBIN1 = 9;
const int pinBIN2 = 10;
const int pinPWMB = 11;
const int pinSTBY = 12;
const int motor = 2;
String receivedData;
const int waitTime = 2000;  //espera entre fases
const int speed = 200;      //velocidad de giro

const int pinMotorA[3] = { pinPWMA, pinAIN2, pinAIN1 };
const int pinMotorB[3] = { pinPWMB, pinBIN1, pinBIN2 };
int inches = 0;

int cm1 = 0;
int cm2 = 0;

enum moveDirection {
  forward,
  backward
};

enum turnDirection {
  clockwise,
  counterClockwise
};

void setup() {
  Serial.begin(9600);
  pinMode(pinAIN2, OUTPUT);
  pinMode(pinAIN1, OUTPUT);
  pinMode(pinPWMA, OUTPUT);
  pinMode(pinBIN1, OUTPUT);
  pinMode(pinBIN2, OUTPUT);
  pinMode(pinPWMB, OUTPUT);
}

long readUltrasonicDistance(int triggerPin, int echoPin) {
  pinMode(triggerPin, OUTPUT);  // Clear the trigger
  digitalWrite(triggerPin, LOW);
  //delayMicroseconds(2);
  // Sets the trigger pin to HIGH state for 10 microseconds
  digitalWrite(triggerPin, HIGH);
  //delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  pinMode(echoPin, INPUT);
  // Reads the echo pin, and returns the sound wave travel time in microseconds
  return pulseIn(echoPin, HIGH);
}
void loop() {

  if (Serial.available() > 0) {

    receivedData = "";
    receivedData = Serial.readStringUntil('\n');  // Read the data received from Raspberry Pi as a character
    if (receivedData == "T") {
      tirarCarta();
    }

    if (receivedData == "A") {
      ataca();
    }
  }

  cm2 = 0.01723 * readUltrasonicDistance(5, 4);

  cm1 = 0.01723 * readUltrasonicDistance(3, 2);

  if ((cm1 < 10) && (cm2 > 10)) {
    Serial.write("1");
    delay(10000); // per evitar llegir res durants uns segons un cop s'ha picat la taula (hi ha un delay de 20 segons abans no comenci la següent a la raspi)
  }
  else if ((cm2<10) && (cm1>10)){ 
    Serial.write("2"); 
    delay(10000); // per evitar llegir res durants uns segons un cop s'ha picat la taula (hi ha un delay de 20 segons abans no comenci la següent a la raspi)
  }

}

void ataca() {
  enableMotors();
  moveB(forward, 205);
  delay(1600);

  fullStop();
}

void tirarCarta() {
  enableMotors();
  //tira endavant per llençar carta i endarrera per recollir la següent i que no és llenci també; el segon moviment com a correcció del primer moviment
  moveA(backward, 140);
  delay(200);

  moveA(forward, 150);
  delay(350);

  fullStop();
}

//Funciones que controlan el vehiculo
void moveA(int direction, int speed) {
  if (direction == forward) {
    moveMotorForward(pinMotorA, speed);
  } else {
    moveMotorBackward(pinMotorA, speed);
  }
}

void moveB(int direction, int speed) {
  if (direction == forward) {
    moveMotorForward(pinMotorB, speed);
  } else {
    moveMotorBackward(pinMotorB, speed);
  }
}

void turn(int direction, int speed) {
  if (direction == forward) {
    moveMotorForward(pinMotorA, speed);
    moveMotorBackward(pinMotorB, speed);
  } else {
    moveMotorBackward(pinMotorA, speed);
    moveMotorForward(pinMotorB, speed);
  }
}

void fullStop() {
  disableMotors();
  stopMotor(pinMotorA);
  stopMotor(pinMotorB);
}

//Funciones que controlan los motores
void moveMotorForward(const int pinMotor[3], int speed) {
  digitalWrite(pinMotor[1], HIGH);
  digitalWrite(pinMotor[2], LOW);

  analogWrite(pinMotor[0], speed);
}

void moveMotorBackward(const int pinMotor[3], int speed) {
  digitalWrite(pinMotor[1], LOW);
  digitalWrite(pinMotor[2], HIGH);

  analogWrite(pinMotor[0], speed);
}

void stopMotor(const int pinMotor[3]) {
  digitalWrite(pinMotor[1], LOW);
  digitalWrite(pinMotor[2], LOW);

  analogWrite(pinMotor[0], 0);
}

void enableMotors() {
  digitalWrite(pinSTBY, HIGH);
}

void disableMotors() {
  digitalWrite(pinSTBY, LOW);
}