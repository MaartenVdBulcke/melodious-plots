genres = {
    'blues': 0, 'classical': 1, 'country': 2, 'disco': 3, 'hiphop': 4,
    'jazz': 5, 'metal': 6, 'pop': 7, 'reggae': 8, 'rock': 9
}

options_radio = ['What are spectrograms?', 'Upload a mp3 or wav file', 'Choose a preloaded sound', 'Paste a YouTube link']

# allowed_extensions = ['mp3', 'wav']

sound_choices = ['Make a choice', 'Your own file', 'Choose an example sound']

y_ax_dict = {'log frequency': 'log', 'linear frequency': 'linear'}

colormap_dict = {
    'copper': 'copper', 'black & white': 'gray_r', 'white & black': 'gray', 'blues': 'Blues',
    'orange & purple': 'CMRmap', 'dark yellow green blue': 'YlGnBu_r', 'ocean': 'ocean_r',
    'sunset': 'plasma', 'blue yellow red':'gist_stern', 'bright':'jet'
}

list_librosa_examples = ['None selected', 'brahms', 'acoustic guitar', 'choice', 'fishin', 'nutcracker',
                         'trumpet', 'vibeace']

error_message_one = "<p style='text-align: center; color: #D33682; font-size: 15px;'>" \
                    "Sorry, but only mp3 or wav files are accepted</p>"

error_message_two = "<p style='text-align: center; color: #D33682; font-size: 15px;'> " \
                    "Woops, we do not seem to be able to read that file. Sorry about that. <br>" \
                    "Is it a valid mp3 or wav file? </p>"

error_message_three = "<p style='text-align: center; color: #D33682; font-size: 15px;'> " \
                      "Wow, that is a big file you've linked there. <br>" \
                      "Unfortunately we only accept files up to 10MB. <br>" \
                      "Could you try again with a shorter song, please? </p>"

error_message_four = "<p style='text-align: center; color: #D33682; font-size: 15px;'> " \
                      "We have trouble reading some YouTube-formats. <br>" \
                      "Try simplifying your link in one of the following formats: <br>" \
                      "   * https://www.youtube.com/watch?v=tSv04ylc6To <br> " \
                      "   * https://youtu.be/oz2BZ8uTVsE </p> "

error_message_five = "<p style='text-align: center; color: #D33682; font-size: 15px;'> " \
                      "The app is mainly developed for desktop. It can also work " \
                      "on some mobile devices. <br> Sometimes there are errors while " \
                      "trying to read YouTube audio. Like now. Sorry for that.<br>" \
                      "What should always work is taking a look at the example sounds <br>"\
                      " preloaded in the app </p>"

