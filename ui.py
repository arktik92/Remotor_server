from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QSystemTrayIcon, QMenu, QAction, QMessageBox
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
import qrcode
from io import BytesIO
from utils import get_local_ip

class RemoteMouseApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remote Mouse Server")
        self.setGeometry(100, 100, 400, 300)

        # Layout principal
        layout = QVBoxLayout()

        # Adresse IP du serveur
        server_ip = get_local_ip()
        server_label = QLabel(f"Server IP: {server_ip}:12345")
        server_label.setAlignment(Qt.AlignCenter)  # Centre le texte horizontalement
        layout.addWidget(server_label)

        # Générer le QR Code
        qr_code_image = self.generate_qr_code(server_ip)
        qr_label = QLabel()
        qr_label.setPixmap(qr_code_image)
        qr_label.setAlignment(Qt.AlignCenter)  # Centre l'image horizontalement
        layout.addWidget(qr_label, alignment=Qt.AlignCenter)

        # Appliquer le layout
        self.setLayout(layout)

        # Ajout de l'icône dans la barre système
        self.create_system_tray()

    def generate_qr_code(self, server_ip):
        server_url = f"http://{server_ip}:12345"
        qr = qrcode.make(server_url)

        img_io = BytesIO()
        qr.save(img_io, 'PNG')
        img_io.seek(0)

        pixmap = QPixmap()
        pixmap.loadFromData(img_io.read())
        return pixmap

    def create_system_tray(self):
        # Icône de la barre système
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setIcon(QIcon("icon.png"))  # Remplacez "icon.png" par une icône valide
        self.tray_icon.setToolTip("Remote Mouse Server")

        # Menu contextuel de la barre système
        tray_menu = QMenu()

        # Action pour afficher la fenêtre principale
        show_action = QAction("Afficher", self)
        show_action.triggered.connect(self.show)
        tray_menu.addAction(show_action)

        # Action pour quitter l'application
        quit_action = QAction("Quitter", self)
        quit_action.triggered.connect(self.quit_app)
        tray_menu.addAction(quit_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    def closeEvent(self, event):
        # Minimise l'application dans la barre système au lieu de la fermer
        if self.tray_icon.isVisible():
            QMessageBox.information(self, "Minimisé", "L'application reste active dans la barre système.")
            self.hide()
            event.ignore()

    def quit_app(self):
        # Quitte proprement l'application
        QApplication.quit()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = RemoteMouseApp()
    window.show()

    sys.exit(app.exec_())
