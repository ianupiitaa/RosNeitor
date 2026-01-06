/*
 * Práctica 4: "TERRENEITOR" - VERSIÓN ROS 2 (Micro-ROS)
 * AJUSTE DE VELOCIDAD: MÁS LENTO Y CONTROLADO
 */

#include <micro_ros_arduino.h>
#include <stdio.h>
#include <rcl/rcl.h>
#include <rcl/error_handling.h>
#include <rclc/rclc.h>
#include <rclc/executor.h>
#include <std_msgs/msg/string.h>

// --- MAPEADO DE PINES (Hardware) ---
#define ENA 25  
#define IN1 26
#define IN2 27
#define ENB 14  
#define IN3 12
#define IN4 13
#define LED_PIN 2 

// --- CONFIGURACIÓN PWM ---
const int FREQ = 5000;
const int RES = 8; 

// --- VARIABLES ROS ---
rcl_subscription_t subscriber;
std_msgs__msg__String msg;
rclc_executor_t executor;
rclc_support_t support;
rcl_allocator_t allocator;
rcl_node_t node;

// --- Macros de Error ---
#define RCCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){error_loop();}}
#define RCSOFTCHECK(fn) { rcl_ret_t temp_rc = fn; if((temp_rc != RCL_RET_OK)){}}

// ==========================================================
//   --- CALIBRACIÓN DE VELOCIDADES 
// ==========================================================

const int VEL_BAJA = 140;   // Límite físico (no tocar)
const int VEL_MEDIA = 160;  // ANTES: 180 -> AHORA: 160 (Más lento)
const int VEL_ALTA = 220;   // ANTES: 255 -> AHORA: 220 (Giros suaves)

// --- CALIBRACIÓN DE TIEMPOS ---
const unsigned long T_GIRO_45_R = 500;
const unsigned long T_AVANCE_20CM = 1500;
const unsigned long T_GIRO_90_R = 1000;
const unsigned long T_GIRO_135_R = 1500;
const unsigned long T_AVANCE_30CM = 2200;
const unsigned long T_SPIN_10S = 10000;
const unsigned long T_CIRCULO_10S = 10000;
const unsigned long T_ZIGZAG_PASO = 700;
const unsigned long T_ZIGZAG_10S = 10000;
const unsigned long T_INFINITO_PASO = 5000;
const unsigned long T_PAUSA_2S = 2000; 

// --- MAQUINA DE ESTADOS ---
enum State { IDLE, FREE_MODE, ROUTINE, PAUSED };
State currentState = IDLE;

// --- VARIABLES DE RUTINA ---
int currentRoutine = 0; 
int routineStep = 0; 
unsigned long stepStartTime = 0; 
unsigned long stepTimeElapsed = 0; 

// --- KICK-START ---
int currentSpeedA = 0; 
int currentSpeedB = 0;
const int KICK_START_DURATION_MS = 75;

// Declaraciones
void parseCommand(String cmd);
void stopMotors();

// -------------------------------------------------------------------
//   FUNCIONES DE HARDWARE (MOTORES)
// -------------------------------------------------------------------

void error_loop(){
  while(1){
    digitalWrite(LED_PIN, !digitalRead(LED_PIN));
    delay(100);
  }
}

void motorA(int speed) { 
  if (speed == currentSpeedA) return; 

  bool needsKick = false;
  if (speed != 0) {
    if (currentSpeedA == 0) needsKick = true;
    else if (speed > 0 && currentSpeedA < 0) needsKick = true;
    else if (speed < 0 && currentSpeedA > 0) needsKick = true;
  }

  if (speed > 0) { 
    digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW);
    if (needsKick) { ledcWrite(ENA, 255); delay(KICK_START_DURATION_MS); }
    ledcWrite(ENA, speed);
  } else if (speed < 0) { 
    digitalWrite(IN1, LOW); digitalWrite(IN2, HIGH);
    if (needsKick) { ledcWrite(ENA, 255); delay(KICK_START_DURATION_MS); }
    ledcWrite(ENA, abs(speed));
  } else { 
    digitalWrite(IN1, LOW); digitalWrite(IN2, LOW); ledcWrite(ENA, 0);
  }
  currentSpeedA = speed; 
}

void motorB(int speed) {
  if (speed == currentSpeedB) return;

  bool needsKick = false;
  if (speed != 0) {
    if (currentSpeedB == 0) needsKick = true;
    else if (speed > 0 && currentSpeedB < 0) needsKick = true;
    else if (speed < 0 && currentSpeedB > 0) needsKick = true;
  }

  if (speed > 0) { 
    digitalWrite(IN3, HIGH); digitalWrite(IN4, LOW);
    if (needsKick) { ledcWrite(ENB, 255); delay(KICK_START_DURATION_MS); }
    ledcWrite(ENB, speed);
  } else if (speed < 0) { 
    digitalWrite(IN3, LOW); digitalWrite(IN4, HIGH);
    if (needsKick) { ledcWrite(ENB, 255); delay(KICK_START_DURATION_MS); }
    ledcWrite(ENB, abs(speed));
  } else { 
    digitalWrite(IN3, LOW); digitalWrite(IN4, LOW); ledcWrite(ENB, 0);
  }
  currentSpeedB = speed;
}

