# 🤖 RosNeitor

<div align="center">

![Estado](https://img.shields.io/badge/Estado-Completo-success?style=for-the-badge)
![ROS](https://img.shields.io/badge/ROS-Micro--ROS-blue?style=for-the-badge&logo=ros)
![ESP32](https://img.shields.io/badge/ESP32-Compatible-green?style=for-the-badge&logo=espressif)
![Arduino](https://img.shields.io/badge/Arduino-.ino-00979D?style=for-the-badge&logo=arduino)

**Sistema de control robótico inteligente para ESP32 con ROS y micro-ROS**

[Características](#-características) • [Tecnologías](#-tecnologías) • [Estructura](#-estructura-del-proyecto) • [Instalación](#-instalación) • [Uso](#-uso)

</div>

---

## 📋 Descripción

**RosNeitor** es un proyecto de control robótico que integra una **ESP32** con **ROS (Robot Operating System)** y **micro-ROS**. El sistema permite controlar un carrito robótico mediante una interfaz amigable, proporcionando comunicación bidireccional entre el microcontrolador y el sistema ROS.

### 🎯 Objetivo

Crear una solución completa para el control de robots móviles utilizando tecnologías modernas de robótica, combinando la potencia de ESP32 con la flexibilidad de ROS.

---

## ✨ Características

- 🔌 **Control ESP32**: Código Arduino (.ino) optimizado para ESP32
- 🌐 **Integración ROS**: Comunicación completa con ROS mediante micro-ROS
- 🎮 **Interfaz de Control**: Sistema de órdenes para manejo del carrito
- 📡 **Comunicación Bidireccional**: Envío y recepción de comandos en tiempo real
- ⚡ **Bajo Consumo**: Optimizado para eficiencia energética
- 🔄 **Arquitectura Modular**: Fácil de extender y modificar

---

## 🛠️ Tecnologías

| Tecnología | Descripción | Uso en el Proyecto |
|------------|-------------|-------------------|
| **ESP32** | Microcontrolador de doble núcleo con WiFi y Bluetooth | Controlador principal del carrito |
| **Arduino IDE** | Entorno de desarrollo para ESP32 | Programación de archivos .ino |
| **ROS (Robot Operating System)** | Framework de código abierto para robots | Sistema de comunicación y control |
| **micro-ROS** | ROS 2 para microcontroladores | Puente entre ESP32 y ROS |
| **C/C++** | Lenguajes de programación | Implementación del código embebido |

---

## 📁 Estructura del Proyecto

```
RosNeitor/
│
├── 📄 README.md                    # Este archivo
│
├── 🔧 Códigos ESP32/
│   ├── control_motor.ino          # Control de motores del carrito
│   ├── comunicacion_ros.ino       # Interfaz de comunicación micro-ROS
│   └── sensores.ino               # Lectura de sensores (opcional)
│
├── 🖥️ Interfaz de Control/
│   ├── controlador_web/           # Interfaz web (opcional)
│   └── nodos_ros/                 # Nodos ROS para control
│
└── 📚 Documentación/
    ├── diagramas/                 # Diagramas de arquitectura
    └── guias/                     # Guías de configuración
```

---

## 📦 Instalación

### Requisitos Previos

- ✅ **Arduino IDE** (versión 1.8.x o superior)
- ✅ **Soporte para ESP32** en Arduino IDE
- ✅ **ROS 2** (Foxy, Galactic o Humble)
- ✅ **micro-ROS** para ESP32
- ✅ Placa **ESP32** (NodeMCU, DevKit, etc.)

### Pasos de Instalación

1️⃣ **Clonar el repositorio**
```bash
git clone https://github.com/ianupiitaa/RosNeitor.git
cd RosNeitor
```

2️⃣ **Configurar Arduino IDE para ESP32**
```
- Abrir Arduino IDE
- Ir a Archivo > Preferencias
- Agregar en "Gestor de URLs Adicionales de Tarjetas":
  https://dl.espressif.com/dl/package_esp32_index.json
- Instalar ESP32 desde Herramientas > Placa > Gestor de tarjetas
```

3️⃣ **Instalar micro-ROS**
```bash
# En tu workspace de ROS 2
source /opt/ros/<tu_distro>/setup.bash
git clone -b <distro> https://github.com/micro-ROS/micro_ros_setup.git src/micro_ros_setup
rosdep update && rosdep install --from-paths src --ignore-src -y
colcon build
source install/local_setup.bash
```

4️⃣ **Configurar micro-ROS para ESP32**
```bash
ros2 run micro_ros_setup create_firmware_ws.sh freertos esp32
ros2 run micro_ros_setup configure_firmware.sh [tu_app] -t udp -i [IP_de_tu_PC] -p 8888
ros2 run micro_ros_setup build_firmware.sh
```

---

## 🚀 Uso

### Cargar el Código a ESP32

1. Abre el archivo `.ino` correspondiente en Arduino IDE
2. Selecciona tu placa ESP32 en `Herramientas > Placa`
3. Selecciona el puerto correcto en `Herramientas > Puerto`
4. Haz clic en "Subir" ⬆️

### Ejecutar el Sistema ROS

```bash
# Terminal 1: Iniciar el agente micro-ROS
ros2 run micro_ros_agent micro_ros_agent udp4 --port 8888

# Terminal 2: Lanzar los nodos de control
ros2 launch rosneitor control.launch.py

# Terminal 3: Enviar comandos (ejemplo)
ros2 topic pub /cmd_vel geometry_msgs/Twist "linear: {x: 0.5, y: 0.0, z: 0.0}"
```

---

## 📝 Descripción de Códigos

### 🔹 `control_motor.ino`
**Propósito**: Controla los motores del carrito robótico

**Funcionalidades**:
- Control PWM de velocidad de motores
- Dirección de movimiento (adelante, atrás, izquierda, derecha)
- Funciones de parada de emergencia
- Calibración de velocidad

**Componentes**:
- Driver de motores (L298N o similar)
- Motores DC
- Alimentación adecuada

### 🔹 `comunicacion_ros.ino`
**Propósito**: Establece la comunicación entre ESP32 y ROS mediante micro-ROS

**Funcionalidades**:
- Inicialización de micro-ROS
- Suscripción a tópicos de comando (`/cmd_vel`)
- Publicación de estado del robot
- Manejo de conexión WiFi
- Sincronización de tiempo con ROS

**Protocolo**:
- Comunicación UDP/TCP
- Mensajes estándar de ROS 2

### 🔹 `sensores.ino` (Opcional)
**Propósito**: Lectura y procesamiento de sensores del carrito

**Funcionalidades**:
- Lectura de sensores ultrasónicos (distancia)
- Lectura de sensores infrarrojos (línea/obstáculos)
- Lectura de encoders (odometría)
- Publicación de datos de sensores a ROS

---

## 🎨 Diagrama de Arquitectura

```
┌─────────────────────────────────────────────────────────────┐
│                    SISTEMA ROSNEITOR                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐         ┌──────────────┐                │
│  │   Interfaz   │  WiFi   │    ESP32     │                │
│  │   Usuario/   │◄───────►│  + micro-ROS │                │
│  │     ROS      │   UDP   │              │                │
│  └──────────────┘         └───────┬──────┘                │
│                                   │                         │
│                                   ▼                         │
│                          ┌─────────────────┐               │
│                          │  Control PWM    │               │
│                          │                 │               │
│                          │  ┌───┐   ┌───┐ │               │
│                          │  │ M1│   │ M2│ │               │
│                          │  └───┘   └───┘ │               │
│                          │   Motores DC    │               │
│                          └─────────────────┘               │
│                                                             │
│           🤖 Carrito Robótico Controlado 🤖                │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔧 Configuración

### Variables Importantes

En los archivos `.ino`, asegúrate de configurar:

```cpp
// WiFi
const char* WIFI_SSID = "tu_red_wifi";
const char* WIFI_PASSWORD = "tu_contraseña";

// micro-ROS
const char* AGENT_IP = "192.168.1.100";  // IP de tu PC con ROS
const int AGENT_PORT = 8888;

// Pines de Motores
#define MOTOR_A_PIN1 25
#define MOTOR_A_PIN2 26
#define MOTOR_B_PIN1 27
#define MOTOR_B_PIN2 14
```

---

## 📊 Estado del Proyecto

| Componente | Estado | Descripción |
|------------|--------|-------------|
| Código ESP32 | ✅ Completo | Firmware listo para usar |
| Integración micro-ROS | ✅ Completo | Comunicación establecida |
| Control de Motores | ✅ Completo | Sistema PWM funcional |
| Interfaz de Usuario | ✅ Completo | Comandos ROS operativos |
| Documentación | ✅ Completo | Guías y ejemplos incluidos |

**Estado General del Proyecto**: 🟢 **COMPLETO**

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto:

1. 🍴 Fork el proyecto
2. 🌿 Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. 💾 Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. 📤 Push a la rama (`git push origin feature/nueva-caracteristica`)
5. 🔃 Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo licencia libre para uso educativo y de desarrollo.

---

## 👤 Autor

**ianupiitaa**

- GitHub: [@ianupiitaa](https://github.com/ianupiitaa)

---

## 📞 Soporte

Si tienes preguntas o problemas:

- 📧 Abre un [Issue](https://github.com/ianupiitaa/RosNeitor/issues)
- 💬 Participa en las [Discussions](https://github.com/ianupiitaa/RosNeitor/discussions)

---

<div align="center">

### ⭐ Si este proyecto te fue útil, considera darle una estrella ⭐

**Hecho con ❤️ para la comunidad de robótica**

</div>
