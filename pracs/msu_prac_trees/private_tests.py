import numpy as np
from numpy import array
import pandas as pd


compute_criterion_tests_private = [
    {
        "target_vector": np.array([1, 1, 1]),
        "feature_vector": np.arange(3),
        "threshold": 1.5,
        "criterion": 'entropy',
        "true_result": 0.0,
    },#1

    {
        "target_vector": np.array([1, 1, 1]),
        "feature_vector": np.array([1, 1, 1]),
        "threshold": 5,
        "criterion": 'gini',
        "true_result": 0.0,
    },#2
]



find_best_split_tests_private = [
    {
        "feature_vector": np.array([1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 1, 1, 2, 2]),
        "target_vector": np.array([0, 1, 1, 1, 0, 0, 2, 2, 2, 1, 1, 1, 1, 2]),
        "criterion": "gini",
        "true_result": (
            np.array([1.5, 2.5, 3.5, 4.5]),
            np.array([0.058, 0.105, 0.015, 0.029]),
            2.5,
            0.105,
        )
    }, #1

    {
        "feature_vector": np.array([0.  , 0.9 , 0.33, 0.3 , 0.24, 0.66, 0.56, 0.01, 0.25, 0.85, 0.81,
           0.3 , 0.34, 0.9 , 0.6 , 0.8 , 0.05, 0.33, 0.29, 0.56, 0.2 , 0.66,
           0.65, 0.28, 0.25, 0.85, 0.1 , 0.25, 0.56, 0.81, 0.59, 0.24, 0.16,
           0.82, 0.78, 0.29, 0.26, 0.33, 0.  , 0.45, 0.1 , 0.78, 0.6 , 0.25,
           0.04, 0.66, 0.62, 0.77, 0.9 , 0.67, 0.25, 0.45, 0.05, 0.86, 0.55,
           0.26, 0.25, 0.59, 0.82, 0.1 , 0.01, 0.56, 0.51, 0.28, 0.28, 0.15,
           0.24, 0.51, 0.32, 0.67, 0.58, 0.75, 0.08, 0.53, 0.78, 0.1 , 0.1 ,
           0.3 , 0.2 , 0.28, 0.24, 0.67, 0.62, 0.26, 0.25, 0.03, 0.79, 0.28,
           0.18, 0.67, 0.56, 0.34, 0.09, 0.24, 0.8 , 0.15, 0.19, 0.77, 0.57,
           0.29, 0.26, 0.87, 0.54, 0.27, 0.1 , 0.67, 0.59, 0.54, 0.3 , 0.84,
           0.33, 0.3 , 0.58, 0.79, 0.55, 0.45, 0.07, 0.7 , 0.66, 0.81, 0.13,
           0.25, 0.33, 0.83, 0.76, 0.5 , 0.66, 0.28, 0.14, 0.28, 0.34, 0.67,
           0.07, 0.71, 0.65, 0.5 , 0.26, 0.1 , 0.58, 0.3 , 0.1 , 0.4 , 0.56,
           0.29, 0.48, 0.65, 0.35, 0.1 , 0.13, 0.77, 0.86, 0.3 , 0.13, 0.14,
           0.64, 0.52, 0.51, 0.83, 0.59, 0.54, 0.18, 0.3 , 0.88, 0.89, 0.12,
           0.9 , 0.61, 0.78, 0.16, 0.92, 0.25, 0.49, 0.85, 0.16, 0.66, 0.3 ,
           0.19, 0.71, 0.6 , 0.83, 0.18, 0.55, 0.89, 0.3 , 0.2 , 0.21, 0.93,
           0.57, 0.25, 0.47, 0.64, 0.8 , 0.5 , 0.67, 0.66, 0.29, 0.1 , 0.26,
           0.63, 0.1 , 0.09, 0.5 , 0.1 , 0.29, 0.75, 0.15, 0.66, 0.53, 0.11,
           0.68, 0.62, 0.51, 0.79, 0.34, 0.6 , 0.3 , 0.3 , 0.58, 0.64, 0.3 ,
           0.24, 0.28, 0.66, 0.57, 0.21, 0.68, 0.59, 0.31, 0.78, 0.69, 0.65,
           0.28, 0.23, 0.66, 0.62, 0.3 , 0.22, 0.83, 0.64, 0.52, 0.2 , 0.86,
           0.63, 0.25, 0.25, 0.88, 0.66, 0.29, 0.9 , 0.45, 0.66, 0.5 , 0.19,
           0.58, 0.6 , 0.77, 0.26, 0.74]),
        "target_vector": np.array([0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1,
           1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1,
           0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0,
           0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0,
           0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1,
           0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1,
           0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0,
           1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0,
           0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0,
           1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0,
           0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1,
           1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1]),
        "criterion": "gini",
        "true_result": (
            np.array([0.005, 0.02 , 0.035, 0.045, 0.06 , 0.075, 0.085, 0.095, 0.105,
                   0.115, 0.125, 0.135, 0.145, 0.155, 0.17 , 0.185, 0.195, 0.205,
                   0.215, 0.225, 0.235, 0.245, 0.255, 0.265, 0.275, 0.285, 0.295,
                   0.305, 0.315, 0.325, 0.335, 0.345, 0.375, 0.425, 0.46 , 0.475,
                   0.485, 0.495, 0.505, 0.515, 0.525, 0.535, 0.545, 0.555, 0.565,
                   0.575, 0.585, 0.595, 0.605, 0.615, 0.625, 0.635, 0.645, 0.655,
                   0.665, 0.675, 0.685, 0.695, 0.705, 0.725, 0.745, 0.755, 0.765,
                   0.775, 0.785, 0.795, 0.805, 0.815, 0.825, 0.835, 0.845, 0.855,
                   0.865, 0.875, 0.885, 0.895, 0.91 , 0.925]),
            np.array([0.005, 0.011, 0.014, 0.016, 0.022, 0.028, 0.031, 0.036, 0.074,
                   0.077, 0.08 , 0.09 , 0.097, 0.108, 0.118, 0.129, 0.141, 0.157,
                   0.165, 0.169, 0.173, 0.199, 0.219, 0.242, 0.247, 0.259, 0.299,
                   0.35 , 0.356, 0.363, 0.399, 0.388, 0.396, 0.389, 0.366, 0.36 ,
                   0.355, 0.349, 0.323, 0.304, 0.295, 0.285, 0.272, 0.26 , 0.236,
                   0.225, 0.207, 0.191, 0.175, 0.172, 0.16 , 0.155, 0.144, 0.133,
                   0.104, 0.089, 0.085, 0.083, 0.081, 0.077, 0.075, 0.071, 0.069,
                   0.061, 0.052, 0.047, 0.042, 0.037, 0.034, 0.027, 0.026, 0.021,
                   0.017, 0.015, 0.012, 0.01 , 0.003, 0.001]),
            0.335,
            0.399
        )
    }, #2
]

