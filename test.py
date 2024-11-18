import streamlit as st

def main():
    st.title("YouTube Video")

    video_url = "https://www.youtube.com/embed/O3DPVlynUM0"
    width = 640
    height = 360

    iframe_html = f"""
    <iframe width="{width}" height="{height}" src="{video_url}" title="YouTube video" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    """
    st.write(iframe_html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()