// Movimientos básicos
void stopMotors() { motorA(0); motorB(0); }
void forward(int speed) { motorA(speed); motorB(speed); }
void backward(int speed) { motorA(-speed); motorB(-speed); }
void spinRight(int speed) { motorA(speed); motorB(-speed); }
void spinLeft(int speed) { motorA(-speed); motorB(speed); }
void turnRight(int speed) { motorA(VEL_ALTA); motorB(VEL_MEDIA); }
void turnLeft(int speed) { motorA(VEL_MEDIA); motorB(VEL_ALTA); }

// -------------------------------------------------------------------
//   LÓGICA DE RUTINAS
// -------------------------------------------------------------------

void terminateRoutine() {
  stopMotors();
  currentState = IDLE;
  currentRoutine = 0;
  routineStep = 0;
}

void applyCurrentStepAction() {
  switch (currentRoutine) {
    case 1: if(routineStep%2==0) spinRight(VEL_MEDIA); else forward(VEL_MEDIA); break;
    // Puedes agregar más casos si notas saltos extraños al despausar
  }
}

void runRoutine1() {
  unsigned long timeInStep = millis() - stepStartTime;
  switch (routineStep) {
    case 0: spinRight(VEL_MEDIA); stepStartTime = millis(); routineStep = 1; break;
    case 1: if (timeInStep > T_GIRO_45_R) { forward(VEL_MEDIA); stepStartTime = millis(); routineStep = 2; } break;
    case 2: if (timeInStep > T_AVANCE_20CM) { spinRight(VEL_MEDIA); stepStartTime = millis(); routineStep = 3; } break;
    case 3: if (timeInStep > T_GIRO_90_R) { forward(VEL_MEDIA); stepStartTime = millis(); routineStep = 4; } break;
    case 4: if (timeInStep > T_AVANCE_20CM) { spinRight(VEL_MEDIA); stepStartTime = millis(); routineStep = 5; } break;
    case 5: if (timeInStep > T_GIRO_135_R) { forward(VEL_MEDIA); stepStartTime = millis(); routineStep = 6; } break;
    case 6: if (timeInStep > T_AVANCE_30CM) { terminateRoutine(); } break;
  }
}

void runRoutine2() {
  unsigned long timeInStep = millis() - stepStartTime;
  switch (routineStep) {
    case 0: spinRight(VEL_MEDIA); stepStartTime = millis(); routineStep = 1; break;
    case 1: if (timeInStep > T_SPIN_10S) { spinLeft(VEL_MEDIA); stepStartTime = millis(); routineStep = 2; } break;
    case 2: if (timeInStep > T_SPIN_10S) { turnRight(VEL_MEDIA); stepStartTime = millis(); routineStep = 3; } break;
    case 3: if (timeInStep > T_CIRCULO_10S) { turnLeft(VEL_MEDIA); stepStartTime = millis(); routineStep = 4; } break;
    case 4: if (timeInStep > T_CIRCULO_10S) { turnRight(VEL_MEDIA); stepStartTime = millis(); routineStep = 5; } break;
    case 5: if (timeInStep > T_INFINITO_PASO) { turnLeft(VEL_MEDIA); stepStartTime = millis(); routineStep = 6; } break;
    case 6: if (timeInStep > T_INFINITO_PASO) { terminateRoutine(); } break;
  }
}

void runRoutine3() {
  unsigned long timeInStep = millis() - stepStartTime;
  switch (routineStep) {
    case 0: stepStartTime = millis(); routineStep = 1; break;
    case 1: 
      if (timeInStep > T_ZIGZAG_10S) { stepStartTime = millis(); routineStep = 2; }
      else {
        // En zigzag usamos VEL_BAJA para diferenciar el giro
        if ( (timeInStep / T_ZIGZAG_PASO) % 2 == 0 ) { motorA(VEL_MEDIA); motorB(VEL_BAJA); } 
        else { motorA(VEL_BAJA); motorB(VEL_MEDIA); }
      }
      break;
    case 2: routineStep = 3; break;
    case 3: 
      if (timeInStep > T_ZIGZAG_10S) { terminateRoutine(); }
      else {
        if ( (timeInStep / T_ZIGZAG_PASO) % 2 == 0 ) { motorA(-VEL_MEDIA); motorB(-VEL_BAJA); } 
        else { motorA(-VEL_BAJA); motorB(-VEL_MEDIA); }
      }
      break;
  }
}

