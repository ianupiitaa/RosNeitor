"""
--------------------------------------------------------------------------------
Archivo: juego.py
Proyecto: ROSneitor
Autor: Equipo COCOMORA UDG
Materia: Programación Avanzada
Fecha: [30/12/2025]

Descripción:
    Este módulo contiene la lógica de la ventana de control (GUI) y la 
    comunicación con el sistema ROS 2.
    
    Clases:
    - CommanderNode: Nodo Publisher de ROS 2.
    - VentanaJuego: Interfaz gráfica que captura eventos de usuario y 
      los envía como comandos al robot.
--------------------------------------------------------------------------------
"""

import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

from PyQt6.QtWidgets import QWidget
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt, pyqtSignal, QTimer

class CommanderNode(Node):
    """
    Clase que hereda de rclpy.node.Node.
    Actúa como el 'Publisher' del sistema, enviando cadenas de texto (Strings)
    al tópico '/robot_commands' para que el ESP32 las interprete.
    """
    def __init__(self):
        super().__init__('pc_controller_node')
        # Creamos un publisher que envía mensajes de tipo String
        # Queue size = 10 (mantiene los últimos 10 mensajes si la red se satura)
        self.publisher_ = self.create_publisher(String, 'robot_commands', 10)

    def send_command(self, command_str):
        """
        Empaqueta un string de Python en un mensaje ROS y lo publica.
        Args:
            command_str (str): El comando a enviar (Ej: "M,F,180")
        """
        msg = String()
        msg.data = command_str
        self.publisher_.publish(msg)

