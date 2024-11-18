import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, linregress, norm

# Carregar os dados
file_path = '/content/drive/MyDrive/Python/Frequencia Igreja/Frequência_Ceia IBCA 2022-2024.xlsx'
data = pd.read_excel(file_path)

# Remover colunas desnecessárias (Unnamed)
data = data[['Dias', 'Manhã', 'Noite']]

# Converter coluna 'Dias' para tipo de data
data['Dias'] = pd.to_datetime(data['Dias'], errors='coerce')

# Filtrar apenas datas que caíram em domingo
sundays_data = data[data['Dias'].dt.dayofweek == 6].copy()  # 6 representa domingo

# Adicionar coluna 'Ano' para separar dados por ano
sundays_data['Ano'] = sundays_data['Dias'].dt.year

# Selecionar as colunas de interesse e remover valores NaN
sundays_data = sundays_data[['Manhã', 'Noite']].dropna()

# Garantir que ambas as colunas são do tipo numérico
sundays_data['Manhã'] = pd.to_numeric(sundays_data['Manhã'], errors='coerce')
sundays_data['Noite'] = pd.to_numeric(sundays_data['Noite'], errors='coerce')

# Após garantir que não há valores nulos, prosseguir com a regressão
morning_service = sundays_data['Manhã']
evening_service = sundays_data['Noite']

# Calcular a regressão linear
slope, intercept, r_value, p_value, std_err = linregress(morning_service, evening_service)

# Plotar gráfico de dispersão com a linha de regressão
plt.figure(figsize=(10, 6))
plt.scatter(morning_service, evening_service, alpha=0.7, label="Dados de Frequência")
plt.plot(morning_service, slope * morning_service + intercept, color="red", label=f"y = {slope:.2f}x + {intercept:.2f}")

# Adicionar títulos e rótulos
plt.title('Gráfico de Dispersão: Culto da Manhã vs. Culto da Noite com Regressão Linear')
plt.xlabel('Frequência do Culto da Manhã')
plt.ylabel('Frequência do Culto da Noite')
plt.legend()
plt.show()

# Exibir a equação da linha de regressão e o coeficiente de correlação
print(f"Equação da linha de regressão: y = {slope:.2f}x + {intercept:.2f}")
print(f"Coeficiente de correlação (R²): {r_value**2:.2f}")
print(f"Correlação (R): {r_value:.2f}, Valor-p: {p_value:.4f}")
