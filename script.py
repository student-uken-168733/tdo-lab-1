import os

message = os.getenv("MESSAGE", "Brak zmiennej środowiskowej!")
print("Odebrana wiadomość:", message)
