# FantasyScout – GitHub APK Build

## Upload

Den **Inhalt dieses Projektordners** in ein neues GitHub-Repository hochladen (nicht einen zusätzlichen FantasyScout-Unterordner erzeugen).

Die relevante Struktur muss so aussehen:

```text
.github/workflows/android-build.yml
app/
backend/
build.gradle.kts
gradle.properties
settings.gradle.kts
...
```

## Automatischer Build

Nach einem Push auf `main` oder `master` startet GitHub Actions automatisch den Android-Build.

Alternativ in GitHub:

**Actions → FantasyScout Android APK → Run workflow**

Der Workflow installiert:

- JDK 21
- Gradle 9.4.0
- Android SDK Platform 36
- Android Build Tools 36.0.0

Danach wird `:app:assembleDebug` ausgeführt.

## APK herunterladen

Nach erfolgreichem Lauf:

**GitHub → Actions → FantasyScout Android APK → erfolgreicher Lauf → Artifacts → FantasyScout-debug-apk**

Darin liegt:

`app-debug.apk`

## Wichtig

Für den Debug-Build ist kein eigener Signatur-Key erforderlich. Die Debug-APK wird automatisch mit dem Android-Debug-Key signiert und kann auf einem Android-Gerät installiert werden.

Für eine spätere Veröffentlichung im Play Store sollte ein eigener Release-Key bzw. GitHub Secret/Environment verwendet werden. Dieser Key gehört **nicht** ins Repository.
