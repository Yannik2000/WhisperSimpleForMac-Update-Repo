# Whisper Simple for Mac — Update Repo

This repository is the **release channel** for the in-app updater of
*Whisper Studio Simple*. The app checks `latest.json` here and, on request,
downloads the files listed in it.

It contains **no source code** — only the compiled application modules, the two
small launcher scripts, and the manifest.

| File | Purpose |
|---|---|
| `latest.json` | Manifest: version, SHA-256 checksums, download URLs |
| `whisper_studio_gui.cpython-312-darwin.so` | The app, compiled |
| `ws_pipeline.cpython-312-darwin.so` | The transcription pipeline, compiled |
| `WhisperStudio_mac.py` | Launcher (starts the compiled app) |
| `transcribe.py` | Launcher (starts the compiled pipeline) |

The compiled modules are built for **macOS 12.1+ on Apple Silicon** with
CPython 3.12 (`cp312-darwin-arm64`). The manifest states this, and the app
refuses any package that does not match its own runtime.

Every file is listed with a SHA-256 checksum. The app verifies each download
against it *before* replacing anything, keeps a backup of the running version,
and restores it automatically if the new one fails to load.

Development happens in a separate, private repository.
