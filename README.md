# Project notes

A static HTML/CSS portfolio. No package install is needed.

## Develop

From the repository root:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

`index.html` is a welcome page with an introduction, section buttons, and social
links. `projects.html` is the dedicated project collection; full technical write-ups are under `projects/`.
Styling uses system fonts and supports light and dark preferences.

To add a project, copy `projects/_template.html`, replace its example text, and
link the finished write-up from `projects.html`. Use actual project images and
include the conditions behind any performance measurements.

The About page groups education, threads, coursework, skills, and experience;
project showcases stay on the Projects page. Résumé and Career Goals complete
the other portfolio sections. `assets/resume.pdf` is a separate public résumé; never
replace it with an unredacted upload. LinkedIn and GitHub are the only personal
contact links. Phone, email, address, GPA, and graduation timeline are omitted.
Check PDF text, link annotations, metadata, and image contents before publishing.

The Discovery Project feature remains deferred for the later showcase, as
permitted by the published-portfolio assignment. Do not invent its results.

## Publish

After editing `assets/site.css`, run:

```sh
python3 scripts/version_styles.py
```

This writes a stylesheet with a content hash in its filename and updates every
HTML page to reference it. Commit the generated CSS and HTML changes together.
Edit `assets/site.css`, not the generated copy. Keep earlier versioned files so
cached pages can still load the stylesheet they were published with. Versioned
URLs prevent an old cached stylesheet from breaking a newly deployed layout.


GitHub Pages serves `main` from the repository root. Local edits are not live
until committed and pushed through the usual publishing workflow.
