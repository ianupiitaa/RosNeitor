# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana_juego.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QStackedWidget,
    QWidget)
import recursos_imagenes_rc

class Ui_Terreneitor(object):
    def setupUi(self, Terreneitor):
        if not Terreneitor.objectName():
            Terreneitor.setObjectName(u"Terreneitor")
        Terreneitor.resize(400, 300)
        Terreneitor.setMinimumSize(QSize(400, 300))
        Terreneitor.setMaximumSize(QSize(400, 300))
        icon = QIcon()
        icon.addFile(u"icono.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Terreneitor.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Terreneitor)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Terreneitor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.horizontalLayout_2 = QHBoxLayout(self.page_3)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.page_3)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.rutina_juego = QLabel(self.frame)
        self.rutina_juego.setObjectName(u"rutina_juego")
        self.rutina_juego.setGeometry(QRect(30, 20, 331, 31))
        font = QFont()
        font.setFamilies([u"Stencil"])
        font.setPointSize(14)
        self.rutina_juego.setFont(font)
        self.btnadelante = QPushButton(self.frame)
        self.btnadelante.setObjectName(u"btnadelante")
        self.btnadelante.setGeometry(QRect(170, 90, 71, 61))
        self.btnadelante.setStyleSheet(u"QPushButton#btnadelante {\n"
"    border-image: url(:/Flechas/arriba.jpg) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent; \n"
"    border: none; \n"
"	border-radius: 30px;\n"
"}\n"
"QPushButton#btnadelante:pressed {\n"
"    border-image: url(:/Flechas/arriba.jpg) 0 0 0 0 stretch stretch; /\n"
"}")
        self.btnadelante.setIconSize(QSize(64, 64))
        self.btnderecha = QPushButton(self.frame)
        self.btnderecha.setObjectName(u"btnderecha")
        self.btnderecha.setGeometry(QRect(270, 160, 71, 61))
        self.btnderecha.setStyleSheet(u"QPushButton#btnderecha {\n"
"    border-image: url(:/Flechas/derecha.jpg) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent; \n"
"    border: none; \n"
"	border-radius: 30px;\n"
"}\n"
"QPushButton#btnderecha:pressed {\n"
"    border-image: url(:/Flechas/derecha.jpg) 0 0 0 0 stretch stretch; /\n"
"}")
        self.btnderecha.setIconSize(QSize(64, 64))
        self.btnizquierda = QPushButton(self.frame)
        self.btnizquierda.setObjectName(u"btnizquierda")
        self.btnizquierda.setGeometry(QRect(70, 160, 71, 61))
        self.btnizquierda.setStyleSheet(u"QPushButton#btnizquierda {\n"
"    border-image: url(:/Flechas/izquierda.jpg) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent; \n"
"    border: none; \n"
"	border-radius: 30px;\n"
"}\n"
"QPushButton#btnizquierda:pressed {\n"
"    border-image: url(:/Flechas/izquierda.jpg) 0 0 0 0 stretch stretch; /\n"
"}")
        self.btnizquierda.setIconSize(QSize(64, 64))
        self.btnatras = QPushButton(self.frame)
        self.btnatras.setObjectName(u"btnatras")
        self.btnatras.setGeometry(QRect(170, 230, 71, 61))
        self.btnatras.setStyleSheet(u"QPushButton#btnatras {\n"
"    border-image: url(:/Flechas/abajo.jpg) 0 0 0 0 stretch stretch;\n"
"    background-color: transparent; \n"
"    border: none; \n"
"	border-radius: 30px;\n"
"}\n"
"QPushButton#btnatras:pressed {\n"
"    border-image: url(:/Flechas/abajo.jpg) 0 0 0 0 stretch stretch; /\n"
"}")
        self.btnatras.setIconSize(QSize(64, 64))
        self.pausarRutina = QPushButton(self.frame)
        self.pausarRutina.setObjectName(u"pausarRutina")
        self.pausarRutina.setGeometry(QRect(60, 150, 91, 51))
        self.pausarRutina.setStyleSheet(u"/* Estilo para la ventana principal (el fondo) */\n"
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
        self.finalizarRutina = QPushButton(self.frame)
        self.finalizarRutina.setObjectName(u"finalizarRutina")
        self.finalizarRutina.setGeometry(QRect(260, 150, 91, 51))
        self.finalizarRutina.setStyleSheet(u"/* Estilo para la ventana principal (el fondo) */\n"
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
        self.AjustarVelocidad = QSlider(self.frame)
        self.AjustarVelocidad.setObjectName(u"AjustarVelocidad")
        self.AjustarVelocidad.setGeometry(QRect(20, 90, 18, 160))
        self.AjustarVelocidad.setStyleSheet(u"")
        self.AjustarVelocidad.setOrientation(Qt.Orientation.Vertical)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 60, 161, 20))
        font1 = QFont()
        font1.setFamilies([u"BBH Sans Bogle"])
        font1.setPointSize(16)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(-260, -70, 711, 491))
        self.label_4.setPixmap(QPixmap(u"fondoventana.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.raise_()
        self.rutina_juego.raise_()
        self.btnderecha.raise_()
        self.btnizquierda.raise_()
        self.btnatras.raise_()
        self.pausarRutina.raise_()
        self.AjustarVelocidad.raise_()
        self.label_3.raise_()
        self.finalizarRutina.raise_()
        self.btnadelante.raise_()

        self.horizontalLayout_2.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.horizontalLayout_3 = QHBoxLayout(self.page_4)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.page_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 30, 131, 61))
        font2 = QFont()
        font2.setFamilies([u"BBH Sans Bogle"])
        font2.setPointSize(48)
        self.label.setFont(font2)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 105, 91, 21))
        font3 = QFont()
        font3.setFamilies([u"BBH Sans Bogle"])
        font3.setPointSize(20)
        self.label_2.setFont(font3)
        self.Volumen = QSlider(self.frame_2)
        self.Volumen.setObjectName(u"Volumen")
        self.Volumen.setGeometry(QRect(120, 140, 160, 18))
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
        self.btnvolverjuego = QPushButton(self.frame_2)
        self.btnvolverjuego.setObjectName(u"btnvolverjuego")
        self.btnvolverjuego.setGeometry(QRect(140, 190, 131, 31))
        self.btnvolverjuego.setStyleSheet(u"/* Estilo para la ventana principal (el fondo) */\n"
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
        self.btnvolvermenu = QPushButton(self.frame_2)
        self.btnvolvermenu.setObjectName(u"btnvolvermenu")
        self.btnvolvermenu.setGeometry(QRect(140, 230, 131, 31))
        self.btnvolvermenu.setStyleSheet(u"/* Estilo para la ventana principal (el fondo) */\n"
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
" \n"
"}")
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(-190, -100, 601, 481))
        self.label_5.setPixmap(QPixmap(u"fondoventana.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.Volumen.raise_()
        self.btnvolverjuego.raise_()
        self.btnvolvermenu.raise_()

        self.horizontalLayout_3.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.page_4)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Terreneitor)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Terreneitor)
    # setupUi

    def retranslateUi(self, Terreneitor):
        Terreneitor.setWindowTitle(QCoreApplication.translate("Terreneitor", u"Terreneitor", None))
        self.rutina_juego.setText("")
        self.btnadelante.setText("")