DecisionTree_fit_tests_private = [
    {
        'ADD_SCORE_FOR_THIS_TEST': 2.5,
        "X": pd.read_csv('./data/adult.csv').values[:, :-1],
        'y': pd.read_csv('./data/adult.csv')['target'].astype('category').cat.codes.values.astype(int),
        "tree_params": {
            "feature_types": ['real', 'categorical', 'real', 'categorical', 'real', 'categorical', 'categorical',
                              'categorical', 'categorical', 'categorical', 'real', 'real', 'real', 'categorical'],
            "criterion": 'gini',
            "min_samples_split": 100,
            'max_depth': 5,
        },
        'true_result': {
            'type': 'nonterminal',
            'feature_type': 'categorical',
            'feature_number': 5,
            'threshold': 0.2797402043742814,
            'left_child': {
                'type': 'nonterminal',
                'feature_type': 'real',
                'feature_number': 10,
                'threshold': 7139.5,
                'left_child': {
                    'type': 'nonterminal',
                    'feature_type': 'categorical',
                    'feature_number': 3,
                    'threshold': 0.36281953564727953,
                    'left_child': {
                        'type': 'nonterminal',
                        'feature_type': 'categorical',
                        'feature_number': 6,
                        'threshold': 0.3018707482993197,
                        'left_child': {'type': 'terminal', 'classes_distribution': array([1872, 26])},
                        'right_child': {'type': 'terminal', 'classes_distribution': array([253, 20])}
                    },
                    'right_child': {
                        'type': 'nonterminal',
                        'feature_type': 'real',
                        'feature_number': 0,
                        'threshold': 29.5,
                        'left_child': {'type': 'terminal', 'classes_distribution': array([184, 5])},
                        'right_child': {'type': 'terminal', 'classes_distribution': array([255, 75])}
                    }
                },
                'right_child': {'type': 'terminal', 'classes_distribution': array([2, 38])}
            },
            'right_child': {
                'type': 'nonterminal',
                'feature_type': 'categorical',
                'feature_number': 6,
                'threshold': 0.26893424036281177,
                'left_child': {
                    'type': 'nonterminal',
                    'feature_type': 'real',
                    'feature_number': 10,
                    'threshold': 5095.5,
                    'left_child': {
                        'type': 'nonterminal',
                        'feature_type': 'categorical',
                        'feature_number': 3,
                        'threshold': 0.12582375478927205,
                        'left_child': {'type': 'terminal', 'classes_distribution': array([207, 24])},
                        'right_child': {'type': 'terminal', 'classes_distribution': array([640, 306])}
                    },
                    'right_child': {'type': 'terminal', 'classes_distribution': array([4, 61])}
                },
                'right_child': {
                    'type': 'nonterminal',
                    'feature_type': 'real',
                    'feature_number': 10,
                    'threshold': 5095.5,
                    'left_child': {
                        'type': 'nonterminal',
                        'feature_type': 'real',
                        'feature_number': 11,
                        'threshold': 1794.0,
                        'left_child': {'type': 'terminal', 'classes_distribution': array([361, 448])},
                        'right_child': {'type': 'terminal', 'classes_distribution': array([1, 83])}
                    },
                    'right_child': {'type': 'terminal', 'classes_distribution': array([0, 135])}
                }
            }
        }
    }, #1

    {
        'ADD_SCORE_FOR_THIS_TEST': 2.5,
        "X": pd.read_csv('./data/adult.csv').values[:, :-1],
        'y': pd.read_csv('./data/adult.csv')['target'].astype('category').cat.codes.values.astype(int),
        "tree_params": {
            "feature_types": ['real', 'categorical', 'real', 'categorical', 'real', 'categorical', 'categorical',
                              'categorical', 'categorical', 'categorical', 'real', 'real', 'real', 'categorical'],
            "criterion": 'entropy',
            'max_depth': 4,
        },
        'true_result': {
            'type': 'nonterminal',
             'feature_type': 'categorical',
             'feature_number': 5,
             'threshold': 0.2797402043742814,
             'left_child': {
                 'type': 'nonterminal',
                  'feature_type': 'real',
                  'feature_number': 10,
                  'threshold': 7139.5,
                  'left_child': {
                      'type': 'nonterminal',
                       'feature_type': 'categorical',
                       'feature_number': 3,
                       'threshold': 0.36281953564727953,
                       'left_child': {'type': 'terminal', 'classes_distribution': array([2125,   46])},
                       'right_child': {'type': 'terminal', 'classes_distribution': array([439,  80])}
                  },
                  'right_child': {
                      'type': 'nonterminal',
                       'feature_type': 'real',
                       'feature_number': 0,
                       'threshold': 20.0,
                       'left_child': {'type': 'terminal', 'classes_distribution': array([2, 0])},
                       'right_child': {'type': 'terminal', 'classes_distribution': array([ 0, 38])}
                  }
             },
             'right_child': {
                 'type': 'nonterminal',
                  'feature_type': 'real',
                  'feature_number': 10,
                  'threshold': 5095.5,
                  'left_child': {
                      'type': 'nonterminal',
                       'feature_type': 'categorical',
                       'feature_number': 6,
                       'threshold': 0.26893424036281177,
                       'left_child': {'type': 'terminal', 'classes_distribution': array([847, 330])},
                       'right_child': {'type': 'terminal', 'classes_distribution': array([362, 531])}
                  },
                  'right_child': {
                      'type': 'nonterminal',
                       'feature_type': 'real',
                       'feature_number': 0,
                       'threshold': 60.5,
                       'left_child': {'type': 'terminal', 'classes_distribution': array([  0, 179])},
                       'right_child': {'type': 'terminal', 'classes_distribution': array([ 4, 17])}
                  }
             }
        }
    }, #2
]


DecisionTree_predict_proba_tests_private = [
    {
        'ADD_SCORE_FOR_THIS_TEST': 1,
        "X": pd.read_csv('./data/adult.csv').values[:, :-1],
        'y': pd.read_csv('./data/adult.csv')['target'].astype('category').cat.codes.values.astype(int),
        "tree_params": {
            "feature_types": ['real', 'categorical', 'real', 'categorical', 'real', 'categorical', 'categorical',
                              'categorical', 'categorical', 'categorical', 'real', 'real', 'real', 'categorical'],
            "criterion": 'gini',
            'max_depth': 5,
        },
        'true_result': 0.8356
    }, #1

    {
        'ADD_SCORE_FOR_THIS_TEST': 1.5,
        "X": pd.read_csv('./data/adult.csv').values[:, :-1],
        'y': pd.read_csv('./data/adult.csv')['target'].astype('category').cat.codes.values.astype(int),
        "tree_params": {
            "feature_types": ['real', 'categorical', 'real', 'categorical', 'real', 'categorical', 'categorical',
                              'categorical', 'categorical', 'categorical', 'real', 'real', 'real', 'categorical'],
            "criterion": 'entropy',
            'max_depth': 4,
        },
        'true_result': 0.8352
    }, #2
]




