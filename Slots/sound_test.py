import winsound
from pathlib import Path

#winsound.Beep(1000, 500)

file = Path(__file__).parent / "floraphonic-playful-casino-slot-machine-jackpot-3-183921.wav"


winsound.PlaySound(str(file), winsound.SND_FILENAME)
print("working")