#if QT_CONFIG(shortcut)
        self.btnadelante.setShortcut(QCoreApplication.translate("Terreneitor", u"W", None))
#endif // QT_CONFIG(shortcut)
        self.btnderecha.setText("")
#if QT_CONFIG(shortcut)
        self.btnderecha.setShortcut(QCoreApplication.translate("Terreneitor", u"D", None))
#endif // QT_CONFIG(shortcut)
        self.btnizquierda.setText("")
#if QT_CONFIG(shortcut)
        self.btnizquierda.setShortcut(QCoreApplication.translate("Terreneitor", u"A", None))
#endif // QT_CONFIG(shortcut)
        self.btnatras.setText("")
#if QT_CONFIG(shortcut)
        self.btnatras.setShortcut(QCoreApplication.translate("Terreneitor", u"S", None))
#endif // QT_CONFIG(shortcut)
        self.pausarRutina.setText(QCoreApplication.translate("Terreneitor", u"Pausar", None))
        self.finalizarRutina.setText(QCoreApplication.translate("Terreneitor", u"Finalizar", None))
        self.label_3.setText(QCoreApplication.translate("Terreneitor", u"Esc para abrir menu", None))
        self.label_4.setText("")
        self.label.setText(QCoreApplication.translate("Terreneitor", u"Pausa", None))
        self.label_2.setText(QCoreApplication.translate("Terreneitor", u"Volumen", None))
        self.btnvolverjuego.setText(QCoreApplication.translate("Terreneitor", u"Volver al Juego", None))
        self.btnvolvermenu.setText(QCoreApplication.translate("Terreneitor", u"Volver al Menu", None))
        self.label_5.setText("")
    # retranslateUi

