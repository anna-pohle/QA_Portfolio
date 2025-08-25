def count_word_matches(text, target):
    """
    Zählt, wie oft ein Zielwort als eigenständiges Wort im Text vorkommt.
    Die Übereinstimmung erfolgt ohne Berücksichtigung der Groß-/Kleinschreibung,
    und Wörter sind durch Leerzeichen getrennt.

    Args:
        text (str): Eingabetext, in dem gesucht wird.
        target (str): Das gesuchte Wort.

    Returns:
        int: Anzahl der Vorkommen des Zielwortes als eigenständiges Wort.
    """
    if not text or not target:
        return 0

    # Text in Wörter aufteilen und für case-insensitive Vergleich in Kleinbuchstaben umwandeln
    words = text.lower().split()
    target = target.lower()

    # Eigenständige Vorkommen des Zielwortes zählen
    return words.count(target)