import os
import google.genai as genai
from dotenv import load_dotenv
load_dotenv()




class BaseModelResponse:

  def get_model(self):

    try:
        GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
        client = genai.Client(api_key=GEMINI_API_KEY)
        return client

    except Exception as e:
        print(f"An error occurred: {e}")


class AppFeature(BaseModelResponse):

    def __init__(self):
        self.__database = {}
        self.first_menu()

    def first_menu(self):
        first_input = input("""
        Please choose an option:
           1. Not a member? Sign up
           2. Already a member? Log in
           3. Exit
        Your choice: """)
        if first_input == "1":
            self.__sign_up()
        elif first_input == "2":
            self.__log_in()
            self.second_menu()
        elif first_input == "3":
            self.exit_menu()
        else:
            print("Invalid option. Please try again.")

    def second_menu(self):
        second_input = input("""
        Please choose an option:
           1. Sentiment Analysis
           2. Language Translation
           3. Text Summarization
           4. Text Generation
           5. Text Classification
           6. Text Extraction
           7. Topic Modeling
           8. Named Entity Recognition
           9. Language Detection
        Your choice: """)
        if second_input == "1":
            self.sentiment_analysis() # Call sentiment analysis function
        elif second_input == "2":
            self.language_translation()  # Call language translation function
        elif second_input == "3":
            self.text_summarization()  # Call text summarization function
        elif second_input == "4":
            self.text_generation()  # Call text generation function
        elif second_input == "5":
            self.text_classification()  # Call text classification function
        elif second_input == "6":
            self.text_extraction()  # Call text extraction function
        elif second_input == "7":
            self.topic_modeling()  # Call topic modeling function
        elif second_input == "8":
            self.named_entity_recognition()  # Call named entity recognition function
        elif second_input == "9":
            self.language_detection()  # Call language detection function
        
        else:
            print("Invalid option. Please try again.")
        
    def __sign_up(self):
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            email = input("Enter your email: ")

            if username in self.__database:
                print("Username already exists. Please try a different one.")
                return
            else:
                self.__database[username] = {"password": password, "email": email}
                print("Sign up successful! You can now log in.")
                self.first_menu()


    def __log_in(self):
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in self.__database:
                if self.__database[username]["password"] == password:
                    print("Log in successful!")
                    # Proceed to the main application
                else:
                    print("Invalid password. Please try again.")
            else:
                print("User not found. Please sign up.")


    def sentiment_analysis(self):
        client = self.get_model()
        user_input = input("Enter text for sentiment analysis: ")

        prompt = f"""
    Analyze the sentiment of the following text.
    Respond only with one word: Positive, Negative, or Neutral.

    Text: {user_input}
    """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("Sentiment Analysis Result:")
        print(response.text.strip())
        self.second_menu()

    

    
    def language_translation(self):
        client = self.get_model()
        user_input = input("Enter text to translate: ")
        target_language = input("Enter target language (e.g., French, Spanish): ")

        prompt = f"""
    Translate the following text into {target_language}.
    Only provide the translated text.

    Text: {user_input}
    """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("Translation Result:")
        print(response.text.strip())
        self.second_menu()


    def text_summarization(self):
        client = self.get_model()
        user_input = input("Enter text to summarize: ")

        prompt = f"""
    Summarize the following text.
    Respond with a concise summary.

    Text: {user_input}
    """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("Summarization Result:")
        print(response.text.strip())
        self.second_menu()

    def text_generation(self):
        client = self.get_model()
        user_input = input("Enter a prompt for text generation: ")

        prompt = f"""
    Generate text based on the following prompt.

    Prompt: {user_input}
    """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("Text Generation Result:")
        print(response.text.strip())
        self.second_menu()

    def text_classification(self):
        client = self.get_model()
        user_input = input("Enter text for classification: ")

        prompt = f"""
    Classify the following text into predefined categories.
    Respond only with the category label.

    Text: {user_input}
    """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("Text Classification Result:")
        print(response.text.strip())
        self.second_menu()
    
    def text_extraction(self):
        client = self.get_model()
        user_input = input("Enter text for information extraction: ")

        prompt = f"""
    Extract key information from the following text.
    Respond only with the extracted information.

    Text: {user_input}
    """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("Text Extraction Result:")
        print(response.text.strip())   
        self.second_menu()

    def topic_modeling(self):
        client = self.get_model()
        user_input = input("Enter text for topic modeling: ")

        prompt = f"""
    Identify the main topics in the following text.
    Respond only with the identified topics.

    Text: {user_input}
    """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("Topic Modeling Result:")
        print(response.text.strip())
        self.second_menu()

    def named_entity_recognition(self):
        client = self.get_model()
        user_input = input("Enter text for named entity recognition: ")

        prompt = f"""
    Identify and classify the named entities in the following text.
    Respond only with the identified entities and their categories.

    Text: {user_input}
    """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("Named Entity Recognition Result:")
        print(response.text.strip())
        self.second_menu()

    def language_detection(self):
        client = self.get_model()
        user_input = input("Enter text for language detection: ")

        prompt = f"""
    Detect the language of the following text.
    Respond only with the language name.

    Text: {user_input}
    """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        print("Language Detection Result:")
        print(response.text.strip())
        self.second_menu()


app = AppFeature()

