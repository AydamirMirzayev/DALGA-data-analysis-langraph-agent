from typing import Optional, Dict, Any

class ConversationMemory:
    """Keep latest interaction: user_text, response"""

    def __init__(self):
        self.last_interaction: Optional[Dict[str, Any]] = None

    def add_interaction(self, user_input: str, final_answer: str):
        self.last_interaction = {
            "user_input" : user_input,
            "final_answer" : final_answer
        }

    def get_memory(self) -> Dict[str, Any]:
        """For passing to the garph"""
        if self.last_interaction is None:
            history =  {"has_previous" : False}
        else:
            history = {"has_revious": True, 
                       "previous_question": self.last_interaction["user_input"],
                       "previous_answer" : self.last_interaction["final_answer"]
                }

        return history

    def clear(self):
        "To reset the history"
        self.last_interaction = None



