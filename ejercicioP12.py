# definir las variables constantes
horasxsemana = 48
valorxhora = 5000
porcentaje_retencion = 12.5 / 100
# calcular salario bruto
salario_bruto = horasxsemana * valorxhora
# calcular la retención en la fuente
retencion = int(salario_bruto * porcentaje_retencion)
# calcular salario neto
salario_neto = int(salario_bruto - retencion)
# resultados con los valores x semana
print("El salario bruto es de:", salario_bruto)
print("El valor de la retencion en la fuente es de:", retencion)
print("El salario neto es de:", salario_neto)
