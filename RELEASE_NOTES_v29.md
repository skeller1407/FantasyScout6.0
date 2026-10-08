# FantasyScout v29

## Build-Fix
- Vollständiges Android-Projekt mit `app/` im Repository-Root.
- GitHub Actions prüft vor dem Gradle-Build ausdrücklich, dass `app/`, `app/build.gradle.kts` und das Haupt-Manifest vorhanden sind.
- Gradle 9.6.0 bleibt aktiv.

## Wichtig
Das ZIP muss mit seinem Inhalt direkt in das Repository-Root übernommen werden. Es darf nicht so hochgeladen werden, dass nur einzelne Root-Dateien ohne den Ordner `app/` übernommen werden.
