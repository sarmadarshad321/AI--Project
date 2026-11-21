# # """
# # Conversational Chatbot for Car Price Prediction
# # Rule-based chatbot with context management and step-by-step data collection
# # """

# # from datetime import datetime
# # import re

# # class ConversationalChatbot:
# #     """
# #     Rule-based chatbot that guides users through car price prediction
# #     """
    
# #     def __init__(self):
# #         self.sessions = {}  # Store user sessions
        
# #         # Conversation steps
# #         self.steps = [
# #             'car_brand',
# #             'car_model', 
# #             'city',
# #             'fuel_type',
# #             'engine',
# #             'transmission',
# #             'registered_in',
# #             'mileage'
# #         ]
        
# #         # Valid options (loaded from feature_info)
# #         self.valid_options = {
# #             'car_brand': ['honda', 'toyota', 'suzuki', 'daihatsu', 'nissan', 'mitsubishi', 'hyundai', 'kia'],
# #             'car_model': ['civic', 'corolla', 'city', 'cultus', 'swift', 'vitz', 'yaris', 'fit'],
# #             'fuel_type': ['petrol', 'diesel', 'hybrid', 'cng', 'lpg'],
# #             'transmission': ['manual', 'automatic'],
# #         }
        
# #         # City mapping
# #         self.city_mapping = {
# #             'karachi': 'karachi', 'khi': 'karachi', 'hyderabad': 'karachi',
# #             'lahore': 'lahore', 'lhr': 'lahore', 'faisalabad': 'lahore', 'multan': 'lahore',
# #             'islamabad': 'islamabad', 'isb': 'islamabad', 'rawalpindi': 'islamabad', 'peshawar': 'islamabad'
# #         }
    
# #     def create_session(self, session_id):
# #         """Create new chat session"""
# #         self.sessions[session_id] = {
# #             'step': 0,
# #             'data': {},
# #             'started': datetime.now(),
# #             'last_message': None
# #         }
    
# #     def get_session(self, session_id):
# #         """Get or create session"""
# #         if session_id not in self.sessions:
# #             self.create_session(session_id)
# #         return self.sessions[session_id]
    
# #     def detect_intent(self, message):
# #         """Detect user intent from message"""
# #         message = message.lower().strip()
        
# #         intents = {
# #             'greeting': ['hello', 'hi', 'hey', 'start', 'salam'],
# #             'predict': ['predict', 'price', 'value', 'estimate', 'worth'],
# #             'help': ['help', 'how', 'what', 'guide'],
# #             'reset': ['reset', 'restart', 'start over', 'cancel'],
# #             'info': ['accuracy', 'model', 'about', 'info'],
# #             'thanks': ['thank', 'thanks', 'bye', 'goodbye']
# #         }
        
# #         for intent, keywords in intents.items():
# #             if any(kw in message for kw in keywords):
# #                 return intent
        
# #         return 'answer'  # Default: treat as answer to current question
    
# #     def validate_input(self, step_name, value):
# #         """Validate user input for current step"""
# #         value = value.lower().strip()
        
# #         if step_name == 'car_brand':
# #             return value in self.valid_options['car_brand'], self.valid_options['car_brand']
        
# #         elif step_name == 'car_model':
# #             return value in self.valid_options['car_model'], self.valid_options['car_model']
        
# #         elif step_name == 'city':
# #             return value in self.city_mapping or len(value) > 2, list(self.city_mapping.keys())[:10]
        
# #         elif step_name == 'fuel_type':
# #             return value in self.valid_options['fuel_type'], self.valid_options['fuel_type']
        
# #         elif step_name == 'engine':
# #             try:
# #                 engine = float(value)
# #                 return 500 <= engine <= 5000, "Engine should be between 500cc - 5000cc"
# #             except:
# #                 return False, "Please enter a valid number (e.g., 1300)"
        
# #         elif step_name == 'transmission':
# #             return value in self.valid_options['transmission'], self.valid_options['transmission']
        
# #         elif step_name == 'registered_in':
# #             try:
# #                 year = int(value)
# #                 return 1990 <= year <= 2025, "Year should be between 1990-2025"
# #             except:
# #                 return False, "Please enter a valid year (e.g., 2018)"
        
# #         elif step_name == 'mileage':
# #             try:
# #                 mileage = float(value)
# #                 return 0 <= mileage <= 500000, "Mileage should be between 0-500,000 km"
# #             except:
# #                 return False, "Please enter a valid number (e.g., 50000)"
        
# #         return False, "Invalid input"
    
# #     def get_question(self, step_name):
# #         """Get question for current step"""
# #         questions = {
# #             'car_brand': "🚗 What's the car brand?\n(e.g., Honda, Toyota, Suzuki)",
# #             'car_model': "🏷️ What's the model?\n(e.g., Civic, Corolla, Cultus)",
# #             'city': "📍 Which city?\n(e.g., Karachi, Lahore, Islamabad, or any Pakistan city)",
# #             'fuel_type': "⛽ Fuel type?\n(e.g., Petrol, Diesel, Hybrid)",
# #             'engine': "🔧 Engine capacity in cc?\n(e.g., 1300, 1500, 1800)",
# #             'transmission': "⚙️ Transmission type?\n(Manual or Automatic)",
# #             'registered_in': "📅 Registration year?\n(e.g., 2018, 2020)",
# #             'mileage': "📏 Mileage in km?\n(e.g., 50000, 80000)"
# #         }
# #         return questions.get(step_name, "Please provide the information")
    
# #     def process_message(self, session_id, message, model_info=None):
# #         """
# #         Process user message and return response
        
# #         Returns:
# #             dict: {
# #                 'reply': str,
# #                 'options': list (optional),
# #                 'action': str (optional),
# #                 'prediction': dict (optional)
# #             }
# #         """
# #         session = self.get_session(session_id)
# #         intent = self.detect_intent(message)
        
# #         # Handle intents
# #         if intent == 'greeting':
# #             return {
# #                 'reply': "👋 Hello! I'm your AI Car Price Assistant.\n\n"
# #                         "I can help you predict the price of used cars in Pakistan.\n\n"
# #                         "Just tell me the car details, and I'll give you an instant estimate!\n\n"
# #                         "Ready to start? 🚗",
# #                 'action': 'start'
# #             }
        
# #         elif intent == 'predict':
# #             session['step'] = 0
# #             session['data'] = {}
# #             question = self.get_question(self.steps[0])
# #             return {
# #                 'reply': f"Great! Let's predict the price. 💰\n\n{question}",
# #                 'action': 'collect_data'
# #             }
        
# #         elif intent == 'help':
# #             return {
# #                 'reply': "🤖 **How to use:**\n\n"
# #                         "1. Tell me you want to predict a price\n"
# #                         "2. I'll ask 8 simple questions about the car\n"
# #                         "3. Answer each question\n"
# #                         "4. I'll predict the price instantly!\n\n"
# #                         f"**Model Accuracy:** {model_info.get('test_r2', 0.94)*100:.1f}% ✨\n\n"
# #                         "Say 'predict' to start!",
# #                 'action': None
# #             }
        
# #         elif intent == 'reset':
# #             session['step'] = 0
# #             session['data'] = {}
# #             return {
# #                 'reply': "🔄 Session reset! Say 'predict' to start fresh.",
# #                 'action': 'reset'
# #             }
        
# #         elif intent == 'info':
# #             return {
# #                 'reply': f"📊 **Model Information:**\n\n"
# #                         f"• Algorithm: {model_info.get('model_name', 'Random Forest')}\n"
# #                         f"• Accuracy (R²): {model_info.get('test_r2', 0.94)*100:.1f}%\n"
# #                         f"• Average Error: ±{model_info.get('test_mae', 185000):,.0f} PKR\n"
# #                         f"• Features: Polynomial + K-Means Clustering\n"
# #                         f"• Dataset: 5,497 cars\n\n"
# #                         f"Want to predict a price? Say 'predict'! 🚗",
# #                 'action': None
# #             }
        
# #         elif intent == 'thanks':
# #             return {
# #                 'reply': "You're welcome! 😊\n\n"
# #                         "Feel free to predict more car prices anytime!\n\n"
# #                         "Have a great day! 🚗✨",
# #                 'action': 'end'
# #             }
        
# #         # Handle data collection (answering questions)
# #         elif intent == 'answer' and session['step'] < len(self.steps):
# #             current_step = self.steps[session['step']]
            
