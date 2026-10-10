# AFTERIMAGE

**Music × Visuals × Infinite Possibilities**

AFTERIMAGE turns any song into a living 3D sculpture and a world that grows from its mood. It runs entirely in your browser: no account, no backend, and your music never leaves your device.

<img width="1200" height="750" alt="screenshot" src="https://github.com/user-attachments/assets/c3cb8ea6-db41-43bd-8768-062d25dbfafc" />

## Features

- **Four sculptures:** Orb, Fractal, Ribbon and Void, shaped by custom GLSL shaders that react separately to bass, mids, highs and beats.
- **Five worlds:** City (every building is a frequency band), Desert, Forest, Ocean and Cosmos. Each one waves with the spectrum, and beats send shockwaves across it.
- **Song journeys:** open a file and AFTERIMAGE reads the whole song first, splits it into chapters and builds a world for each one.
- **Atmospheres:** Natural, Dark (drained colour, blood-red highlights) and Psychedelic (sweeping hues, kaleidoscope trails), picked from the sound or chosen by hand.
- **Mutation engine:** Mutate, Melt, Fracture, Warp, Grow, Unstable and New Universe. Every mutation is seeded and reproducible, with undo, redo and a visual lineage.
- **Three ways in:** listen to a browser tab (Spotify, YouTube Music, anything), open a local file, or use the microphone.
- **Record clips** of up to 30 seconds with sound, and **share links** that carry the visual settings only.
- **Guided tour** on first visit; press `?` to reopen it.

## Run it

Open `index.html` in a modern browser. That's it: no install and no build step. The 3D library loads from a CDN on first open.

Tab audio capture works in desktop Chrome and Edge. Other browsers can use a file or the microphone.

### Keys

| Key | Action |
|---|---|
| M | Mutate |
| N | New universe |
| E | Change world |
| A | Change atmosphere |
| 1–4 | Choose a form |
| R | Record a clip |
| H | Hide the interface |
| F | Fullscreen |
| Space | Play / pause |
| Ctrl+Z / Ctrl+Shift+Z | Undo / redo |
| ? | Guided tour |

## Hosting

`index.html` is a complete static site. Put it on any static host: GitHub Pages, Netlify, Cloudflare Pages, Vercel or itch.io (as an HTML game).

## Developing

The source lives in `src/` as plain ES modules:

| File | What it does |
|---|---|
| `core.js` | Config, bounds, seeded RNG, mutations, share codes, mood and atmosphere rules, journeys |
| `scan.js` | Whole-song analysis: FFT, features, chapters |
| `audio.js` | Sound sources and live feature extraction |
| `glsl.js` | Shared shader code (simplex noise) |
| `engine.js` | Three.js scene, sculpture shaders, afterimage trails, bloom, colour grading |
| `env.js` | The landscapes: City, Desert, Forest, Ocean, Cosmos |
| `app.js` | Interface, tour, recording, sharing, keyboard |
| `shell.html` | Markup and styles |

After editing, rebuild the single-file page:

```bash
python3 build.py              # writes dist/afterimage.html (copy it to index.html)
node --test tests/*.mjs       # unit tests, Node 18 or newer
```

## Contributing

Bug reports, new worlds, shaders and mutations are welcome. Please open an issue first for anything large. When you add a mutation, keep it deterministic (use the provided seeded RNG) and inside the parameter bounds in `core.js`, and add a test.

## License

MIT. See [LICENSE](LICENSE).
