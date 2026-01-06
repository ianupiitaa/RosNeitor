# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_principal.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Terreneitor(object):
    def setupUi(self, Terreneitor):
        if not Terreneitor.objectName():
            Terreneitor.setObjectName(u"Terreneitor")
        Terreneitor.resize(600, 500)
        Terreneitor.setMinimumSize(QSize(600, 500))
        Terreneitor.setMaximumSize(QSize(600, 500))
        icon = QIcon()
        icon.addFile(u"icono.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Terreneitor.setWindowIcon(icon)
        self.centralwidget = QWidget(Terreneitor)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedwindow = QStackedWidget(self.centralwidget)
        self.stackedwindow.setObjectName(u"stackedwindow")
        self.pagina_menu = QWidget()
        self.pagina_menu.setObjectName(u"pagina_menu")
        self.verticalLayout = QVBoxLayout(self.pagina_menu)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.pagina_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.btnjugar = QPushButton(self.frame)
        self.btnjugar.setObjectName(u"btnjugar")
        self.btnjugar.setEnabled(True)
        self.btnjugar.setGeometry(QRect(250, 240, 100, 40))
        self.btnjugar.setMinimumSize(QSize(100, 40))
        self.btnjugar.setMaximumSize(QSize(100, 30))
        self.btnjugar.setStyleSheet(u"/* Estilo para la ventana principal (el fondo) */\n"
"#ventanaPrincipal {\n"
"    background-image: url(menu.jpg); /* Aseg\u00farate que menu.jpg est\u00e9 accesible */\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover;\n"
"}\n"
"\n"
"/* Estilo para TODOS los QPushButton */\n"
"QPushButton {\n"
"    /* Tama\u00f1o espec\u00edfico */\n"
"    width: 100px; /* Ancho del bot\u00f3n */\n"
"    height: 54px; /* Altura del bot\u00f3n */\n"
"\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF; /* Texto blanco */\n"
"    background-color: rgba(30, 0, 70, 0.8); /* Fondo oscuro m\u00e1s intenso y opaco */\n"
"    border: 3px solid #FF00FF; /* Borde ne\u00f3n m\u00e1s grueso y vibrante (fuchsia) */\n"
"    border-radius: 15px; /* Bordes redondeados */\n"
"    padding: 0px; /* Quitamos el padding para que width/height controlen el tama\u00f1o total */\n"
"    \n"
"}\n"
"\n"
"/* Efecto al pasar el mouse por encima */\n"
"QPushButton:hover {\n"
""
                        "    background-color: rgba(255, 0, 255, 0.8); /* Se ilumina con el color fuchsia ne\u00f3n, m\u00e1s opaco */\n"
"    border: 3px solid #FFFFFF; /* Borde cambia a blanco */\n"
"\n"
"}\n"
"\n"
"/* Efecto al presionar el bot\u00f3n */\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 0, 255, 1); /* Completamente opaco y brillante */\n"
"    border: 3px solid #DDDDDD;\n"
"\n"
"}")
        self.btnopciones = QPushButton(self.frame)
        self.btnopciones.setObjectName(u"btnopciones")
        self.btnopciones.setGeometry(QRect(250, 290, 100, 40))
        self.btnopciones.setMinimumSize(QSize(100, 30))
        self.btnopciones.setMaximumSize(QSize(100, 40))
        self.btnopciones.setStyleSheet(u"/* Estilo para la ventana principal (el fondo) */\n"
"#ventanaPrincipal {\n"
"    background-image: url(menu.jpg); /* Aseg\u00farate que menu.jpg est\u00e9 accesible */\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover;\n"
"}\n"
"\n"
"/* Estilo para TODOS los QPushButton */\n"
"QPushButton {\n"
"    /* Tama\u00f1o espec\u00edfico */\n"
"    width: 100px; /* Ancho del bot\u00f3n */\n"
"    height: 54px; /* Altura del bot\u00f3n */\n"
"\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF; /* Texto blanco */\n"
"    background-color: rgba(30, 0, 70, 0.8); /* Fondo oscuro m\u00e1s intenso y opaco */\n"
"    border: 3px solid #FF00FF; /* Borde ne\u00f3n m\u00e1s grueso y vibrante (fuchsia) */\n"
"    border-radius: 15px; /* Bordes redondeados */\n"
"    padding: 0px; /* Quitamos el padding para que width/height controlen el tama\u00f1o total */\n"
"    \n"
"\n"
"}\n"
"\n"
"/* Efecto al pasar el mouse por encima */\n"
"QPushButton:hover {"
                        "\n"
"    background-color: rgba(255, 0, 255, 0.8); /* Se ilumina con el color fuchsia ne\u00f3n, m\u00e1s opaco */\n"
"    border: 3px solid #FFFFFF; /* Borde cambia a blanco */\n"
"\n"
"}\n"
"\n"
"/* Efecto al presionar el bot\u00f3n */\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 0, 255, 1); /* Completamente opaco y brillante */\n"
"    border: 3px solid #DDDDDD;\n"
"\n"
"}")
        self.btnsalir = QPushButton(self.frame)
        self.btnsalir.setObjectName(u"btnsalir")
        self.btnsalir.setGeometry(QRect(250, 430, 100, 30))
        self.btnsalir.setMinimumSize(QSize(100, 30))
        self.btnsalir.setMaximumSize(QSize(100, 30))
        self.btnsalir.setStyleSheet(u"/* Estilo para la ventana principal (el fondo) */\n"
"#ventanaPrincipal {\n"
"    background-image: url(menu.jpg); /* Aseg\u00farate que menu.jpg est\u00e9 accesible */\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover;\n"
"}\n"
"\n"
"/* Estilo para TODOS los QPushButton */\n"
"QPushButton {\n"
"    /* Tama\u00f1o espec\u00edfico */\n"
"    width: 100px; /* Ancho del bot\u00f3n */\n"
"    height: 54px; /* Altura del bot\u00f3n */\n"
"\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    color: #FFFFFF; /* Texto blanco */\n"
"    background-color: rgba(30, 0, 70, 0.8); /* Fondo oscuro m\u00e1s intenso y opaco */\n"
"    border: 3px solid #FF00FF; /* Borde ne\u00f3n m\u00e1s grueso y vibrante (fuchsia) */\n"
"    border-radius: 15px; /* Bordes redondeados */\n"
"    padding: 0px; /* Quitamos el padding para que width/height controlen el tama\u00f1o total */\n"
"    \n"
"\n"
"}\n"
"\n"
"/* Efecto al pasar el mouse por encima */\n"
"QPushButton:hover {"
                        "\n"
"    background-color: rgba(255, 0, 255, 0.8); /* Se ilumina con el color fuchsia ne\u00f3n, m\u00e1s opaco */\n"
"    border: 3px solid #FFFFFF; /* Borde cambia a blanco */\n"
"\n"
"}\n"
"\n"
"/* Efecto al presionar el bot\u00f3n */\n"
"QPushButton:pressed {\n"
"    background-color: rgba(255, 0, 255, 1); /* Completamente opaco y brillante */\n"
"    border: 3px solid #DDDDDD;\n"
"\n"
"}")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-50, -20, 691, 601))
        self.label_4.setPixmap(QPixmap(u"menu.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.raise_()
        self.btnjugar.raise_()
        self.btnopciones.raise_()
        self.btnsalir.raise_()

        self.verticalLayout.addWidget(self.frame)

        self.stackedwindow.addWidget(self.pagina_menu)
        self.pagina_jugar = QWidget()
        self.pagina_jugar.setObjectName(u"pagina_jugar")
        self.horizontalLayout = QHBoxLayout(self.pagina_jugar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.pagina_jugar)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.neonTextLabel = QLabel(self.frame_3)
        self.neonTextLabel.setObjectName(u"neonTextLabel")
        self.neonTextLabel.setGeometry(QRect(90, 120, 411, 71))
        font = QFont()
        font.setFamilies([u"BBH Sans Bogle"])
        font.setPointSize(36)
        font.setBold(False)
        self.neonTextLabel.setFont(font)
        self.neonTextLabel.setStyleSheet(u"")
        self.elegir_modo = QComboBox(self.frame_3)
        self.elegir_modo.addItem("")
        self.elegir_modo.addItem("")
        self.elegir_modo.addItem("")
        self.elegir_modo.addItem("")
        self.elegir_modo.addItem("")
        self.elegir_modo.setObjectName(u"elegir_modo")
        self.elegir_modo.setGeometry(QRect(230, 220, 141, 31))
        self.elegir_modo.setMinimumSize(QSize(100, 30))
        self.elegir_modo.setMaximumSize(QSize(200, 35))
        self.elegir_modo.setStyleSheet(u"/* Pega esto DIRECTAMENTE en el ComboBox */\n"
"QComboBox {\n"
"    color: #E0E0E0;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    background-color: rgba(30, 30, 30, 0.7);\n"
"    border: 1px solid #707070;\n"
"    border-radius: 5px;\n"
"    padding: 8px 10px;\n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: rgba(50, 50, 50, 0.8);\n"
"    border: 1px solid #AAAAAA;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left-width: 1px;\n"
"    border-left-color: #707070;\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"/* ...y as\u00ed con el resto de las reglas (quitando #darkCombo)... */")
        self.btniniciar = QPushButton(self.frame_3)
        self.btniniciar.setObjectName(u"btniniciar")
        self.btniniciar.setGeometry(QRect(250, 280, 100, 30))
        self.btniniciar.setMinimumSize(QSize(100, 30))
        self.btniniciar.setMaximumSize(QSize(100, 30))
        self.btniniciar.setStyleSheet(u"/* Estilo para la ventana principal (el fondo) */\n"
"#ventanaPrincipal {\n"
"    background-image: url(tu_imagen_fondo_negro.jpg); /* Aseg\u00farate de usar la nueva imagen de fondo */\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover;\n"
"}\n"
"\n"
"/* Estilo para TODOS los QPushButton */\n"
"QPushButton {\n"
"    width: 100px;\n"
"    height: 54px;\n"
"    font-size: 16px; /* Un poco m\u00e1s peque\u00f1o para un look m\u00e1s serio */\n"
"    font-weight: bold;\n"
"    color: #E0E0E0; /* Texto blanco gris\u00e1ceo para un look sutil */\n"
"    background-color: rgba(30, 30, 30, 0.7); /* Fondo gris oscuro semi-transparente */\n"
"    border: 1px solid #707070; /* Borde gris sutil */\n"
"    border-radius: 5px; /* Bordes ligeramente redondeados, m\u00e1s cuadrados */\n"
"    padding: 0px;\n"
"    \n"
"\n"
"}\n"
"\n"
"/* Efecto al pasar el mouse por encima */\n"
"QPushButton:hover {\n"
"    color: #FFFFFF; /* Texto blanco puro */\n"
"    background-color"
                        ": rgba(50, 50, 50, 0.8); /* Fondo un poco m\u00e1s claro y opaco */\n"
"    border: 1px solid #AAAAAA; /* Borde m\u00e1s claro */\n"
"\n"
"}\n"
"\n"
"/* Efecto al presionar el bot\u00f3n */\n"
"QPushButton:pressed {\n"
"    color: #DDDDDD;\n"
"    background-color: rgba(20, 20, 20, 0.9); /* M\u00e1s oscuro y opaco para simular \"hundimiento\" */\n"
"    border: 1px solid #505050;\n"
"\n"
"}")
        self.btnvolver1 = QPushButton(self.frame_3)
        self.btnvolver1.setObjectName(u"btnvolver1")
        self.btnvolver1.setGeometry(QRect(250, 420, 100, 30))
        self.btnvolver1.setMinimumSize(QSize(100, 30))
        self.btnvolver1.setMaximumSize(QSize(100, 30))
        self.btnvolver1.setStyleSheet(u"/* Estilo para la ventana principal (el fondo) */\n"
"#ventanaPrincipal {\n"
"    background-image: url(tu_imagen_fondo_negro.jpg); /* Aseg\u00farate de usar la nueva imagen de fondo */\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover;\n"
"}\n"
"\n"
"/* Estilo para TODOS los QPushButton */\n"
"QPushButton {\n"
"    width: 100px;\n"
"    height: 54px;\n"
"    font-size: 16px; /* Un poco m\u00e1s peque\u00f1o para un look m\u00e1s serio */\n"
"    font-weight: bold;\n"
"    color: #E0E0E0; /* Texto blanco gris\u00e1ceo para un look sutil */\n"
"    background-color: rgba(30, 30, 30, 0.7); /* Fondo gris oscuro semi-transparente */\n"
"    border: 1px solid #707070; /* Borde gris sutil */\n"
"    border-radius: 5px; /* Bordes ligeramente redondeados, m\u00e1s cuadrados */\n"
"    padding: 0px;\n"
"    \n"
" \n"
"}\n"
"\n"
"/* Efecto al pasar el mouse por encima */\n"
"QPushButton:hover {\n"
"    color: #FFFFFF; /* Texto blanco puro */\n"
"    background-colo"
                        "r: rgba(50, 50, 50, 0.8); /* Fondo un poco m\u00e1s claro y opaco */\n"
"    border: 1px solid #AAAAAA; /* Borde m\u00e1s claro */\n"
"  \n"
"}\n"
"\n"
"/* Efecto al presionar el bot\u00f3n */\n"
"QPushButton:pressed {\n"
"    color: #DDDDDD;\n"
"    background-color: rgba(20, 20, 20, 0.9); /* M\u00e1s oscuro y opaco para simular \"hundimiento\" */\n"
"    border: 1px solid #505050;\n"
"\n"
"}")
        self.label_6 = QLabel(self.frame_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-50, -80, 691, 661))
        self.label_6.setPixmap(QPixmap(u"menuopciones.jpg"))
        self.label_6.setScaledContents(True)
        self.neonTextLabel_2 = QLabel(self.frame_3)
        self.neonTextLabel_2.setObjectName(u"neonTextLabel_2")
        self.neonTextLabel_2.setGeometry(QRect(80, 130, 411, 71))
        self.neonTextLabel_2.setFont(font)
        self.neonTextLabel_2.setStyleSheet(u"QLabel {\n"
"    color: #000000; /* C\u00f3digo hexadecimal para negro */\n"
"}")
        self.label_6.raise_()
        self.elegir_modo.raise_()
        self.btniniciar.raise_()
        self.btnvolver1.raise_()
        self.neonTextLabel_2.raise_()
        self.neonTextLabel.raise_()

        self.horizontalLayout.addWidget(self.frame_3)

        self.stackedwindow.addWidget(self.pagina_jugar)
        self.pagina_opciones = QWidget()
        self.pagina_opciones.setObjectName(u"pagina_opciones")
        self.verticalLayout_3 = QVBoxLayout(self.pagina_opciones)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.pagina_opciones)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(210, 140, 171, 41))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 280, 71, 21))
        font1 = QFont()
        font1.setFamilies([u"BBH Sans Bogle"])
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.label_3.setFont(font1)
        self.Volumen = QSlider(self.frame_2)
        self.Volumen.setObjectName(u"Volumen")
        self.Volumen.setGeometry(QRect(220, 260, 160, 18))
        self.Volumen.setStyleSheet(u"/* Estilo para el QSlider (horizontal) */\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background-color: rgba(30, 30, 30, 0.7); /* Fondo oscuro como los botones */\n"
"    border: 1px solid #505050; /* Borde oscuro */\n"
"    height: 8px; /* Altura del canal */\n"
"    border-radius: 4px;\n"
"    \n"
"\n"
"}\n"
"\n"
"/* Estilo para la parte \"rellena\" del slider (lo que ya pas\u00f3) */\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #AAAAAA; /* Gris claro s\u00f3lido para el progreso */\n"
"    border: 1px solid #505050;\n"
"    height: 8px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* Estilo para el \"mango\" o \"perilla\" que se arrastra */\n"
"QSlider::handle:horizontal {\n"
"    background-color: #E0E0E0; /* Color principal (como el texto del label) */\n"
"    border: 1px solid #707070; /* Borde gris medio */\n"
"    width: 18px; /* Ancho del mango */\n"
"    height: 18px; /* Alto del mango */\n"
"    border-radius: 9px; /* Esto lo hace un c\u00edrculo perfecto */\n"
"    \n"
"    /* Marge"
                        "n negativo para que el mango se superponga al canal */\n"
"    /* (Alto del mango - Alto del canal) / 2 = (18 - 8) / 2 = 5 */\n"
"    margin: -5px 0; \n"
"}\n"
"\n"
"/* Efecto al pasar el mouse por encima del mango */\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: #FFFFFF; /* Blanco puro */\n"
"    border: 1px solid #AAAAAA; /* Borde m\u00e1s claro */\n"
"\n"
"}\n"
"\n"
"/* Efecto al presionar el mango */\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: #D0D0D0; /* Un gris un poco m\u00e1s oscuro */\n"
"    border: 1px solid #505050;\n"
"\n"
"}")
        self.Volumen.setOrientation(Qt.Orientation.Horizontal)
        self.btnvolver2 = QPushButton(self.frame_2)
        self.btnvolver2.setObjectName(u"btnvolver2")
        self.btnvolver2.setGeometry(QRect(250, 400, 100, 30))
        self.btnvolver2.setMinimumSize(QSize(100, 30))
        self.btnvolver2.setStyleSheet(u"/* Estilo para la ventana principal (el fondo) */\n"
"#ventanaPrincipal {\n"
"    background-image: url(tu_imagen_fondo_negro.jpg); /* Aseg\u00farate de usar la nueva imagen de fondo */\n"
"    background-position: center;\n"
"    background-repeat: no-repeat;\n"
"    background-size: cover;\n"
"}\n"
"\n"
"/* Estilo para TODOS los QPushButton */\n"
"QPushButton {\n"
"    width: 100px;\n"
"    height: 54px;\n"
"    font-size: 16px; /* Un poco m\u00e1s peque\u00f1o para un look m\u00e1s serio */\n"
"    font-weight: bold;\n"
"    color: #E0E0E0; /* Texto blanco gris\u00e1ceo para un look sutil */\n"
"    background-color: rgba(30, 30, 30, 0.7); /* Fondo gris oscuro semi-transparente */\n"
"    border: 1px solid #707070; /* Borde gris sutil */\n"
"    border-radius: 5px; /* Bordes ligeramente redondeados, m\u00e1s cuadrados */\n"
"    padding: 0px;\n"
"    \n"
"\n"
"}\n"
"\n"
"/* Efecto al pasar el mouse por encima */\n"
"QPushButton:hover {\n"
"    color: #FFFFFF; /* Texto blanco puro */\n"
"    background-color"
                        ": rgba(50, 50, 50, 0.8); /* Fondo un poco m\u00e1s claro y opaco */\n"
"    border: 1px solid #AAAAAA; /* Borde m\u00e1s claro */\n"
"\n"
"}\n"
"\n"
"/* Efecto al presionar el bot\u00f3n */\n"
"QPushButton:pressed {\n"
"    color: #DDDDDD;\n"
"    background-color: rgba(20, 20, 20, 0.9); /* M\u00e1s oscuro y opaco para simular \"hundimiento\" */\n"
"    border: 1px solid #505050;\n"
"\n"
"}")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-50, -80, 691, 661))
        self.label_5.setPixmap(QPixmap(u"menuopciones.jpg"))
        self.label_5.setScaledContents(True)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(200, 150, 171, 41))
        font2 = QFont()
        font2.setFamilies([u"BBH Sans Bogle"])
        font2.setPointSize(37)
        font2.setBold(False)
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: #000000; /* C\u00f3digo hexadecimal para negro */\n"
"}")
        self.label_5.raise_()
        self.label_3.raise_()
        self.Volumen.raise_()
        self.btnvolver2.raise_()
        self.label_7.raise_()
        self.label_2.raise_()

        self.verticalLayout_3.addWidget(self.frame_2)

        self.stackedwindow.addWidget(self.pagina_opciones)

        self.verticalLayout_2.addWidget(self.stackedwindow)

        Terreneitor.setCentralWidget(self.centralwidget)

        self.retranslateUi(Terreneitor)

        self.stackedwindow.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Terreneitor)
    # setupUi

    def retranslateUi(self, Terreneitor):
        Terreneitor.setWindowTitle(QCoreApplication.translate("Terreneitor", u"Terreneitor", None))
        self.btnjugar.setText(QCoreApplication.translate("Terreneitor", u"JUGAR", None))
        self.btnopciones.setText(QCoreApplication.translate("Terreneitor", u"OPCIONES", None))
        self.btnsalir.setText(QCoreApplication.translate("Terreneitor", u"SALIR", None))
        self.label_4.setText("")
        self.neonTextLabel.setText(QCoreApplication.translate("Terreneitor", u"Elige tu Modo de Juego", None))
        self.elegir_modo.setItemText(0, QCoreApplication.translate("Terreneitor", u"Modo Libre", None))
        self.elegir_modo.setItemText(1, QCoreApplication.translate("Terreneitor", u"Rutina 1", None))
        self.elegir_modo.setItemText(2, QCoreApplication.translate("Terreneitor", u"Rutina 2", None))
        self.elegir_modo.setItemText(3, QCoreApplication.translate("Terreneitor", u"Rutina 3", None))
        self.elegir_modo.setItemText(4, QCoreApplication.translate("Terreneitor", u"Rutina 4", None))

        self.btniniciar.setText(QCoreApplication.translate("Terreneitor", u"INICIAR", None))
        self.btnvolver1.setText(QCoreApplication.translate("Terreneitor", u"VOLVER", None))
        self.label_6.setText("")
        self.neonTextLabel_2.setText(QCoreApplication.translate("Terreneitor", u"Elige tu Modo de Juego", None))
        self.label_2.setText(QCoreApplication.translate("Terreneitor", u"Opciones", None))
        self.label_3.setText(QCoreApplication.translate("Terreneitor", u"Volumen", None))
        self.btnvolver2.setText(QCoreApplication.translate("Terreneitor", u"VOLVER", None))
        self.label_5.setText("")
        self.label_7.setText(QCoreApplication.translate("Terreneitor", u"Opciones", None))
    # retranslateUi

