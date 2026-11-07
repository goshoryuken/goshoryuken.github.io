# Project notes

A static HTML/CSS portfolio. No package install or build step.

## Develop

From the repository root:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

`index.html` contains the brief introduction and selected projects. `projects.html`
is the featured collection; full technical write-ups are under `projects/`.
Styling uses system fonts and supports light and dark preferences.

To add a project, copy `projects/_template.html`, replace its example text, and
link the finished write-up from `projects.html`. Use actual project images and
include the conditions behind any performance measurements.

The old about, résumé, and goals URLs point visitors to the project collection.
Personal biography, contact information, and academic records are intentionally
omitted. Check page metadata and image contents as well as visible text before
adding new material.

## Publish

GitHub Pages serves `main` from the repository root. Local edits are not live
until committed and pushed through the usual publishing workflow.
