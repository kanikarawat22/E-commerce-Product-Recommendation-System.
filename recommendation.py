import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from data import get_purchase_data

class Recommender:
    def __init__(self):
        self.purchase_data = get_purchase_data()
        self.similarity_matrix = None
        self._calculate_similarity()

    def _calculate_similarity(self):
        # Cosine similarity between customers based on purchase history
        self.similarity_matrix = cosine_similarity(self.purchase_data)
        self.similarity_matrix = pd.DataFrame(self.similarity_matrix,
                                              index=self.purchase_data.index,
                                              columns=self.purchase_data.index)

    def recommend(self, customer_id, n_recommendations=2):
        if customer_id not in self.purchase_data.index:
            return f"Customer {customer_id} not found."

        sim_scores = self.similarity_matrix[customer_id].drop(customer_id)

        most_similar_customer = sim_scores.idxmax()

        similar_customer_products = self.purchase_data.loc[most_similar_customer]
        target_customer_products = self.purchase_data.loc[customer_id]

        # Recommend products bought by similar customer but not by target customer
        recommendations = similar_customer_products[(similar_customer_products == 1) & (target_customer_products == 0)]

        return list(recommendations.index)[:n_recommendations]

if __name__ == "__main__":
    rec = Recommender()
    print(rec.recommend('Cust_2'))
