genres = {
    'blues': 0, 'classical': 1, 'country': 2, 'disco': 3, 'hiphop': 4,
    'jazz': 5, 'metal': 6, 'pop': 7, 'reggae': 8, 'rock': 9
}

options_radio = ['About spectrograms', 'Upload a mp3 or wav file', 'Choose a preloaded sound', 'Paste a YouTube link']

y_ax_dict = {'log frequency': 'log', 'linear frequency': 'linear'}

colormap_dict = {
    'copper': 'copper', 'black & white': 'gray_r', 'white & black': 'gray', 'blues': 'Blues',
    'orange & purple': 'CMRmap', 'dark yellow green blue': 'YlGnBu_r', 'ocean': 'ocean_r',
    'sunset': 'plasma', 'blue yellow red': 'gist_stern', 'bright': 'jet'
}

list_librosa_examples = ['No sound selected', 'acoustic guitar', 'trumpet', 'nightingale',
                         'accordeon', 'electric guitar', 'harmonica', 'pure tone (e)',
                         'gregorian', 'xylophone', 'saxophone', 'clair de lune',
                         'mozart', 'electropop song', 'jazz song']

error_message_one = "<p style='text-align: center; color: #D33682; font-size: 15px;'>" \
                    "Sorry, but only mp3 or wav files are accepted</p>"

error_message_two = "<p style='text-align: center; color: #D33682; font-size: 15px;'> " \
                    "Woops, we do not seem to be able to read that file. Sorry about that. <br>" \
                    "Is it a valid mp3 or wav file? </p>"

error_message_three = "<p style='text-align: center; color: #D33682; font-size: 15px;'> " \
                      "Wow, that is a big file you've linked there. <br>" \
                      "Unfortunately we only accept files up to 15MB. <br>" \
                      "Could you try again with a shorter song, please? </p>"

error_message_four = "<p style='text-align: center; color: #D33682; font-size: 15px;'> " \
                     "Woops, something went wrong. Sorry for the inconvenience </p> "

error_message_five = "<p style='text-align: center; color: #D33682; font-size: 15px;'> " \
                     "We have trouble reading some YouTube-formats. <br>" \
                     "What could help is to trim down your YouTube-link to the following format:<br>" \
                     "     https://www.youtube.com/watch?v=tSv04ylc6To <br>" \
                     "<br>" \
                     "If that doesn't help, then we are sorry for the inconvenience." \
                     " May we invite you to take a look at some of the example sounds" \
                     " preloaded in the app?"

error_message_six = "<p style='text-align: center; color: #D33682; font-size: 15px;'> " \
                    "That does not seem to be a valid YouTube link. </p> "

about_this_app_part_one = "<p style='text-align: center; color:white; font-size: 15px;'> " \
                          "Spectrograms are melodious plots.<br> They make sound visible. <br><br> " \
                          "They do not only look fascinating. <br> They are also used in practical" \
                          " applications like speech and animal sound recognition, or music analysis." \
                          " </p>"

about_this_app_part_two = "<p style='text-align: center; color:white; font-size: 15px;'> " \
                          "This app shows you the spectrogram of input sounds.<br>" \
                          " Based upon that spectrogram, the app also makes a prediction on the genre" \
                          " of the input sound. <br> And does so correctly in 72% of the cases. <br>" \
                          "Be sure to give it a try. </p>"

about_this_app_part_three = "<p style='text-align: center; color:white; font-size: 15px;'> " \
                            "You can choose if you want to plot the y-axis on a linear or a logarithmic scale.<br>" \
                            "One: human hearing responds logarithmically to sound instead of linear. <br>" \
                            "Two: switching between linear of logarithmic " \
                            "can improve the readability (and beauty) of a spectrogram. " \
                            "</p>"

about_this_app_part_four = "<p style='text-align: center; color:white; font-size: 15px;'> " \
                           "Spectrograms show the different characteristics in sounds. <br>" \
                           "When using simple audio signals, it is easy for the human eye to distinguish between different types of music.<br> " \
                           "Take a look at the differences in the spectrograms below. <br>" \
                           "The guitar has a vertical pattern, the trumpet a horizontal one. <br>" \
                           "The guitar is more likely to be classified as country, the trumpet as jazz. <br>" \
                           "</p>"

show_hyperlinks = "<a style='display:inline;margin:0 0 0 72%;font-size:11px;color: #deb887;;' " \
                  "href='https://www.linkedin.com/in/maartenvdbulcke-gent'>LinkedIn</a>" \
                  "<a style='display:inline;margin:0 0 0 1%;font-size:11px;color: #deb887;' " \
                  "href='https://github.com/MaartenVdBulcke/some-melodious-plots'>GitHub</a>"
