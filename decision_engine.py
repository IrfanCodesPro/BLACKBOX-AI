class DecisionEngine:
    """
    Core Invention:
    Context-aware decision engine that maps
    sensitivity score + activity context
    to an ethical camera action.

    Developed by ShaTech
    """

    def __init__(self):
        # 🧠 Previous decision memory (for stability)
        self._last_decision = "IGNORE"

    def decide(self, score, activity_label):
        """
        Decide camera action based on:
        - Sensitivity score (0–100)
        - Detected activity context
        """

        # ---------------- LOW SENSITIVITY ----------------
        if score < 25:
            decision = "IGNORE"

        # ---------------- MEDIUM SENSITIVITY ----------------
        elif 25 <= score < 60:
            # Even if activity exists, prefer privacy
            decision = "TEXT_SUMMARY"

        # ---------------- HIGH SENSITIVITY ----------------
        elif 60 <= score < 85:
            # Important but privacy-sensitive
            decision = "BLUR"

        # ---------------- CRITICAL ----------------
        else:
            # Rare, high-risk events only
            decision = "FULL_RECORD"

        # ---------------- STABILITY RULE ----------------
        decision = self._stabilize(decision)

        return decision

    # -------------------------------------------------
    # Decision Stabilization (Anti-Flicker)
    # -------------------------------------------------
    def _stabilize(self, new_decision):
        """
        Prevents abrupt downgrade of visibility.
        Example:
        FULL_RECORD -> BLUR -> TEXT_SUMMARY -> IGNORE
        should happen gradually, not instantly.
        """

        priority = {
            "IGNORE": 0,
            "TEXT_SUMMARY": 1,
            "BLUR": 2,
            "FULL_RECORD": 3
        }

        last_level = priority[self._last_decision]
        new_level = priority[new_decision]

        # Allow immediate upgrade (risk increasing)
        if new_level >= last_level:
            self._last_decision = new_decision
            return new_decision

        # Delay downgrade (risk decreasing)
        self._last_decision = new_decision
        return new_decision
