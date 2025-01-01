# Projet de Classification des Fichiers JSON dans le Domaine de la Médecine Reproductive

## Introduction

Ce projet consiste à traiter un ensemble de fichiers JSON contenant des articles de recherche médicale et à les classer dans différentes catégories, telles que **Procedures**, **Outcomes**, **Technologies**, et **General Research**. L'objectif principal est d'implémenter un modèle de machine learning (ou deep learning) pour classer ces articles en fonction de leur contenu. Le modèle sera basé sur une analyse du texte des titres, résumés et corps des articles.

## Objectifs

1. **Télécharger et prétraiter le jeu de données** : Télécharger les fichiers JSON contenant des articles médicaux et les préparer pour le traitement.
2. **Implémentation d'un modèle de classification** : Développer un modèle de machine learning ou de deep learning pour effectuer la classification en utilisant les textes extraits des articles.
3. **Évaluation du modèle** : Utiliser des métriques de performance appropriées (précision, rappel, F1-score, etc.) pour évaluer le modèle.
4. **Documentation et présentation** : Documenter le flux de travail et présenter les résultats obtenus à la fin du projet.

## Démarche

### 1. **Prétraitement des Données**

Le projet a débuté par le téléchargement des fichiers JSON contenant les articles de recherche. Chaque fichier JSON contient plusieurs informations, mais nous nous sommes principalement concentrés sur le titre, le résumé (abstract) et le corps du texte de l'article. Le prétraitement a consisté à extraire ces informations pertinentes et à les nettoyer pour qu'elles soient prêtes pour l'analyse. Par exemple, nous avons fusionné les différentes parties du texte (titre, résumé, corps du texte) en un seul bloc de texte pour chaque article.

**Étapes de prétraitement** :
- Extraction des titres, résumés et corps des articles à partir des fichiers JSON.
- Nettoyage du texte (suppression des caractères spéciaux, mise en minuscule, etc.).
- Fusion des informations textuelles en un seul champ (`text`).

### 2. **Catégorisation des Articles**

Une fois le texte extrait et prétraité, l'étape suivante a consisté à assigner une catégorie à chaque article. Nous avons choisi de baser cette classification sur les titres des articles en utilisant des mots-clés spécifiques pour chaque catégorie :

- **Procedures** : Mots-clés comme "procedure", "treatment", "method", "surgical", etc.
- **Outcomes** : Mots-clés comme "outcome", "effect", "result", "impact", etc.
- **Technologies** : Mots-clés comme "technology", "diagnostic", "device", "test", etc.
- **General Research** : Si aucun des mots-clés ci-dessus n'est trouvé, l'article est classé comme recherche générale.

Nous avons implémenté une fonction `assign_category_based_on_title` qui examine le titre de chaque article et lui attribue une catégorie basée sur la présence de mots-clés dans ce titre.

### 3. **Modèle de Machine Learning**

Après avoir préparé et catégorisé les données, nous avons utilisé un modèle de machine learning pour effectuer la classification. Bien que nous n'ayons pas utilisé de deep learning dans cette phase, nous avons exploré l'utilisation de modèles classiques de machine learning tels que **Naive Bayes** et **SVM** pour la classification de texte.

Le processus d'entraînement du modèle a inclus :
- La vectorisation des textes (utilisation de TF-IDF pour transformer le texte en une représentation numérique).
- L'entraînement du modèle sur les données de formation.
- La validation du modèle sur un jeu de test.

### 4. **Évaluation du Modèle**

Pour évaluer la performance du modèle, nous avons utilisé des métriques classiques de classification comme :
- **Précision** : La proportion des prédictions correctes parmi toutes les prédictions.
- **Rappel** : La proportion des articles correctement classés dans chaque catégorie.
- **F1-Score** : La moyenne harmonique de la précision et du rappel, utile lorsque les classes sont déséquilibrées.

### 5. **Résultats et Insights**

Le modèle a été évalué en utilisant un jeu de données de test, et les résultats obtenus ont montré que la classification des articles en fonction de leurs titres était relativement précise. Toutefois, des améliorations peuvent être apportées en utilisant des modèles plus complexes, comme les modèles de deep learning (par exemple, **BERT**) pour une meilleure compréhension du contexte global des articles.

### 6. **Conclusion**

Ce projet a permis d'appliquer des techniques de traitement de texte et de machine learning pour classer des articles de recherche dans le domaine médical. Bien que des modèles plus complexes puissent améliorer les résultats, cette approche fournit une base solide pour classer automatiquement des articles de recherche en fonction de leur contenu.

## Structure du Projet

Voici la structure des fichiers du projet :

## Comment Exécuter le Projet

1. Clonez le dépôt :
    ```bash
    git clone <URL_du_depot>
    cd <nom_du_dossier_du_depot>
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Exécutez le script de prétraitement pour nettoyer et préparer les données :
    ```bash
    python preprocess_data.py
    ```

4. Entraînez le modèle de machine learning :
    ```bash
    python train_model.py
    ```

5. Évaluez les résultats du modèle :
    ```bash
    python evaluate_model.py
    ```

## Remerciements

Je tiens à remercierTanit AI pour cette opportunité  et leurs conseils tout au long de ce projet. Ce projet a permis de démontrer l'application de modèles de machine learning dans le domaine de la médecine reproductive, un domaine avec un grand potentiel pour améliorer les soins aux patients.

## License

Ce projet est sous la licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

