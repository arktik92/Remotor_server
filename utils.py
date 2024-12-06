import socket

def get_local_ip():
    try:
        # Crée une socket pour détecter l'adresse IP locale
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            # Une adresse arbitraire est utilisée pour vérifier l'IP locale
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
        return local_ip
    except Exception:
        return "127.0.0.1"
