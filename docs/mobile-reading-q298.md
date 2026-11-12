# Mobile reading preview package

`dist/reading/q298` contains 85 deterministic reading previews and their source
manifest. Each preview resizes the already published, original JPEG composition
to 1000 pixels wide using LANCZOS, then encodes WebP at quality 90/method 6.
There is no generated or redrawn artwork. The manifest binds each result to the
canonical source SHA-256, native dimensions, output dimensions, byte size and
output SHA-256.

Preview images total 11,083,956 bytes; their canonical JPEGs total 22,418,655
bytes. They are a temporary mobile reading layer. The reader still uses the
original images for final reading, translated lettering protection and orbit
composition. Review included a six-page contact sheet and enlarged source/text
comparisons for pages 43 and 78.

All six existing orbit payloads and the legacy asset manifest remain byte exact.
The complete static asset repository remains 94 files / 24,314,823 bytes. Its
existing workflow and publication settings are unchanged.
