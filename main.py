import sys
from PyQt5.QtWidgets import QApplication
from ui import RemoteMouseApp
from server import start_server

if __name__ == "__main__":
    # Démarrer le serveur Flask en arrière-plan
    start_server()

    # Lancer l'application graphique
    app = QApplication(sys.argv)
    window = RemoteMouseApp()
    window.show()
    sys.exit(app.exec())
