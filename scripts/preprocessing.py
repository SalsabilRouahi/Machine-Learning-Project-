import zipfile
import os

# Spécifiez le chemin vers votre fichier .zip
zip_path = "assignementdataset.zip"
extraction_path = "Data_set"

# Extraction
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_path)

print(f"Fichiers extraits dans : {extraction_path}")
import os
import json
import pandas as pd

# Define categories
categories = {
    "Procedures": 0,
    "Outcomes": 1,
    "Technologies": 2,
    "General Research": 3
}

# Path to extracted JSON files
data_dir = '/content/Data_set/assignementdataset'  # Remplacez par votre chemin de répertoire
data = []

# Fonction pour assigner une catégorie en fonction du titre
def assign_category_based_on_title(title):
    # Mots-clés pour chaque catégorie
    procedures_keywords = ["procedure", "treatment", "method", "surgical", "intervention"]
    outcomes_keywords = ["outcome", "effect", "result", "consequence", "impact"]
    technologies_keywords = ["technology", "diagnostic", "device", "test", "machine"]

    # Assigner la catégorie en fonction de la présence de mots-clés dans le titre
    title_lower = title.lower()
    if any(keyword in title_lower for keyword in procedures_keywords):
        return categories["Procedures"]
    elif any(keyword in title_lower for keyword in outcomes_keywords):
        return categories["Outcomes"]
    elif any(keyword in title_lower for keyword in technologies_keywords):
        return categories["Technologies"]
    else:
        return categories["General Research"]

# Parse JSON files
for file_name in os.listdir(data_dir):
    if file_name.endswith(".json"):
        with open(os.path.join(data_dir, file_name), 'r') as f:
            content = json.load(f)
            title = content.get("title", "")
            abstract = " ".join([item["text"] for item in content.get("pdf_parse", {}).get("abstract", [])])
            body_text = " ".join([item["text"] for item in content.get("pdf_parse", {}).get("body_text", [])])
            text = title + " " + abstract + " " + body_text

            # Assigner la catégorie basée sur le titre
            label = assign_category_based_on_title(title)
            data.append({"text": text, "label": label})

# Convert to DataFrame
df = pd.DataFrame(data)
print(df.head())
from sklearn.model_selection import train_test_split

# Split dataset
train_texts, test_texts = train_test_split(df, test_size=0.2, random_state=42)

print(f"Train size: {len(train_texts)}")
print(f"Test size: {len(test_texts)}")
