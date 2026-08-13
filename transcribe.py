#!/usr/bin/env python3
"""Starter fuer die Transkriptions-Pipeline.

Die eigentliche Pipeline liegt in `ws_pipeline` — als Quelltext waehrend der
Entwicklung, als kompilierte `.so` in der Auslieferung. Diese Datei bleibt
bewusst Klartext und bewusst `transcribe.py`: Die GUI startet die Pipeline als
eigenen Prozess ueber genau diesen Pfad (`INSTALL_DIR / "transcribe.py"`),
und das soll sich nicht aendern.

Zwei Dinge sind hier wichtig:

1. `sys.path` wird auf den eigenen Ordner gesetzt, damit `ws_pipeline` daneben
   gefunden wird — egal aus welchem Arbeitsverzeichnis gestartet wird.
   Das passiert AUSSERHALB des __main__-Blocks, weil es auch im
   multiprocessing-Kindprozess gebraucht wird.

2. Der `__main__`-Block ist ZWINGEND. Die Pipeline startet fuer das
   Wort-Alignment einen Kindprozess per "spawn"; der reimportiert diese Datei
   als `__mp_main__`. Ohne den Block liefe die komplette Transkription im Kind
   ein zweites Mal.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

if __name__ == "__main__":
    from ws_pipeline import main
    main()
