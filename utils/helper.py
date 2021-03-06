import librosa
import numpy as np
import youtube_dl
from tensorflow.keras import models
import streamlit as st
from pydub import AudioSegment

from utils import my_variables


##### STREAMLIT #######

@st.cache
def load_model(model_path):
    return models.load_model(model_path)


# @st.cache
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in my_variables.allowed_extensions


@st.cache
def get_song(file):
    try:
        try:
            return AudioSegment.from_mp3(file).set_channels(1)
        except:
            return AudioSegment.from_wav(file)
    except:
        return None


def display_expander_and_explanation():
    b, col, bu = st.columns((1, 4, 1))
    my_expander = col.expander('Tell me more...')
    with my_expander:
        st.markdown("<h3 style='text-align: center; color: #deb887;'>What are spectrograms?</h3>",
                    unsafe_allow_html=True)
        st.markdown(my_variables.about_this_app_part_one, unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #deb887;'>Plotting and genre classifying</h3>",
                    unsafe_allow_html=True)
        st.markdown(my_variables.about_this_app_part_two, unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #deb887;'>The vertical axis</h3>",
                    unsafe_allow_html=True)
        st.markdown(my_variables.about_this_app_part_three, unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #deb887;'>Distinguishing sounds visually</h3>",
                    unsafe_allow_html=True)
        st.markdown(my_variables.about_this_app_part_four, unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #deb887;'>Enjoy some melodious plots</h3>",
                    unsafe_allow_html=True)

    buf, col0, buff, col1, buffer = st.columns((2, 3, 1, 3, 2))
    col0.image('visuals/acousticguitar.png', caption='acoustic guitar')
    col1.image('visuals/trumpet.png', caption='trumpet')


@st.cache
def get_librosa_input(signal, hop_length=1024):
    return librosa.amplitude_to_db(np.abs(librosa.stft(signal, hop_length=hop_length)), ref=np.max)


def show_y_slider(y_ax_choice, column):
    if y_ax_choice == 'log':
        y_min, y_max = column.slider('zoom frequency axis', min_value=0, max_value=8193, value=(0, 8192))
    else:
        y_min, y_max = column.slider('zoom frequency axis', min_value=0, max_value=10000, value=(0, 10000))
    return y_min, y_max


def show_x_slider(column, signal):
    max = int(librosa.get_duration(signal) / 2)
    x_min, x_max = column.slider('zoom time axis', min_value=0,
                                 max_value=max, value=(0, max))
    return x_min, x_max


###### SPECTROGRAM ######
def to_melspectrogram(songs, n_fft=1024, hop_length=256):
    # Transformation function
    melspec = lambda x: librosa.feature.melspectrogram(x, n_fft=n_fft,
                                                       hop_length=hop_length, n_mels=128)[:, :, np.newaxis]

    # map transformation of input songs to melspectrogram using log-scale
    tsongs = map(melspec, songs)
    # np.array([librosa.power_to_db(s, ref=np.max) for s in list(tsongs)])
    return np.array(list(tsongs))


def splitsongs(X, overlap=0.5):
    # Empty lists to hold our results
    temp_X = []

    # Get the input song array size
    xshape = X.shape[0]
    chunk = 33000
    offset = int(chunk * (1. - overlap))

    # Split the song and create new ones on windows
    spsong = [X[i: i + chunk] for i in range(0, xshape - chunk + offset, offset)]
    for s in spsong:
        if s.shape[0] != chunk:
            continue

        temp_X.append(s)

    return np.array(temp_X)


def majority_voting(scores, dict_genres):
    preds = np.argmax(scores, axis=1)
    values, counts = np.unique(preds, return_counts=True)
    counts = np.round(counts / np.sum(counts), 2)
    votes = {k: v for k, v in zip(values, counts)}
    votes = {k: v for k, v in sorted(votes.items(), key=lambda item: item[1], reverse=True)}
    return [(get_genres(x, dict_genres), prob) for x, prob in votes.items()]


def get_genres(key, dict_genres):
    # Transforming data to help on transformation
    # labels = []
    tmp_genre = {v: k for k, v in dict_genres.items()}
    return tmp_genre[key]


#### PREDICTING
def get_values_and_labels(votes):
    labels, values = [], []
    for pair in votes:
        values.append(pair[1])
        labels.append(pair[0])
    return labels, values


def predict_song_genre(signal, model):
    signals = splitsongs(signal)
    specs = to_melspectrogram(signals)
    preds = model.predict(specs)
    return majority_voting(preds, my_variables.genres)


#### EXTRACT AUDIO
def get_signal_from_song(example_choice):
    if example_choice == 'trumpet':
        song = 'audio/trumpet_melody.wav'
        signal, _ = librosa.load(song, 44100)
    elif example_choice == 'acoustic guitar':
        song = 'audio/oasis_acoustic.wav'
        signal, _ = librosa.load(song, 44100)
    elif example_choice == 'nightingale':
        song = 'audio/nightingale.mp3'
        signal, _ = librosa.load(song, 44100)
        # song = librosa.ex(example_choice)
        # signal, _ = librosa.load(song, 44100, duration=45.0)
    elif example_choice == 'accordeon':
        song = 'audio/accordeon.wav'
        signal, _ = librosa.load(song, 44100)
    elif example_choice == 'electric guitar':
        song = 'audio/electricalguitar.wav'
        signal, _ = librosa.load(song, 44100)
    elif example_choice == 'harmonica':
        song = 'audio/harmonica.wav'
        signal, _ = librosa.load(song, 44100)
    elif example_choice == 'pure tone (e)':
        song = 'audio/pure_e.wav'
        signal, _ = librosa.load(song, 44100)
    elif example_choice == 'gregorian':
        song = 'audio/gregorian.wav'
        signal, _ = librosa.load(song, 44100)
    elif example_choice == 'xylophone':
        song = 'audio/xylophone.wav'
        signal, _ = librosa.load(song, 44100)
    elif example_choice == 'saxophone':
        song = 'audio/sax.wav'
        signal, _ = librosa.load(song, 44100)
    elif example_choice == 'clair de lune':
        song = 'audio/debussy_clairdelune.mp3'
        signal, _ = librosa.load(song, 44100, duration=45.0)
    elif example_choice == 'mozart':
        song = 'audio/mozart_rondaallaturca.mp3'
        signal, _ = librosa.load(song, 44100, duration=45.0)
    elif example_choice == 'electropop song':
        song = 'audio/electropop.mp3'
        signal, _ = librosa.load(song, 44100, duration=45.0)
    elif example_choice == 'jazz song':
        song = 'audio/jazzsong.mp3'
        signal, _ = librosa.load(song, 44100, duration=45.0)
    else:
        song, signal = None, None

    return song, signal


def take_first_part_of_songs(song, seconds):
    start_seconds = seconds * 1000  # 1000ms = 1s
    return song[:start_seconds]


def define_column_widths():
    return st.columns((2, 0.25, 5, 4))


def define_column_zero():
    return st.columns((2, 3, 2))


def download_from_youtube(url):
    ydl_opts = {
        'format': 'worstaudio/worst',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '100',
        }],
        # 'outtmpl': 'down/%(title)s.%(ext)s'
        # 'outtmpl': '%(title)s.%(ext)s'
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except:
        st.markdown(my_variables.error_message_four, unsafe_allow_html=True)
        return False


@st.cache
def get_filesize(link):
    ydl_opts = {
        'format': 'worstaudio/worst',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '100',
        }],
        'outtmpl': 'down/%(title)s.%(ext)s'
    }
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            return info_dict['filesize'], info_dict['title']
    except:
        return None, None
