import os

import librosa.display
import streamlit as st
import gc
import glob
import validators


from utils import helper, plot_and_predict, my_variables

# set-up streamlit layout
st.set_page_config(page_title="some melodious plots", layout="wide")
hide_st_style = """ <style> footer {visibility: hidden;} </style> """
st.markdown(hide_st_style, unsafe_allow_html=True)

if 'latest_link' not in st.session_state:
    st.session_state.latest_link = None

model = helper.load_model('custom_cnn_2d.h5')  # load keras model

st.markdown("<h1 style='text-align: center; color: white;'>SOME MELODIOUS PLOTS</h3>", unsafe_allow_html=True)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center}</style>',
         unsafe_allow_html=True)

sound_choice = st.radio('', my_variables.options_radio)

if sound_choice == my_variables.options_radio[0]:
    b, col, bu = st.columns((1,4,1))
    my_expander = col.expander('More about spectrograms')
    with my_expander:
        st.markdown("<h3 style='text-align: center; color: #deb887;'>What are spectrograms?</h3>", unsafe_allow_html=True)
        st.markdown(my_variables.about_this_app_part_one, unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #deb887;'>The vertical axis</h3>", unsafe_allow_html=True)
        st.markdown(my_variables.about_this_app_part_two, unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #deb887;'>Distinguishing sounds visually</h3>", unsafe_allow_html=True)
        st.markdown(my_variables.about_this_app_part_three, unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #deb887;'>Enjoy creating some melodious plots</h3>", unsafe_allow_html=True)

    buf, col0, buff, col1, buffer = st.columns((2,3,1,3,2))
    col0.image('visuals/acousticguitar.png', caption='acoustic guitar')
    col1.image('visuals/trumpet.png', caption='trumpet')

elif sound_choice == my_variables.options_radio[1]:
    buf, col0, buff = helper.define_column_zero()
    uploaded_file = col0.file_uploader('')
    col1, buffer, col2, col3 = helper.define_column_widths()

    if uploaded_file is not None:
        upload_name = uploaded_file.name

        # if not helper.allowed_file(upload_name):
        #     st.markdown(my_variables.error_message_one, unsafe_allow_html=True)
        # DELETE THIS OPTION BECAUSE OF FILES WITHOUT EXTENSION

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


elif sound_choice == my_variables.options_radio[2]:
    buf, col0, buff = helper.define_column_zero()
    example_choice = col0.selectbox('', my_variables.list_librosa_examples)
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

elif sound_choice == my_variables.options_radio[3]:
    buf, col0, buff = helper.define_column_zero()

    provided_link = col0.text_input('', 'Paste your valid link here: https://...')

    if validators.url(provided_link) and 'youtu' in provided_link.lower():
        # if 'list' in provided_link.lower():
        #     col0.write('We have trouble with this list-format. Please choose a shorter youtube url')
        # else:
        if st.session_state.latest_link != provided_link:
            if st.session_state is not None:
                filtered_files = [file for file in os.listdir('.') if file.endswith(".mp3")]
                for file in filtered_files:
                    os.remove(file)

        filesize, artist_title = helper.get_filesize(provided_link)
        if filesize is None and artist_title is None:
            st.markdown(my_variables.error_message_five, unsafe_allow_html=True)
        elif filesize > 10000000:  # 10MB
            size_mb = round(int(filesize) / 1000000, 1)
            col0.markdown(f"<p style='text-align: center; color: #D33682; font-size: 15px;'>filesize: {size_mb}MB</p>",
                      unsafe_allow_html=True)
            st.markdown(my_variables.error_message_three, unsafe_allow_html=True)
        else:
            valid = helper.download_from_youtube(provided_link)
            if valid:
                buf, col0, buff = helper.define_column_zero()
                col1, buffer, col2, col3 = helper.define_column_widths()
                audio = None
                for audio in glob.glob('*.mp3'):
                    if audio is not None:
                        col0.audio(audio)
                        col0.markdown(artist_title)

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
    elif provided_link.startswith('Paste'):
        pass
    else:
        st.markdown(my_variables.error_message_six, unsafe_allow_html=True)

gc.collect()  # clean up
