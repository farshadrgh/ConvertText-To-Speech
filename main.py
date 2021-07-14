from playsound import playsound
import gtts

# Make request to google to get synthesis
# Write your text in string
Text = gtts.gTTS("Hello world, this is just a little test for my program, you can write anything you want in this string, and then it becomes into sound")
# Save the audio file
Text.save("The_sound_of_your_text.mp3")
# Play the audio file
playsound("The_sound_of_your_text.mp3")
