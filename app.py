import streamlit as st
from streamlit_player import st_player

def main():
    st.set_page_config(layout="wide")
    st.text("Live News Channels")
    
    col1, col2, col3 = st.columns(3)

    video_urls = [
        "https://www.youtube.com/embed/O3DPVlynUM0", # Geo
        "https://www.youtube.com/embed/sUKwTVAc0Vo", # ARY
        "https://www.youtube.com/embed/9V1wa4s1oVQ", # 92 News
        "https://www.youtube.com/embed/aNFPcK2vLR8", # Sama News
        "https://www.youtube.com/embed/Mm5S_cSij1o",  # BOL News
        "https://www.youtube.com/embed/4T0MDgV2dKQ", # Capital
        # ... add more URLs here
    ]

    video_url = "https://www.youtube.com/embed/O3DPVlynUM0"
    width = 350
    height = 300

   


    # Iterate over the video URLs and embed them in expandable sections
    for i in range(0, len(video_urls), 3):
        with col1:
            iframe_html = f"""
            <iframe width="{width}" height="{height}" src="{video_urls[i]}" title="YouTube video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            """
            st.write(iframe_html, unsafe_allow_html=True)

        with col2:
            iframe_html = f"""
            <iframe width="{width}" height="{height}" src="{video_urls[i+1]}" title="YouTube video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            """
            st.write(iframe_html, unsafe_allow_html=True)
        with col3:
            iframe_html = f"""
            <iframe width="{width}" height="{height}" src="{video_urls[i+2]}" title="YouTube video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            """
            st.write(iframe_html, unsafe_allow_html=True)




if __name__ == "__main__":
    main()