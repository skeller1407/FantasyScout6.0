# FantasyScout v28

## Build-Fixes
- Gradle 9.6.0 bleibt aktiv; damit ist die vorherige Gradle-Kompatibilitätsmeldung behoben.
- `LiveData.kt`: Cache-Serialisierung vollständig strukturiert und Syntaxfehler beseitigt.
- `MainActivity.kt`: Cache-Zugriff, horizontales Scrollen, Material-3-Opt-in und Typfehler korrigiert.
- Dashboard-Statkarten verwenden nun gültige Layout-Gewichte über umschließende `Box`-Elemente.
- Transferplaner konvertiert das berechnete Restbudget korrekt für die Marktwertanzeige.

## Erwarteter nächster Schritt
GitHub Actions soll mit `:app:assembleDebug` prüfen, ob die Kotlin-Kompilierung nun vollständig durchläuft.
