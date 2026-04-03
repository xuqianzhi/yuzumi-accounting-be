import os
import tempfile
from dotenv import load_dotenv

load_dotenv()

class Settings:
    TELLER_TOKEN = os.getenv("TELLER_TOKEN")
    
    @property
    def mtls_tuple(self):
        # We create temporary files for the certs since Vercel's FS is ephemeral
        cert_content = os.getenv("TELLER_CERT_CONTENT")
        key_content = os.getenv("TELLER_KEY_CONTENT")
        
        # Write to /tmp (the only writable space in Vercel functions)
        cert_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pem")
        key_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pem")
        
        cert_file.write(cert_content.encode())
        key_file.write(key_content.encode())
        
        cert_file.close()
        key_file.close()
        
        return (cert_file.name, key_file.name)

settings = Settings()