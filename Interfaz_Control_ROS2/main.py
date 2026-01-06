"""
--------------------------------------------------------------------------------
Archivo: main.py
Proyecto: ROSneitor - Control con ROS 2
Autor: Equipo COCOMORA UDG
Materia: Programación Avanzada
Fecha: [30/12/2025]

Descripción:
    Este archivo gestiona la Ventana Principal (Menú), la reproducción de música
    de fondo, la selección del modo de operación y la transición hacia la 
    interfaz de control del robot (VentanaJuego).
--------------------------------------------------------------------------------
"""

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.uic import loadUi
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput
from PyQt6.QtCore import QUrl

# Importamos la clase de la ventana de juego (Lógica ROS 2)
from juego import VentanaJuego
# Importamos los recursos compilados (imágenes, iconos, etc.)
import recursos_imagenes_rc

class Terreneitor(QMainWindow):
    """
    Clase principal que gestiona el menú de inicio y la configuración global.
    Hereda de QMainWindow.
    """
    def __init__(self):
        super().__init__()
        
        # Cargar la interfaz gráfica desde el archivo .ui
        try:
            loadUi("menu_principal.ui", self)
        except Exception as e:
            print(f"Error al cargar UI del menú: {e}")
        
        # --- CONFIGURACIÓN DE AUDIO (Música de Fondo) ---
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
        # Cargar archivo de audio local
        source = QUrl.fromLocalFile("Bruce_Wayne.mp3")
        self.player.setSource(source)
        
        # Configurar bucle infinito para la música
        self.player.setLoops(QMediaPlayer.Loops.Infinite)
        
        # Configuración inicial del Slider de Volumen
        self.Volumen.setRange(0, 100)
        self.Volumen.setValue(50)
        self.audio_output.setVolume(0.5) # 0.5 equivale al 50%
        
        # Conectar el slider a la función de cambio de volumen
        self.Volumen.valueChanged.connect(self.cambiar_volumen)
        
        # Iniciar reproducción
        self.player.play()
        
        # --- NAVEGACIÓN DEL MENÚ (QStackedWidget) ---
        # El stackedwindow permite cambiar entre "páginas" (Inicio, Jugar, Opciones)
        # Índice 0: Menú Principal
        # Índice 1: Selección de Modo (Jugar)
        # Índice 2: Opciones / Créditos
        
        self.btnjugar.clicked.connect(lambda: self.stackedwindow.setCurrentIndex(1))
        self.btnopciones.clicked.connect(lambda: self.stackedwindow.setCurrentIndex(2))
        
        # Botones de retorno (volver al índice 0)
        self.btnvolver1.clicked.connect(lambda: self.stackedwindow.setCurrentIndex(0))
        self.btnvolver2.clicked.connect(lambda: self.stackedwindow.setCurrentIndex(0))
        
        # Botón para salir de la aplicación
        self.btnsalir.clicked.connect(self.close) 
        
        # Botón para iniciar la conexión ROS y abrir la ventana de control
        self.btniniciar.clicked.connect(self.iniciar_juego)
        
        # Variable para controlar la instancia de la ventana de juego
        self.ventana_de_juego_activa = None
    
    def cambiar_volumen(self, valor):
        """
        Ajusta el volumen de la música y sincroniza el slider 
        con la ventana de juego si esta está abierta.
        
        Args:
            valor (int): Valor del slider (0-100).
        """
        # QAudioOutput requiere un valor float entre 0.0 y 1.0
        volumen_float = valor / 100.0
        self.audio_output.setVolume(volumen_float)
        
        # Sincronización: Si la ventana de juego está abierta, actualizamos su slider también
        if self.ventana_de_juego_activa and self.ventana_de_juego_activa.isVisible():
            # Verificamos que la ventana tenga el atributo 'Volumen'
            if hasattr(self.ventana_de_juego_activa, 'Volumen'):
                # Bloqueamos señales temporalmente para evitar bucle infinito de actualizaciones
                self.ventana_de_juego_activa.Volumen.blockSignals(True)
                self.ventana_de_juego_activa.Volumen.setValue(valor)
                self.ventana_de_juego_activa.Volumen.blockSignals(False)
        
    def iniciar_juego(self):
        """
        Instancia la ventana de control (VentanaJuego), inicia el nodo de ROS 2
        y oculta el menú principal.
        """
        # Obtener el modo seleccionado del ComboBox (Ej: "Modo Libre", "Rutina 1")
        rutina_elegida = self.elegir_modo.currentText()
        
        # Crear instancia de la ventana de juego
        # Pasamos el volumen actual para mantener consistencia
        self.ventana_de_juego_activa = VentanaJuego(
            rutina_seleccionada=rutina_elegida,
            Volumen_principal=self.Volumen
            )
        
        # Conectar la señal personalizada 'volver_menu' para saber cuándo regresar
        self.ventana_de_juego_activa.volver_menu.connect(self.regresar_menu)
        
        # Mostrar ventana de juego y ocultar menú
        self.ventana_de_juego_activa.show()
        self.hide()
        
    def regresar_menu(self):
        """
        Maneja el retorno desde la ventana de juego al menú principal.
        Restaura la visibilidad y reinicia el estado de selección.
        """
        # Regresar a la página inicial del menú
        self.stackedwindow.setCurrentIndex(0)
        self.elegir_modo.setCurrentIndex(0)
        
        # Mostrar nuevamente el menú
        self.show()
        
        # Sincronizar volumen de regreso (por si se cambió durante el juego)
        if self.ventana_de_juego_activa:
            vol_juego = self.ventana_de_juego_activa.Volumen.value()
            self.Volumen.setValue(vol_juego)
            
            # Limpiar la referencia
            self.ventana_de_juego_activa = None

if __name__ == '__main__':
    # Inicialización de la aplicación Qt
    app = QApplication(sys.argv)
    ventana = Terreneitor()
    ventana.show()
    sys.exit(app.exec())