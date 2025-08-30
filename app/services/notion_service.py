def get_recent_tasks(limit: int = 5):
    return [{"title": f"Task {i}", "status": "Todo"} for i in range(limit)]
