import pandas as pd
from datetime import datetime

# 1. Función para rellenar 'birth_date' faltante con la fecha de otros años del mismo jugador
def fill_missing_birth_date(df):
    birth_dates = df.groupby('Fullname')['birth_date'].first()  # Obtener la primera fecha válida para cada jugador
    df['birth_date'] = df.apply(
        lambda row: birth_dates[row['Fullname']] if pd.isnull(row['birth_date']) else row['birth_date'],
        axis=1
    )
    return df

# 2. Función para rellenar 'preferred_positions' faltante con la posición más frecuente del jugador
def fill_missing_positions(df):
    most_common_positions = df.groupby('Fullname')['preferred_positions'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else None)
    df['preferred_positions'] = df.apply(
        lambda row: most_common_positions[row['Fullname']] if pd.isnull(row['preferred_positions']) else row['preferred_positions'],
        axis=1
    )
    return df

# 3. Función para rellenar 'work_rate' faltante con el valor más frecuente del jugador
def fill_missing_work_rate(df):
    most_common_work_rate = df.groupby('Fullname')['work_rate'].agg(lambda x: x.mode().iloc[0] if not x.mode().empty else 'Medium/Medium')
    df['work_rate'] = df.apply(
        lambda row: most_common_work_rate[row['Fullname']] if pd.isnull(row['work_rate']) else row['work_rate'],
        axis=1
    )
    return df

# 4. Función para rellenar 'value' faltante con el promedio del jugador en otros años
def fill_missing_value(df):
    # Convertir la columna 'value' a numérica, eliminando símbolos de moneda y convirtiendo los nulos
    df['value'] = pd.to_numeric(df['value'].replace('[\$,]', '', regex=True), errors='coerce')
    average_values = df.groupby('Fullname')['value'].mean()  # Calcular el valor promedio para cada jugador
    df['value'] = df.apply(
        lambda row: average_values[row['Fullname']] if pd.isnull(row['value']) else row['value'],
        axis=1
    )
    return df

# 5. Función para rellenar valores numéricos faltantes (excepto 'gk_*') con el promedio global de la columna
def fill_missing_numeric_values(df):
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    for column in numeric_columns:
        if not column.startswith('gk_'):  # Evitar modificar columnas de porteros si el jugador no es portero
            mean_value = df[column].mean()
            df[column].fillna(mean_value, inplace=True)
    return df

# 6. Función para filtrar columnas de atributos específicos de porteros si el jugador no es portero y rellenar con 0
def filter_goalkeeper_columns(df):
    def filter_columns(row):
        if pd.notnull(row['preferred_positions']) and 'gk' in row['preferred_positions'].lower():
            return row
        else:
            for col in df.columns:
                if col.startswith('gk_'):
                    row[col] = 0  # Rellenar con 0 si el jugador no es portero
            return row
    
    return df.apply(filter_columns, axis=1)

# 7. Crear el dataset combinado con la columna 'age' y aplicar las funciones de limpieza
def create_and_clean_dataset():
    combined_fifa_df = pd.read_csv("combined_fifa_data.csv", low_memory=False)

    # Convertir la columna 'birth_date' a un formato de fecha
    combined_fifa_df['birth_date'] = pd.to_datetime(combined_fifa_df['birth_date'], errors='coerce', dayfirst=True)

    # Calcular la edad usando el año del dataset y la fecha de nacimiento
    def calculate_age(row):
        if pd.notnull(row['birth_date']):
            return row['year'] - row['birth_date'].year
        else:
            return None

    combined_fifa_df['age'] = combined_fifa_df.apply(calculate_age, axis=1)

    # Aplicar funciones para limpiar datos
    combined_fifa_df = fill_missing_birth_date(combined_fifa_df)
    combined_fifa_df = fill_missing_positions(combined_fifa_df)
    combined_fifa_df = fill_missing_work_rate(combined_fifa_df)
    combined_fifa_df = fill_missing_value(combined_fifa_df)
    combined_fifa_df = fill_missing_numeric_values(combined_fifa_df)
    combined_fifa_df = filter_goalkeeper_columns(combined_fifa_df)

    # Guardar el dataset con la nueva columna de edad y datos corregidos
    combined_fifa_df.to_csv("cleaned_combined_fifa_data_filtered.csv", index=False)
    print("The cleaned dataset with 'age' column and filtered attributes has been saved as 'cleaned_combined_fifa_data_filtered.csv'.")

# 8. Consultar las columnas con valores nulos
def consult_null_values():
    # Cargar el dataset combinado limpio y filtrado
    combined_fifa_df = pd.read_csv("cleaned_combined_fifa_data_filtered.csv", low_memory=False)

    # Identificar las columnas que tienen valores nulos
    null_columns = combined_fifa_df.isnull().sum()
    null_columns = null_columns[null_columns > 0]

    # Crear un DataFrame con las columnas que tienen valores nulos y el tipo de dato correspondiente
    null_info_df = pd.DataFrame({
        'Column': null_columns.index,
        'Null_Count': null_columns.values,
        'Data_Type': combined_fifa_df.dtypes[null_columns.index]
    })

    # Mostrar el DataFrame con la información de valores nulos
    print(null_info_df)

# Ejecutar las funciones
create_and_clean_dataset()
consult_null_values()
