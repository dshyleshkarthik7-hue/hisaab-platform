# Full source archive

The complete Hisaab v3.1 tree (including engine, Mitra, web UI, Java gateway, and fonts) is packaged as `hisaab-v3.1-complete-platform.zip` from the build session.

To finish populating this repository from the zip:

```bash
git clone https://github.com/dshyleshkarthik7-hue/hisaab-platform.git
cd hisaab-platform
unzip -o /path/to/hisaab-v3.1-complete-platform.zip
cp -r hisaab/* .
git add -A
git commit -m "Hisaab v3.1 complete platform source"
git push
```

Already on this branch: docs, Dockerfile, run.sh, llm_provider, tests skeleton, render.yaml.
