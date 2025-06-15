from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    _model = None

    @staticmethod
    def get_model():
        if EmbeddingModel._model is None:
            print("Loading embedding model...")
            EmbeddingModel._model = SentenceTransformer("all-MiniLM-L6-v2")
        return EmbeddingModel._model
