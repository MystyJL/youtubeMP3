import dearpygui.dearpygui as dpg
from downloadSong import mp3Convert

dpg.create_context()

# callback functions
def callback(sender, app_data):
    global filepath
    filepath = app_data["file_path_name"]
    dpg.set_value("directory_box",f"Download Directory: {filepath}")

def downloaderCallback():
    dpg.configure_item(item="download", enabled=False)
    dpg.show_item("spinner")
    mp3Convert(video=dpg.get_value("video"),path_for_song=filepath)
    dpg.set_value("video","")
    dpg.hide_item("spinner")
    dpg.configure_item(item="download", enabled=True)

filepath = None
dpg.add_file_dialog(directory_selector=True, show=False, callback=callback, tag="file_dialog_id", width=600 ,height=300, modal=True)
# main window
with dpg.window(tag="Primary Window"):
    dpg.add_text("Download Directory: None",tag="directory_box")
    dpg.add_button(label="Directory Selector", callback=lambda: dpg.show_item("file_dialog_id"))
    dpg.add_spacer(height=50)
    dpg.add_input_text(label="link", tag="video")
    dpg.add_button(label="download", callback=downloaderCallback, tag="download")
    dpg.add_loading_indicator(show=False, tag="spinner")



dpg.create_viewport(title='Youtube to MP3', width=700, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()