# #             # Validate input
# #             is_valid, options = self.validate_input(current_step, message)
            
# #             if not is_valid:
# #                 if isinstance(options, list):
# #                     return {
# #                         'reply': f"❌ Invalid {current_step.replace('_', ' ')}.\n\n"
# #                                 f"Please choose from: {', '.join(options[:5])}...\n\n"
# #                                 f"Or type 'help' for guidance.",
# #                         'options': options
# #                     }
# #                 else:
# #                     return {
# #                         'reply': f"❌ {options}\n\nPlease try again.",
# #                         'action': None
# #                     }
            
# #             # Store valid input
# #             if current_step == 'city':
# #                 session['data'][current_step] = self.city_mapping.get(message.lower(), message.lower())
# #             else:
# #                 session['data'][current_step] = message.lower().strip()
            
# #             session['step'] += 1
            
# #             # Check if all data collected
# #             if session['step'] >= len(self.steps):
# #                 return {
# #                     'reply': "✅ Got all the details!\n\n"
# #                             "📊 Let me calculate the price...\n\n"
# #                             "⏳ Processing...",
# #                     'action': 'predict',
# #                     'data': session['data']
# #                 }
            
# #             # Ask next question
# #             next_step = self.steps[session['step']]
# #             question = self.get_question(next_step)
            
# #             return {
# #                 'reply': f"✓ Got it!\n\n{question}",
# #                 'action': 'continue'
# #             }
        
# #         # Default response
# #         return {
# #             'reply': "I didn't understand that. 🤔\n\n"
# #                     "Say 'predict' to start, or 'help' for guidance.",
# #             'action': None
# #         }


# # # Global chatbot instance
# # chatbot = ConversationalChatbot()


# """
# Conversational Chatbot for Car Price Prediction
# Rule-based chatbot with context management and step-by-step data collection
# """

# from datetime import datetime
# import re

# class ConversationalChatbot:
#     """
#     Rule-based chatbot that guides users through car price prediction
#     """
    
#     def __init__(self):
#         self.sessions = {}  # Store user sessions
        
#         # Conversation steps
#         self.steps = [
#             'car_brand',
#             'car_model', 
#             'city',
#             'fuel_type',
#             'engine',
#             'transmission',
#             'registered_in',
#             'mileage'
#         ]
        
#         # Valid options (loaded from feature_info)
#         self.valid_options = {
#             'car_brand': ['honda', 'toyota', 'suzuki', 'daihatsu', 'nissan', 'mitsubishi', 'hyundai', 'kia'],
#             'car_model': ['civic', 'corolla', 'city', 'cultus', 'swift', 'vitz', 'yaris', 'fit'],
#             'fuel_type': ['petrol', 'diesel', 'hybrid', 'cng', 'lpg'],
#             'transmission': ['manual', 'automatic'],
#         }
        
#         # City mapping
#         self.city_mapping = {
#             'karachi': 'karachi', 'khi': 'karachi', 'hyderabad': 'karachi',
#             'lahore': 'lahore', 'lhr': 'lahore', 'faisalabad': 'lahore', 'multan': 'lahore',
#             'islamabad': 'islamabad', 'isb': 'islamabad', 'rawalpindi': 'islamabad', 'peshawar': 'islamabad'
#         }
    
#     def create_session(self, session_id):
#         """Create new chat session"""
#         self.sessions[session_id] = {
#             'step': 0,
#             'data': {},
#             'started': datetime.now(),
#             'last_message': None
#         }
    
#     def get_session(self, session_id):
#         """Get or create session"""
#         if session_id not in self.sessions:
#             self.create_session(session_id)
#         return self.sessions[session_id]
    
#     def detect_intent(self, message, session):
#         """
#         Detect user intent from message
#         Considers session context to avoid false positives
#         """
#         message = message.lower().strip()
        
#         # If in data collection mode, treat as answer unless explicit command
#         if session['step'] > 0 and session['step'] < len(self.steps):
#             # Check for explicit commands only
#             explicit_commands = {
#                 'reset': ['reset', 'restart', 'cancel'],
#                 'help': ['help me', 'i need help']
#             }
            
#             for intent, keywords in explicit_commands.items():
#                 if any(message == kw for kw in keywords):
#                     return intent
            
#             # Otherwise treat as answer
#             return 'answer'
        
#         # Not in collection mode - detect intent normally
#         intents = {
#             'greeting': ['hello', 'hi', 'hey', 'salam', 'start'],
#             'predict': ['predict', 'price', 'value', 'estimate', 'worth', 'check price'],
#             'help': ['help', 'how', 'guide', 'what can you do'],
#             'reset': ['reset', 'restart', 'start over', 'cancel'],
#             'info': ['accuracy', 'model', 'about', 'info', 'details'],
#             'thanks': ['thank', 'thanks', 'bye', 'goodbye']
#         }
        
#         # Exact matches first
#         for intent, keywords in intents.items():
#             if message in keywords:
#                 return intent
        
#         # Partial matches
#         for intent, keywords in intents.items():
#             if any(kw in message for kw in keywords):
#                 return intent
        
#         return 'answer'  # Default: treat as answer
    
#     def validate_input(self, step_name, value):
#         """Validate user input for current step"""
#         value = value.lower().strip()
        
#         if step_name == 'car_brand':
#             return value in self.valid_options['car_brand'], self.valid_options['car_brand']
        
#         elif step_name == 'car_model':
#             return value in self.valid_options['car_model'], self.valid_options['car_model']
        
#         elif step_name == 'city':
#             return value in self.city_mapping or len(value) > 2, list(self.city_mapping.keys())[:10]
        
#         elif step_name == 'fuel_type':
#             return value in self.valid_options['fuel_type'], self.valid_options['fuel_type']
        
#         elif step_name == 'engine':
#             try:
#                 engine = float(value)
#                 return 500 <= engine <= 5000, "Engine should be between 500cc - 5000cc"
#             except:
#                 return False, "Please enter a valid number (e.g., 1300)"
        
#         elif step_name == 'transmission':
#             return value in self.valid_options['transmission'], self.valid_options['transmission']
        
#         elif step_name == 'registered_in':
#             try:
#                 year = int(value)
#                 return 1990 <= year <= 2025, "Year should be between 1990-2025"
#             except:
#                 return False, "Please enter a valid year (e.g., 2018)"
        
#         elif step_name == 'mileage':
#             try:
#                 mileage = float(value)
#                 return 0 <= mileage <= 500000, "Mileage should be between 0-500,000 km"
#             except:
#                 return False, "Please enter a valid number (e.g., 50000)"
        
#         return False, "Invalid input"
    
#     def get_question(self, step_name):
#         """Get question for current step"""
#         questions = {
#             'car_brand': "🚗 What's the car brand?\n(e.g., Honda, Toyota, Suzuki)",
#             'car_model': "🏷️ What's the model?\n(e.g., Civic, Corolla, Cultus)",
#             'city': "📍 Which city?\n(e.g., Karachi, Lahore, Islamabad, or any Pakistan city)",
#             'fuel_type': "⛽ Fuel type?\n(e.g., Petrol, Diesel, Hybrid)",
#             'engine': "🔧 Engine capacity in cc?\n(e.g., 1300, 1500, 1800)",
#             'transmission': "⚙️ Transmission type?\n(Manual or Automatic)",
#             'registered_in': "📅 Registration year?\n(e.g., 2018, 2020)",
#             'mileage': "📏 Mileage in km?\n(e.g., 50000, 80000)"
#         }
#         return questions.get(step_name, "Please provide the information")
    
#     def process_message(self, session_id, message, model_info=None):
#         """
#         Process user message and return response
        
#         Returns:
#             dict: {
#                 'reply': str,
#                 'options': list (optional),
#                 'action': str (optional),
#                 'prediction': dict (optional),
#                 'session_info': dict (for debugging)
#             }
#         """
#         session = self.get_session(session_id)
#         intent = self.detect_intent(message, session)  # Pass session for context
        
#         # Debug info
#         session_info = {
#             'step': session['step'],
#             'total_steps': len(self.steps),
#             'current_field': self.steps[session['step']] if session['step'] < len(self.steps) else 'completed',
#             'collected_data': list(session['data'].keys())
#         }
        
