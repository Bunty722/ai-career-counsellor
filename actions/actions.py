import json
import logging
import os
from typing import Any, Text, Dict, List

import nltk
from nltk.tokenize import word_tokenize
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Set up logging for better debugging
logger = logging.getLogger(__name__)

# --- 1. Dynamic NLTK Path (Portable) ---
# This builds the path to your nltk_data folder relative to this file.
# It means you can move your project folder anywhere, and it will still work.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
nltk_data_path = os.path.join(project_root, "nltk_data")
nltk.data.path.append(nltk_data_path)

# --- 2. Centralized Keywords and Responses (Easier to Update) ---
# Instead of a long if/elif chain, we store all keywords and responses here.
# To add a new career, you just add an entry to this dictionary.
CAREER_DATA = {
    "tech": {
        "keywords": ["tech", "technology", "software", "programming", "aiml", "machine"],
        "response": "Tech is a great field! You could be a Software Developer, Data Scientist, or a Cybersecurity Analyst. These roles involve programming, data analysis, and protecting systems."
    },
    "arts": {
        "keywords": ["art", "arts", "creative", "design"],
        "response": "A career in the arts is very rewarding. You could explore being a Graphic Designer, a UI/UX Designer, or a Content Creator. These roles focus on creativity and visual communication."
    },
    "commerce": {
        "keywords": ["commerce", "business", "finance", "accounts"],
        "response": "Commerce offers many stable careers. You might enjoy being a Chartered Accountant, an Investment Banker, or a Marketing Manager. These roles involve finance, business strategy, and management."
    }
}


class ActionProvideRecommendation(Action):

    def name(self) -> Text:
        """A unique name for the action."""
        return "action_provide_recommendation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        Executes the action. It tokenizes the user's message, checks for keywords
        from the CAREER_DATA dictionary, and provides a recommendation.
        """
        
        message = tracker.latest_message.get('text', '').lower()
        tokens = word_tokenize(message)
        
        response = "I'm not sure which field you're asking about. Can you be more specific? For example, you can ask about tech, arts, or commerce."
        
        # --- 3. Clean and Scalable Logic ---
        # This loop is much cleaner and easier to expand than a long if/elif block.
        for career_category in CAREER_DATA:
            if any(keyword in tokens for keyword in CAREER_DATA[career_category]["keywords"]):
                response = CAREER_DATA[career_category]["response"]
                break  # Stop searching once a match is found
            
        dispatcher.utter_message(text=response)
        return []