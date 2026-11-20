# Security

Please report security issues privately to **iletisim@yoldas.io**, not in public issues. We reply within a few days.

## Verify a download

Every APK on the [Releases](https://github.com/yoldas-io/yoldas/releases) page and on yoldas.io is signed with the same certificate:

```
Signing certificate SHA-256: dd695000acb1d946491b04d2f5f69a019c57c0b6c45588562044fec255a1277e
```

Check it with `apksigner verify --print-certs yoldas-arac-<code>.apk`, and compare the file's SHA-256 with the value listed in the release.
Yoldaş's in-app updater checks the package name, version and this signature before installing an update.