#         # Handle intents
#         if intent == 'greeting':
#             return {
#                 'reply': "👋 Hello! I'm your AI Car Price Assistant.\n\n"
#                         "I can help you predict the price of used cars in Pakistan.\n\n"
#                         "Just tell me the car details, and I'll give you an instant estimate!\n\n"
#                         "Ready to start? 🚗",
#                 'action': 'start',
#                 'session_info': session_info
#             }
        
#         elif intent == 'predict':
#             session['step'] = 0
#             session['data'] = {}
#             question = self.get_question(self.steps[0])
#             return {
#                 'reply': f"Great! Let's predict the price. 💰\n\n{question}",
#                 'action': 'collect_data',
#                 'session_info': session_info
#             }
        
#         elif intent == 'help':
#             return {
#                 'reply': "🤖 **How to use:**\n\n"
#                         "1. Tell me you want to predict a price\n"
#                         "2. I'll ask 8 simple questions about the car\n"
#                         "3. Answer each question\n"
#                         "4. I'll predict the price instantly!\n\n"
#                         f"**Model Accuracy:** {model_info.get('test_r2', 0.94)*100:.1f}% ✨\n\n"
#                         "Say 'predict' to start!",
#                 'action': None
#             }
        
#         elif intent == 'reset':
#             session['step'] = 0
#             session['data'] = {}
#             return {
#                 'reply': "🔄 Session reset! Say 'predict' to start fresh.",
#                 'action': 'reset'
#             }
        
#         elif intent == 'info':
#             return {
#                 'reply': f"📊 **Model Information:**\n\n"
#                         f"• Algorithm: {model_info.get('model_name', 'Random Forest')}\n"
#                         f"• Accuracy (R²): {model_info.get('test_r2', 0.94)*100:.1f}%\n"
#                         f"• Average Error: ±{model_info.get('test_mae', 185000):,.0f} PKR\n"
#                         f"• Features: Polynomial + K-Means Clustering\n"
#                         f"• Dataset: 5,497 cars\n\n"
#                         f"Want to predict a price? Say 'predict'! 🚗",
#                 'action': None
#             }
        
#         elif intent == 'thanks':
#             return {
#                 'reply': "You're welcome! 😊\n\n"
#                         "Feel free to predict more car prices anytime!\n\n"
#                         "Have a great day! 🚗✨",
#                 'action': 'end'
#             }
        
#         # Handle data collection (answering questions)
#         elif intent == 'answer' and session['step'] < len(self.steps):
#             current_step = self.steps[session['step']]
            
#             # Validate input
#             is_valid, options = self.validate_input(current_step, message)
            
#             if not is_valid:
#                 if isinstance(options, list):
#                     return {
#                         'reply': f"❌ Invalid {current_step.replace('_', ' ')}.\n\n"
#                                 f"Please choose from: {', '.join(options[:5])}...\n\n"
#                                 f"Or type 'help' for guidance.",
#                         'options': options
#                     }
#                 else:
#                     return {
#                         'reply': f"❌ {options}\n\nPlease try again.",
#                         'action': None
#                     }
            
#             # Store valid input
#             if current_step == 'city':
#                 session['data'][current_step] = self.city_mapping.get(message.lower(), message.lower())
#             else:
#                 session['data'][current_step] = message.lower().strip()
            
#             session['step'] += 1
            
#             # Check if all data collected
#             if session['step'] >= len(self.steps):
#                 return {
#                     'reply': "✅ Got all the details!\n\n"
#                             "📊 Let me calculate the price...\n\n"
#                             "⏳ Processing...",
#                     'action': 'predict',
#                     'data': session['data']
#                 }
            
#             # Ask next question
#             next_step = self.steps[session['step']]
#             question = self.get_question(next_step)
            
#             return {
#                 'reply': f"✓ Got it!\n\n{question}",
#                 'action': 'continue'
#             }
        
#         # Default response
#         return {
#             'reply': "I didn't understand that. 🤔\n\n"
#                     "Say 'predict' to start, or 'help' for guidance.",
#             'action': None,
#             'session_info': session_info
#         }


# # Global chatbot instance
# chatbot = ConversationalChatbot()


# """
# Conversational Chatbot for Car Price Prediction
# Rule-based chatbot with context management and step-by-step data collection
# """

# from datetime import datetime
# import re

# class ConversationalChatbot:
#     """
#     Rule-based chatbot that guides users through car price prediction
#     """
    
#     def __init__(self):
#         self.sessions = {}  # Store user sessions
        
#         # Conversation steps
#         self.steps = [
#             'car_brand',
#             'car_model', 
#             'city',
#             'fuel_type',
#             'engine',
#             'transmission',
#             'registered_in',
#             'mileage'
#         ]
        
#         # Valid options (loaded from feature_info)
#         self.valid_options = {
#             'car_brand': ['honda', 'toyota', 'suzuki', 'daihatsu', 'nissan', 'mitsubishi', 'hyundai', 'kia'],
#             'car_model': ['civic', 'corolla', 'city', 'cultus', 'swift', 'vitz', 'yaris', 'fit'],
#             'fuel_type': ['petrol', 'diesel', 'hybrid', 'cng', 'lpg'],
#             'transmission': ['manual', 'automatic'],
#         }
        
#         # City mapping
#         self.city_mapping = {
#             'karachi': 'karachi', 'khi': 'karachi', 'hyderabad': 'karachi',
#             'lahore': 'lahore', 'lhr': 'lahore', 'faisalabad': 'lahore', 'multan': 'lahore',
#             'islamabad': 'islamabad', 'isb': 'islamabad', 'rawalpindi': 'islamabad', 'peshawar': 'islamabad'
#         }
    
#     def create_session(self, session_id):
#         """Create new chat session"""
#         self.sessions[session_id] = {
#             'step': 0,
#             'data': {},
#             'started': datetime.now(),
#             'last_message': None
#         }
    
#     def get_session(self, session_id):
#         """Get or create session"""
#         if session_id not in self.sessions:
#             self.create_session(session_id)
#         return self.sessions[session_id]
    
#     def detect_intent(self, message, session):
#         """
#         Detect user intent from message
#         Considers session context to avoid false positives
#         """
#         message = message.lower().strip()
        
#         # If in data collection mode, treat as answer unless explicit command
#         if session['step'] > 0 and session['step'] < len(self.steps):
#             # Check for explicit commands only
#             explicit_commands = {
#                 'reset': ['reset', 'restart', 'cancel'],
#                 'help': ['help me', 'i need help']
#             }
            
#             for intent, keywords in explicit_commands.items():
#                 if any(message == kw for kw in keywords):
#                     return intent
            
#             # Otherwise treat as answer
#             return 'answer'
        
#         # Not in collection mode - detect intent normally
#         intents = {
#             'greeting': ['hello', 'hi', 'hey', 'salam', 'start'],
#             'predict': ['predict', 'price', 'value', 'estimate', 'worth', 'check price'],
#             'help': ['help', 'how', 'guide', 'what can you do'],
#             'reset': ['reset', 'restart', 'start over', 'cancel'],
#             'info': ['accuracy', 'model', 'about', 'info', 'details'],
#             'thanks': ['thank', 'thanks', 'bye', 'goodbye']
#         }
        
#         # Exact matches first
#         for intent, keywords in intents.items():
#             if message in keywords:
#                 return intent
        
#         # Partial matches
#         for intent, keywords in intents.items():
#             if any(kw in message for kw in keywords):
#                 return intent
        
#         return 'answer'  # Default: treat as answer
    
#     def validate_input(self, step_name, value):
#         """Validate user input for current step"""
#         value = value.lower().strip()
        
#         if step_name == 'car_brand':
#             return value in self.valid_options['car_brand'], self.valid_options['car_brand']
        
#         elif step_name == 'car_model':
#             return value in self.valid_options['car_model'], self.valid_options['car_model']
        
#         elif step_name == 'city':
#             return value in self.city_mapping or len(value) > 2, list(self.city_mapping.keys())[:10]
        
#         elif step_name == 'fuel_type':
#             return value in self.valid_options['fuel_type'], self.valid_options['fuel_type']
        
#         elif step_name == 'engine':
#             try:
#                 engine = float(value)
#                 return 500 <= engine <= 5000, "Engine should be between 500cc - 5000cc"
#             except:
#                 return False, "Please enter a valid number (e.g., 1300)"
        
#         elif step_name == 'transmission':
#             return value in self.valid_options['transmission'], self.valid_options['transmission']
        
