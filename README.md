# Whisper Simple for Mac — Update Repo

This repository is the **release channel** for the in-app updater of
*Whisper Studio Simple*. The app checks `latest.json` here and, on request,
downloads the files listed in it.

It contains **no source code** — only the compiled application modules, the two
small launcher scripts, and the manifest.

| File | Purpose |
|---|---|
| `latest.json` | Manifest: version, SHA-256 checksums, download URLs |
| `<version>/whisper_studio_gui.cpython-312-darwin.so` | The app, compiled |
| `<version>/ws_pipeline.cpython-312-darwin.so` | The transcription pipeline, compiled |
| `<version>/WhisperStudio_mac.py` | Launcher (starts the compiled app) |
| `<version>/transcribe.py` | Launcher (starts the compiled pipeline) |

Since `studio-v39-20261008`, every release lives in its own folder named after
its version, and `latest.json` points into that folder. GitHub caches each file
for about five minutes; with fixed file names, a freshly published manifest
could be served together with the *previous* release's modules, so their
checksums would not match. A new folder means new URLs that cannot be stale.
The files in the repository root belong to older releases and stay in place,
because a manifest still cached from before points to them.

The compiled modules are built for **macOS 12.1+ on Apple Silicon** with
CPython 3.12 (`cp312-darwin-arm64`). The manifest states this, and the app
refuses any package that does not match its own runtime.

Every file is listed with a SHA-256 checksum. The app verifies each download
against it *before* replacing anything, keeps a backup of the running version,
and restores it automatically if the new one fails to load.

Development happens in a separate, private repository.
