def generate_recommendations(
    savings_ratio,
    debt_ratio,
    emergency_buffer_months,
    skill_upgrade_gap,
    work_hours_level
):

    suggestions = []

    if debt_ratio > 0.5:
        suggestions.append("⚠ Reduce debt burden and avoid new loans")

    if savings_ratio < 0.2:
        suggestions.append("💰 Increase monthly savings to build safety buffer")

    if emergency_buffer_months < 3:
        suggestions.append("📉 Build emergency fund for at least 3 months survival")

    if skill_upgrade_gap > 3:
        suggestions.append("📚 Upgrade professional skills to improve job security")

    if work_hours_level > 10:
        suggestions.append("⏳ Maintain work-life balance to avoid burnout risk")

    if len(suggestions) == 0:
        suggestions.append("✅ Financial behaviour appears stable. Continue disciplined planning")

    return suggestions