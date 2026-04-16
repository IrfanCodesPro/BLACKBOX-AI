class SensitivityScorer:
    """
    Calculates a scalar sensitivity score (0–100)
    representing ethical risk or importance of a scene.

    Developed by ShaTech
    """

    def calculate(self, activity_label, feature_dict, avg_motion):
        """
        Inputs:
        - activity_label : output from ML model
        - feature_dict   : contextual features (dict)
        - avg_motion     : motion trend over time
        """

        motion = feature_dict.get("motion", 0)
        contours = feature_dict.get("contours", 0)
        brightness = feature_dict.get("brightness", 128)
        entropy = feature_dict.get("entropy", 0)

        score = 0

        # -------------------------------------------------
        # 1️⃣ Activity Base Score (ML-driven)
        # -------------------------------------------------
        if activity_label == "STATIC":
            score = 10
        elif activity_label == "NORMAL_ACTIVITY":
            score = 45
        elif activity_label == "CHAOTIC":
            score = 80
        else:
            score = 30  # Unknown / fallback

        # -------------------------------------------------
        # 2️⃣ Motion Trend Modifier (Context Awareness)
        # -------------------------------------------------
        if avg_motion > 20:
            score += 20
        elif avg_motion > 8:
            score += 10

        # -------------------------------------------------
        # 3️⃣ Scene Complexity (Entropy & Contours)
        # -------------------------------------------------
        score += min(entropy * 2, 20)
        score += min(contours * 2, 15)

        # -------------------------------------------------
        # 4️⃣ Privacy Heuristic (Low Light)
        # -------------------------------------------------
        if brightness < 60:
            score += 15  # Dark environment → privacy-sensitive

        # -------------------------------------------------
        # Clamp score to 0–100
        # -------------------------------------------------
        return max(0, min(int(score), 100))
