from textblob import TextBlob
import colorama 
from colorama import Fore, Back, Style
import sys
import time
username =""
conversation_history=[]
positivecount=0
negative_count=0
neutralcount=0 
def show_processing_ammunation () :
    print (f"{Fore.CYAN}","detection sentiment clues",end="")
    for _ in range (3):
        time.sleep (0.5)
        print (".",end="")
        sys.stdout.flush()
def analyze_sentiment (text):
    try: 
        global positivecount,negative_count,mutualcount 
        blob=TextBlob (text)
        sentiment=blob.sentiment.polarity
        conversation_history.append (text)
        if sentiment > 0.75:
            positivecount+=1
            return f"\n{Fore.GREEN}very positive sentiments"
        elif 0.25 < sentiment  <= 0.75:
            positivecount+=1
            return f"\n{Fore.GREEN}positive sentiments"
        elif -0.25 <=sentiment <=0.25:
            neutralcount+=1
            return f"\n {Fore.YELLOW}neutral sentiment"
        elif -0.75 <=sentiment <= 0.25:
            negative_count+=1 
            return f"\n{Fore.RED}negative sentiments"
        else:
            negative_count+=1 
            return "\n{Fore.RED} very negative sentiments" 
    except Exception as e :
        return f"{Fore.RED}an error occured during sentiment analysis"