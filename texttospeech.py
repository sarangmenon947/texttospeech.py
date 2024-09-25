import pyttsx3

engine = pyttsx3.init()
engine . say("We are in the month of July 2021")
engine . setProperty ( "rate", 500)
engine . runAndWait ()