#         elif step_name == 'registered_in':
#             try:
#                 year = int(value)
#                 return 1990 <= year <= 2025, "Year should be between 1990-2025"
#             except:
#                 return False, "Please enter a valid year (e.g., 2018)"
        
#         elif step_name == 'mileage':
#             try:
#                 # Remove commas if present
#                 value = value.replace(',', '').strip()
#                 mileage = float(value)
#                 return 0 <= mileage <= 500000, "Mileage should be between 0-500,000 km"
#             except:
#                 return False, "Please enter a valid number (e.g., 50000)"
        
#         return False, "Invalid input"
    
#     def get_question(self, step_name):
#         """Get question for current step"""
#         questions = {
#             'car_brand': "🚗 What's the car brand?\n(e.g., Honda, Toyota, Suzuki)",
#             'car_model': "🏷️ What's the model?\n(e.g., Civic, Corolla, Cultus)",
#             'city': "📍 Which city?\n(e.g., Karachi, Lahore, Islamabad, or any Pakistan city)",
#             'fuel_type': "⛽ Fuel type?\n(e.g., Petrol, Diesel, Hybrid)",
#             'engine': "🔧 Engine capacity in cc?\n(e.g., 1300, 1500, 1800)",
#             'transmission': "⚙️ Transmission type?\n(Manual or Automatic)",
#             'registered_in': "📅 Registration year?\n(e.g., 2018, 2020)",
#             'mileage': "📏 Mileage in km?\n(e.g., 50000, 80000)"
#         }
#         return questions.get(step_name, "Please provide the information")
    
#     def process_message(self, session_id, message, model_info=None):
#         """
#         Process user message and return response
        
#         Returns:
#             dict: {
#                 'reply': str,
#                 'options': list (optional),
#                 'action': str (optional),
#                 'prediction': dict (optional),
#                 'session_info': dict (for debugging)
#             }
#         """
#         session = self.get_session(session_id)
#         intent = self.detect_intent(message, session)  # Pass session for context
        
#         # Debug info
#         session_info = {
#             'step': session['step'],
#             'total_steps': len(self.steps),
#             'current_field': self.steps[session['step']] if session['step'] < len(self.steps) else 'completed',
#             'collected_data': list(session['data'].keys())
#         }
        
#         # Handle intents
#         if intent == 'greeting':
#             return {
#                 'reply': "👋 Hello! I'm your AI Car Price Assistant.\n\n"
#                         "I can help you predict the price of used cars in Pakistan.\n\n"
#                         "Just tell me the car details, and I'll give you an instant estimate!\n\n"
#                         "Ready to start? 🚗",
#                 'action': 'start',
#                 'session_info': session_info
#             }
        
#         elif intent == 'predict':
#             session['step'] = 0
#             session['data'] = {}
#             question = self.get_question(self.steps[0])
#             return {
#                 'reply': f"Great! Let's predict the price. 💰\n\n{question}",
#                 'action': 'collect_data',
#                 'session_info': session_info
#             }
        
#         elif intent == 'help':
#             return {
#                 'reply': "🤖 **How to use:**\n\n"
#                         "1. Tell me you want to predict a price\n"
#                         "2. I'll ask 8 simple questions about the car\n"
#                         "3. Answer each question\n"
#                         "4. I'll predict the price instantly!\n\n"
#                         f"**Model Accuracy:** {model_info.get('test_r2', 0.94)*100:.1f}% ✨\n\n"
#                         "Say 'predict' to start!",
#                 'action': None
#             }
        
#         elif intent == 'reset':
#             session['step'] = 0
#             session['data'] = {}
#             return {
#                 'reply': "🔄 Session reset! Say 'predict' to start fresh.",
#                 'action': 'reset'
#             }
        
#         elif intent == 'info':
#             return {
#                 'reply': f"📊 **Model Information:**\n\n"
#                         f"• Algorithm: {model_info.get('model_name', 'Random Forest')}\n"
#                         f"• Accuracy (R²): {model_info.get('test_r2', 0.94)*100:.1f}%\n"
#                         f"• Average Error: ±{model_info.get('test_mae', 185000):,.0f} PKR\n"
#                         f"• Features: Polynomial + K-Means Clustering\n"
#                         f"• Dataset: 5,497 cars\n\n"
#                         f"Want to predict a price? Say 'predict'! 🚗",
#                 'action': None
#             }
        
#         elif intent == 'thanks':
#             return {
#                 'reply': "You're welcome! 😊\n\n"
#                         "Feel free to predict more car prices anytime!\n\n"
#                         "Have a great day! 🚗✨",
#                 'action': 'end'
#             }
        
#         # Handle data collection (answering questions)
#         elif intent == 'answer' and session['step'] < len(self.steps):
#             current_step = self.steps[session['step']]
            
#             # Validate input
#             is_valid, options = self.validate_input(current_step, message)
            
#             if not is_valid:
#                 if isinstance(options, list):
#                     return {
#                         'reply': f"❌ Invalid {current_step.replace('_', ' ')}.\n\n"
#                                 f"Please choose from: {', '.join(options[:5])}...\n\n"
#                                 f"Or type 'help' for guidance.",
#                         'options': options
#                     }
#                 else:
#                     return {
#                         'reply': f"❌ {options}\n\nPlease try again.",
#                         'action': None
#                     }
            
#             # Store valid input
#             if current_step == 'city':
#                 session['data'][current_step] = self.city_mapping.get(message.lower(), message.lower())
#             else:
#                 session['data'][current_step] = message.lower().strip()
            
#             session['step'] += 1
            
#             # Check if all data collected
#             if session['step'] >= len(self.steps):
#                 return {
#                     'reply': "✅ Got all the details!\n\n"
#                             "📊 Let me calculate the price...\n\n"
#                             "⏳ Processing...",
#                     'action': 'predict',
#                     'data': session['data']
#                 }
            
#             # Ask next question
#             next_step = self.steps[session['step']]
#             question = self.get_question(next_step)
            
#             return {
#                 'reply': f"✓ Got it!\n\n{question}",
#                 'action': 'continue'
#             }
        
#         # Default response
#         return {
#             'reply': "I didn't understand that. 🤔\n\n"
#                     "Say 'predict' to start, or 'help' for guidance.",
#             'action': None,
#             'session_info': session_info
#         }


# # Global chatbot instance
# chatbot = ConversationalChatbot()





# """
# Enhanced Conversational Chatbot with Gemini API
# Supports natural conversations + car price predictions
# """

# import google.generativeai as genai
# from datetime import datetime
# import re
# import os

# class GeminiChatbot:
#     """
#     AI-powered chatbot using Gemini for natural conversations
#     """
    
#     def __init__(self, api_key=None):
#         # Configure Gemini API
#         self.api_key = api_key or os.getenv('GEMINI_API_KEY')
#         if self.api_key:
#             genai.configure(api_key=self.api_key)
#             self.model = genai.GenerativeModel('gemini-1.5-flash')
#         else:
#             print("⚠️ Warning: GEMINI_API_KEY not set. Using rule-based fallback.")
#             self.model = None
        
#         self.sessions = {}
        
#         # System prompt for Gemini
#         self.system_prompt = """You are an AI assistant for a Pakistani car price prediction service. Your role:

# 1. Help users predict used car prices in Pakistan
# 2. Answer questions about car values, market trends, depreciation
# 3. Explain why certain factors affect price (brand, mileage, age, city, etc.)
# 4. Be friendly, conversational, and use simple Urdu/English mix if needed

# When user wants to predict price, collect these details conversationally:
# - Car brand (Honda, Toyota, Suzuki, etc.)
# - Model (Civic, Corolla, Cultus, etc.)
# - City (Karachi, Lahore, Islamabad, or any Pakistan city)
# - Fuel type (Petrol, Diesel, Hybrid, CNG)
# - Engine (cc, e.g., 1300, 1800)
# - Transmission (Manual/Automatic)
# - Registration year (e.g., 2018)
# - Mileage (km, e.g., 50000)

# Important guidelines:
# - Don't ask all questions at once - collect one by one naturally
# - If user asks "why is my car cheaper?", explain based on age, mileage, brand depreciation
# - If asked about market trends, explain Pakistani car market insights
# - Keep responses concise (2-3 sentences max unless explaining)
# - Use emojis moderately 🚗💰

