import os


class GoogleAuthConfig:
    CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
    CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
    DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
