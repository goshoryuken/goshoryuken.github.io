# Project notes

A static HTML/CSS portfolio. No package install is needed.

## Develop

From the repository root:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

`index.html` is a welcome page with an introduction, section buttons, and social
links. `projects.html` contains all project write-ups and images in one scrolling page.
The old individual project URLs redirect to the corresponding section.
Every page shares the homepage palette, `.site-shell` frame, `.welcome-header`,
and `.site-footer`. Styling uses system fonts and supports light and dark
preferences. Keep shared colors in the root CSS variables so new pages match.

To add a project, copy the article fragment in `projects/_template.html` into
`projects.html`, replace its example text, and add its section ID to the jump links. Use actual project images and
include the conditions behind any performance measurements.

The About page groups education, threads, coursework, skills, and experience;
project showcases stay on the Projects page. Résumé and Career Goals complete
the other portfolio sections. `assets/resume.pdf` is a separate public résumé; never
replace it with an unredacted upload. LinkedIn and GitHub are the only personal
contact links. Phone, email, address, GPA, and graduation timeline are omitted.
Check PDF text, link annotations, metadata, and image contents before publishing.

The Discovery Project feature remains deferred for the later showcase, as
permitted by the published-portfolio assignment. Do not invent its results.

## Profile photo

The homepage reserves a circular photo spot beside the introduction (above it on
mobile). To add a portrait, put the photo in `assets/img/`, replace the contents
of `.portrait-slot` in `index.html` with an image, and remove the placeholder's
`role` and `aria-label` attributes:

```html
<div class="portrait-slot">
  <img src="assets/img/profile.jpg" alt="Ryu" width="112" height="112">
</div>
```

Use the actual image filename; the frame crops it to fit without stretching.

## Publish

After editing page content or `assets/site.css`, run:

```sh
python3 scripts/version_styles.py
```

This writes a stylesheet with a content hash in its filename and updates every
HTML page to reference it. It also versions internal page links, so navigation
does not reuse HTML cached from an older design or content update. Page versions
are derived from both the HTML content and CSS. Commit the generated CSS and
HTML changes together.
Edit `assets/site.css`, not the generated copy. Keep earlier versioned files so
cached pages can still load the stylesheet they were published with. Versioned
URLs prevent an old cached stylesheet from breaking a newly deployed layout.


GitHub Pages serves `main` from the repository root. Local edits are not live
until committed and pushed through the usual publishing workflow.
