import librosa.display
import streamlit as st
import gc
import glob
import validators


from utils import helper, plot_and_predict, my_variables

# set-up streamlit layout
st.set_page_config(page_title="to disco", layout="wide")
hide_st_style = """ <style> footer {visibility: hidden;} </style> """
st.markdown(hide_st_style, unsafe_allow_html=True)

if 'latest_link' not in st.session_state:
    st.session_state.latest_link = None

model = helper.load_model('custom_cnn_2d.h5')  # load keras model

st.markdown("<h1 style='text-align: center; color: white;'>TO DISCO OR NOT TO DISCO</h3>", unsafe_allow_html=True)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center}</style>',
         unsafe_allow_html=True)

sound_choice = st.radio('', my_variables.options_radio)

if sound_choice == my_variables.options_radio[0]:
    buf, col0, buff = helper.define_column_zero()
    uploaded_file = col0.file_uploader('Only .mp3 or .wav files are accepted')
    col1, buffer, col2, col3 = helper.define_column_widths()

    if uploaded_file is not None:
        upload_name = uploaded_file.name

        if not helper.allowed_file(upload_name):
            st.markdown(my_variables.error_message_one, unsafe_allow_html=True)
        else:
            song = helper.get_song(uploaded_file)
            if song is None:
                st.markdown(my_variables.error_message_two, unsafe_allow_html=True)
            else:
                col0.audio(uploaded_file)  # option to play the example audio
                col1.markdown("<h3 style='text-align: center; color: white;'>CUSTOMIZE</h3>", unsafe_allow_html=True)
                uploaded_file.close()  # delete buffered upload data
                song_beginnings = helper.take_first_part_of_songs(song, 45)
                file_au = song_beginnings.export(format='au')
                signal, _ = librosa.load(file_au, sr=None)
                librosa_input = helper.get_librosa_input(signal)
                plot_and_predict.predict_genre_show_plots(librosa_input, signal, model, col1, col2, col3)

elif sound_choice == my_variables.options_radio[1]:
    buf, col0, buff = helper.define_column_zero()
    example_choice = col0.selectbox('Your example sound:', my_variables.list_librosa_examples)
    col1, buffer, col2, col3 = helper.define_column_widths()
    if example_choice == my_variables.list_librosa_examples[0]:
        pass
    else:
        song, signal = helper.get_signal_from_song(example_choice)
        col0.audio(song)  # option to play the example audio
        librosa_input = helper.get_librosa_input(signal)
        col1.markdown("<h3 style='text-align: center; color: white;'>CUSTOMIZE</h3>", unsafe_allow_html=True)
        plot_and_predict.predict_genre_show_plots(librosa_input, signal, model, col1, col2, col3)

###################### YOUTUBE ########################

elif sound_choice == my_variables.options_radio[2]:
#
    buf, col0, buff = helper.define_column_zero()
#
    provided_link = col0.text_input('Accepted formats: www.youtube.com/watch?v=xxxxxxxxx, '
                                    'https://youtu.be/xxxxxxxxxx', 'Paste your valid link here: https://...')

    if validators.url(provided_link) and 'youtu' in provided_link.lower():
        if 'list' in provided_link.lower():
            col0.write('We have trouble with this list-format. Please choose a shorter youtube url')
        else:
        #     if st.session_state.latest_link != provided_link:
            #     if st.session_state is not None:
            #         folder = 'down'
            #         files_in_directory = os.listdir(folder)
            #         filtered_files = [file for file in files_in_directory if file.endswith(".mp3")]
            #         for file in filtered_files:
            #             path_to_file = os.path.join(folder, file)
            #             os.remove(path_to_file)
                    # st.markdown("<p style='text-align: center; color: #D33682; font-size: 15px;'> " \
                    #           "We get here, and now.</p>",
                    #             unsafe_allow_html=True)
            filesize, artist_title = helper.get_filesize(provided_link)

            if filesize > 10000000:  # 10MB
                size_mb = round(int(filesize) / 1000000, 1)
                col0.markdown(f"<p style='text-align: center; color: #D33682; font-size: 15px;'>filesize: {size_mb}MB</p>",
                          unsafe_allow_html=True)
                st.markdown(my_variables.error_message_three, unsafe_allow_html=True)
            else:
                helper.download_from_youtube(provided_link)
                buf, col0, buff = helper.define_column_zero()
                col1, buffer, col2, col3 = helper.define_column_widths()

                audio = None
                for audio in glob.glob('down/*.mp3'):
                    if audio is not None:
                        col0.audio(audio)
                        col0.markdown(artist_title)

                        if not helper.allowed_file(audio):
                            st.markdown(my_variables.error_message_one, unsafe_allow_html=True)
                        else:
                            song = helper.get_song(audio)
                            if song is None:
                                st.markdown(my_variables.error_message_two, unsafe_allow_html=True)
                            else:
                                col1.markdown("<h3 style='text-align: center; color: white;'>CUSTOMIZE</h3>",
                                          unsafe_allow_html=True)
                                song_beginnings = helper.take_first_part_of_songs(song, 45)
                                file_au = song_beginnings.export(format='au')
                                signal, _ = librosa.load(file_au, sr=None)
                                librosa_input = helper.get_librosa_input(signal)
                                plot_and_predict.predict_genre_show_plots(librosa_input, signal, model, col1, col2, col3)

                st.session_state.latest_link = provided_link

gc.collect()  # clean up
