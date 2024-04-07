import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# Cargar el dataset desde un archivo CSV
df = pd.read_csv('all-weeks-global.csv')




categories = df.iloc[:, 1].unique()
category_counts = df.iloc[:, 1].value_counts()
labels = categories
sizes = [category_counts[category] for category in categories]
colors = plt.cm.tab20.colors  
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  
plt.show()
#comportamiento de las horas visuallzadasa semanalmente y semanas acumuladas en el Top 10 de acuerdo a cada variable
# Sumar las horas semanales para cada título de programa
total_hours_per_title = df.groupby('show_title')['weekly_hours_viewed'].sum()
total_weeks_per_title = df.groupby('show_title')['cumulative_weeks_in_top_10'].sum()

total_hours_per_category = df.groupby('category')['weekly_hours_viewed'].sum()
total_weeks_per_category = df.groupby('category')['cumulative_weeks_in_top_10'].sum()

total_hours_per_runtime = df.groupby('runtime')['weekly_hours_viewed'].sum()
total_weeks_per_runtime = df.groupby('runtime')['cumulative_weeks_in_top_10'].sum()

total_hours_per_staggered_launch = df.groupby('is_staggered_launch')['weekly_hours_viewed'].sum()
total_weeks_per_staggered_launch = df.groupby('is_staggered_launch')['cumulative_weeks_in_top_10'].sum()

df_prima = df[df['weekly_views'] != 0]
df_prima = df_prima.dropna(subset=['weekly_views'])
categorys = df['show_title'].unique()
categorys = df['category'].value_counts()
# Convertir la serie de pandas a un nuevo DataFrame

# Sumar las horas semanales para cada título de programa

total_views_per_title = df_prima.groupby('show_title')['weekly_views'].sum()

df_total_views = total_views_per_title.reset_index()
df_total_hours = total_hours_per_title.reset_index()
df_total_weeks = total_weeks_per_title.reset_index()

# Convertir las series de pandas a nuevos DataFrames
df_total_hours_category = total_hours_per_category.reset_index()
df_total_hours_runtime = total_hours_per_runtime.reset_index()
df_total_hours_staggered_launch = total_hours_per_staggered_launch.reset_index()

df_total_weeks_category = total_weeks_per_category.reset_index()
df_total_weeks_runtime = total_weeks_per_runtime.reset_index()
df_total_weeks_staggered_launch = total_weeks_per_staggered_launch.reset_index()


# Ordenar los resultados de manera descendente según las horas totales
df_total_hours_sorted = df_total_hours.sort_values(by='weekly_hours_viewed', ascending=False)
df_total_views_sorted = df_total_views.sort_values(by='weekly_views', ascending=False)
print(df_total_hours_sorted)
print(df_total_views_sorted)
print(categorys)

print(df_total_hours_category)
print(df_total_weeks_category)
print(df_total_hours_runtime)
print(df_total_weeks_runtime)
print(df_total_hours_staggered_launch)
print(df_total_weeks_staggered_launch)


# Mostrar los 20 programas con más horas totales visualizadas



plt.title('Top 20 programas con más horas totales visualizadas')

combined_viewed_hours = df.groupby('show_title')['weekly_hours_viewed'].sum().reset_index()
top_20_most_viewed_combined = combined_viewed_hours.sort_values(by='weekly_hours_viewed', ascending=False).head(20)
plt.figure(figsize=(12, 8))
bars = plt.bar(top_20_most_viewed_combined['show_title'], top_20_most_viewed_combined['weekly_hours_viewed'], color='skyblue')
plt.xticks(rotation=90) 
formatter = ticker.FuncFormatter(lambda x, pos: '{:.1f}M'.format(x / 1_000_000))
plt.gca().yaxis.set_major_formatter(formatter)
plt.tight_layout()
plt.show()




plt.title('Top 20 programas con más horas vistas por semanas en el top 10 totales')
category_viewed_hours = df.groupby('category')['weekly_hours_viewed'].sum().reset_index()
colors = ['#FFA500', '#FF8C00', '#FFA07A', '#FF7F50', '#FF6347']  
plt.figure(figsize=(6, 6))
plt.pie(category_viewed_hours['weekly_hours_viewed'], labels=category_viewed_hours['category'], autopct='%1.1f%%', startangle=140, colors=colors)
plt.axis('equal') 
plt.show()

top_show_counts = df.groupby('show_title')['cumulative_weeks_in_top_10'].max().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 8))
top_show_counts.plot(kind='bar', color='Pink')
plt.ylabel('Cumulative Weeks in Top 10')
plt.title('Top 20 programas con más horas vistas por semanas acumuladas en el top 10 totales')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

df['month'] = pd.to_datetime(df['week']).dt.strftime('%Y-%m')
monthly_category_viewed_hours = df.groupby(['month', 'category'])['weekly_hours_viewed'].sum().reset_index()
plt.figure(figsize=(12, 6))
for category, group_data in monthly_category_viewed_hours.groupby('category'):
    plt.plot(group_data['month'], group_data['weekly_hours_viewed'], marker='o', label=category)
plt.title('Horas totales visualizadas por mes y categoría')
plt.xlabel('Month')
plt.ylabel('Total Monthly Hours Viewed')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

df_escalonados = df[df['is_staggered_launch'] != False]
df_escalonados_prima = df_escalonados.groupby('show_title').max().sort_values(by=['cumulative_weeks_in_top_10', 'weekly_hours_viewed', 'weekly_views', 'weekly_rank'], ascending=False).reset_index()[['show_title', 'cumulative_weeks_in_top_10', 'weekly_hours_viewed', 'weekly_views', 'weekly_rank']]

print(df_escalonados_prima)
print(top_show_counts)


plt.figure(figsize=(24, 6))
sns.lineplot(x='week', y='weekly_views', data=df )
plt.title('Tendencia temporal de las visualizaciones semanales a lo largo del tiempo')
plt.xticks(rotation=90)
plt.xlabel('Fecha')
plt.ylabel('Visualizaciones semanales')
plt.show()

plt.figure(figsize=(24, 6))
sns.lineplot(x='week', y='weekly_hours_viewed', data=df )
plt.title('Tendencia temporal de las visualizaciones semanales a lo largo del tiempo')
plt.xticks(rotation=90)
plt.xlabel('Fecha')
plt.ylabel('Visualizaciones semanales')
plt.show()
