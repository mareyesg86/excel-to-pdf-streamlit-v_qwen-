import streamlit as st
from utils.excel_to_pdf import process_excel_to_pdf

st.set_page_config(page_title="Excel a PDF", layout="wide")
st.title("📄 Conversor Excel a PDF")
st.markdown("Sube un archivo Excel y convierte su contenido en un informe PDF.")

uploaded_file = st.file_uploader("Selecciona un archivo Excel (.xlsx)", type=["xlsx"])

if uploaded_file is not None:
    with st.spinner("Procesando archivo..."):
        try:
            # Generar PDF en memoria
            pdf_bytes = process_excel_to_pdf(uploaded_file)

            # Mostrar botón de descarga
            st.success("✅ PDF generado exitosamente.")
            st.download_button(
                label="📥 Descargar PDF",
                data=pdf_bytes,
                file_name="informe_generado.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"❌ Error al procesar el archivo: {e}")
else:
    st.info("Por favor, carga un archivo Excel para comenzar.")
