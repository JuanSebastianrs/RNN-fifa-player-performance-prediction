# Football Player Rating Prediction

**Recurrent neural networks and regression baselines for historical FIFA video-game player ratings.**

A machine-learning project exploring temporal modeling of yearly player attributes. The target comes from FIFA ratings; it should not be interpreted as a validated forecast of real match performance.

[Training and evaluation notebook](Entrega%20final/Entrega%20Final%20Deep%20Learning.ipynb) · [Data-cleaning functions](Entrega%20final/funciones_de_limpieza.py) · [Saved RNN model](Entrega%20final/best_RNN_Ponderado.keras)

## Approach

1. Combine historical player-attribute tables from FIFA editions covering 2005–2021.
2. Clean records and select relevant features.
3. Build five-year temporal sequences.
4. Compare regression baselines and a recurrent neural network.
5. Evaluate with MSE, MAE and R².

The project documents experiments with Ridge, Lasso, Bayesian Ridge, SVR and Random Forest, followed by the recurrent model.

## Reported results

| Metric | Reported RNN result |
| --- | ---: |
| MSE | 3.70 |
| MAE | 1.42 |
| R² | 0.90 |

These values are reported in the original project documentation. They describe that experiment and dataset, rather than a benchmark on real-world player outcomes.

## Repository contents

```text
Entrega final/
  Entrega Final Deep Learning.ipynb   # Main experiment
  funciones_de_limpieza.py           # Data preprocessing
  best_RNN_Ponderado.keras           # Saved Keras model
README.md
```

## Explore the experiment

```bash
git clone https://github.com/JuanSebastianrs/RNN-fifa-player-performance-prediction.git
cd RNN-fifa-player-performance-prediction
jupyter lab
```

Open the notebook in `Entrega final/` using a Python environment compatible with its imports. Inspect the data paths before running cells; the original experiment environment is not locked in a requirements file.

The source FIFA tables are not bundled as a complete dataset in this repository. Reproduction requires obtaining the matching historical tables and adjusting the notebook's input paths. The notebook is the reference for the input schema and preprocessing.

## Interpretation and next steps

Useful extensions include a clearly documented temporal holdout, comparison with simple persistence baselines, an environment specification and evaluation on external football data. These are future improvements, not completed features.

## Resumen en español

Proyecto de modelado temporal con redes neuronales recurrentes para predecir valoraciones de jugadores en datos históricos del videojuego FIFA. Incluye el notebook, funciones de limpieza y un modelo guardado; se documenta la diferencia entre predecir estas valoraciones y predecir rendimiento deportivo real.