class VentanaJuego(QWidget):
    """
    Clase de la interfaz gráfica de control.
    Gestiona los botones de movimiento, selección de rutinas y estados de pausa.
    """
    
    # Señal personalizada para notificar al main.py que queremos volver al menú
    volver_menu = pyqtSignal()
    
    def __init__(self, rutina_seleccionada, Volumen_principal):
        super().__init__()
        
        # Cargar archivo de interfaz (.ui)
        try:
            loadUi("ventana_juego.ui", self)
        except Exception as e:
            print(f"Error cargando UI en juego.py: {e}")
        
        # --- INICIALIZACIÓN DE ROS 2 ---
        # Verificamos si rclpy ya está corriendo para no iniciarlo doble
        if not rclpy.ok():
            rclpy.init()
        
        # Instanciamos nuestro nodo publicador
        self.ros_node = CommanderNode()

        # Configuración inicial de variables
        self.rutina_actual = rutina_seleccionada
        self.rutina_juego.setText(f"Rutina en ejecución: {self.rutina_actual}")
  
        # --- SINCRONIZACIÓN DE VOLUMEN ---
        self.Volumen_principal = Volumen_principal
        if hasattr(self, 'Volumen'):
            self.Volumen.setRange(0, 100)
            self.Volumen.setValue(self.Volumen_principal.value())
            self.Volumen.valueChanged.connect(self.Volumen_principal.setValue)
        
        # --- CONEXIÓN DE BOTONES ---
        
        # Botones del menú de pausa (StackedWidget Página 1)
        self.btnvolverjuego.clicked.connect(self.reanudar_rutina)
        self.btnvolvermenu.clicked.connect(self.regresar)
        
        # Botones de movimiento (Modo Libre - Página 0)
        # Usamos 'pressed' para iniciar movimiento y 'released' para detenerlo
        # Esto crea el efecto de "hombre muerto" (si sueltas, se para)
        self.btnadelante.pressed.connect(self.mover_adelante)
        self.btnadelante.released.connect(self.detener_motores)
        
        self.btnatras.pressed.connect(self.mover_atras)
        self.btnatras.released.connect(self.detener_motores)
        
        self.btnderecha.pressed.connect(self.girar_derecha)
        self.btnderecha.released.connect(self.detener_motores)
        
        self.btnizquierda.pressed.connect(self.girar_izquierda)
        self.btnizquierda.released.connect(self.detener_motores)
        
        # Configuración visual inicial (ocultar flechas si es Rutina)
        self.configurar_controles()
        
        # Botones de control de rutina (Pausar/Finalizar)
        self.pausarRutina.setCheckable(True)
        self.pausarRutina.toggled.connect(self.pausar_reanudar_rutina)
        self.finalizarRutina.clicked.connect(self.parar_rutina)
        
    
        # Usamos QTimer para esperar 1000ms (1 segundo) antes de enviar 
        # el comando de inicio. Esto permite que el Micro-ROS Agent y el ESP32
        # establezcan la conexión Wi-Fi antes de recibir datos.
        QTimer.singleShot(1000, self.logica_juego)

    def keyPressEvent(self, event):
        """
        Manejo de eventos de teclado.
        Tecla ESC: Pausa de emergencia y muestra el menú de pausa.
        """
        if event.key() == Qt.Key.Key_Escape:
            # Enviar comando de pausa al robot inmediatamente
            self.enviar_comando('P,0')
            
            # Cambiamos a la página del menú de pausa (Índice 1)
            if hasattr(self, 'stackedWidget'):
                self.stackedWidget.setCurrentIndex(1)

    def reanudar_rutina(self):
        """Regresa a la pantalla de juego y envía comando de continuar."""
        if hasattr(self, 'stackedWidget'):
            self.stackedWidget.setCurrentIndex(0)
        self.enviar_comando('C,0') # Protocolo: C = Continue

    # --- COMUNICACIÓN ROS ---
    def enviar_comando(self, comando):
        """Wrapper seguro para enviar comandos vía el nodo ROS."""
        if self.ros_node:
            self.ros_node.send_command(comando)

    # --- FUNCIONES DE CONTROL VISUAL ---
    def configurar_controles(self):
        """
        Muestra u oculta elementos de la UI dependiendo si estamos 
        en 'Modo Libre' o ejecutando una 'Rutina'.
        """
        modo_libre = self.rutina_actual == "Modo Libre"
        
        # En modo libre, mostramos flechas y control de velocidad
        self.btnadelante.setVisible(modo_libre)
        self.btnatras.setVisible(modo_libre)
        self.btnderecha.setVisible(modo_libre)
        self.btnizquierda.setVisible(modo_libre)
        self.AjustarVelocidad.setVisible(modo_libre)
        
        # En rutinas, mostramos botones de gestión (Pausar/Terminar)
        self.pausarRutina.setVisible(not modo_libre)
        self.finalizarRutina.setVisible(not modo_libre)
        
        if modo_libre:
            # Rango de PWM para el ESP32 (0-255)
            # Limitamos el mínimo a 100 para vencer inercia
            self.AjustarVelocidad.setRange(100, 250)
            self.AjustarVelocidad.setValue(180)

    # --- LÓGICA DE MOVIMIENTO (Protocolo de Texto) ---
    # Formato: TIPO, DIRECCIÓN, VELOCIDAD
    # M = Movimiento, F=Front, B=Back, R=Right, L=Left, S=Stop
    
    def pausar_reanudar_rutina(self, presionado):
        if presionado:
            self.enviar_comando("P,0") # P = Pause
            self.pausarRutina.setText("Reanudar")
        else:
            self.enviar_comando("C,0") # C = Continue
            self.pausarRutina.setText("Pausar")
    
    def parar_rutina(self):
        self.enviar_comando("T,0") # T = Terminate
        self.regresar()
        
    def mover_adelante(self):
        velocidad = self.AjustarVelocidad.value()
        self.enviar_comando(f"M,F,{velocidad}")

    def mover_atras(self):
        velocidad = self.AjustarVelocidad.value()
        self.enviar_comando(f"M,B,{velocidad}")

    def girar_derecha(self):
        velocidad = self.AjustarVelocidad.value()
        self.enviar_comando(f"M,R,{velocidad}")

    def girar_izquierda(self):
        velocidad = self.AjustarVelocidad.value()
        self.enviar_comando(f"M,L,{velocidad}")

    def detener_motores(self):
        self.enviar_comando("M,S,0")

    def regresar(self):
        """Finaliza la operación actual y emite señal para volver al menú principal."""
        # Si salimos, mandamos señal de terminar o detener motores por seguridad
        if "Rutina" in self.rutina_actual:
            self.enviar_comando("T,0") 
        elif self.rutina_actual == "Modo Libre":
            self.detener_motores()

        self.volver_menu.emit()
        self.close()
        
    def logica_juego(self):
        """
        Se ejecuta automáticamente tras el delay de inicio.
        Parsea el nombre de la rutina y envía el comando de arranque.
        """
        # Si es una rutina (Ej: "Rutina 2"), extraemos el número
        if "Rutina" in self.rutina_actual:
            try:
                # "Rutina 2" -> split(" ") -> ["Rutina", "2"] -> "2"
                numero_rutina = self.rutina_actual.split(" ")[1]
                self.enviar_comando(f"R,{numero_rutina}")
            except IndexError:
                pass
            
    def closeEvent(self, event):
        """
        Se llama automáticamente al cerrar la ventana.
        Destruye el nodo ROS para liberar recursos del sistema.
        """
        if self.ros_node:
            self.ros_node.destroy_node()
        event.accept()