#!/usr/bin/env python3
"""Starter der App — wird vom Installer als `WhisperStudio_mac.py` abgelegt.

Bleibt bewusst Klartext: Er enthaelt keine Produktlogik, nur den Aufruf.
Die App selbst liegt daneben als kompiliertes Modul
`whisper_studio_gui.cpython-312-darwin.so`.

`sys.path` zeigt auf den eigenen Ordner, damit das Modul gefunden wird,
unabhaengig vom Arbeitsverzeichnis des Starts (Doppelklick, Terminal,
App-Bundle).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from whisper_studio_gui import main
except ImportError as e:
    # Haeufigster Fall: Die kompilierte Datei passt nicht zur Python-Version
    # der Umgebung (sie ist an cp312/arm64 gebunden). Verstaendlich melden
    # statt wortlos abzustuerzen.
    msg = ("Whisper Studio Simple konnte nicht geladen werden.\n\n"
           f"{e}\n\n"
           "Meist hilft es, den Installer aus dem DMG erneut auszufuehren.")
    try:
        import subprocess
        subprocess.run(["osascript", "-e",
                        'display dialog "{}" with title "Whisper Studio Simple" '
                        'buttons {{"OK"}} default button "OK" with icon stop'
                        .format(msg.replace("\\", "\\\\").replace('"', '\\"')
                                   .replace("\n", "\\n"))],
                       capture_output=True, timeout=60)
    except Exception:
        print(msg, file=sys.stderr)
    sys.exit(1)

if __name__ == "__main__":
    main()
