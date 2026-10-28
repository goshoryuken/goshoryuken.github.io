# ePortfolio

Plain HTML/CSS, no build step. Open `index.html` in a browser to preview.

## Fill in

Everything you still need to write is wrapped in `<span class="todo">…</span>` and shows up
highlighted yellow on the page. Find them all with:

```sh
grep -rn 'class="todo"' --include=*.html .
```

Still to do:

- `assets/img/portrait.jpg`: add a photo, then point the `<img>` in `index.html` and `about.html` at it.
- Discovery Project: fill in `projects/discovery.html` and replace its placeholder images with your own photos.
- Resume: save a redacted PDF (no phone, no personal email) as `assets/resume.pdf`; `resume.html` already embeds it.

## Add a project

1. Copy `projects/_template.html` to `projects/<name>.html` and fill it in.
2. Add a `<li>` for it at the top of the list in `projects.html` (and `index.html` if it's a highlight).

## Publishing

GitHub Pages serves `main` at https://goshoryuken.github.io/ (Settings → Pages → Deploy from a branch,
`main`, `/ (root)`). Pushes go live in a minute or two.
