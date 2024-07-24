import os

import plotly.graph_objects as go
import streamlit as st
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import pipeline

# Load environment variables from .env file
load_dotenv()


def authenticate():  # noqa: ANN201, D103
    token = os.getenv("HUGGINGFACE_TOKEN")
    if token:
        login(token=token)
    else:
        st.warning(
            "HUGGINGFACE_TOKEN not found in environment variables. Some models may not be accessible."
        )


# Call authenticate at the start of the script
authenticate()


def analyze_sentiment(text: str, model_name: str) -> dict:  # noqa: D417
    """Perform sentiment analysis on the given text using the specified pretrained model.

    Parameters
    ----------
    text (str): The input text to analyze.
    model_name (str): The name of the pretrained model to use for sentiment analysis.

    Returns
    -------
    dict: The result of the sentiment analysis, including the sentiment label and confidence score.

    """
    sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)
    return sentiment_pipeline(text)[0]


def create_gauge_chart(score, sentiment):  # noqa: ANN001, ANN201, D417
    """Create a gauge chart to visualize the sentiment confidence score.

    Parameters
    ----------
    score (float): The confidence score of the sentiment analysis.
    sentiment (str): The sentiment label.

    Returns
    -------
    plotly.graph_objects.Figure: The gauge chart figure.

    """
    return go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=score,
            domain={"x": [0, 1], "y": [0, 1]},
            title={"text": f"Sentiment: {sentiment}"},
            gauge={
                "axis": {"range": [0, 1]},
                "bar": {"color": "darkblue"},
                "steps": [
                    {"range": [0, 0.33], "color": "lightcoral"},
                    {"range": [0.33, 0.67], "color": "lightyellow"},
                    {"range": [0.67, 1], "color": "lightgreen"},
                ],
            },
        )
    )


# Set page config
st.set_page_config(page_title="Sentiment Analysis App", page_icon="😊", layout="wide")


def main():  # noqa: ANN201
    """Main function to run the Streamlit app for sentiment analysis."""  # noqa: D401
    st.title("📊 Sentiment Analysis App")

    # Sidebar
    st.sidebar.header("About")
    st.sidebar.info(
        "This app performs sentiment analysis using pretrained models from Hugging Face. "
        "Enter your text, choose a model, and click 'Analyze' to see the results!"
    )

    st.sidebar.header("Models")
    st.sidebar.markdown(
        """
        - **distilbert-base-uncased-finetuned-sst-2-english**: A lightweight model fine-tuned for sentiment analysis.
        - **roberta-base-go-emotion**: A RoBERTa model trained on the GoEmotions dataset for more nuanced emotion detection.
        """
    )

    # Main content
    col1, col2 = st.columns([2, 1])

    with col1:
        text_input = st.text_area(
            "Enter text for sentiment analysis:",
            "I absolutely love using Streamlit for creating interactive web apps! It's so intuitive and powerful.",
            height=150,
        )

        model_name = st.selectbox(
            "Choose a pretrained model:",
            (
                "distilbert/distilbert-base-uncased-finetuned-sst-2-english",
                "SamLowe/roberta-base-go_emotions",
            ),
        )

        if st.button("Analyze Sentiment"):
            with st.spinner("Analyzing sentiment..."):
                result = analyze_sentiment(text_input, model_name)

            st.success("Analysis complete!")

            sentiment = result["label"]
            score = result["score"]

            st.subheader("Results")
            st.write(f"**Sentiment:** {sentiment}")
            st.write(f"**Confidence:** {score:.4f}")

            # Create and display gauge chart
            fig = create_gauge_chart(score, sentiment)
            st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("How it works")
        st.markdown(
            """
            1. Enter your text in the text area.
            2. Choose a pretrained model from the dropdown.
            3. Click the 'Analyze Sentiment' button.
            4. View the results, including:
                - Detected sentiment
                - Confidence score
                - Visual gauge representation
            """
        )


if __name__ == "__main__":
    main()
