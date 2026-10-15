# Protected native Wiki synchronization

This directory contains eight source-controlled native GitHub Wiki tutorials. A GitHub Actions workflow copies them into the separate native Wiki repository **without deleting user-created pages**.

**The hand-authored Home and SQL Performance pages remain untouched.** The script updates only approved tutorial filenames and an explicitly marked section of the existing Sidebar; everything outside that section stays in place.

- Source of truth: the detailed Markdown guides under the main repository's knowledge-base directory.
- Wiki summary pages: this wiki-pages directory (all links to canonical guides are absolute).
- Update mechanism: the scripts/sync_wiki.py Python script, invoked after offline tests in .github/workflows/wiki-sync.yml.
- Permissions: standard per-repository GitHub Actions token, limited to contents: write. No personal access token or API keys required.
- Safe failure: missing original pages, malformed Sidebar markers or unavailable Wiki Git access stop the publication before any push.

Validate safely with:

~~~bash
python -m unittest discover -s tests/wiki -v
~~~

Rerunning the script with unchanged files results in no changes. The source is readable and version-controlled, while the Wiki provides friendly navigation.

[Open the Wiki](https://github.com/Dicureck/Dicureck/wiki) · [Engineering Board](https://github.com/users/Dicureck/projects/1/views/2).