# Pakistani Car Market Context:
# - Economy segment: Under 20 Lacs
# - Mid-Range: 20-40 Lacs  
# - Premium: 40-70 Lacs
# - Luxury: Above 70 Lacs
# - Popular brands: Toyota (holds value best), Honda, Suzuki (affordable)
# - Cities: Karachi/Lahore have more demand, better resale
# - Depreciation: ~15-20% per year for first 5 years
# """
        
#         self.steps = [
#             'car_brand', 'car_model', 'city', 'fuel_type',
#             'engine', 'transmission', 'registered_in', 'mileage'
#         ]
    
#     def create_session(self, session_id):
#         """Create new chat session"""
#         self.sessions[session_id] = {
#             'step': 0,
#             'data': {},
#             'collecting': False,  # Is actively collecting car details
#             'history': [],  # Conversation history for Gemini
#             'started': datetime.now()
#         }
    
#     def get_session(self, session_id):
#         """Get or create session"""
#         if session_id not in self.sessions:
#             self.create_session(session_id)
#         return self.sessions[session_id]
    
#     def detect_prediction_intent(self, message):
#         """Check if user wants to predict price"""
#         keywords = ['predict', 'price', 'value', 'kitni', 'kya', 'estimate', 'worth', 'check price']
#         message_lower = message.lower()
#         return any(kw in message_lower for kw in keywords)
    
#     def extract_car_data(self, message, current_step):
#         """Extract car information from natural language"""
#         message = message.lower().strip()
        
#         if current_step == 'car_brand':
#             brands = ['honda', 'toyota', 'suzuki', 'daihatsu', 'nissan', 'mitsubishi', 'hyundai', 'kia']
#             for brand in brands:
#                 if brand in message:
#                     return brand
        
#         elif current_step == 'car_model':
#             models = ['civic', 'corolla', 'city', 'cultus', 'swift', 'vitz', 'yaris', 'fit', 'alto', 'mehran', 'bolan']
#             for model in models:
#                 if model in message:
#                     return model
        
#         elif current_step == 'fuel_type':
#             fuels = ['petrol', 'diesel', 'hybrid', 'cng', 'lpg']
#             for fuel in fuels:
#                 if fuel in message:
#                     return fuel
        
#         elif current_step == 'transmission':
#             if 'auto' in message:
#                 return 'automatic'
#             elif 'manual' in message:
#                 return 'manual'
        
#         elif current_step == 'engine':
#             # Extract numbers (engine cc)
#             numbers = re.findall(r'\d+', message)
#             if numbers:
#                 engine = int(numbers[0])
#                 if 500 <= engine <= 5000:
#                     return str(engine)
        
#         elif current_step == 'registered_in':
#             # Extract year
#             numbers = re.findall(r'\b(19|20)\d{2}\b', message)
#             if numbers:
#                 year = int(numbers[0])
#                 if 1990 <= year <= 2025:
#                     return str(year)
        
#         elif current_step == 'mileage':
#             # Extract mileage
#             numbers = re.findall(r'\d+', message.replace(',', ''))
#             if numbers:
#                 mileage = int(numbers[0])
#                 if 0 <= mileage <= 500000:
#                     return str(mileage)
        
#         elif current_step == 'city':
#             # Accept any city name
#             return message
        
#         return None
    
#     def get_gemini_response(self, session, user_message):
#         """Get response from Gemini API"""
#         if not self.model:
#             return self.get_fallback_response(session, user_message)
        
#         try:
#             # Build conversation history
#             conversation_history = "\n".join([
#                 f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
#                 for msg in session['history'][-10:]  # Last 10 messages for context
#             ])
            
#             # Add context about data collection
#             context = ""
#             if session['collecting']:
#                 current_step = self.steps[session['step']]
#                 collected = list(session['data'].keys())
#                 context = f"\n\nCurrent task: Collecting {current_step}. Already collected: {collected}"
            
#             # Generate response
#             prompt = f"{self.system_prompt}\n\nConversation:\n{conversation_history}\nUser: {user_message}{context}\n\nAssistant:"
            
#             response = self.model.generate_content(prompt)
#             return response.text
        
#         except Exception as e:
#             print(f"Gemini API Error: {e}")
#             return self.get_fallback_response(session, user_message)
    
#     def get_fallback_response(self, session, message):
#         """Simple rule-based fallback if Gemini unavailable"""
#         if self.detect_prediction_intent(message):
#             return "Sure! I can help you predict the car price. Let's start - what's the car brand? (e.g., Honda, Toyota, Suzuki)"
        
#         return "I'm here to help you predict car prices! Say 'predict' to start, or ask me anything about car values in Pakistan. 🚗"
    
#     def process_message(self, session_id, message, model_info=None):
#         """
#         Process user message with Gemini AI
        
#         Returns response dict with reply and optional prediction action
#         """
#         session = self.get_session(session_id)
        
#         # Add to history
#         session['history'].append({
#             'role': 'user',
#             'content': message,
#             'timestamp': datetime.now().isoformat()
#         })
        
#         # Check if user wants to predict (start collection)
#         if not session['collecting'] and self.detect_prediction_intent(message):
#             session['collecting'] = True
#             session['step'] = 0
#             session['data'] = {}
#             reply = "Great! Let's predict the price. What's the car brand? (e.g., Honda, Toyota, Suzuki) 🚗"
        
#         # If collecting data
#         elif session['collecting'] and session['step'] < len(self.steps):
#             current_step = self.steps[session['step']]
            
#             # Try to extract data
#             extracted_value = self.extract_car_data(message, current_step)
            
#             if extracted_value:
#                 session['data'][current_step] = extracted_value
#                 session['step'] += 1
                
#                 # Check if done
#                 if session['step'] >= len(self.steps):
#                     session['collecting'] = False
#                     reply = "Perfect! I have all the details. Let me calculate the price... 💰"
#                     action = 'predict'
                    
#                     session['history'].append({
#                         'role': 'assistant',
#                         'content': reply,
#                         'timestamp': datetime.now().isoformat()
#                     })
                    
#                     return {
#                         'reply': reply,
#                         'action': action,
#                         'data': session['data']
#                     }
                
#                 # Ask next question
#                 next_step = self.steps[session['step']]
#                 questions = {
#                     'car_model': 'Got it! What model?',
#                     'city': 'Which city?',
#                     'fuel_type': 'Fuel type? (Petrol/Diesel/Hybrid)',
#                     'engine': 'Engine capacity in cc? (e.g., 1300, 1800)',
#                     'transmission': 'Manual or Automatic?',
#                     'registered_in': 'Registration year? (e.g., 2018)',
#                     'mileage': 'Mileage in km? (e.g., 50000)'
#                 }
#                 reply = questions.get(next_step, 'Next?')
#             else:
#                 # Couldn't extract, ask again with Gemini help
#                 reply = self.get_gemini_response(session, message)
        
#         # Normal conversation (not collecting)
#         else:
#             reply = self.get_gemini_response(session, message)
        
#         # Add assistant reply to history
#         session['history'].append({
#             'role': 'assistant',
#             'content': reply,
#             'timestamp': datetime.now().isoformat()
#         })
        
#         return {
#             'reply': reply,
#             'action': None
#         }


# # Initialize with API key from environment
# # Set your key: export GEMINI_API_KEY="your-key-here"
# chatbot = GeminiChatbot()


# # ============================================
# # Usage in Flask app.py:
# # ============================================
# """
# @app.route("/api/chatbot", methods=["POST"])
# def chatbot_endpoint():
#     try:
#         data = request.json
#         session_id = data.get("session_id", "default")
#         message = data.get("message", "")
        
#         response = chatbot.process_message(session_id=session_id, message=message, model_info=model_info)

#         if response.get('action') == 'predict' and 'data' in response:
#             car_data = response['data']
#             # Convert to proper types
#             car_data['engine'] = float(car_data['engine'])
#             car_data['registered_in'] = int(car_data['registered_in'])
#             car_data['mileage'] = float(car_data['mileage'])
            
#             prediction_result = make_prediction(car_data).json
#             if prediction_result['success']:
#                 pred = prediction_result
#                 response['reply'] = (
#                     f"🎉 Price Prediction\n"
#                     f"💰 Estimated: {pred['price_display']['formatted']}\n"
#                     f"📊 Range: {pred['price_range']['min_display']['lacs']} - {pred['price_range']['max_display']['lacs']} Lacs\n"
#                     f"🏷️ Segment: {pred['segment']}\n"
#                     f"✅ Confidence: {pred['model_performance']['confidence'].upper()}"
#                 )
#                 response['prediction'] = prediction_result
#             else:
#                 response['reply'] = f"❌ Prediction failed: {prediction_result.get('error')}"
        
