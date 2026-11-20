# ytp: Future Roadmap & Architectural Evolution

ytp is a streamlined, user-friendly wrapper for `yt-dlp` and `aria2c` optimized for index-range playlist downloads and stream-friendly media pre-allocation. This roadmap outlines planned technical additions.

---

## 1. Incremental Synchronization & Watcher

- **Playlist Diffing & Auto-Sync Daemon**:
  - Store local playlist state indices and timestamps in SQLite.
  - Implement a `ytp --sync <alias>` command that checks the remote playlist and downloads only newly added items without re-querying existing metadata.
- **YouTube Music Track Auto-Tagging**:
  - Automatically query MusicBrainz / Spotify APIs to embed verified ID3v2 tags (album, artist, track number, high-res 1000x1000 album art) for audio extracts.

---

## 2. Network & Performance Enhancements

- **Dynamic Bandwidth Shaper**:
  - Add configurable rate-limiting flags (`--limit-rate 5M`) and scheduled off-peak download triggers.
- **Direct Stream Relay Pipe to MPV**:
  - Implement a `ytp --stream <url_or_alias>` mode that spawns `mpv` directly with FIFO buffer pipes for zero-disk playback.

---

## 3. Web UI Companion

- **Micro Web Interface**:
  - Provide a lightweight single-binary FastAPI / Go web dashboard to monitor active aria2 download queues, browse saved aliases, and trigger downloads from mobile phones on the local LAN.
