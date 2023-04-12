import pandas as pd
import numpy as np
from scipy.stats import ttest_1samp

chat_id = 1219503064 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # исторические данные о затратах на аналогичную подписку
    costs = x

    # задаем уровень значимости
    alpha = 0.1

    # задаем порог затрат на подписку
    threshold = 300

    # выполняем одновыборочный t-тест
    t_statistic, p_value = ttest_1samp(costs, threshold)

    # проверяем гипотезу на уровне значимости alpha
    return(p_value < alpha and t_statistic < 0)
