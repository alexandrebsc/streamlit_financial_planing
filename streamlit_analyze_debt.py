import streamlit as st

st.title("Simulação de Pagamento de Dívidas")

num_dividas = st.number_input("Número de Dívidas", min_value=1, value=2, step=1)
DIVIDAS = []
for i in range(num_dividas):
    valor = st.number_input(f"Valor da Dívida {i + 1}", min_value=0.0, value=200_000.0 if i == 0 else 300_000.0, step=1_000.0)
    juros = st.number_input(f"Taxa de Juros da Dívida {i + 1} (%)", min_value=0.0, value=2.5 if i == 0 else 1.6, step=0.1) / 100
    parcela = st.number_input(f"Valor das parcelas {i + 1}", min_value=0.0, value=5_000.0, step=1_000.0)
    DIVIDAS.append({"valor": valor, "juros": juros, "parcela": parcela})

VALOR_VENDA = st.number_input("Valor da Venda", min_value=0.0, value=700_000.0, step=10_000.0)
MES_DA_VENDA = st.number_input("Mês da Venda", min_value=1, max_value=12, value=12, step=1)
TEMPO = st.number_input("Tempo (em meses)", min_value=1, value=12, step=1)

acumulado = 0

for m in range(1, int(TEMPO) + 1):
    if m == MES_DA_VENDA:
        valor_restante = VALOR_VENDA
        for divida in DIVIDAS:
            divida["valor"] -= valor_restante
            if divida["valor"] < 0:
                valor_restante = -divida["valor"]
                divida["valor"] = 0
            else:
                break

        if valor_restante > 0:
            acumulado += valor_restante

    for divida in DIVIDAS:
        if divida["valor"] > 0:
            divida["valor"] -= divida["parcela"]

            if divida["valor"] < 0:
                divida["valor"] = 0
            else:
                divida["valor"] *= (1 + divida["juros"])
        else:
            acumulado += parcela

st.write("## Resultados")
st.write(f"Acumulado: R$ {acumulado:,.2f}")
st.write("Dívidas Restantes:", [round(d["valor"], 2) for d in DIVIDAS])
