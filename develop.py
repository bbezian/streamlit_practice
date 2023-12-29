import streamlit as st 
import time

if 'photo' not in st.session_state:
    st.session_state['photo']='not done'

col1, col2, col3 = st.columns([1,2,3])

col1.markdown('Hello')
col2.markdown('these are some info')

def change_photo_state():
    st.session_state['photo'] = 'done'

upload_file = col2.file_uploader('upload file', on_change=change_photo_state)
camera_photo = col2.camera_input('Take a photo', on_change=change_photo_state)


if st.session_state['photo'] == 'done':
    progress_bar = col2.progress(0)


    for perc_completed in range(100):
        time.sleep(0.005)
        progress_bar.progress(perc_completed+1)

    col2.success('photo uploaded successfully!')

    col3.metric(label='Temperature', value='60 C', delta='3 C')

    with st.expander('click to read more'):
        st.write('Hello, here are more details')

        if upload_file is None:
            st.image(camera_photo)
        else:
            st.image(upload_file)