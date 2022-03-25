# PolybarDiscord
Simple polybar module for discord

### Usage
When launched, script will spawns a window with the options to:
- start / show Discord
- Shutdown Discord
- Inject Betterdiscord (betterdiscordctl requires to be installed)
- Remove the injection (same thing here you not dumb)

To use with polybar, use:
```python
[module/discord]
type = custom/script
exec = "Whatever icon / text you want"
tail = true
click-left = python3 /path/to/script
```

With specifying the icon / text and the path to the script.
Have a great day.
