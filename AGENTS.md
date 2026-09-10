# Project instructions

## README updates for every commit and push

The user requires the root `README.md` to be updated with the project status and file organization every time work is committed and pushed.

- Before every commit, update the current project-status and file-organization sections of `README.md` and include that README update in the same commit. If the layout did not change, state that it was reviewed and remains current.
- Before every push, verify that each new commit prepared for the task contains its required README update and that the README describes the state being pushed. A commit already prepared this way does not require an extra commit just to push it.
- Date repository/documentation updates separately from the scientific manuscript revision. Report completed work, validation actually performed, and remaining research limitations accurately.
- Use the existing uppercase filename `README.md`; do not create a second `readme.md`.
- This maintenance rule does not independently authorize a commit or push when the user's task does not request one.

## Artifact integrity

- Preserve dated research snapshots, historical manifests, and existing simulation results unless the task explicitly requires changing them.
- When changing a file covered by `MANIFEST.sha256`, refresh its hash. Add newly delivered project files while preserving existing manifest entries. Do not hash the manifest into itself or include `.git/` and local caches.
- Run `python audit/revision_2026_09_09/validate_revision.py` after manifest updates. Its `--refresh-manifest` option reconstructs the September 9 inventory and can omit later additions, so do not use it to replace an expanded inventory without preserving those additions.
- For downloaded references, retain the source URL, version information, access date, and SHA-256 hash in `references/sources.json`.
