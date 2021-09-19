from matplotlib import pyplot as plt
import librosa.display
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from utils import helper, my_variables


def plot_spectrogram(input_for_librosa, x_min, x_max, y_ax_choice, colormap_choice,
                     y_min, y_max):
    fig, ax = plt.subplots()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    librosa.display.specshow(input_for_librosa, x_axis='time', y_axis=y_ax_choice, cmap=colormap_choice)
    plt.xlim([x_min, x_max])
    plt.ylim([y_min, y_max])
    plt.xlabel('Time [seconds]')
    plt.ylabel('Frequency [Hz]')
    return fig


def plot_prediction_pie(labels, values):
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_traces(
        hoverinfo='label+percent',
        marker=dict(colors=px.colors.qualitative.Set2,
                    line=dict(color='gray', width=1.5)))
    return fig


@st.cache
def plot_pie(votes):
    labels, values = helper.get_values_and_labels(votes)
    return plot_prediction_pie(labels, values)


def get_plot_choices(column, signal):
    colormap_key = column.selectbox('color', my_variables.colormap_dict.keys())
    colormap_choice = my_variables.colormap_dict.get(colormap_key)
    y_ax_key = column.selectbox('linear or logarithmic scale:', my_variables.y_ax_dict.keys())
    y_ax_choice = my_variables.y_ax_dict.get(y_ax_key)
    x_min, x_max = helper.show_x_slider(column, signal)
    y_min, y_max = helper.show_y_slider(y_ax_choice, column)
    return colormap_choice, x_min, x_max, y_ax_choice, y_min, y_max


def plot_spectrogram_title_style(librosa_input, x_min, x_max, y_ax_choice,
                                 colormap_choice, y_min, y_max, column_one, column_two):
    plt.style.use('Solarize_Light2')
    column_two.markdown("<h3 style='text-align: center; color: white;'>SPECTROGRAM</h3>", unsafe_allow_html=True)
    fig = plot_spectrogram(librosa_input, x_min, x_max, y_ax_choice, colormap_choice, y_min, y_max)
    column_two.pyplot(fig)
