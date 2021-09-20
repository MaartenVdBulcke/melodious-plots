from utils import plotting, helper

def predict_genre_show_plots(librosa_input, signal, model, col1, col2, col3):
    colormap_choice, x_min, x_max, y_ax_choice, y_min, y_max = plotting.get_plot_choices(col1, signal)
    plotting.plot_spectrogram_title_style(librosa_input, x_min, x_max, y_ax_choice, colormap_choice,
                                          y_min, y_max, col1, col2)
    votes = helper.predict_song_genre(signal, model)
    col3.markdown("<h3 style='text-align: center; color: white;'>PREDICTION PIE</h3>", unsafe_allow_html=True)
    fig = plotting.plot_pie(votes)
    col3.plotly_chart(fig, use_container_width=True)