#         response['timestamp'] = datetime.now().isoformat()
#         return jsonify(response)
    
#     except Exception as e:
#         return jsonify({
#             "error": str(e),
#             "reply": "Sorry, something went wrong.",
#             "timestamp": datetime.now().isoformat()
#         }), 500
# """


"""
Enhanced Conversational Chatbot with Gemini API (UPDATED)
Using new google-genai package
"""

import google.generativeai as genai
from datetime import datetime
import re
import os
from dotenv import load_dotenv
import requests
import json

# Load environment variables from .env file in the same directory
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

class GeminiChatbot:
    """
    AI-powered chatbot using Gemini for natural conversations
    """
    
    def __init__(self, api_key=None):
        # Configure Gemini API
        self.api_key = api_key or os.getenv('GEMINI_API_KEY')
        
        # Debug: Check if API key was found
        if not self.api_key:
            print("⚠️ Warning: GEMINI_API_KEY not found in environment variables.")
            print(f"   Current working directory: {os.getcwd()}")
            print(f"   Looking for .env in: {os.path.dirname(__file__)}")
            print(f"   GEMINI_API_KEY value: {os.getenv('GEMINI_API_KEY')}")
            self.model = None
        else:
            # Check if API key is just a placeholder
            if self.api_key == 'your_gemini_api_key_here' or len(self.api_key) < 10:
                print("⚠️ Warning: GEMINI_API_KEY appears to be a placeholder. Please set your actual API key in .env file.")
                self.model = None
            else:
                try:
                    genai.configure(api_key=self.api_key)
                    
                    # First, try to list available models
                    available_models = []
                    try:
                        for model in genai.list_models():
                            if 'generateContent' in model.supported_generation_methods:
                                model_name = model.name.replace('models/', '')
                                available_models.append(model_name)
                                print(f"   Found available model: {model_name}")
                    except Exception as list_error:
                        print(f"   Could not list models: {list_error}")
                    
                    # Try model names in order of preference (using actual available models)
                    # Priority: newer models first, then fallback to older ones
                    model_names = [
                        'gemini-2.5-flash',        # Latest flash
                        'gemini-2.5-pro',           # Latest pro
                        'gemini-2.0-flash',         # Stable flash
                        'gemini-pro-latest',        # Latest pro
                        'gemini-flash-latest',       # Latest flash
                        'gemini-1.5-flash-latest',  # Older flash
                        'gemini-1.5-pro-latest',    # Older pro
                        'gemini-1.5-flash',         # Flash version
                        'gemini-1.5-pro',           # Pro version
                        'gemini-pro',               # Legacy pro
                    ]
                    
                    # If we found available models, prioritize those
                    if available_models:
                        # Add available models to the front of the list, but keep order
                        priority_models = [m for m in model_names if m in available_models]
                        other_available = [m for m in available_models if m not in model_names]
                        model_names = priority_models + other_available + [m for m in model_names if m not in available_models]
                    
                    self.model = None
                    self.model_name = None
                    
                    for model_name in model_names:
                        try:
                            # Remove 'models/' prefix if present for consistency
                            clean_name = model_name.replace('models/', '')
                            self.model = genai.GenerativeModel(clean_name)
                            self.model_name = clean_name
                            print(f"✅ Gemini API configured successfully! Using model: {clean_name}")
                            print(f"   API Key loaded: {self.api_key[:10]}...{self.api_key[-4:]}")
                            break
                        except Exception as model_error:
                            # Try next model
                            continue
                    
                    if not self.model:
                        print("❌ None of the Gemini models are available.")
                        if available_models:
                            print(f"   Available models found: {available_models[:5]}...")
                        print("   Please check your API key permissions at https://aistudio.google.com/app/apikey")
                        self.model = None
                        
                except Exception as e:
                    print(f"❌ Gemini API configuration failed: {e}")
                    print(f"   Error type: {type(e).__name__}")
                    import traceback
                    traceback.print_exc()
                    self.model = None
        
        self.sessions = {}
        
        # System prompt for Gemini with emphasis on varied, random responses for ANY topic
        self.system_prompt = """You are a friendly, knowledgeable AI assistant who can chat about ANY topic with creative, random, and varied responses! Your personality:

1. **Universal Conversational AI**: You can discuss ANYTHING - technology, science, history, movies, music, sports, food, travel, philosophy, jokes, stories, current events, Pakistani culture, world news, personal advice, and much more!
2. **Car Price Prediction Expert**: When specifically asked, help users predict used car prices in Pakistan
3. **Cultural Bridge**: Use simple Urdu/English mix when appropriate, be relatable to Pakistani users
4. **Helpful & Friendly**: Always be polite, engaging, and helpful regardless of the topic
5. **RANDOM & VARIED**: CRITICAL - Your responses MUST be random and varied! Never repeat the same phrases. Be creative, use different expressions, vary your tone, style, and approach. Each response should feel fresh and unpredictable!

**CONVERSATION MODE - ANY TOPIC**:
- You can discuss ANY topic the user brings up - no restrictions!
- Movies, TV shows, books, music, art, literature
- Science, technology, AI, programming, space, nature
- Sports, cricket, football, gaming, esports
- Food, cooking, recipes, restaurants
- Travel, places, cultures, languages
- History, politics, economics, philosophy
- Personal advice, relationships, career, education
- Jokes, memes, fun facts, trivia
- Current events, news, trends
- Pakistani culture, traditions, festivals
- Health, fitness, lifestyle
- Business, finance, investments
- And literally ANYTHING else!

**Response Style Guidelines:**
- **RANDOMNESS IS KEY**: Vary your responses dramatically! Use different:
  * Greetings (Hey, Hi, Hello, Assalam-o-Alaikum, etc.)
  * Expressions and phrases
  * Sentence structures
  * Tone (casual, formal, humorous, thoughtful)
  * Emoji usage (sometimes more, sometimes less)
  * Response length (short quips, detailed explanations, bullet points, etc.)
- Be creative and unpredictable - surprise the user!
- Keep responses engaging (2-5 sentences usually, but vary this too!)
- Use emojis moderately but vary their usage
- Be respectful and positive
- Ask follow-up questions to keep conversations going
- Share interesting facts, opinions, or perspectives
- **NEVER use the exact same phrase or structure twice in a row!**

**CAR PRICE PREDICTION MODE** (only when user explicitly wants to predict car prices):
When user wants to predict price, collect these details conversationally:
- Car brand (Honda, Toyota, Suzuki, etc.)
- Model (Civic, Corolla, Cultus, etc.)
- City (Karachi, Lahore, Islamabad, or any Pakistan city)
- Fuel type (Petrol, Diesel, Hybrid, CNG)
- Engine (cc, e.g., 1300, 1800)
- Transmission (Manual/Automatic)
- Registration year (e.g., 2018)
- Mileage (km, e.g., 50000)

**Pakistani Car Market Context** (for car-related queries):
- Economy segment: Under 20 Lacs
- Mid-Range: 20-40 Lacs
- Premium: 40-70 Lacs
- Luxury: Above 70 Lacs
- Popular brands: Toyota (holds value best), Honda, Suzuki (affordable)
- Cities: Karachi/Lahore have more demand, better resale
- Depreciation: ~15-20% per year for first 5 years

**REMEMBER**: Your primary role is to be a fun, engaging conversationalist about ANY topic with RANDOM, VARIED responses!
"""
        
        self.steps = [
            'car_brand', 'car_model', 'city', 'fuel_type',
            'engine', 'transmission', 'registered_in', 'mileage'
        ]
    
    def create_session(self, session_id):
        """Create new chat session"""
        self.sessions[session_id] = {
            'step': 0,
            'data': {},
            'collecting': False,
            'history': [],
            'started': datetime.now()
        }
    
    def get_session(self, session_id):
        """Get or create session"""
        if session_id not in self.sessions:
            self.create_session(session_id)
        return self.sessions[session_id]
    
    def detect_prediction_intent(self, message):
        """Check if user wants to predict price - must be explicit about car/price"""
        message_lower = message.lower()
        
        # Explicit car price keywords (must be combined with car/price context)
        car_price_keywords = [
            'predict price', 'price predict', 'car price', 'price of car', 'car ki price',
            'kitni price', 'price kitni', 'car value', 'value of car', 'car worth',
            'estimate price', 'price estimate', 'check price', 'price check',
            'car ki qeemat', 'qeemat', 'car price batao', 'price batao', 'car price bata',
            'meri car ki price', 'car price kya', 'price kya hai', 'car ka price'
        ]
        
        # Check for explicit car price intent
        for keyword in car_price_keywords:
            if keyword in message_lower:
                return True
        
        # Also check if message contains both car-related AND price-related words
        car_words = ['car', 'gari', 'vehicle', 'automobile']
        price_words = ['price', 'value', 'worth', 'qeemat', 'kitni', 'estimate']
        
        has_car_word = any(word in message_lower for word in car_words)
        has_price_word = any(word in message_lower for word in price_words)
        
        # Only trigger if BOTH car and price words are present
        return has_car_word and has_price_word
    
    def extract_car_data(self, message, current_step):
        """Extract car information from natural language"""
        message = message.lower().strip()
        
        if current_step == 'car_brand':
            brands = ['honda', 'toyota', 'suzuki', 'daihatsu', 'nissan', 'mitsubishi', 'hyundai', 'kia']
            for brand in brands:
                if brand in message:
                    return brand
        
        elif current_step == 'car_model':
            models = ['civic', 'corolla', 'city', 'cultus', 'swift', 'vitz', 'yaris', 'fit', 'alto', 'mehran', 'bolan']
            for model in models:
                if model in message:
                    return model
        
        elif current_step == 'fuel_type':
            fuels = ['petrol', 'diesel', 'hybrid', 'cng', 'lpg']
            for fuel in fuels:
                if fuel in message:
                    return fuel
        
        elif current_step == 'transmission':
            if 'auto' in message:
                return 'automatic'
            elif 'manual' in message:
                return 'manual'
        
        elif current_step == 'engine':
            numbers = re.findall(r'\d+', message)
            if numbers:
                engine = int(numbers[0])
                if 500 <= engine <= 5000:
                    return str(engine)
        
        elif current_step == 'registered_in':
            numbers = re.findall(r'\b(19|20)\d{2}\b', message)
            if numbers:
                year = int(numbers[0])
                if 1990 <= year <= 2025:
                    return str(year)
        
        elif current_step == 'mileage':
            numbers = re.findall(r'\d+', message.replace(',', ''))
            if numbers:
                mileage = int(numbers[0])
                if 0 <= mileage <= 500000:
                    return str(mileage)
        
        elif current_step == 'city':
            return message
        
        return None
    
    def get_gemini_response(self, session, user_message):
        """Get response from Gemini API using new package"""
        # Always reload API key from environment to ensure it's current
        if not self.api_key or self.api_key == 'your_gemini_api_key_here':
            # Reload from environment
            env_path = os.path.join(os.path.dirname(__file__), '.env')
            load_dotenv(dotenv_path=env_path, override=True)
            self.api_key = os.getenv('GEMINI_API_KEY')
            print(f"🔄 Reloaded API key from environment: {'Found' if self.api_key and len(self.api_key) > 10 else 'Not found'}")
        
        # Validate API key
        if not self.api_key or self.api_key == 'your_gemini_api_key_here' or len(self.api_key) < 10:
            print("❌ Invalid or missing API key")
            return self.get_fallback_response(session, user_message)
        
        # Always try SDK first (more reliable and uses correct model names)
        try:
            if not self.model:
                genai.configure(api_key=self.api_key)
                model_names = [
                    'gemini-2.5-flash',        # Latest
                    'gemini-2.5-pro',
                    'gemini-2.0-flash',
                    'gemini-pro-latest',
                    'gemini-flash-latest',
                    'gemini-1.5-flash-latest',
                    'gemini-1.5-pro-latest',
                    'gemini-1.5-flash',
                    'gemini-1.5-pro',
                    'gemini-pro'
                ]
                for model_name in model_names:
                    try:
                        clean_name = model_name.replace('models/', '')
                        self.model = genai.GenerativeModel(clean_name)
                        self.model_name = clean_name
                        print(f"✅ Gemini SDK initialized with model: {clean_name}")
                        break
                    except Exception as model_err:
                        print(f"   Model {model_name} failed: {str(model_err)[:50]}")
                        continue
            
            if self.model:
                # Build conversation history
                conversation_history = "\n".join([
                    f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
                    for msg in session['history'][-10:]
                ])
                
                # Add context
                context = ""
                if session['collecting']:
                    current_step = self.steps[session['step']]
                    collected = list(session['data'].keys())
                    context = f"\n\nCurrent task: Collecting {current_step}. Already collected: {collected}"
                
                prompt = f"{self.system_prompt}\n\nConversation:\n{conversation_history}\nUser: {user_message}{context}\n\nAssistant:"
                
                # Try with generation config
                try:
                    generation_config = genai.types.GenerationConfig(
                        temperature=0.9,
                        top_p=0.95,
                        top_k=40,
                        max_output_tokens=1024,
                    )
                    response = self.model.generate_content(prompt, generation_config=generation_config)
                except:
                    try:
                        response = self.model.generate_content(prompt, temperature=0.9)
                    except:
                        response = self.model.generate_content(prompt)
                
                return response.text
            else:
                raise Exception("SDK model initialization failed")
        except Exception as sdk_error:
                error_str = str(sdk_error)
                # Check if it's a quota error
                if "429" in error_str or "quota" in error_str.lower() or "ResourceExhausted" in error_str:
                    print(f"⚠️ Quota exceeded. Error: {error_str[:100]}")
                    return "I've reached my daily request limit. Please try again tomorrow, or upgrade your API plan for more requests. 😊"
                elif "403" in error_str or "permission" in error_str.lower():
                    print(f"❌ Permission error: {error_str[:100]}")
                    return "I'm having trouble with API permissions. Please check your GEMINI_API_KEY permissions."
                else:
                    print(f"❌ SDK failed: {sdk_error}")
                    # Last resort: try REST API
                    try:
                        print("🔄 Trying REST API as fallback...")
                        return self._get_gemini_response_rest(session, user_message)
                    except Exception as final_error:
                        print(f"❌ All methods failed. Final error: {final_error}")
                        return f"Sorry, I'm having trouble connecting to the AI service. Error: {str(final_error)[:100]}"
    
    def _get_gemini_response_rest(self, session, user_message):
        """Use REST API directly - more reliable than SDK"""
        if not self.api_key:
            raise Exception("No API key available")
        
        # Build conversation history
        conversation_history = "\n".join([
            f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
            for msg in session['history'][-10:]
        ])
        
        # Add context
        context = ""
        if session['collecting']:
            current_step = self.steps[session['step']]
            collected = list(session['data'].keys())
            context = f"\n\nCurrent task: Collecting {current_step}. Already collected: {collected}"
        
        prompt = f"{self.system_prompt}\n\nConversation:\n{conversation_history}\nUser: {user_message}{context}\n\nAssistant:"
        
        # Generation config for random/varied responses
        generation_config = {
            "temperature": 0.9,  # High temperature for more randomness
            "topP": 0.95,        # Nucleus sampling
            "topK": 40,          # Top-k sampling
            "maxOutputTokens": 1024,
        }
        
        # Try different API versions and model endpoints
        # Use v1beta first as it's more stable, then v1
        api_versions = ['v1beta', 'v1']
        # Use actual model names that work (from SDK listing)
        # Note: REST API might use different names, so try both with and without models/ prefix
        model_endpoints = [
            'gemini-2.5-flash',        # Latest
            'models/gemini-2.5-flash',
            'gemini-2.5-pro',
            'models/gemini-2.5-pro',
            'gemini-2.0-flash',
            'models/gemini-2.0-flash',
            'gemini-pro-latest',
            'models/gemini-pro-latest',
            'gemini-flash-latest',
            'models/gemini-flash-latest',
            'gemini-1.5-flash-latest',
            'models/gemini-1.5-flash-latest',
            'gemini-1.5-pro-latest',
            'models/gemini-1.5-pro-latest',
            'gemini-1.5-flash',
            'models/gemini-1.5-flash',
            'gemini-1.5-pro',
            'models/gemini-1.5-pro',
            'gemini-pro',
            'models/gemini-pro',
        ]
        
        last_error = None
        for api_version in api_versions:
            for model_name in model_endpoints:
                try:
                    # Try with API key in URL
                    url = f"https://generativelanguage.googleapis.com/{api_version}/models/{model_name}:generateContent?key={self.api_key}"
                    
                    # Prepare request payload
                    payload = {
                        "contents": [{
                            "parts": [{"text": prompt}]
                        }],
                        "generationConfig": generation_config
                    }
                    
                    print(f"🔄 Trying REST API: {api_version}/{model_name}")
                    
                    response = requests.post(
                        url,
                        json=payload,
                        headers={
                            'Content-Type': 'application/json',
                        },
                        timeout=30
                    )
                    
                    if response.status_code == 200:
                        data = response.json()
                        if 'candidates' in data and len(data['candidates']) > 0:
                            if 'content' in data['candidates'][0] and 'parts' in data['candidates'][0]['content']:
                                text = data['candidates'][0]['content']['parts'][0]['text']
                                if text and len(text.strip()) > 0:
                                    print(f"✅ REST API worked with model: {model_name} (API: {api_version})")
                                    return text
                                else:
                                    print(f"   Warning: Empty response from {model_name}")
                                    continue
                            else:
                                print(f"   Warning: Unexpected response structure from {model_name}")
                                continue
                        else:
                            error_msg = data.get('error', {}).get('message', 'Unknown error') if 'error' in data else 'No candidates in response'
                            print(f"   REST API error for {model_name}: {error_msg}")
                            last_error = error_msg
                            continue
                    elif response.status_code == 404:
                        print(f"   Model {model_name} not found (404), trying next...")
                        continue  # Try next model
                    elif response.status_code == 403:
                        error_data = response.json() if response.text else {}
                        error_msg = error_data.get('error', {}).get('message', 'Permission denied')
                        print(f"   Permission error for {model_name}: {error_msg}")
                        last_error = f"Permission denied: {error_msg}"
                        # Don't continue - permission errors won't be fixed by trying other models
                        break
                    else:
                        error_text = response.text[:500] if response.text else "No error message"
                        print(f"   REST API error {response.status_code} for {model_name}: {error_text[:200]}")
                        last_error = f"HTTP {response.status_code}: {error_text[:100]}"
                        continue
                        
                except requests.exceptions.Timeout:
                    print(f"   Timeout for {model_name}, trying next...")
                    last_error = "Request timeout"
                    continue
                except requests.exceptions.RequestException as e:
                    print(f"   Request error for {model_name}: {str(e)[:100]}")
                    last_error = str(e)
                    continue
                except Exception as e:
                    print(f"   Unexpected error for {model_name}: {str(e)[:100]}")
                    last_error = str(e)
                    continue
        
        # If we get here, all models failed
        error_message = f"All REST API endpoints failed. Last error: {last_error}" if last_error else "All REST API endpoints failed"
        raise Exception(error_message)
    
    def get_fallback_response(self, session, message):
        """Fallback - only used when API key is missing or invalid"""
        # Only use hardcoded fallback if API key is truly missing/invalid
        if not self.api_key or self.api_key == 'your_gemini_api_key_here' or len(self.api_key) < 10:
            if self.detect_prediction_intent(message):
                fallback_responses = [
                    "Sure! I can help you predict the car price. Let's start - what's the car brand? (e.g., Honda, Toyota, Suzuki)",
                    "Great! Let's predict your car's price. First, tell me the brand - Honda, Toyota, Suzuki, or another?",
                    "Awesome! I'll help you estimate the car price. What brand is it? (Honda, Toyota, Suzuki, etc.)"
                ]
                return fallback_responses[len(session['history']) % len(fallback_responses)]

            # General conversational fallback with variety
            general_responses = [
                "I'm here to chat about anything! Ask me about cars, technology, sports, movies, or anything else. What would you like to talk about? 😊",
                "Feel free to ask me anything - from car prices to current events, movies, music, or just casual chat! What's on your mind? 🚗💬",
                "I'm your friendly AI assistant! We can talk about Pakistani cars, global news, entertainment, sports, or whatever interests you. What shall we discuss? 🌟",
                "Hey there! I'm ready to chat about cars, tech, sports, movies, or anything else. What interests you today? 🎯",
                "Hello! I'm here to help with car prices or just have a friendly chat. What would you like to know? 💭"
            ]
            return general_responses[len(session['history']) % len(general_responses)]
        else:
            # If we have a valid API key but still reached fallback, something is wrong
            return "I'm having trouble connecting to the AI service. Please check your GEMINI_API_KEY in the .env file and ensure it's valid. If the problem persists, please try again in a moment."
    
    def process_message(self, session_id, message, model_info=None):
        """Process user message with Gemini AI - handles ANY topic with random responses"""
        session = self.get_session(session_id)
        
        # Add to history
        session['history'].append({
            'role': 'user',
            'content': message,
            'timestamp': datetime.now().isoformat()
        })
        
        # Check if user wants to predict (only if explicitly about car prices)
        if not session['collecting'] and self.detect_prediction_intent(message):
            session['collecting'] = True
            session['step'] = 0
            session['data'] = {}
            # Use Gemini to generate a varied response for starting prediction
            reply = self.get_gemini_response(session, f"User wants to predict car price. Start collecting car details. First ask about car brand in a creative, varied way.")
        
        # If user is collecting data but asks about something else, reset and chat normally
        elif session['collecting'] and not self.detect_prediction_intent(message) and session['step'] < len(self.steps):
            # If message is clearly NOT about cars or doesn't contain car-related info, reset and chat about the new topic
            non_car_keywords = ['movie', 'film', 'sport', 'cricket', 'football', 'music', 'song', 'news', 'weather', 'technology', 'tech', 'ai', 'food', 'cooking', 'book', 'travel', 'joke', 'fun', 'tell me', 'what is', 'how', 'why', 'explain', 'who', 'when', 'where', 'story', 'joke', 'fact', 'help', 'advice', 'recommend', 'suggest']
            car_keywords = ['car', 'gari', 'vehicle', 'brand', 'model', 'engine', 'mileage', 'transmission', 'fuel', 'honda', 'toyota', 'suzuki']
            
            # If message has non-car keywords OR doesn't have car keywords, treat as general conversation
            has_non_car = any(kw in message.lower() for kw in non_car_keywords)
            has_car = any(kw in message.lower() for kw in car_keywords)
            
            if has_non_car or (not has_car and len(message.split()) > 2):
                # User wants to talk about something else, reset collection and use Gemini
                session['collecting'] = False
                session['step'] = 0
                session['data'] = {}
                reply = self.get_gemini_response(session, message)
            else:
                # Continue collecting car data
                current_step = self.steps[session['step']]
                extracted_value = self.extract_car_data(message, current_step)
                
                if extracted_value:
                    session['data'][current_step] = extracted_value
                    session['step'] += 1
                    
                    # Check if done
                    if session['step'] >= len(self.steps):
                        session['collecting'] = False
                        reply = "Perfect! I have all the details. Let me calculate the price... 💰"
                        action = 'predict'
                        
                        session['history'].append({
                            'role': 'assistant',
                            'content': reply,
                            'timestamp': datetime.now().isoformat()
                        })
                        
                        return {
                            'reply': reply,
                            'action': action,
                            'data': session['data']
                        }
                    
                    # Use Gemini to ask next question in a varied way
                    next_step = self.steps[session['step']]
                    step_prompts = {
                        'car_model': 'Ask about car model in a creative, varied way',
                        'city': 'Ask about city in a creative, varied way',
                        'fuel_type': 'Ask about fuel type in a creative, varied way',
                        'engine': 'Ask about engine capacity in a creative, varied way',
                        'transmission': 'Ask about transmission type in a creative, varied way',
                        'registered_in': 'Ask about registration year in a creative, varied way',
                        'mileage': 'Ask about mileage in a creative, varied way'
                    }
                    prompt_for_gemini = step_prompts.get(next_step, 'Ask the next question')
                    reply = self.get_gemini_response(session, prompt_for_gemini)
                else:
                    # Couldn't extract, use Gemini to handle the response
                    reply = self.get_gemini_response(session, message)
        
        # Normal conversation - ALWAYS use Gemini for ANY topic with random responses
        else:
            reply = self.get_gemini_response(session, message)
        
        # Add assistant reply to history
        session['history'].append({
            'role': 'assistant',
            'content': reply,
            'timestamp': datetime.now().isoformat()
        })
        
        return {
            'reply': reply,
            'action': None
        }


# Initialize chatbot
chatbot = GeminiChatbot()