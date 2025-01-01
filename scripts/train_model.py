from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
from sklearn.metrics import accuracy_score, precision_recall_fscore_support

# Load pre-trained model
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=4)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=10,
    num_train_epochs=180,
    weight_decay=0.01,
    logging_dir="./logs",  # Répertoire pour les journaux
    logging_steps=10,      # Journaliser toutes les 10 étapes
    report_to="none"       # Désactiver les intégrations externes comme W&B
)


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = logits.argmax(axis=-1)  # Obtenir la classe prédite
    
    # Calcul des métriques
    accuracy = accuracy_score(labels, predictions)
    precision, recall, f1, _ = precision_recall_fscore_support(labels, predictions, average="weighted")
    
    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics  # Ajout de la fonction de calcul des métriques
)


# Train the model
trainer.train()
# Save model
model.save_pretrained("./trained_model")
tokenizer.save_pretrained("./trained_model")

# Load and test
from transformers import pipeline

classifier = pipeline("text-classification", model="./trained_model", tokenizer=tokenizer)
test_text = "This study evaluates the efficacy of saline solutions for outpatient procedures."
result = classifier(test_text)
print(result)
