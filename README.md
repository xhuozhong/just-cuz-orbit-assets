# Just Cuz immutable orbit assets

This repository serves the reviewed P43 orbit payloads used by the [Just Cuz comic reader](https://xhuozhong.github.io/just-cuz-episode-1/collection/). `dist/` contains six media payloads plus their manifest and Pages marker, totaling 13,192,064 bytes.

`dist/p043-q286/` is immutable: retain its exact names and bytes for cached readers. Add future media under a new versioned path. The companion frontend verifies each configured payload's full SHA-256 and actual HTTP 206 byte range before deploying.

## Publish

1. Set GitHub Pages to GitHub Actions.
2. Run `python tools/verify_assets.py` to verify the complete payload inventory.
3. Dispatch the `Publish reviewed orbit assets` workflow.
4. Verify the deployed full files and ranges, then deploy the matching frontend.

The manually dispatched workflow publishes exactly `dist/`. No third-party hosting service is required.
