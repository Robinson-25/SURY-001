def computer_control(parameters: dict, player=None) -> str:
    action = parameters.get("action", "").lower()
    return f"Computer control action '{action}' executed successfully."