void runRoutine4() {
  unsigned long timeInStep = millis() - stepStartTime;
  switch (routineStep) {
    case 0: forward(VEL_MEDIA); stepStartTime = millis(); routineStep = 1; break;
    case 1: if (timeInStep > T_AVANCE_20CM) { spinRight(VEL_MEDIA); stepStartTime = millis(); routineStep = 2; } break;
    case 2: if (timeInStep > T_GIRO_90_R) { forward(VEL_MEDIA); stepStartTime = millis(); routineStep = 3; } break;
    case 3: if (timeInStep > T_AVANCE_30CM) { turnRight(VEL_MEDIA); stepStartTime = millis(); routineStep = 4; } break;
    case 4: if (timeInStep > T_CIRCULO_10S) { stopMotors(); stepStartTime = millis(); routineStep = 5; } break;
    case 5: if (timeInStep > T_PAUSA_2S) { backward(VEL_MEDIA); stepStartTime = millis(); routineStep = 6; } break;
    case 6: if (timeInStep > T_AVANCE_20CM) { terminateRoutine(); } break;
  }
}

void runRoutines() {
  switch (currentRoutine) {
    case 1: runRoutine1(); break;
    case 2: runRoutine2(); break;
    case 3: runRoutine3(); break;
    case 4: runRoutine4(); break; 
  }
}

// -------------------------------------------------------------------
//   PARSING Y COMUNICACIÓN
// -------------------------------------------------------------------

String getValue(String data, char separator, int index) {
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length() - 1;
  for (int i = 0; i <= maxIndex && found <= index; i++) {
    if (data.charAt(i) == separator || i == maxIndex) {
      found++;
      strIndex[0] = strIndex[1] + 1;
      strIndex[1] = (i == maxIndex) ? i + 1 : i;
    }
  }
  return found > index ? data.substring(strIndex[0], strIndex[1]) : "";
}

void parseCommand(String cmd) {
  if (cmd.length() == 0) return;
  
  Serial.print("ROS CMD: "); Serial.println(cmd);

  char commandType = cmd.charAt(0);
  String p1 = getValue(cmd, ',', 1);
  String p2 = getValue(cmd, ',', 2);

  switch (commandType) {
    case 'M': // Modo Libre
      if (currentState == IDLE || currentState == FREE_MODE) {
        currentState = FREE_MODE;
        int vel = p2.toInt();
        // Ajustamos también la velocidad del modo libre si viene muy alta
        // Aunque generalmente aquí usas lo que manda el slider
        if (p1 == "F") forward(vel);
        else if (p1 == "B") backward(vel);
        else if (p1 == "R") spinRight(vel);
        else if (p1 == "L") spinLeft(vel);
        else if (p1 == "S") { stopMotors(); currentState = IDLE; }
      }
      break;

    case 'R': // Rutina
      if (currentState == IDLE || currentState == FREE_MODE) {
        if (currentState == FREE_MODE) stopMotors();
        currentRoutine = p1.toInt();
        if (currentRoutine > 0 && currentRoutine <= 4) {
          currentState = ROUTINE;
          routineStep = 0;
          stepTimeElapsed = 0;
        }
      }
      break;

    case 'P': // Pause
      if (currentState == ROUTINE) {
        stepTimeElapsed = millis() - stepStartTime;
        currentState = PAUSED;
        stopMotors();
      }
      break;

    case 'C': // Continue
      if (currentState == PAUSED) {
        currentState = ROUTINE;
        stepStartTime = millis() - stepTimeElapsed;
        applyCurrentStepAction();
      }
      break;

    case 'T': // Terminate
      if (currentState == ROUTINE || currentState == PAUSED || currentState == FREE_MODE) {
         terminateRoutine();
      }
      break;
  }
}

void subscription_callback(const void * msgin) {  
  const std_msgs__msg__String * msg_received = (const std_msgs__msg__String *)msgin;
  if (msg_received->data.data != NULL) {
      String comandoStr = String(msg_received->data.data);
      parseCommand(comandoStr);
  }
}


void setup() {
  Serial.begin(115200);
  
  pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT); ledcAttach(ENA, FREQ, RES);
  pinMode(IN3, OUTPUT); pinMode(IN4, OUTPUT); ledcAttach(ENB, FREQ, RES);
  pinMode(LED_PIN, OUTPUT);
  stopMotors();

  set_microros_wifi_transports("Toluca", "cruzAzul69", "10.189.43.250", 8888);
  
  delay(2000);

  allocator = rcl_get_default_allocator();
  RCCHECK(rclc_support_init(&support, 0, NULL, &allocator));
  RCCHECK(rclc_node_init_default(&node, "terreneitor_node", "", &support));

  msg.data.capacity = 100;
  msg.data.data = (char*) malloc(msg.data.capacity * sizeof(char));
  msg.data.size = 0;

  RCCHECK(rclc_subscription_init_default(
    &subscriber,
    &node,
    ROSIDL_GET_MSG_TYPE_SUPPORT(std_msgs, msg, String),
    "robot_commands"));

  RCCHECK(rclc_executor_init(&executor, &support.context, 1, &allocator));
  RCCHECK(rclc_executor_add_subscription(&executor, &subscriber, &msg, &subscription_callback, ON_NEW_DATA));
}

void loop() {
  RCCHECK(rclc_executor_spin_some(&executor, RCL_MS_TO_NS(100)));
  
  switch (currentState) {
    case ROUTINE:
      runRoutines();
      break;
    default:
      break;
  }
  delay(10);
}